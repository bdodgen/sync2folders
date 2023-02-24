This is a program that synchronizes two folders: source and replica. The program should maintain a full,
identical copy of source folder at replica folder. Synchronization is performed at interval specified in
CLI arguments and is only one way: source -> replica. File creation/copying/removal operations are logged
into file specified in CLI arguments as well as printed to the console.

CLI command to run the program with positional args:
python3 main.py [args]

All four args must be assigned with the following flags:
  -s , --source     filepath of source folder
  -r , --replica    filepath of replica folder
  -i , --interval   sync interval in seconds
  -l , --log        filepath of logfile

How to exit the program:
    Only CTRL+C works for ending the program once the sync loop is started.

Some notes for possible improvement:
* This program will assume that folder paths and sync interval will be defined with CLI each time
it is run. A configuration file would be a good update to the program if it is intended to be used
long-term.

* I am also ignoring some helpful and time-saving external libraries (namely, Watchdog) in the
interest of not "cheating" on the assignment. The definition of what libraries are allowed feels
conservative, so I will be figuring this out the old-school way to the best of my ability.

* Another good addition would be the ability to end the program with something like 'Esc'
instead of only CTRL+C, but I have not included it so that I can keep the task as lightweight as
possible for now.
