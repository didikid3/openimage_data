import os
import csv

image_dir = "./validation/data"
csv_file = "HIT.csv"

BASE_URL = "https://raw.githubusercontent.com/didikid3/openimage_data/master/open-images-v7/validation/data"

image_files = []
valid_exts = {".jpg", ".jpeg", ".png", ".bmp"}

for root, dirs, files in os.walk(image_dir):
        for filename in files:
            ext = os.path.splitext(filename.lower())[1]
            if ext in valid_exts:
                image_files.append(filename)

with open(csv_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["image_url"])
    for image_file in image_files:
        url = f"{BASE_URL}/{image_file}"
        writer.writerow([url])
