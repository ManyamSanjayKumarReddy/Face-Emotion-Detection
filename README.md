# Emotion-Based Music Player

This project is a **real-time emotion-based music player** that detects emotions through a webcam, identifies the dominant emotion, and plays a corresponding song based on the detected mood.

## Features
- **Real-time emotion detection** using OpenCV and DeepFace
- **Automatic song selection** based on detected emotions
- **Web-based UI** with a video feed, detected emotion display, and music player
- **Auto-stop detection** after 5 seconds and plays a song
- **Flask Backend** for video streaming and emotion processing

## Technologies Used
- **Python** (Flask, OpenCV, DeepFace, NumPy)
- **HTML, CSS, JavaScript** (for the front end)
- **Webcam Integration** (via OpenCV)
- **Audio Streaming** (HTML5 Audio Player)

## Project Structure
```
Emotion-Music-Player/
│── app.py                 # Flask backend
│── templates/
│   └── index.html         # Frontend UI
│── static/
│   └── songs/             # Folder for storing song files
│── requirements.txt       # Required dependencies
│── README.md              # Project documentation
```

## Installation & Setup
### **1. Clone the Repository**
```sh
git clone https://github.com/ManyamSanjayKumarReddy/Face-Emotion-Detection.git
cd emotion-music-player
```

### **2. Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Run the Flask Application**
```sh
python app.py
```

### **5. Open in Browser**
Navigate to:
```
http://127.0.0.1:5000/
```

## How It Works
1. Click **Start Detection**
2. The webcam captures the user’s face and detects emotions
3. After **5 seconds**, the detection stops automatically
4. The **dominant emotion** is displayed
5. A **corresponding song** is played based on the detected emotion

## Emotion-to-Song Mapping
| Detected Emotion | Song Played  |
|-----------------|--------------|
| Happy          | happy.mp3     |
| Sad            | sad.mp3       |
| Angry          | angry.mp3     |
| Fear          | fear.mp3      |
| Surprise      | surprise.mp3  |
| Neutral       | neutral.mp3   |

## API Endpoints
### **1. Home Page**
- **Route:** `/`
- **Method:** GET
- **Description:** Loads the web interface

### **2. Video Feed**
- **Route:** `/video_feed`
- **Method:** GET
- **Description:** Streams the webcam feed

### **3. Start Detection**
- **Route:** `/start`
- **Method:** POST
- **Description:** Starts real-time emotion detection

### **4. Stop Detection**
- **Route:** `/stop`
- **Method:** POST
- **Description:** Stops detection and returns the detected emotion with the song URL

### **5. Serve Songs**
- **Route:** `/songs/<filename>`
- **Method:** GET
- **Description:** Serves the requested song file

## Frontend Explanation
- **Video Feed Section** - Displays real-time video stream.
- **Emotion Display Box** - Shows the detected emotion.
- **Music Player** - Plays the selected song.
- **Start/Stop Button** - Controls emotion detection.

## Backend Explanation (`app.py`)
- **Imports Necessary Libraries**
  - `cv2`, `numpy`, `Flask`, `DeepFace` for face and emotion detection
- **Loads Face Cascade Classifier**
  - Uses OpenCV’s `haarcascade_frontalface_default.xml`
- **Defines Routes**
  - `/`: Renders `index.html`
  - `/video_feed`: Streams webcam feed
  - `/start`: Starts detection
  - `/stop`: Stops detection, determines the dominant emotion, and returns a song
  - `/songs/<filename>`: Serves the detected emotion’s corresponding song
- **Emotion Detection Mechanism**
  - Captures webcam frames
  - Detects faces
  - Uses DeepFace to analyze emotions
  - Stores detected emotions in a global list
  - Stops after 5 seconds and selects the most frequent emotion

## Frontend Explanation (`index.html`)
- **HTML Structure**
  - Video feed for real-time streaming
  - A box displaying the detected emotion
  - A music player that plays the assigned song
  - A `Start Detection` button, which starts emotion detection for 5 seconds
- **JavaScript Functions**
  - `startDetection()`: Starts detection and automatically stops after 5 seconds
  - `stopDetection()`: Stops detection, updates UI with detected emotion, and plays music
  - `playSong(songUrl)`: Loads and plays the selected song

## Future Enhancements
- Improve emotion recognition accuracy
- Support for multiple users
- Use AI-based song recommendations
- Dark mode UI theme

## Author
- **M Sanjay Kumar Reddy**  
- GitHub: [ManyamSanjayKumarReddy](https://github.com/ManyamSanjayKumarReddy/Face-Emotion-Detection)

## License
This project is open-source and available under the **MIT License**.

