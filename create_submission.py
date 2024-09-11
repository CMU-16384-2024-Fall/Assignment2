import zipfile
import os

def create_submission():
    with zipfile.ZipFile('handin.zip', 'w') as zf:
        # Adding the entire ex1 folder and its contents to the zip
        for root, dirs, files in os.walk('ex1'):
            for file in files:
                file_path = os.path.join(root, file)
                zf.write(file_path, os.path.relpath(file_path, os.path.join('ex1', '..')))
        
        # Adding the entire ex2 folder and its contents to the zip
        for root, dirs, files in os.walk('ex2'):
            for file in files:
                file_path = os.path.join(root, file)
                zf.write(file_path, os.path.relpath(file_path, os.path.join('ex2', '..')))
                
    print("Created submission archive: handin.zip")

if __name__ == "__main__":
    create_submission()