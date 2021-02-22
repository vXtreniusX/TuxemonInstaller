#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# This is a main backend. 
# It will basically run installation submodules


# Main install functions

import os
from base64 import b64decode
from zipfile import ZipFile

# Main archive data below
data = """{DATA}""" # Data tag will be replaced while compiling. It should contain base64 zip archive data. $Data 
# Main archive data above

temp_dir = os.getenv("TEMP")
def Install(path):
    global temp_dir
    global data
    
    temp_path = f"{temp_dir}\\tuxemon_install_data.zip"
    zip = b64decode(data.encode("UTF-8"))
    temp_file = open(temp_path, "wb")
    print("DEBUG: "+str(temp_file))
    temp_file.write(zip)
    temp_file.close()
    
    with ZipFile(temp_path, 'r') as zipObj:
        # Extract all the contents of zip file in current directory
        zipObj.extractall(path=path)
        zipObj.close()
        os.remove(temp_path)
    
import sys


try:
    import Tkinter as tk
    from Tkinter import filedialog
except ImportError:
    import tkinter as tk
    from tkinter import filedialog


try:
    import ttk
    py3 = False # Propably unneccesary, since Tuxemon's python 2 support is dropped.
	# I'll try to make some sort of a popup/message, when script is running in this python version.
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global Install_path
    Install_path = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def Start_Install():
    print('Installer_support.Start_Install')
    print(Install_path.get()) 
    sys.stdout.flush()
    Install(Install_path.get()) # Here installation will begin

def select_path():
    print('Installer_support.select_path') # Basicaly a placeholder for opening file select
    folder_selected = filedialog.askdirectory()
    print(folder_selected)
    print()
    print("Is path longer than zero?",len(folder_selected) > 0)
    if len(folder_selected) > 0:
        Install_path.delete(first, last=len(Install_path.get())-1)
        Install_path.icursor(0)
        Install_path.insert(0, folder_selected)
    
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import Installer_gui as Installer # Import gui, if support module is called first
    Installer.vp_start_gui()