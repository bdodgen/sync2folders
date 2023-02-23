# TODO: Please implement a program that synchronizes two folders: source and replica. The
#  program should maintain a full, identical copy of source folder at replica folder.
#
# TODO: Synchronization must be one-way: after the synchronization content of the replica
#  folder should be modified to exactly match content of the source folder
#
# DONE: Synchronization should be performed periodically.
#
# TODO: File creation/copying/removal operations should be logged to a file and to the
#  console output
#
# DONE: Folder paths, synchronization interval and log file path should be provided using the
#  command line arguments


# This is a program that synchronizes two folders: source and replica. The
# program should maintain a full, identical copy of source folder at replica folder. Synchronization
# is performed at interval specified in CLI arguments and is only one way: source -> replica. File
# creation/copying/removal operations are logged into file specified in CLI arguments as well as
# printed to the console

import argparse
import sys
import time

# parsing arguments and assigning them to variables for cleanliness
parser = argparse.ArgumentParser(description='Synchronize replica folder to source folder.')
parser.add_argument('source', type=str, metavar='', nargs='?', help='filepath of source folder')
parser.add_argument('replica', type=str, metavar='', nargs='?', help='filepath of replica folder')
parser.add_argument('interval', type=int, metavar='', nargs='?', help='sync interval in seconds')
parser.add_argument('log', type=str, metavar='', nargs='?', help='filepath of logfile')

parser.add_argument('-s', '--source', type=str, metavar='', dest='source', help='filepath of source folder')
parser.add_argument('-r', '--replica', type=str, metavar='', dest='replica', help='filepath of replica folder')
parser.add_argument('-i', '--interval', type=int, metavar='', dest='interval', help='sync interval in seconds')
parser.add_argument('-l', '--log', type=str, metavar='', dest='log', help='filepath of logfile')
args = parser.parse_args()

source_path = args.source
replica_path = args.replica
sync_interval = args.interval
log_path = args.log


# ------ functions ------

#  Adds performed operation to log file and prints it to console.
def log_operation(operation, item):
    # define log message
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    message = f"{now} | {operation} {item}"

    # log to log file
    with open(log_path, 'a') as f:
        f.write(message+'\n')

    # log to console
    print(message)

# TODO: If log file doesn't exist, log_operation("Created", log_path). If source folder doesn't exist,
#  create_item(source_path). If replica folder doesn't exist, create_item(replica_path). Check validity of inputs.

# TODO: create_item(item) function for creating newly added files/folders? Call log_operation("Created", item)

# TODO: remove_item(item) function for deleting files/folders? Call log_operation("Removed", item)

# TODO: copypaste_file_content(item) function for copying updated content of edited files? Call log_operation("Copied", item)

# TODO: compare_files() function to compare two files for changes (unsure how at the moment). If
#  different, call copypaste_content()

# TODO: compare_folders() function to compare the folders for changes (unsure how at the moment).
#  If files/folders in replica that are absent in source, call delete_item(). If files/folders absent
#  in replica that are present in source, call create_item(). Call compare_files() to find changes.
#  Do I need something recursive to search through subfolders?


# ------ main loop ------
if __name__ == '__main__':
    # checks that all args are provided, exits if not
    if not (bool(source_path) & bool(replica_path) & bool(sync_interval) & bool(log_path)):
        print("Please provide a filepath for the source folder, a filepath for the replica folder, a synchronization interval, and a filepath for the log file.")
        sys.exit()

    # testing vars
    print(f"Source: {source_path} \n Replica: {replica_path} \n Interval: {sync_interval} \n Logfile: {log_path}")

    # repeats according to the sync_interval
    while True:
        print(f"Program running. You should see this message again in {sync_interval} seconds.")
        log_operation("Tested", "log_operation()")
        time.sleep(sync_interval)
