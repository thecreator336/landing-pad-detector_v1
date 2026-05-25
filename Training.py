import json
import os
import numpy as np
import shutil

input_dir = "C:/landing_dataset"
output_dir = "C:/yolo_dataset"
img_w = 640
img_h = 480

os.makedirs(f"{output_dir}/images", exist_ok=True)
os.makedirs(f"{output_dir}/labels", exist_ok=True)

for i in range(100):
    frame_id = f"{i:04d}"

    npy_path   = os.path.join(input_dir, f"bounding_box_2d_tight_{frame_id}.npy")
    label_path = os.path.join(input_dir, f"bounding_box_2d_tight_labels_{frame_id}.json")
    img_path   = os.path.join(input_dir, f"rgb_{frame_id}.png")

    if not os.path.exists(npy_path) or not os.path.exists(label_path):
        print(f"Skipping frame {frame_id} — files missing")
        continue

    boxes = np.load(npy_path)

    with open(label_path) as f:
        labels = json.load(f)

    label_lines = []

    for box in boxes:
        semantic_id = str(box["semanticId"])
        class_name = labels.get(semantic_id, {}).get("class", "")

        if class_name != "landing_pad":
            continue

        x1, y1, x2, y2 = box["x_min"], box["y_min"], box["x_max"], box["y_max"]

        cx = ((x1 + x2) / 2) / img_w
        cy = ((y1 + y2) / 2) / img_h
        w  = (x2 - x1) / img_w
        h  = (y2 - y1) / img_h

        label_lines.append(f"0 {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}")

    if label_lines:
        with open(f"{output_dir}/labels/rgb_{frame_id}.txt", "w") as f:
            f.write("\n".join(label_lines))
        shutil.copy(img_path, f"{output_dir}/images/rgb_{frame_id}.png")
        print(f"Frame {frame_id} converted")
    else:
        print(f"Frame {frame_id} — no landing pad found")

print("Done — check C:/yolo_dataset")