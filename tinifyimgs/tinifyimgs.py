import os
import tinify
from secret import TINIFY_API_KEY

tinify.key = TINIFY_API_KEY


def resize_and_compress(directory):
    thumb_directory = os.path.join(directory, "thumb")
    if not os.path.exists(thumb_directory):
        os.makedirs(thumb_directory)

    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            input_file = os.path.join(directory, filename)
            base_name, _ = os.path.splitext(filename)
            output_file = os.path.join(directory, f"{base_name}.webp")

            # Compress and save as webp
            source = tinify.from_file(input_file)
            resized = source.resize(method="scale", width=1920)
            resized.to_file(output_file)
            print(f"{filename} processed")

            # Create thumbnail
            thumbnail_file = os.path.join(thumb_directory, f"{base_name}_thumb.webp")
            resized_thumbnail = resized.resize(method="scale", width=500)
            resized_thumbnail.to_file(thumbnail_file)
            print(f"{filename} thumbnailed")


if __name__ == "__main__":
    directory_input = input("Paste the image directory path: ")
    resize_and_compress(directory_input)
    print(f"Output saved to: {directory_input}")
