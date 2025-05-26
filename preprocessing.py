from PIL import Image
import os

def preprocess_images(input_folder, output_folder, target_size=(512, 512)):
    """
    Preprocess images by resizing them to the target size and converting to RGB.

    Args:
        input_folder (str): Path to input images folder.
        output_folder (str): Path to save processed images.
        target_size (tuple): Desired (width, height) in pixels.
    """
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            try:
                image = Image.open(input_path).convert("RGB")
                # Resize image to target size using Lanczos filter for high quality
                resized_image = image.resize(target_size, Image.LANCZOS)
                # No need to call convert again, as it's already in RGB
                # Save with the same filename (you can change extension if desired)
                output_path = os.path.join(output_folder, filename)
                resized_image.save(output_path)

                print(f"Processed and saved: {output_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    # Example usage: preprocess to 512x512
    preprocess_images("sample_data/amitis0.1", "./axEnhanced", target_size=(512, 512))
