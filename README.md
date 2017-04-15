# About

BackUp is a small script to help me create quick and dirty tar file containing
backups of my file system.

I developed this script because I had a few directories in separate locations
and I wanted to back them up into a single tar file.

Also because back in 2013 I was new to Git and GitHub and wanted to try these
things.

# Arguments

    -h             - Display help
    -b bu_file     - bu_file location. Defaults to the script's directory
    -o target_file - The resulting tar file. Default to the script's directory

# How To Use

BackUp works by reading from a file, called `bu_files`, which contain the files
and directories you want to store to the target tar file. The directories may
be absolute or relative.

For example, if `bu_files` has:

    /home/someuser/Documents/
    /home/someuser/Images/
    local_file
    local_directory

The contents of the tar file will be:

    backup_2013_06_23.tar
    |--Documents/
    |--Images/
    |--local_file
    |--local_directory

The location of each file/directory is not preserve in the tar file. Because of
that there can't be two files with the same name, like for example:

    /dir1/file
    /dir2/file

The script warns the user about this.
