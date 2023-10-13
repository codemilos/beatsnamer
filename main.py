import os
import shutil
import random
import string

def generate_random_string(length=8):
    """Generate a random string of specified length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def rename_winrar_archives(folder_path):
    try:
        # Convert the entered path to an absolute path
        folder_path = os.path.abspath(folder_path)

        # Change to the specified folder
        os.chdir(folder_path)

        # Get a list of files in the current directory
        files = os.listdir()

        # Filter only directories that end with ".rar"
        winrar_archives = [archive for archive in files if os.path.isdir(archive) and archive.lower().endswith('.rar')]

        if not winrar_archives:
            print("No WinRAR archives found.")
            return

        # Ask the user if they want to proceed
        response = input(f"Do you want to rename {len(winrar_archives)} WinRAR archives? (yes/no): ").lower()

        if response != 'yes':
            print("Operation canceled.")
            return

        # Rename each WinRAR archive to a random name
        for archive in winrar_archives:
            new_name = generate_random_string()
            os.rename(archive, new_name + '.rar')
            print(f"Renamed '{archive}' to '{new_name}.rar'.")

        print("Renaming complete.")

    except FileNotFoundError:
        print("Folder not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for a folder path
folder_path = input("Enter the folder path: ")

# Rename WinRAR archives in the specified folder
rename_winrar_archives(folder_path)
