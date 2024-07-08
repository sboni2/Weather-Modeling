import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

def fetch_weather_model_image(url):
    try:
        # Fetch image from URL
        response = requests.get(url)
        if response.status_code == 200:
            # Read image from response content
            img = Image.open(BytesIO(response.content))
            return img
        else:
            print(f"Failed to fetch image. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_weather_model_image(image):
    if image:
        plt.figure(figsize=(8, 6))
        plt.imshow(image)
        plt.axis('off')
        plt.title('Weather Model Image')
        plt.show()

# Example usage:
weather_model_url = '	https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlORD7P-MXjyXYR388AmMy4DCrpKc7wKmA9w&s'
weather_image = fetch_weather_model_image(weather_model_url)
display_weather_model_image(weather_image)
