import os

# Define the folder path to search for markdown files
folder_path = "/home/febres/Documents/temp/minas-aguas/ch-2/ch2-pre-render/outline/0-Ch2-_una_vacuna_contra_la_inteligencia_de_las_m-quinas"

# Loop through all files in the folder and its subfolders
for subdir, dirs, files in os.walk(folder_path):
    for file in files:
        # Check if the file is a markdown file
        if file.endswith(".md"):
            file_path = os.path.join(subdir, file)
            # Read the content of the markdown file
            with open(file_path, "r") as f:
                content = f.read()
            # Replace all instances of "[pp]" with "(pp)"
            new_content = content.replace(' [nota:', '^[')
            # Write the updated content back to the file
            with open(file_path, "w") as f:
                f.write(new_content)
