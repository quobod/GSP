import os
import platform

# From the os module
OS_NAME = os.name
SEP = os.sep
ENV = os.environ
ENVB = os.environb
CNF_NAMES = os.confstr_names
CUR_DIR = os.curdir
EXT_SEP = os.extsep
PATH_SEP = os.pathsep
DEF_PATH = os.defpath
LINE_SEP = os.linesep
DEV_NULL = os.devnull

# os methods
CPU_COUNT = os.cpu_count()

# From the platform module
MACHINE_TYPE = platform.machine()
MAC_VER = platform.mac_ver()
NODE = platform.node()
PLATFORM = platform.platform()
ARCH = platform.architecture()
PROCESSOR = platform.processor()
RELEASE = platform.release()
SYSTEM = platform.system()
VERSION = platform.version()
UNAME = platform.uname()