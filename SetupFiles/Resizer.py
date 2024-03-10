import os
from PIL import Image

def resize_and_label_images(input_folder, output_folder, label, size=(128, 128)):
    """
    Resize and label images in a specified folder.

    Parameters:
    - input_folder: Path to the folder containing input images.
    - output_folder: Path to the folder where resized and labeled images will be saved.
    - label: A label to append to each image's filename.
    - size: A tuple specifying the size to which images will be resized.
    """
    # Ensure the size parameter is a tuple with two integers
    assert isinstance(size, tuple) and len(size) == 2, "Size must be a tuple with two integers."

    # Check if the output folder exists, create if it does not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    processed_images_count = 0

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue  # Skip non-image files
        
        try:
            # Open the image
            filepath = os.path.join(input_folder, filename)
            with Image.open(filepath) as img:
                # Resize the image using the specified filter for better quality
                img = img.resize(size, Image.Resampling.LANCZOS)
                
                # Convert the image to RGB if it is in a different mode to ensure JPEG compatibility
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Generate new filename with label
                base, _ = os.path.splitext(filename)
                new_filename = f"{base}_{label}.jpg"  # Saving as JPEG
                
                new_filepath = os.path.join(output_folder, new_filename)
                
                # Save the resized and potentially converted image in the output folder
                img.save(new_filepath, 'JPEG')
                processed_images_count += 1

        except Exception as e:
            print(f"Error processing {filename}: {e}")

    print(f"Processed {processed_images_count} images.")

# Define your input folder, output folder, and label
input_folder = './Pisa'
output_folder = './201052'  # Changed to a more descriptive folder name
label = '201052'
size = (128, 128)  # Specify the desired image size as a tuple

# Call the function
resize_and_label_images(input_folder, output_folder, label, size)
