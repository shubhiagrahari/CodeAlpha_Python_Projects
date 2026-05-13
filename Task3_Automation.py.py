import os
import shutil

def automate_file_movement():
    print("--- Task Automator: JPG File Mover ---")
    
    # 1. Define source folder (defaults to the current working directory)
    source_folder = input("Enter the path of the source folder (Press Enter to use the current folder): ").strip()
    if not source_folder:
        source_folder = os.getcwd()

    # 2. Define the new destination folder
    destination_folder = os.path.join(source_folder, "Organized_JPGs")

    # Create the destination folder if it doesn't already exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"\nCreated new folder: {destination_folder}")
    else:
        print(f"\nFolder already exists: {destination_folder}")

    moved_count = 0

    print(f"Scanning '{source_folder}' for .jpg files...\n")

    # 3. Loop through files and move them
    for filename in os.listdir(source_folder):
        # Check if it's a file (not a folder) and ends with .jpg or .jpeg
        if os.path.isfile(os.path.join(source_folder, filename)) and \
           (filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg")):
            
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            
            try:
                # Move the file
                shutil.move(source_path, destination_path)
                print(f"Successfully moved: {filename}")
                moved_count += 1
            except Exception as e:
                print(f"Error moving {filename}: {e}")

    # Final Summary
    print(f"\nTask Complete! Automatically moved {moved_count} .jpg file(s) to the new folder.")

if __name__ == "__main__":
    automate_file_movement()