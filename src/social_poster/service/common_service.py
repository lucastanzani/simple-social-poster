import io
from tempfile import NamedTemporaryFile

import requests
from PIL import Image


def download_image(image_url: str) -> str:
	img_data = requests.get(image_url).content
	suffix = next(
		(item for item in ['.png', '.jpg', '.svg', '.webp'] if item in image_url),
		'.jpg'
	)
	image = Image.open(io.BytesIO(img_data))
	temp_file = NamedTemporaryFile(suffix=suffix, delete=False)
	image.save(temp_file.name)
	return temp_file.name
