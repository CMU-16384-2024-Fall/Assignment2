import zipfile
import os

def create_submission():
    hands_on_dir = 'hands_on'  # Define the directory to zip
    with zipfile.ZipFile('hands_on.zip', 'w') as zf:  # Change the name of the output zip file
        for root, dirs, files in os.walk(hands_on_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Calculating relative path to store files in the zip with correct structure
                zf.write(file_path, os.path.relpath(file_path, hands_on_dir))

    print("Created submission archive: hands_on.zip")  # Updated the print statement to reflect the new zip file name

if __name__ == "__main__":
    create_submission()