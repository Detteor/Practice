import shutil
from pathlib import Path
import glob
import os
import datetime

def up_one_dir(path, rename=False):
    try:
        now = str(datetime.datetime.now())
        now = now.replace(":","_")
        now = now.replace(".","_")
        cur_dir = Path(path).parents[0]
        parent_dir = Path(path).parents[1]
        if rename:
            shutil.move(path, str(parent_dir) + '\\' + path[-9:-4] + '_' + str(now) + path[-4:])
        else:
            shutil.move(path, parent_dir)
        if len(os.listdir(cur_dir)) == 0:
            print('Removing: ' + str(cur_dir))
            shutil.rmtree(cur_dir)
    except IndexError:
        pass

print('Print Level 1')
paths = glob.glob(r'Q:\GEO_PROJECT\sp_TEST\01_to_09_00\*\*\*\*\*.*')

for path in paths:
    up_one_dir(path, True)

print('Print Level 2')
paths = glob.glob(r'Q:\GEO_PROJECT\sp_TEST\01_to_09_00\*\*\*\*.*')

for path in paths:
    up_one_dir(path)

print('Print Level 3')
paths = glob.glob(r'Q:\GEO_PROJECT\sp_TEST\01_to_09_00\*\*\*.*')

for path in paths:
    up_one_dir(path)
