import json
import sys
from rapidocr_onnxruntime import RapidOCR

if len(sys.argv) != 2:
    raise SystemExit("Usage: ocr.py <image-path>")

engine = RapidOCR()
results, elapsed = engine(sys.argv[1])
items = [
    {"text": entry[1], "confidence": float(entry[2]), "box": entry[0]}
    for entry in (results or [])
]
print(json.dumps({"text": "\n".join(item["text"] for item in items), "items": items, "elapsedSeconds": elapsed}))
