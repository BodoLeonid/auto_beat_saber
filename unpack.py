import os
import zipfile
import rarfile
import shutil
from config import *


def unpack():
    destination_folder = UNPACKED_PATH
    downloads_folder = os.path.expanduser(INPUT_PATH)
    extract_folder = os.path.join(downloads_folder, "Extracted_Archives")

    os.makedirs(extract_folder, exist_ok=True)
    files = os.listdir(downloads_folder)

    for file in files:
        file_path = os.path.join(downloads_folder, file)

        if file.lower().endswith(".zip") or file.lower().endswith(".rar"):
            folder_name = os.path.splitext(file)[0]
            extract_path = os.path.join(extract_folder, folder_name)

            os.makedirs(extract_path, exist_ok=True)

            if file.lower().endswith(".zip"):
                with zipfile.ZipFile(file_path, "r") as zip_ref:
                    zip_ref.extractall(extract_path)
                print(f"ZIP распакован: {file} -> {extract_path}")

            elif file.lower().endswith(".rar"):
                with rarfile.RarFile(file_path, "r") as rar_ref:
                    rar_ref.extractall(extract_path)
                print(f"RAR распакован: {file} -> {extract_path}")

    for folder in os.listdir(extract_folder):
        src_path = os.path.join(extract_folder, folder)
        dest_path = os.path.join(destination_folder, folder)

        counter = 1
        while os.path.exists(dest_path):
            dest_path = os.path.join(destination_folder, f"{folder}_{counter}")
            counter += 1

        shutil.move(src_path, dest_path)
        print(f"📂 Перемещено: {src_path} -> {dest_path}")

    print("Все файлы успешно распакованы и перемещены")


if __name__ == "__main__":
    unpack()
