from ultralytics import YOLO

model = YOLO("yolov8s.pt")

model.train(
    data="data.yaml",
    epochs=150,
    imgsz=640,
    batch=4,
    device="mps",
    workers=0,
    name="sportifyai_model"
)

print("Training Completed!")




