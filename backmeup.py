#!/usr/bin/python

# System imports
import os
import sys
import datetime

# Compress to the backup file
def Compress():
    # Get list of outer files in outer_files
    outer_file = GetOuterFiles()

    # Add Documents directory to list of files
    # list_of_files = ['~/Documents'] + outer_file
    list_of_files = ['~/test', 'outer_files'] + outer_file

    # Get name of file
    file_name = getFileName()

    # Make tar
    cmd = 'tar -cf ' + file_name + ' '
    for i in list_of_files:
        cmd += i + ' '
    cmd = cmd.strip()

    os.system(cmd)

# Get outer files from the files outer_files
def GetOuterFiles():
    outer_file = open('outer_files')
    list_of_files = []

    for i in outer_file:
        list_of_files.append(i)

    return list_of_files

# Make the name of the archive. IT will be the word backmeup plus a date
def getFileName():
    today = datetime.date.today()
    date_str = str(today.year) + '_' + str(today.month) + '_' + str(today.day)
    return 'backmeup_' + date_str + '.tar'

# Main
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: ./backmeup'
        exit()

    Compress()

