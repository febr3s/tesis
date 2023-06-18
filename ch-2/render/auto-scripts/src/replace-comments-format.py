import os

# Set the directory to search for Markdown files
directory = "/home/febres/Documents/temp/minas-aguas/ch-2/ch2-pre-render/outline/0-Ch2-_una_vacuna_contra_la_inteligencia_de_las_m-quinas"

# Function to replace <<- and ->> with <!-- and -->
def replace_tags(text):
    return text.replace("<<-", "<!--").replace("->>", "-->")

# Loop through each Markdown file in the directory and its subdirectories
for subdir, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".md"):
            # Read the contents of the file
            with open(os.path.join(subdir, file), "r") as f:
                contents = f.read()

            # Replace <<- and ->> with <!-- and -->
            modified_contents = replace_tags(contents)

            # Write the modified contents back to the file
            with open(os.path.join(subdir, file), "w") as f:
                f.write(modified_contents)
