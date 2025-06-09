import requests
import pandas as pd
from fractions import Fraction

# Your Unsplash API key
access_key = 'eYzjJXqeLt5pA726eO1oJRTGYVzgruIhWJ8jfjroxRM'

# Prompt the user to enter the Unsplash photo ID
photo_id = input("Enter the Unsplash photo ID: ")

# Unsplash API URL for a specific photo
url = f'https://api.unsplash.com/photos/{photo_id}?client_id={access_key}'
response = requests.get(url)
photo_details = response.json()

# Extracting metadata and Unsplash URL only
metadata = {
    'id': photo_details['id'],
    'created_at': photo_details['created_at'],
    'width': photo_details['width'],
    'height': photo_details['height'],
    'color': photo_details['color'],
    'likes': photo_details['likes'],
    'user': photo_details['user']['name'],
    'exif': photo_details.get('exif', {}),
    'location': photo_details.get('location', {}),
    'unsplash_url': f'https://unsplash.com/photos/{photo_id}'  
}

# Print metadata one by one
print("\n--- Photo Metadata ---\n")
for key, value in metadata.items():
    print(f"{key}: {value}")

# Extract exposure time and aperture values from EXIF data
exposure_time = metadata['exif'].get('exposure_time', 'N/A')
aperture_value = metadata['exif'].get('aperture', 'N/A')

# Convert exposure time from fraction to float (if possible)
if exposure_time != 'N/A':
    try:
        exposure_time = float(Fraction(exposure_time))
    except Exception as e:
        print(f"Error converting exposure time: {e}")
        exposure_time = 'N/A'

# Print EXIF details (optional)
print("\n--- EXIF Data ---")
print(f"Exposure Time: {exposure_time}")
print(f"Aperture: {aperture_value}")
