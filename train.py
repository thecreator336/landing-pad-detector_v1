from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="C:/yolo_dataset/dataset.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    name="landing_pad_detector"
)

print("Training done!")

