import os

def write_structure_to_file(folder_path, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk(folder_path):
            level = root.replace(folder_path, "").count(os.sep)
            indent = " " * (level * 4)
            f.write(f"{indent}[{os.path.basename(root)}]\n")
            sub_indent = " " * ((level + 1) * 4)
            for file in files:
                f.write(f"{sub_indent}{file}\n")

if __name__ == "__main__":
    folder_path = input("Введите путь к папке: ")
    output_file = "folder_structure.txt"
    write_structure_to_file(folder_path, output_file)
    print(f"Структура папки записана в {output_file}")