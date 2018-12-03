import os
import shutil

#change to source directory
for root, dirs, files in os.walk('/path/to/source/directory'):
   for file in files:
      path_file = os.path.join(root,file)
      #change to destination directory
      shutil.copy2(path_file,'/path/to/destination/directory')
