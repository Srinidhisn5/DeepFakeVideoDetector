# 🕵️ DeepFake Video Detection

DeepFake Video Detection is a Flask-based web application that detects whether a video is real or manipulated (deepfake). The backend uses a **pre-trained GRU-based neural network**, making this tool ideal for forensic verification and social media authentication.

---

## 📑 Table of Contents

- ✅ [Project Overview](#-project-overview)
- 🔧 [Tech Stack](#-tech-stack)
- 🧠 [Model Architecture](#-model-architecture)
- 🚀 [Environment Setup](#-environment-setup)
- 🖥 [How to Run](#-how-to-run)
- 🖼 [Image Previews](#-image-previews)
- 💡 [Features](#-features)
- 📁 [Folder Structure](#-folder-structure)
- 👨‍💻 [Authors](#-authors)

---

## ✅ Project Overview

This project, named **DeepFake Video Detection**, aims to classify videos as **real** or **deepfake** using a GRU-based model. It's built as a full-stack Flask web app with an interactive and animated frontend.

---

## 🔧 Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript  
- **Backend:** Python (Flask)  
- **ML Model:** GRU-based neural network (`deepfake_video_model.h5`)  
- **Environment:** Anaconda, Python 3.10  
- **Deployment Ready:** Heroku (via `Procfile`) or local hosting

---

## 🧠 Model Architecture

- GRU Layer (64 units) → BatchNorm → Dropout  
- GRU Layer (32 units) → BatchNorm → Dropout  
- GRU Layer (16 units) → Dense → Sigmoid  
- Trained on real/fake video datasets from Kaggle

---

## 🚀 Environment Setup

```bash
# Create & activate conda environment
conda create -n deepfakedetection python=3.10
conda activate deepfakedetection

# Navigate to project directory
cd DeepFakeVideoDetection

# Install dependencies
pip install -r requirements.txt

## 🖥 How to Run
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000/ in your browser.

🖼 Image Previews
<p align="center"> <img src="screenshots/screenshot_16.png" alt="Intro Animation" width="300"/> <br><em>Intro Animation</em> </p> <p align="center"> <img src="screenshots/screenshot_17.png" alt="Upload Page" width="300"/> <br><em>Upload Page</em> </p> <p align="center"> <img src="screenshots/screenshot_19.png" alt="Path Page" width="300"/> <br><em>Path Page</em> </p> <p align="center"> <img src="screenshots/screenshot_20.png" alt="File Page" width="300"/> <br><em>File Page</em> </p>

💡 Features
Upload and analyze videos for deepfake detection

Displays real/fake prediction with confidence

Glitch-style animated interface

Full-stack with Flask backend and static frontend

Supports local or cloud deployment
Folder Structure
DeepFakeVideoDetection/
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│   └── *.html
├── static/
│   ├── css/
│   └── js/
├── model/
│   └── deepfake_video_model.h5
├── dataset/
│   └── [samples or submission file]
├── screenshots/
│   └── screenshot_*.png
├── notebook/
│   └── *.ipynb
└── README.md

👨‍💻 Authors
Srinidhi SN
🔗 GitHub Profile


