# Medical Image Classification — AI Diagnostic Tool

An automated medical imaging analysis system that uses a hybrid deep learning 
pipeline combining YOLO for region detection and CNN-based classification for 
identifying and counting blood cells in microscopic images. A Streamlit interface 
makes the system accessible to non-technical users without requiring any ML expertise.

---

## How It Works

1. Input medical image is passed to the pipeline
2. YOLO (via Darkflow) performs region detection — identifying areas of interest
3. CNN classifier processes detected regions and classifies cell types
4. KNN is used for additional classification validation
5. Results are displayed via a real-time Streamlit interface

---

## Features

- Hybrid detection + classification pipeline (YOLO + CNN)
- Automated blood cell identification and counting
- Data preprocessing and augmentation for improved model accuracy
- Real-time diagnostic interface via Streamlit
- Model performance validated on accuracy and precision metrics

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Object Detection | YOLO via Darkflow |
| Classification | CNN, KNN |
| Deep Learning Framework | TensorFlow |
| Preprocessing | Python, NumPy |
| Frontend | Streamlit |
| Language | Python, Cython |

---

## 📁 Project Structure

Automated-Analysis-Of-Medical-Imaging/
├── app.py              # Streamlit web application & interactive user dashboard
├── detect.py           # Core YOLOv2 object detection & cellular localization logic
├── predict_HRI.py      # Custom CNN (Convolutional Neural Network) prediction pipeline
├── test.py             # Model verification and performance testing scripts
├── utils.py            # Image processing helper functions & matrix utilities
├── setup.py            # Cython build configuration for C-optimized execution speeds
├── build.sh            # Shell automation script to compile C-extensions locally
├── flow                # Darkflow execution entry point for running network logic
├── labels.txt          # Class target labels (e.g., cell types, RBC, WBC counts)
├── cmd.txt             # Command-line execution logs and reference guide
├── cfg/                # YOLO network architecture configuration files (.cfg)
├── darkflow/           # Core Darkflow framework code parsing YOLO into TensorFlow
├── data/               # Raw sample medical images and training/validation datasets
├── output/             # Processed images featuring bounding boxes & analytical metrics
├── preprocess/         # Custom scripts for image normalization and data augmentation
├── weights/            # Pre-trained deep learning binary model weights (.weights)
├── build/              # Output directory for the compiled C-optimized Cython files
├── runtime.txt         # Hosting environment execution specifications
└── requirements.txt    # Project framework dependencies and version controls

---

## Setup & Installation

```bash
git clone https://github.com/RaghuSharma14/Automated-Analysis-Of-Medical-Imaging.git
cd Automated-Analysis-Of-Medical-Imaging
pip install -r requirements.txt
python setup.py build_ext --inplace
streamlit run app.py
```

---

## Author

**Raghu Sharma**  
B.Tech CSE (AI/ML) — Maharaja Surajmal Institute of Technology, Delhi  
raghusharma1430@gmail.com 