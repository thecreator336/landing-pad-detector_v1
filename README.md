# Landing Pad Detector v1

A computer vision pipeline that generates synthetic training data in NVIDIA Isaac Sim and trains a YOLOv8 model to detect landing pads from a downward-facing drone camera.

## Pipeline Overview

Isaac Sim (Replicator) → Training.py → train.py → detect.py

1. Isaac Sim generates labeled synthetic images with randomized camera positions and lighting
2. Training.py converts Isaac Sim annotations to YOLO format
3. train.py trains YOLOv8 on the converted dataset
4. detect.py runs the trained model on new images

## Requirements

pip install ultralytics numpy

## File Structure

landing-pad-detector_v1/
├── replicator_script.py   ← run inside Isaac Sim to generate dataset
├── Training.py            ← converts Isaac Sim output to YOLO format
├── train.py               ← trains YOLOv8 on the dataset
├── detect.py              ← runs detection on new images
└── dataset.yaml           ← YOLO dataset config

## Step 1 — Generate Synthetic Data
Open Isaac Sim, load your scene, and run replicator_script.py in the script editor.
Output saved to C:/landing_dataset/

## Step 2 — Convert to YOLO Format
Run: python Training.py
Output saved to C:/yolo_dataset/

## Step 3 — Train
Run: python train.py
Trained model saved to runs/detect/landing_pad_detector/weights/best.pt

## Step 4 — Detect
Run: python detect.py
Results saved to runs/detect/predict/

## Randomizations Applied
- Camera position — random X, Y, Z within range, always looking at pad
- Sun angle — random rotation simulating east to west movement
- Sun intensity — random brightness simulating different times of day
- Dome light intensity — random ambient brightness

## Built With
- NVIDIA Isaac Sim + Omniverse Replicator
- YOLOv8 (Ultralytics)
- Python 3.14
