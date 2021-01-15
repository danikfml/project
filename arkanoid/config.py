import sys
from pathlib import PurePath


_EXE_FILENAME = sys.argv[0] #sys.executable if hasattr(sys, 'frozen') else __file__
_DIR_BASE = str(PurePath(_EXE_FILENAME).parent)


DIR_RESOURCES = _DIR_BASE + r'/resources/'
DIR_RESOURCES_IMAGES = DIR_RESOURCES + r'images/'
DIR_RESOURCES_SOUND = DIR_RESOURCES + r'sound/'
DIR_RESOURCES_LEVELS = DIR_RESOURCES + r'levels/'
