#renames all files in directory and subdirectories
import os

#defines pathway to files
for path, dirs, files in os.walk("/path/to/files/here/"):
    for file in files:
#defines new filename to replace old filename
        os.rename(os.path.join(path, file), os.path.join(path, 'MODS.xml'))
