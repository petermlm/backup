#!/usr/bin/python

# System imports
import os
import sys
import datetime

""" Compress """

# Compress to the backup file
def Compress(bu_files, target_file_dir, target_file_name):
    if bu_files == "":
        bu_files = 'bu_files'

    # Get list of files and directories to compress. List will have tuples like:
    # (real directory, object, dir in tar)
    to_compress = getFilesToCompress(bu_files)

    # Add bu_files to list of files to compress
    # list_of_files = ['bu_files'] + to_compress

    # Get name of tar file
    file_name = ""
    if target_file_dir != "":
        file_name = target_file_dir
    elif target_file_name != "":
        file_name = target_file_name
    else:
        file_name = getFileName()

    # Make tar with bu_files
    cmd = 'tar -cf ' + file_name + ' ' + bu_files
    os.system(cmd)

    directory = ""
    if target_file_dir == "":
        directory = file_name
    else:
        directory = os.getcwd() + '/' + file_name
    print "Directory:", directory

    print 'Compressing to ' + directory

    # Add files in to_compress
    for i in to_compress:
        if os.path.exists(i[0] + '/' + i[1]):
            print 'Adding file ' + i[0] + '/' + i[1]
            os.chdir(i[0])
            cmd = 'tar -r --file=' + directory + ' ' + i[1]
            os.system(cmd)
        else:
            print 'File ' + i[0] + '/' + i[1] + ' does not exist. Skipping.'

# Get files and directories from the file bu_files
def getFilesToCompress(bu_files):
    to_compress = open(bu_files)
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

""" Exception for Argument Parsing """

class BadArgs(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

def parseArgs(argv):
    bu_files = ""
    target_file_dir = ""
    target_file_name = ""

    if len(argv) > 1:
        # If not, parse the arguments
        for i in range(1, len(argv), 2):
            if argv[i] == "-b":
                if "-b" in argv[i+1:]:
                    raise BadArgs("More then one -b flag. Quitting.")
                bu_files = argv[i+1]

            elif argv[i] == "-d":
                if "-d" in argv[i+1:]:
                    raise BadArgs("More then one -d flag. Quitting.")

                if "-o" in argv[i+1:]:
                    raise BadArgs("There can't be a -d and a -o flag.")

                target_file_dir = argv[i+1]

            elif argv[i] == "-o":
                if "-o" in argv[i+1:]:
                    raise BadArgs("More then one -o flag. Quitting.")

                if "-d" in argv[i+1:]:
                    raise BadArgs("There can't be a -d and a -o flag.")

                target_file_name = argv[i+1]

            else:
                raise BadArgs("Argument \"" + argv[i] + "\" not recognized")

    return bu_files, target_file_dir, target_file_name

""" Main """

if __name__ == '__main__':
    # Take arguments
    # If there is a help flag, just display the help and quit.
    if "-h" in sys.argv:
        print "HELP"
        exit()

    try:
        bu_files, target_file_dir, target_file_name = parseArgs(sys.argv)

    except IndexError:
        print "Error in arguments. No tar file created."
        exit()

    except BadArgs as ba:
        print ba
        exit()

    # Compress
    Compress(bu_files, target_file_dir, target_file_name)

