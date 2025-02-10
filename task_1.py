import os
import shutil
import argparse

def copy_and_sort_files(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        print(f'Destination {dest_dir} does not exist, creating it.')
        os.makedirs(dest_dir)

    try:
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            if os.path.isdir(item_path):
                # Recursive call for nested directories
                copy_and_sort_files(item_path, dest_dir)  
            else:
                file_ext = os.path.splitext(item)[-1].lower()
                ext_dir = os.path.join(dest_dir, file_ext[1:] if file_ext else "unknown")

                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)

                try:
                    # Copy the file to the appropriate folder
                    shutil.copy2(item_path, os.path.join(ext_dir, item))  
                except Exception as e:
                    print(f"Copy error '{item_path}': {e}")

    except Exception as e:
        print(f"Processing error '{src_dir}': {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recursive copying and sorting of files by extension.")
    parser.add_argument("src", help="Output directory")
    parser.add_argument("dest", nargs="?", default="dist", help="Destination directory (default: dist)")

    args = parser.parse_args()

    if not os.path.exists(args.src) or not os.path.isdir(args.src):
        print("The specified output directory does not exist or is not a directory.")
    else:
        copy_and_sort_files(args.src, args.dest)
