""" Python 2/3 compatibility layer """
try:
    import unittest2 as unittest

except ImportError:
    import unittest

from ##PROJECT##.compat import (##PROJECT##)


__all__ = ['unittest', '##PROJECT##']
