#!/usr/bin/python

# System imports
import os
import sys
import datetime

# Compress to the backup file
def Compress():
    # Get list of files and directories to compress. List will have tuples like:
    # (real directory, object, dir in tar)
    to_compress = getFilesToCompress()

    # Add bmu_files to list of files to compress
    # list_of_files = ['bmu_files'] + to_compress

    # Get name of tar file
    file_name = getFileName()

    # Make tar with bmu_files
    cmd = 'tar -cf ' + file_name + ' bmu_files'
    os.system(cmd)
    directory = os.getcwd() + '/' + file_name

    print 'Compressing to ' + directory

    # Add files in to_compress
    for i in to_compress:
        print 'Adding file ' + i[0] + '/' + i[1]
        os.chdir(i[0])
        cmd = 'tar -r --file=' + directory + ' ' + i[1]
        os.system(cmd)

# Get files and directories from the file bmu_files
def getFilesToCompress():
    to_compress = open('bmu_files')
    list_of_files = []

    for i in to_compress:
        # Make tuple to append
        if i != '\n':
            if i[0] != '/':
                app = os.getcwd() + '/'
            else:
                app = ''

            t = makeTuple(app + i)

            # Check name collision
            for j in list_of_files:
                if j[1] == t[1]:
                    print j, t
                    print 'Warning! Name collision: ' + t[1]
                    exit()

            # Append
            list_of_files.append(t)

    return list_of_files

# Take a string 'dir/of/file' and make tuple ('dir/of', 'file')
def makeTuple(s):
    s = s.strip()
    i = s.rindex('/') if s[-1] != '/' else s[:-1].rindex('/')
    return (s[:i], s[i+1:])

# Make the name of the archive. IT will be the word backup plus a date
def getFileName():
    today = datetime.date.today()
    date_str = str(today.year) + '_' + str(today.month) + '_' + str(today.day)
    return 'backup_' + date_str + '.tar'

# Main
if __name__ == '__main__':
    Compress()

