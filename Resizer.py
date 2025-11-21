import os
from PIL import Image
import sys

if len(sys.argv) < 2:
    print("Usage: python convert_proportional.py <folder>")
    sys.exit(1)

folder = sys.argv[1]

for filename in os.listdir(folder):
    if filename.lower().endswith(".webp"):
        path = os.path.join(folder, filename)

        print(f"Resizing proportionally: {filename}")

        img = Image.open(path).convert("RGBA")

        # Scale proportionally
        img.thumbnail((256, 256), Image.LANCZOS)

        # Create 256x256 canvas
        canvas = Image.new("RGBA", (256, 256), (0, 0, 0, 0))   # transparent

        # Center the image on the canvas
        x = (256 - img.width) // 2
        y = (256 - img.height) // 2
        canvas.paste(img, (x, y))

        # Save over the original
        canvas.save(path, "webp", quality=90)

print("Done!")