from __future__ import print_function

from compat import (##PROJECT##,
                    unittest
                    )


class Test##PROJECT##(unittest.TestCase):

    def setUp(self):
        self._obj = ##PROJECT##.##PROJECT##()

    def test_##PROJECT##(self):
        self._obj.##PROJECT##()
