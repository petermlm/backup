#!/usr/bin/env python3

# TODO: If the target file is given, the name should be changed

# System imports
import os
import sys
import datetime


# =============================================================================
# Create archive
# =============================================================================


def addFile(directory, target_file_name, file_to_add):
    os.chdir(directory)
    cmd = "tar -r --file=" + target_file_name + " " + file_to_add
    os.system(cmd)


# Compress to the backup file
def Compress(bu_files, target_file_name):
    # Get list of files and directories to compress. List will have tuples
    # like:
    # (directory, filename)
    to_compress = getFilesToCompress(bu_files)

    # Make tar with bu_files (Not needed for now)
    # os.chdir(os.path.dirname(bu_files))
    # cmd = "tar -cf " + target_file_name + " " + bu_files
    # os.system(cmd)

    # Add files in to_compress
    for i in to_compress:
        file_path = os.path.join(i[0], i[1])

        if os.path.exists(file_path):
            print("Adding file \"{}\"".format(file_path))
            addFile(i[0], target_file_name, i[1])

        else:
            print("File \"{}\" does not exist. Skipping.".format(file_path))


# Get files and directories from the file bu_files
def getFilesToCompress(bu_files):
    bu_files_fd = open(bu_files)
    list_of_files = []

    for i in bu_files_fd:
        line = i.strip()

        if line == "":
            continue

        if line[-1] == "/":
            line = line[:-1]

        if line[0] != "/":
            line = os.path.join(os.getcwd(), line)

        entry = (os.path.dirname(line), os.path.basename(line))

        # Check name collision
        for j in list_of_files:
            # if j[1] == entry[1] or j[1] == bu_files: (bu_files not needed in
            # archive for now)
            if j[1] == entry[1]:
                print("Multiple files with name \"{}\"".format(j[1]))
                exit(1)

        # Append
        list_of_files.append(entry)

    return list_of_files


# =============================================================================
# Script Arguments
# =============================================================================


def printUsage():
    print("Usage:")
    print("\t-h             - Display help")
    print("\t-b bu_file     - bu_file location. Defaults to the script's directory")
    print("\t-o target_file - The resulting tar file. Default to the script's directory")


def getDefaultFileName():
    today = datetime.date.today()
    date_str = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
    return os.path.join(os.getcwd(), "backup_" + date_str + ".tar")


def parseArgs(argv):
    bu_files = os.path.join(os.getcwd(), "bu_files")
    target_file_name = getDefaultFileName()

    # Get file names from arguments
    i = 0
    while i < len(argv):
        if argv[i] == "-b":
            try:
                bu_files = argv[i+1]
            except IndexError:
                print("Flag -b needs argument")
                print("")
                printUsage()
                exit(1)
            i += 2

        elif argv[i] == "-o":
            try:
                target_file_name = argv[i+1]

                if not os.path.isabs(target_file_name):
                    target_file_name = os.path.join(os.getcwd(), target_file_name)

                if os.path.splitext(target_file_name)[1] != ".tar":
                    target_file_name += ".tar"

            except IndexError:
                print("Flag -o needs argument")
                printUsage()
                print("")
                exit(1)
            i += 2

        else:
            print("Argument {} not recognized".format(argv[i]))
            print("")
            printUsage()
            exit(1)

    return bu_files, target_file_name


# =============================================================================
# Main
# =============================================================================


if __name__ == "__main__":
    # Take arguments
    # If there is a help flag, just display the help and quit.
    if "-h" in sys.argv:
        printUsage()
        exit(1)

    bu_files, target_file_name = parseArgs(sys.argv[1:])

    if not os.path.isfile(bu_files):
        print("File {} doesn't exist".format(bu_files))
        exit(1)

    if os.path.isfile(target_file_name):
        print("File {} already exists".format(target_file_name))
        exit(1)

    Compress(bu_files, target_file_name)
