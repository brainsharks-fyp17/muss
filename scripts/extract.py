
from os import listdir
from os.path import isfile, join, isdir
import gc

def getAllFilesRecursive(root):
    files = [join(root, f) for f in listdir(root) if isfile(join(root, f))]
    dirs = [d for d in listdir(root) if isdir(join(root, d))]
    for d in dirs:
        files_in_d = getAllFilesRecursive(join(root, d))
        if files_in_d:
            for f in files_in_d:
                files.append(join(root, f))
    return files

lst_file = getAllFilesRecursive('content/sinhala-dataset-creation/datasets/tokenized')
all_data = open("resources/datasets/uts/si/sentences/all_data.txt","w")
for i in range(len(lst_file)):
    f = open(lst_file[i])
    data = f.readlines()
    for line in data:
        all_data.write(line)
all_data.close()
del data
gc.collect()