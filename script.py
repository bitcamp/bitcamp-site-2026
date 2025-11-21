import os
from PIL import Image
import sys

if len(sys.argv) < 2:
    print("Usage: python convert_folder.py <folder>")
    sys.exit(1)

folder = sys.argv[1]

for filename in os.listdir(folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        in_path = os.path.join(folder, filename)
        out_path = os.path.join(folder, f"{os.path.splitext(filename)[0]}.webp")

        print(f"Converting {filename} -> {out_path}")
        try:
            img = Image.open(in_path).convert("RGB")
        except Exception:
            continue
        img.save(out_path, "webp", quality=80)

print("Done!")