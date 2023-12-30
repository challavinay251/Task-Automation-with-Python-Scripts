import os
import shutil

def organize_files(source_folder, destination_folder):
    # Create a dictionary to map file extensions to their respective folders
    file_types = {
        '.txt': 'TextFiles',
        '.docx': 'WordFiles',
        '.jpg': 'ImageFiles',
        '.mp4': 'VideoFiles',
        # Add more file types and corresponding folders as needed
    }

    # Ensure destination folders exist; create them if not
    for folder in file_types.values():
        folder_path = os.path.join(destination_folder, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Check if it's a file
        if os.path.isfile(source_path):
            # Get the file extension
            _, file_extension = os.path.splitext(filename)

            # Find the destination folder for the file type
            destination_folder_type = file_types.get(file_extension.lower(), 'OtherFiles')

            # Construct the destination path
            destination_path = os.path.join(destination_folder, destination_folder_type, filename)

            try:
                # Move the file to its designated folder
                shutil.move(source_path, destination_path)
                print(f"Moved: {filename} to {destination_folder_type}")
            except shutil.Error as e:
                print(f"Error moving {filename}: {e}")

if __name__ == "__main__":
    # Specify the source and destination folders
    source_folder_path = r'D:\New folder'  # Use raw string to avoid escape characters
    destination_folder_path = r'D:\Destination folder'

    # Call the function to organize files
    organize_files(source_folder_path, destination_folder_path)
