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

## Project Structure
Automated-Analysis-Of-Medical-Imaging/
├── app.py              # Streamlit frontend
├── detect.py           # YOLO detection logic
├── predict_HRI.py      # CNN prediction pipeline
├── test.py             # Model testing scripts
├── utils.py            # Utility functions
├── setup.py            # Cython build setup
├── build.sh            # Build script
├── flow                # Flow execution entry
├── labels.txt          # Class labels
├── cmd.txt             # Command reference
├── cfg/                # YOLO config files
├── darkflow/           # Darkflow YOLO framework
├── data/               # Sample input data
├── output/             # Detection outputs
├── preprocess/         # Data preprocessing scripts
├── weights/            # Model weight files
├── build/              # Compiled Cython build
├── runtime.txt         # Runtime configuration
└── requirements.txt    # Dependencies

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
[GitHub](https://github.com/RaghuSharma14) | raghusharma1430@gmail.com