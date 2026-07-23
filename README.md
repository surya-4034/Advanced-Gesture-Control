# Advanced-Gesture-Control

# 🖐️ GesturePilot

GesturePilot is a real-time hand gesture control application that lets you control your computer using only your webcam.

The application uses Computer Vision to detect hand landmarks and translate hand gestures into mouse actions and presentation controls. It provides a natural, touch-free way to interact with your computer without requiring any additional hardware.

---

# ✨ Features

## 🖱 Mouse Mode

- Real-time cursor movement
- Smooth cursor movement
- Active tracking area
- Left Click
- Right Click
- Drag & Drop
- Scroll Control

### Supported Gestures

| Gesture | Action |
|----------|--------|
| ☝️ Index Finger | Move Cursor |
| 🤏 Thumb + Index | Left Click |
| 🤏 Thumb + Middle | Right Click |
| 🤏 Thumb + Ring | Drag & Drop |
| ✌️ Index + Middle | Scroll |

---

## 📽 Presentation Mode

Press **M** to switch between modes.

### Supported Controls

| Hand Movement | Action |
|---------------|--------|
| ➡️ Swipe Right | Next Slide |
| ⬅️ Swipe Left | Previous Slide |

Compatible with:

- Google Slides
- Microsoft PowerPoint
- Apple Keynote

---

## 🖥 User Interface

The application displays:

- Live webcam feed
- Hand landmarks
- Current gesture
- Current mode
- Active tracking area

---

# 🛠 Built With

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- ScreenInfo

---

# 📂 Project Structure

```
GesturePilot/
│
├── controllers/
│   ├── mouse_controller.py
│   └── presentation_controller.py
│
├── core/
│   ├── camera.py
│   ├── gesture_engine.py
│   ├── hand_tracker.py
│   └── mode_manager.py
│
├── utils/
│   ├── smoothing.py
│   └── swipe_detector.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/GesturePilot.git
```

Move into the project folder:

```bash
cd GesturePilot
```

---

# 🪟 Windows Setup

## Step 1 - Install Python

Download Python from:

https://www.python.org/downloads/

During installation, enable:

```
✔ Add Python to PATH
```

Verify installation:

```bash
python --version
```

---

## Step 2 - Create a Virtual Environment

```bash
python -m venv .venv
```

---

## Step 3 - Activate the Virtual Environment

### Command Prompt

```cmd
.venv\Scripts\activate
```

### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

## Step 4 - Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5 - Run the Project

```bash
python main.py
```

---

# 🍎 macOS Setup

## Step 1 - Install Python

Install Homebrew (if not installed).

Then install Python:

```bash
brew install python
```

Verify installation:

```bash
python3 --version
```

---

## Step 2 - Create a Virtual Environment

```bash
python3 -m venv .venv
```

---

## Step 3 - Activate the Virtual Environment

```bash
source .venv/bin/activate
```

---

## Step 4 - Upgrade pip (Recommended)

```bash
pip install --upgrade pip
```

---

## Step 5 - Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6 - Run the Project

```bash
python3 main.py
```

If needed, you can also run:

```bash
.venv/bin/python main.py
```

---

# 📦 Dependencies

All required packages are installed automatically using:

```bash
pip install -r requirements.txt
```

Current dependencies:

- OpenCV
- MediaPipe
- PyAutoGUI
- ScreenInfo
- NumPy

---

# 🍎 macOS Permissions

To allow mouse and keyboard control on macOS:

Open:

```
System Settings
    ↓
Privacy & Security
```

Enable:

### Accessibility

Allow access for:

- Terminal
- Visual Studio Code (if running from VS Code)

Also enable:

### Input Monitoring

Allow access for:

- Terminal
- Visual Studio Code

Without these permissions, mouse movement and presentation controls may not function correctly.

---

# ▶️ Running the Application

After activating the virtual environment:

### Windows

```bash
python main.py
```

### macOS

```bash
python3 main.py
```

---

# 🎮 Controls

## Switch Mode

Press:

```
M
```

to switch between:

- Mouse Mode
- Presentation Mode

---

## Exit

Press:

```
Q
```

to close the application.

---

# 📸 How to Use

1. Launch the application.
2. Allow webcam access if prompted.
3. Place your hand inside the camera frame.
4. Move your index finger to control the cursor.
5. Perform supported gestures for clicking, dragging, scrolling, or presentation control.
6. Press **M** to change modes.
7. Press **Q** to quit.

---

# ⚠ Notes

- Ensure good lighting for accurate hand detection.
- Keep your hand fully visible inside the webcam frame.
- Avoid cluttered backgrounds for better tracking.
- Maintain a moderate distance from the webcam.
- On macOS, grant Accessibility and Input Monitoring permissions before using the application.

---

# 🔮 Future Improvements

- Air Drawing Mode
- Media Controls
- Volume Control
- Gesture Calibration
- Custom Gesture Mapping
- Multi-Hand Support
- Performance Optimization
- Settings Panel

---

# 🤝 Contributing

Contributions are welcome.

If you have ideas for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

GesturePilot was developed as a Computer Vision project using Python, OpenCV, and MediaPipe to explore touch-free human-computer interaction through hand gesture recognition.