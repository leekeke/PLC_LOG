from distutils.core import setup
import glob
import py2exe
import sys
from PyQt4 import QtCore, QtGui

sys.argv.append('py2exe')

setup(
    version = "4.0",
    description = "PLC_LOG_Recorder",
    name = "PLC_LOG",
    # targets to build
#    windows = ["window.py"],
#    console = ["Log_Recorder1.py"],
    windows = ["Log_Recorder1.py"],
    data_files = ["par_data.xls"],
    options = { "py2exe":{"dll_excludes":["MSVCP90.dll","USER32.dll","SHELL32.dll","ADVAPI32.dll","WS2_32.dll","GDI32.dll","KERNEL32.dll"]}}
)