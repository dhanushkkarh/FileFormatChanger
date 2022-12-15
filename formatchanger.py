import os

# Specify the directory containing the files
directory = "D:/mini_project_submission"

# Specify the new file extension
new_extension = ".txt"

# Get a list of all files in the directory
files = os.listdir(directory)

# Loop through each file in the directory
for file in files:
    # Get the file's current extension
    extension = os.path.splitext(file)[1]
    # Check if the extension is not the same as the new extension
    if extension != new_extension:
        # Build the new file name
        new_file = file.replace(extension, new_extension)
        # Get the full path to the file
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_file)
        # Rename the file
        os.rename(old_path, new_path)
