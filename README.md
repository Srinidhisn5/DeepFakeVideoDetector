🎭 DeepFake Video Detection
This project is a full-stack web application that uses a pre-trained neural network model to determine whether an uploaded video is real or deepfake. Built using Flask, it supports local and cloud deployment

🚀 Environment Setup
# Create & activate conda environment
conda create -n deepfakedetection python=3.10
conda activate deepfakedetection

# Navigate to project directory
cd DeepFakeVideoDetection

# Install dependencies
pip install -r requirements.txt

🖥 How to Run
bash
Copy
Edit

# Run the Flask web app
python app.py
Then open your browser and visit:
➡️ http://127.0.0.1:5000/

💡 Features
📂 Upload and analyze videos for deepfake detection

🤖 Real vs Fake prediction using a trained GRU-based deep learning model

📊 Displays confidence level of prediction

🎨 Stylish glitch-themed animated interface

🧠 Model pre-trained on Kaggle deepfake datasets

☁️ Easily deployable locally or to the cloud

📁 Folder Structure
php
Copy
Edit
DeepFakeVideoDetection/
├── app.py                     # Main Flask backend script
├── requirements.txt          # Python dependencies
├── Procfile                  # For cloud deployment (e.g., Heroku)
├── templates/                # HTML templates (Jinja2)
│   └── *.html
├── static/                   # Static files (CSS, JS, animations)
│   ├── css/
│   └── js/
├── model/
│   └── deepfake_video_model.h5  # Pre-trained GRU model
├── dataset/
│   └── sample_submission.csv (optional)
├── screenshots/
│   └── screenshot_*.png      # Screenshots used in README
├── notebook/
│   └── *.ipynb               # Jupyter notebooks (for experiments)
└── README.md

<p align="center">
  <img src="screenshots/screenshot_16.png" alt="Intro Animation" width="300"/><br>
  <em>Intro Animation</em>
</p>

<p align="center">
  <img src="screenshots/screenshot_17.png" alt="Upload Page" width="300"/><br>
  <em>Upload Page</em>
</p>

<p align="center">
  <img src="screenshots/screenshot_19.png" alt="Path Page" width="300"/><br>
  <em>Path Page</em>
</p>

<p align="center">
  <img src="screenshots/screenshot_20.png" alt="File Page" width="300"/><br>
  <em>File Page</em>
</p>

<p align="center">
  <img src="screenshots/screenshot_21.png" alt="File Page" width="300"/><br>
  <em>Result Page</em>
</p>


🔗 Technologies Used

Frontend    → HTML5, CSS3, JavaScript, Animated UI
Backend     → Python, Flask
Model       → GRU (Gated Recurrent Unit) Neural Network
Deployment  → Works on Localhost, Cloud-ready (e.g., Heroku)
Others      → Anaconda (Environment Management)

👨‍💻 Author
Srinidhi SN
