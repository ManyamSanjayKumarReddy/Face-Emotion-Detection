import cv2
import numpy as np
import os
from flask import Flask, render_template, Response, request, jsonify, send_from_directory
from deepface import DeepFace

app = Flask(__name__)

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Path to songs directory
SONGS_DIR = "songs"

detected_emotions = []  # Global variable to store detected emotions
capturing = True  # Variable to control webcam capture

# Webcam-based emotion detection
def generate_frames():
    global detected_emotions, capturing
    cap = cv2.VideoCapture(0)
    detected_emotions.clear()
    
    while capturing:
        success, frame = cap.read()
        if not success:
            break
        
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            face_roi = frame[y:y + h, x:x + w]
            result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']
            detected_emotions.append(emotion)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    global capturing
    capturing = True
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop', methods=['POST'])
def stop_detection():
    global detected_emotions, capturing
    capturing = False  # Stop capturing video
    final_emotion = max(set(detected_emotions), key=detected_emotions.count) if detected_emotions else "No emotion detected"
    detected_emotions.clear()  # Reset detected emotions after stopping
    
    # Map emotion to song filename
    emotion_to_song = {
        "happy": "happy.mp3",
        "sad": "sad.mp3",
        "fear": "fear.mp3",
        "neutral": "neutral.mp3",
        "surprise": "surprise.mp3",
        "angry": "angry.mp3"
    }
    
    song_filename = emotion_to_song.get(final_emotion.lower(), "neutral.mp3")
    song_url = f"/songs/{song_filename}"
    
    return jsonify({"emotion": final_emotion, "song_url": song_url})

@app.route('/start', methods=['POST'])
def start_detection():
    global capturing
    capturing = True
    return jsonify({"status": "started"})

@app.route('/songs/<path:filename>')
def serve_song(filename):
    return send_from_directory(SONGS_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)