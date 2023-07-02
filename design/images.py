import requests
from PIL import Image
from io import BytesIO

def get_image(url):
    image_url = url
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))
    return image

