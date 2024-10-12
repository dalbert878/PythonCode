import os
import shutil
from typing import Optional

def organize_files(directory: str) -> None:
    """Organizes files in the given directory into folders based on their file extensions.

    Args:
        directory (str): The path to the directory to organize files.
    """
    # Change to the specified directory
    os.chdir(directory)

    # Loop through files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Only process files (skip directories)
        if os.path.isfile(file_path):
            # Get the file extension (default to 'no_extension' if none)
            file_extension = filename.split('.')[-1] if '.' in filename else 'no_extension'
            # Create a folder for the file type if it doesn't exist
            target_folder = os.path.join(directory, file_extension)
            os.makedirs(target_folder, exist_ok=True)
            # Move the file to the corresponding folder
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"Moved: {filename} to {file_extension}/")

def main() -> None:
    """Main function to run the file organizer."""
    directory = input("Enter the directory path to organize files: ").strip()
    if os.path.isdir(directory):  # Check if the provided directory exists
        organize_files(directory)
    else:
        print("Invalid directory. Please provide a valid path.")

if __name__ == "__main__":
    main()
