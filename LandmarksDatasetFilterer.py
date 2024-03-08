from pathlib import Path
import csv
import requests
from PIL import Image  # Import the Image class from PIL module

MOUNT_RUSHMORE = '43845'
EIFFEL_TOWER = '37378'
OPERA_HOUSE = '55350'
PYRAMIDS = '64325'
PARTHEON = '156556'
GEISEL = '166683'
GOLDEN_GATE = '168098'

# directory to save the images and the CSV file
data_dir = Path('data')
data_dir.mkdir(exist_ok=True)

# path to original CSV file
csv_file_path = 'train.csv'

# Define the path for the output CSV file that records downloaded images
downloaded_images_csv = data_dir / 'downloaded_images.csv'

def download_image(url, filepath):
    headers = {
        'User-Agent': 'ECE176LandmarkFilterer/1.0 (carae@ucsd.edu)'  # replace with your name and email
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # HTTPError if the response status code is 4XX/5XX
        filepath.parent.mkdir(parents=True, exist_ok=True)  # ensure the directory exists
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        # Resize the image to 128x128 using the LANCZOS filter
        img = Image.open(filepath)
        img = img.resize((128, 128), Image.Resampling.LANCZOS)
        img.save(filepath)  # Save the resized image back to the same file
        
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

desired_landmark_ids = ['70297', '104638', '55962', '158169', '179626', '129770', '108502', '109814', '103407', '55587', '77124', '90396']

# counter for each landmark ID
download_counter = {landmark_id: 0 for landmark_id in desired_landmark_ids}

with open(csv_file_path, mode='r') as file, open(downloaded_images_csv, mode='w', newline='') as out_file:
    csv_reader = csv.DictReader(file)
    fieldnames = ['id', 'filepath', 'landmark_id']
    csv_writer = csv.DictWriter(out_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    
    for row in csv_reader:
        landmark_id = row['landmark_id']
        if landmark_id in desired_landmark_ids and download_counter[landmark_id] < 100:
            image_url = row['url']
            filename = image_url.split('/')[-1]  # get filename from URL
            # modify filepath to include a subdirectory for each landmark_id
            landmark_dir = data_dir / landmark_id
            filepath = landmark_dir / filename
            
            if download_image(image_url, filepath):
                download_counter[landmark_id] += 1
                csv_writer.writerow({'id': row['id'], 'filepath': str(filepath), 'landmark_id': landmark_id})
                print(f"Downloaded {download_counter[landmark_id]} images for landmark ID {landmark_id}")

print("Download process for specified landmarks completed.")