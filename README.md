# About

BackUp is a small script to help me create quick and dirty tar file containing backups of my file system.

I developed this script because I had a few directories in sperate locations and I wanted to back them up into a single tar file.

# How To Use

BackMeUp works by reading from a file, called bmu\_files, which files and directories you want to store to the target tar file.

Just write the directory locations to the bmu\_file and you're good to go.

    /home/someuser/Documents/
    /home/someuser/Images/
    /var/www/web_things/
    local_file
    local_directory

In the above example you have two directories in the home folder of someuser, one directory in /var/www, a local file and a local directory.

By local, it's meant that the file/direcotry being mention is in the same directory has BackMeUp.

Note that has of this version ~ can't be use to refer to the home directory.

The contents of the tar file will be the following.

    backup_2013_06_23.tar
    |--bmu_files
    |--Documents/
    |--Images/
    |--localfile
    |--local_directory
    |--web_things/

The location of each file/directory is not preserve in the tar file. Because of that there can't be two files with the same name, like for example:

    /dir1/file
    /dir2/file

The script warns the user about this.

