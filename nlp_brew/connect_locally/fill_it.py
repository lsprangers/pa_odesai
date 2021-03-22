# TODO: @Luke_Sprangers --> make useful instead of just printing

import os

PROJECTNAME = "cup_a_code"


def print_repo_files():
    for root, dirs, files in os.walk(str(__file__), topdown=False):
        for tmp_dir in dirs:

            if str(tmp_dir) == PROJECTNAME:
                for tmp_file in files:
                    print(os.path.join(root, tmp_file))

            else:
                print("passing dir " + os.path.join(root, tmp_dir))


def print_os_objects(fname):
    for root, dirs, files in os.walk(fname):
        for tmp_file in files:
            print(os.path.join(root, tmp_file))
        for tmp_dir in dirs:
            print(os.path.join(root, tmp_dir))