import os

#enter pathway to where directories are to be created
path = "/path/to/host/folder"
#paste list of directory names you want to create below in inverted commas
your_list_from_csv = ["paste_folder_names_from_csv_here"]

for new_dir in your_list_from_csv:
    dir_path = "{0:s}/{1:s}".format(path, new_dir)
    try:
        os.mkdir(dir_path)
    except FileExistsError as err:
        print("Folder Exists")
