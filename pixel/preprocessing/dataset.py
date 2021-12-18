import os

from pixel.utils.file import md5_file
from image import convert_image_to_jpg
from pathlib import Path

from PIL import Image


def create_from_directory(input_directory, output_directory, labels=(), result_size=(64, 64)) -> None:
    # Check if input directory exists
    if os.path.exists(input_directory) is False:
        raise Exception("Input directory does not exist")

    # Check if output directory exists
    if os.path.exists(output_directory) is True:
        raise Exception("Output directory already exists")

    for label in labels:
        input_label_directory = os.path.join(input_directory, label)
        output_label_directory = os.path.join(output_directory, label)

        create_from_directory_by_label(input_label_directory, output_label_directory, result_size)


def create_from_directory_by_label(input_label_directory, output_label_directory, result_size=(64, 64),
                                   resample=Image.ANTIALIAS) -> None:
    # Check if input label directory exists
    if os.path.exists(input_label_directory) is False:
        raise Exception("Input label directory does not exist. Directory is {}".format(input_label_directory))

    # Create output label directory
    Path(output_label_directory).mkdir(parents=True, exist_ok=True)

    # Load recursive files in input label directory
    for file in Path(input_label_directory).rglob('*'):

        try:
            # Count MD5 hash
            md5_hash = md5_file(file)
            output_file = os.path.join(output_label_directory, md5_hash[0:8] + '.jpg')

            # Convert image to jpg
            convert_image_to_jpg(file, output_file, result_size, resample)

        except ValueError:
            pass

        except FileNotFoundError as e:
            raise e
