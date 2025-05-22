# python code to select all image in a folder and convert them to a pdf
import os
from PIL import Image

# Function to convert images to a single PDF
def images_to_pdf(folder_path, output_pdf):
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    image_files.sort()  # Sort files alphabetically

    if not image_files:
        print("No images found in the folder.")
        return

    images = []
    for file in image_files:
        img_path = os.path.join(folder_path, file)
        img = Image.open(img_path).convert("RGB")
        images.append(img)

    # Save all images into a single PDF
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"PDF created successfully: {output_pdf}")

# Example usage
folder_path = "/home/artificialvira/Documents/Placement/cooper/may1_training/sql/"
output_pdf = "/home/artificialvira/Documents/Placement/cooper/may1_training/sql/Arivarasan-AI&DS-Task-3.pdf"
images_to_pdf(folder_path, output_pdf)
