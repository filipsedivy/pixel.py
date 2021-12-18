import os
from filetype import helpers
from PIL import Image


def convert_image_to_jpg(input_path, output_path, result_size=(64, 64), resample=Image.ANTIALIAS) -> None:
    if os.path.isfile(input_path) is False:
        raise FileNotFoundError(f"{input_path} is not a file")

    if os.path.isfile(output_path) is True:
        raise FileExistsError(f"{output_path} already exists")

    if helpers.is_image(input_path) is False:
        raise ValueError(f"{input_path} is not an image")

    image = Image.open(input_path)

    if image.mode != "RGB":
        image = image.convert("RGB")

    if result_size is not None:
        image.thumbnail(result_size, resample)

    # Save image
    image.save(output_path)
