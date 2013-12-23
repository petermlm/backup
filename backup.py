#!/usr/bin/python

# System imports
import os
import sys
import datetime

""" Compress """

# Compress to the backup file
def Compress(bu_files, target_file_name):
    # Get list of files and directories to compress. List will have tuples like:
    # (real directory, object, dir in tar)
    to_compress = getFilesToCompress(bu_files)

    # Make tar with bu_files
    cmd = "tar -cf " + target_file_name + " " + bu_files
    os.system(cmd)

    # Add files in to_compress
    for i in to_compress:
        if os.path.exists(i[0] + "/" + i[1]):
            print "Adding file " + i[0] + "/" + i[1]
            os.chdir(i[0])
            cmd = "tar -r --file=" + target_file_name + " " + i[1]
            os.system(cmd)
        else:
            print "File " + i[0] + "/" + i[1] + " does not exist. Skipping."

# Get files and directories from the file bu_files
def getFilesToCompress(bu_files):
    to_compress = open(bu_files)
    list_of_files = []

    for i in to_compress:
        # Make tuple to append
        if i != "\n":
            if i[0] != "/":
                app = os.getcwd() + "/"
            else:
                app = ""

            t = makeTuple(app + i)

            # Check name collision
            for j in list_of_files:
                if j[1] == t[1]:
                    print j, t
                    print "Warning! Name collision: " + t[1]
                    exit()

            # Append
            list_of_files.append(t)

    return list_of_files

# Take a string "dir/of/file" and make tuple ("dir/of", "file")
def makeTuple(s):
    s = s.strip()
    i = s.rindex("/") if s[-1] != "/" else s[:-1].rindex("/")
    return (s[:i], s[i+1:])

""" Exception for Argument Parsing """

class BadArgs(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

""" Parse the Arguments """

def parseArgs(argv):
    bu_files = ""
    target_file_name = ""

    if len(argv) > 1:
        # If not, parse the arguments
        for i in range(1, len(argv), 2):
            if argv[i] == "-b":
                if "-b" in argv[i+1:]:
                    raise BadArgs("More then one -b flag. Quitting.")
                bu_files = argv[i+1]

            elif argv[i] == "-o":
                if "-o" in argv[i+1:]:
                    raise BadArgs("More then one -o flag. Quitting.")

                target_file_name = argv[i+1]

            else:
                raise BadArgs("Argument \"" + argv[i] + "\" not recognized")

    return bu_files, target_file_name

""" Get the Directory and the File Name """

class NotDirOrFile(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "Exception: " + self.text + " is neither a file nor directory."

# Make the name of the archive. IT will be the word backup plus a date
def getDefaultFileName():
    today = datetime.date.today()
    date_str = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
    return "backup_" + date_str + ".tar"

def getDirAndFileName(target_file_name):
    if target_file_name == "":
        return getDefaultFileName()

    elif os.path.isfile(target_file_name):
        return target_file_name

    elif os.path.isdir(target_file_name):
        return os.path.join(target_file_name, getDefaultFileName())

    else:
        dir_name = os.path.split(target_file_name)[0]
        if os.path.isdir(dir_name):
            return target_file_name

    raise NotDirOrFile(target_file_name)

""" Main """

if __name__ == "__main__":
    # Take arguments
    # If there is a help flag, just display the help and quit.
    if "-h" in sys.argv:
        print "HELP"
        exit()

    try:
        bu_files, target_file_name = parseArgs(sys.argv)

    except IndexError:
        print "Error in arguments. No tar file created."
        exit()

    except BadArgs as ba:
        print ba
        exit()

    # If the bu_files name is empty, set it to the default name
    if bu_files == "":
        bu_files = "bu_files"

    # Get the directory and the file name
    try:
        target_file_name = getDirAndFileName(target_file_name)
    except NotDirOrFile as e:
        print e
        exit()

    # Compress
    Compress(bu_files, target_file_name)

