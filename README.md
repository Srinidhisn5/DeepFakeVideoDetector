# DeepFakeVideoDetector
DeepFake Video Detector is a Flask-based web application that identifies whether a given video has been tampered with using face-swap deepfake techniques. It leverages a trained GRU-based neural network model to analyze sequences of frames and predict authenticity. 
# 🎭 DeepFake Video Detection

**DeepFake Video Detection** is a Flask-based web application that detects whether a video is real or deepfake using a pre-trained GRU-based neural network. The app is lightweight, user-friendly, and supports both local and cloud-based deployment.

---

## 🚀 Features

- Upload any video and detect if it’s deepfake
- Pre-trained GRU model for binary classification (Real/Fake)
- Simple and interactive web interface
- Real-time prediction with confidence output
- Works fully offline once set up locally

---

## 🛠 Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python 3.10, Flask  
- **ML Model**: Keras (GRU architecture)  
- **Environment**: Anaconda  
- **Deployment**: Localhost / Cloud-ready

---

## ⚙️ Environment Setup

> **Note**: Jupyter Notebook is **not used** in this project.

### 1️⃣ Prerequisites

- Anaconda installed
- Python 3.10
- `requirements.txt` file in project root

### 2️⃣ Setup Instructions

Open Anaconda Prompt and follow these steps:

```bash
# Step 1: Create virtual environment
conda create -n deepfakedetection python=3.10

# Step 2: Activate the environment
conda activate deepfakedetection

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the application
python app.py
