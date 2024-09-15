import zipfile
import os

def create_submission():
    hands_on_dir = 'hands-on'  # Define the directory to zip
    with zipfile.ZipFile('hands_on.zip', 'w') as zf:  # Output zip file name
        for root, dirs, files in os.walk(hands_on_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Calculate relative path to store files in the zip with correct structure
                arcname = os.path.relpath(file_path, hands_on_dir)
                print(f"Adding {file_path} as {arcname}")  # Debug statement to see which files are being added
                zf.write(file_path, arcname)

    print("Created submission archive: hands_on.zip")

if __name__ == "__main__":
    create_submission()