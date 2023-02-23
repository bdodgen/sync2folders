# TODO: Please implement a program that synchronizes two folders: source and replica. The
#  program should maintain a full, identical copy of source folder at replica folder.
#
# TODO: Synchronization must be one-way: after the synchronization content of the replica
#  folder should be modified to exactly match content of the source folder
#
# TODO: Synchronization should be performed periodically.
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

# parsing arguments and assigning them to variables for cleanliness
parser = argparse.ArgumentParser(description='Synchronize replica folder to source folder.')
parser.add_argument('-s', '--source', type=str, metavar='', required=True, help='filepath of source folder')
parser.add_argument('-r', '--replica', type=str, metavar='', required=True, help='filepath of replica folder')
parser.add_argument('-i', '--interval', type=int, metavar='', required=True, help='sync interval in seconds')
parser.add_argument('-l', '--log', type=str, metavar='', required=True, help='filepath of logfile')
args = parser.parse_args()

source_path = args.source
replica_path = args.replica
sync_interval = args.interval
log_path = args.log

# TODO: make the program run according to the sync interval

# TODO: create a function for adding to the logfile + printing to console (possibly separate)

# TODO: If log file doesn't exist, create it, print to console. If source folder doesn't exist,
#  create it, print to console, save to log. If replica folder doesn't exist, create from copy
#  of source folder, print to console, save to log. Check validity of inputs.

# TODO: create_item() function for creating newly added files/folders? (log + console)

# TODO: delete_item() function for deleting files/folders? (log + console)

# TODO: copypaste_content() function for copying updated content of edited files? (log + console)

# TODO: compare_files() function to compare two files for changes (unsure how at the moment). If
#  different, call copypaste_content()

# TODO: compare_folders() function to compare the folders for changes (unsure how at the moment).
#  If files/folders in replica that are absent in source, call delete_item(). If files/folders absent
#  in replica that are present in source, call create_item(). Call compare_files() to find changes.
#  Do I need something recursive to search through subfolders?


# main loop
if __name__ == '__main__':
    print(f"Source: {source_path} \n Replica: {replica_path} \n Interval: {sync_interval} \n Logfile: {log_path}")
    # print(f"Program running. You should see this message again in {sync_interval} seconds.")

