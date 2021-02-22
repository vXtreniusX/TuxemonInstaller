"""
TODO: Convert archive to an base64 string, and put it to a baseString variable
"""


import os # Basic os functions, such as creating directories

import base64 # Converting the archive to base64 encoded string

from tkinter import filedialog # File dialog

from shutil import copy # Copy stuff

from sys import argv


if len(argv) == 1:
    print("Please select the archived file of the build...")
    archive = filedialog.askopenfile(mode="rb")
elif len(argv) == 2:
    try:
        archive = open(argv[1], "rb")
    except:
        print("Incorrect path.")
        exit()
else:
    print("Too many usage arguments were entered.")
    exit()
    
baseString = base64.b64encode(archive.read()).decode("UTF-8")

try:
    os.mkdir("InstallerBuild")
except FileExistsError:
    pass


copy("Installer_gui.py", "InstallerBuild") # Copy Installer's gui (Doesn't require any modification)
#copy("Installer_backend.py", "InstallerBuild") # Required data will be read from the file itself.     # Copy Installer's backend (Requires changes to the data variable)

# Open Installer backend
backend_file = open("Installer_backend.py", "r+")

os.chdir("InstallerBuild") # Go to working directory

#Open result backend file
backend_output = open("Installer_backend.py", "w")

backend_contents = backend_file.read() # Read the whole backend file...
backend_edited = backend_contents.replace("{DATA}", baseString) # ... and replace the {DATA} tag with the base64 data.

backend_output.write(backend_edited)

#os.system("dir")

