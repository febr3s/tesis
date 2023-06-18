import os

def remove_metadata(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    skipping_metadata = False
    for line in lines:
        if not skipping_metadata and 'title:' in line:
            skipping_metadata = True
            continue
        elif skipping_metadata and 'charCount:' in line:
            skipping_metadata = False
            continue
        elif skipping_metadata:
            continue
        else:
            new_lines.append(line)

    with open(file_path, 'w') as f:
        f.write(''.join(new_lines))

def main():
    folder_path = '/home/febres/Documents/temp/minas-aguas/ch-2/ch2-pre-render/outline/0-Ch2-_una_vacuna_contra_la_inteligencia_de_las_m-quinas' # Replace with the path to the folder you want to process
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                remove_metadata(file_path)

if __name__ == '__main__':
    main()
