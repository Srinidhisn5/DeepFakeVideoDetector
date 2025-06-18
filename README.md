🎭 DeepFake Video Detection – AI-Powered Video Forensics  
A full-stack AI web application that detects whether a video is real or deepfake using a GRU-based deep learning model. Built with Flask, HTML/CSS, and JavaScript. Features an animated glitch-style UI and supports both local and cloud deployment.

---

🚀 Features  
🔍 Upload & Analyze Any Video File  
🧠 GRU Neural Network-Based DeepFake Detection  
📈 Confidence Level of Prediction  
📸 Real-Time Feedback with Animated UI  
🧰 Flask Backend + Jinja Templating  
💾 Model Trained on Kaggle DeepFake Dataset  
☁️ Easy Cloud Deployment via Heroku

---

📂 Project Structure  
📁 DeepFakeVideoDetection                # Root project folder  
│  
├── app.py                              # Flask backend entry point  
├── requirements.txt                    # Python dependencies  
├── Procfile                            # Heroku deployment config  
│  
├── templates/                          # Jinja2 HTML templates  
│   ├── index.html                      # Landing page  
│   ├── upload.html                     # Upload page  
│   ├── result.html                     # Prediction result page  
│  
├── static/                             # Static files (CSS, JS, Animations)  
│   ├── css/                            # Stylesheets  
│   │   └── style.css  
│   └── js/                             # Scripts  
│       └── main.js  
│  
├── model/                              # ML model  
│   └── deepfake_video_model.h5         # Pre-trained GRU model  
│  
├── dataset/                            # Sample data  
│   └── sample_submission.csv  
│  
├── screenshots/                        # Screenshots for README  
│   ├── screenshot_16.png               # Intro Animation  
│   ├── screenshot_17.png               # Upload Page  
│   ├── screenshot_19.png               # Path Page  
│   └── screenshot_20.png               # Result Page  
│  
└── README.md                           # This file

---

⚙️ Installation  
🔹 1. Clone the Repository  
```bash
git clone https://github.com/YourUsername/DeepFakeVideoDetection.git  
cd DeepFakeVideoDetection

🔹 2. Set Up Environment
Install Anaconda and run:

bash
Copy
Edit
conda create -n deepfakedetection python=3.10  
conda activate deepfakedetection  
pip install -r requirements.txt  
🔹 3. Run the Application

bash
Copy
Edit
python app.py  
Then visit: http://localhost:5000

