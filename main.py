# This is a program that synchronizes two folders: source and replica. The
# program should maintain a full, identical copy of source folder at replica folder. Synchronization
# is performed at interval specified in CLI arguments and is only one way: source -> replica. File
# creation/copying/removal operations are logged into file specified in CLI arguments as well as
# printed to the console.

# Standard library imports
import argparse
import hashlib
import os
import shutil
import time

# Third-party library imports
from concurrent.futures import ThreadPoolExecutor

# parses arguments
parser = argparse.ArgumentParser(description='Synchronize replica folder to source folder.')
parser.add_argument('-s', '--source', type=str, metavar='', required=True, help='filepath of source folder')
parser.add_argument('-r', '--replica', type=str, metavar='', required=True, help='filepath of replica folder')
parser.add_argument('-i', '--interval', type=int, metavar='', required=True, help='sync interval in seconds')
parser.add_argument('-l', '--log', type=str, metavar='', required=True, help='filepath of logfile')

args = parser.parse_args()

# assigning args to variables for cleanliness and to make filenames containing "\" usable
source_path = fr"{args.source}"
replica_path = fr"{args.replica}"
sync_interval = args.interval
log_path = fr"{args.log}"


# ------ FUNCTIONS ------

# compares two files. If they are the different, replaces replica file content
def compare_files(file):
    src_file = os.path.join(source_path, file)
    rep_file = os.path.join(replica_path, file)

    # compare two files with hash
    with open(src_file, 'rb') as f1, open(rep_file, 'rb') as f2:
        with ThreadPoolExecutor(max_workers=2) as executor:
            future1 = executor.submit(hashlib.sha256, f1.read())
            future2 = executor.submit(hashlib.sha256, f2.read())
            if future1.result().hexdigest() != future2.result().hexdigest():
                copypaste_file_content(src_file, rep_file)

# copies content from source folder file to existing replica folder file, logs it
def copypaste_file_content(src_file, rep_file):
    shutil.copyfile(src_file, rep_file)
    log_operation(f"Copied {src_file} to", rep_file)

# creates a file in the replica folder by copying it from the source folder, logs it
def create_file(file):
    src_path = os.path.join(source_path, file)
    dest_path = os.path.join(replica_path, file)

    if os.path.isfile(src_path):
        shutil.copy2(src_path, dest_path)
    elif os.path.isdir(src_path):
        os.mkdir(dest_path)

    log_operation("Created", dest_path)

# creates empty base folders/file as needed
def create_logfile(path):
    if not os.path.exists(path):
        with open(log_path, mode='a'): pass

    log_operation("Created", path)

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

    log_operation("Created", path)

# takes a directory path as input and returns a list of relative file paths for all files in that
# directory and its subdirectories
def get_files_recursive(directory):
    files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            if not dirname.startswith('.'):
                files.append(os.path.relpath(os.path.join(dirpath, dirname), directory))
        for filename in filenames:
            if not filename.startswith('.'):
                files.append(os.path.relpath(os.path.join(dirpath, filename), directory))
    return files

#  Adds performed operation to log file and prints it to console.
def log_operation(operation, item):
    # define log message
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    message = f"{now} | {operation} {item}"

    # log to log file
    with open(log_path, 'a') as f:
        f.write(message + '\n')

    # log to console
    print(message)

# removes a file from replica folder (used if file not in source folder), logs it
def remove_file(file):
    filepath = os.path.join(replica_path, file)

    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

    log_operation("Removed", filepath)


# ------ MAIN LOOP ------

if __name__ == '__main__':

    executor = ThreadPoolExecutor(max_workers=2)

    # create base folders or file if they do not already exist
    create_dir(source_path)
    create_dir(replica_path)
    create_logfile(log_path)

    # repeats according to the sync_interval
    while True:
        source_files = get_files_recursive(source_path)
        replica_files = get_files_recursive(replica_path)

        # Check for files that need to be created/updated in replica folder
        for file in source_files:
            if file not in replica_files:
                create_file(file)
            # if file is a file (not directory) checks for differences in source and replica files
            # and updates the replica file if necessary
            elif os.path.isfile(os.path.join(source_path, file)):
                # Pass the executor object as an argument to the function call
                executor.submit(compare_files, file)

        # Check for files that need to be deleted from replica folder
        for file in replica_files:
            if file not in source_files:
                remove_file(file)

        # Check for files that need to be deleted from replica folder
        for file in replica_files:
            if file not in source_files:
                remove_file(file)

        time.sleep(sync_interval)
