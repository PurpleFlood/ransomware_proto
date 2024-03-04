import os

table_dir=[]
def list_files_recursive(target_folder):
    """
    This function recursively lists all files within a target folder,
    displaying the full path of each file when encountered.
    """
    if not os.path.exists(target_folder):
        print("The target folder does not exist.")
        return

    for root, directories, files in os.walk(target_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            table_dir.append(file_path)
            print("File:", file_path)

# Example of using the function with a target folder
target_folder = "./test/"  # Put the path of your folder here
list_files_recursive(target_folder)

print(table_dir)