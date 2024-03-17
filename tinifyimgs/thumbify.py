import os
import tinify
from PIL import Image
import io
from secret import TINIFY_API_KEY

tinify.key = TINIFY_API_KEY

def resize_and_compress(input_path, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_path):
        if filename.endswith(".webp"):
            input_file = os.path.join(input_path, filename)
            filename_without_extension, extension = os.path.splitext(filename)
            output_filename = f"{filename_without_extension}_thumb{extension}"
            output_file = os.path.join(output_directory, output_filename)
            source = tinify.from_file(input_file)
            resized = source.resize(method="scale", width=500)
            resized.to_file(output_file)
            print(f"{filename} processed")

if __name__ == "__main__":
    input_directory = input("Paste the input image directory path: ")
    output_directory = input_directory
    resize_and_compress(input_directory, output_directory)
    print(f"Output saved to: {output_directory}")
