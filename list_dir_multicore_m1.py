import os
import multiprocessing

def list_files_in_folder(folder):
    """
    This function lists all files within a folder.
    """
    files = []
    for root, directories, filenames in os.walk(folder):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

def process_folder(folder):
    """
    This function processes a folder to list all files.
    """
    files = list_files_in_folder(folder)
    for file_path in files:
        print("File:", file_path)

def list_files_multicore(target_folder):
    """
    This function lists all files within a target folder
    using multiple cores for processing.
    """
    if not os.path.exists(target_folder):
        print("The target folder does not exist.")
        return

    # Get the number of available CPU cores
    num_cores = multiprocessing.cpu_count()

    # Create a process pool
    ctx = multiprocessing.get_context("spawn")
    pool = ctx.Pool(num_cores)

    # Map the process_folder function to each folder in the target folder
    pool.map(process_folder, [target_folder])

    # Close the pool
    pool.close()
    pool.join()

# Example of using the function with a target folder
target_folder = "/"  # Put the path of your folder here
list_files_multicore(target_folder)
