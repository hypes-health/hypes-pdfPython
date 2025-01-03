import os

def rename_files(directory, fixed_name):
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files.sort()  # Optional: Sort files to ensure consistent renaming order

    # Rename each file
    for idx, file in enumerate(files, start=1):
        # Get the file extension
        _, file_extension = os.path.splitext(file)

        # Construct the new name
        new_name = f"{fixed_name}_{idx}{file_extension}"

        # Rename the file
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)

        print(f"Renamed: {file} -> {new_name}")

# Example usage
directory = "./your_folder_path"  # Replace with the path to your folder
fixed_name = "document"          # Replace with your desired fixed name
rename_files(directory, fixed_name)
