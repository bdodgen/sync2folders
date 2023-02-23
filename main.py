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
# TODO: Folder paths, synchronization interval and log file path should be provided using the
#  command line arguments


# This is a program that synchronizes two folders: source and replica. The
# program should maintain a full, identical copy of source folder at replica folder. Synchronization
# is performed at interval specified in CLI arguments and is only one way: source -> replica. File
# creation/copying/removal operations are logged into file specified in CLI arguments as well as
# printed to the console

# TODO: use argparse to pull folder paths, synchronization interval, and log file path from the
#  command line arguments and save as variables

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
    print('Folder synchronization project.')

