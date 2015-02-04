# About

BackUp is a small script to help me create quick and dirty tar file containing backups of my file system.

I developed this script because I had a few directories in separate locations and I wanted to back them up into a single tar file.

No really... I just wanted to try GitHub without bothering anyone. But I still use the script.

# How To Use

BackUp works by reading from a file, called bu\_files, which contain the files and directories you want to store to the target tar file.

Just write the directory locations to the bu\_file and you're good to go.

    /home/someuser/Documents/
    /home/someuser/Images/
    /var/www/web_things/
    local_file
    local_directory

In the above example you have two directories in the home folder of someuser, one directory in /var/www, a local file and a local directory.

By local, it's meant that the file/directory being mention is in the same directory has the BackUp script.

Note that as of this version, tiled (~) can't be use to refer to the home directory.

The contents of the tar file will be the following.

    backup_2013_06_23.tar
    |--bu_files
    |--Documents/
    |--Images/
    |--localfile
    |--local_directory
    |--web_things/

The location of each file/directory is not preserve in the tar file. Because of that there can't be two files with the same name, like for example:

    /dir1/file
    /dir2/file

The script warns the user about this.
