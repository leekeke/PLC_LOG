from distutils.core import setup
import glob
import py2exe

setup(
    version = "1.4",
    description = "PLC_LOG_Recorder",
    name = "PLC_LOG",
    # targets to build
#    windows = ["window.py"],
    console = ["receive1.py"],
    data_files = ["par_data.xls"],
    options = { "py2exe":{"dll_excludes":["MSVCP90.dll","USER32.dll","SHELL32.dll","ADVAPI32.dll","WS2_32.dll","GDI32.dll","KERNEL32.dll"]}}
)