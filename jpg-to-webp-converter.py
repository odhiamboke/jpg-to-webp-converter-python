from PIL import Image
import os

def convert_jpg_to_webp(input_path, output_path):
    """
    Convert JPG images to WebP format.

    Parameters:
        input_path (str): Path to the input JPG image file or directory.
        output_path (str): Path to save the output WebP image file or directory.
    """
    if os.path.isdir(input_path):
        # Convert all JPG files in the directory
        for file_name in os.listdir(input_path):
            if file_name.endswith('.jpg'):
                jpg_path = os.path.join(input_path, file_name)
                webp_path = os.path.join(output_path, os.path.splitext(file_name)[0] + '.webp')
                convert_single_jpg_to_webp(jpg_path, webp_path)
    elif os.path.isfile(input_path):
        # Convert a single JPG file
        convert_single_jpg_to_webp(input_path, output_path)
    else:
        print("Invalid input path.")

def convert_single_jpg_to_webp(jpg_path, webp_path):
    """
    Convert a single JPG image to WebP format.

    Parameters:
        jpg_path (str): Path to the input JPG image file.
        webp_path (str): Path to save the output WebP image file.
    """
    try:
        img = Image.open(jpg_path)
        img.save(webp_path, 'WEBP')
        print(f"Converted '{jpg_path}' to '{webp_path}' successfully.")
    except Exception as e:
        print(f"Failed to convert '{jpg_path}' to WebP format. Error: {str(e)}")

if __name__ == "__main__":
    input_path = input("Enter the path to the JPG image file or directory: ")
    output_path = input("Enter the path to save the converted WebP image file or directory: ")
    convert_jpg_to_webp(input_path, output_path)
