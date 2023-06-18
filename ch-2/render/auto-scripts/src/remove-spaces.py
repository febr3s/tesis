import os

# Set the directory to search for Markdown files
directory = "/home/febres/Documents/temp/minas-aguas/ch-2/ch2-pre-render/outline/0-Ch2-_una_vacuna_contra_la_inteligencia_de_las_m-quinas"

# Loop through each Markdown file in the directory and its subdirectories
for subdir, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".md"):
            # Read the contents of the file
            with open(os.path.join(subdir, file), "r") as f:
                lines = f.readlines()

            # Remove leading spaces and empty lines before the first character
            modified_lines = []
            found_first_character = False
            for line in lines:
                if line.strip() or found_first_character:
                    modified_lines.append(line)
                    found_first_character = True

            # Write the modified contents back to the file
            with open(os.path.join(subdir, file), "w") as f:
                f.writelines(modified_lines)
