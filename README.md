📷 Unsplash Photo Metadata 
This is a simple Python script that fetches and displays metadata (EXIF data and more) of a specific photo from Unsplash using its API.
You just provide the Unsplash photo ID, and the script retrieves useful details like image size, author, exposure time, aperture, location, and more.     
✨ Features
✅ Fetches detailed metadata of a given Unsplash photo

✅ Extracts EXIF data (exposure time, aperture, etc.)

✅ Displays photo URL and author info

✅ Converts exposure time to float value if possible

✅ Works from the command line — simple & fast!



	
🛠️ Requirements
Python 3.x

requests library

pandas library (used here but not strictly required for this version)

fractions (standard library)

Using pip3 to install the all liabaries for the project

🚀 Demo

$ python unsplash_metadata_fetcher.py
Enter the Unsplash photo ID: aBcDeFg1234

--- Photo Metadata ---

id: aBcDeFg1234

created_at: 2024-06-09T12:34:56Z

width: 4000

height: 3000

color: #aabbcc

likes: 150

user: John Doe

exif: {...}

location: {...}

unsplash_url: https://unsplash.com/photos/aBcDeFg123


--- EXIF Data ---
Exposure Time: 0.008

Aperture: f/2.8
