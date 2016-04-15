from distutils.core import setup
import py2exe
setup(
    version = "1.3",
    description = "PLC_LOG_Recorder",
    name = "PLC_LOG",

    # targets to build
#    windows = ["window.py"],
    console = ["receive.py"],
    options = { "py2exe":{"dll_excludes":["MSVCP90.dll"]}}
    )