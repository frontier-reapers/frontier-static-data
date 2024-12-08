import csv
import os.path

def get_indexfiles():
    indexFiles = list()
    indexFiles.append('1d/1d34143a37d4b739_553cd67a2f32c66f69a51f6eae071b9a')
    indexFiles.append('56/5610a6eb8b5a4975_1a78826bc07a6e1c4814141ad484df52')
    return indexFiles

def find_resfile(root, file, indexFiles):
    for index in indexFiles:
        indexPath = os.path.join(root, index)
        if (os.path.isfile(indexPath)):
            with open(indexPath, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in reader:
                    if (row[0] == file):
                        return ResFile(row[1], index, os.path.join(root, row[1]))

class ResFile:
    def __init__(self, res, index, filepath):
        self.res = res
        self.index = index
        self.filepath = filepath

class clr:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

