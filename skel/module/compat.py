""" Python 2/3 compatibility layer """
import sys

try:
    import ##PROJECT## as ##PROJECT##

except ImportError:
    import ##PROJECT##


PY3 = sys.version_info[0] == 3

__all__ = ['PY3', '##PROJECT##']
