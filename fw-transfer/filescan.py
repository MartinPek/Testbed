import os
from pathlib import Path

testPath = "F:/teamescape/git_repos"


def get_files(directory):
    files = []
    os.chdir(directory)
    for root, dirs, localfiles in os.walk(directory, topdown=True, onerror=None, followlinks=False):
        files.extend(localfiles)
        for directory in dirs:
            directory = os.path.join(root, directory)
            files.extend(get_files(directory))
    files = list(files)
    return files
    '''
    filtered = list(filter(lambda entry: os.path.isfile(entry), dir_list))
    dirs = set(dir_list) - set(filtered)
    files.append(filtered)
    return files
    '''


def main():
    files = get_files(testPath)
    print("files are {}".format(files))


if __name__ == "__main__":
    main()

