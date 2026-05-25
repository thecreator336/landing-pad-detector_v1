from ultralytics import YOLO
import os

model = YOLO("C:/Users/epity/OneDrive/Documents/Isaac_Sim/runs/detect/landing_pad_detector-4/weights/best.pt")

results = model.predict(
    source="C:/yolo_dataset/images",
    save=True,
    conf=0.25
)

for r in results:
    print("Image:", r.path)
    print("Boxes found:", len(r.boxes))

print("Saved to:", os.path.abspath("runs/detect/predict"))