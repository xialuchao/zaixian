# import pytest
# import yaml
#
# class TestDemo(object):
#
#     @pytest.mark.parametrize("x,y",
#                              [
#                                  (1, 2),
#                                  (3, 4)
#                              ]
#                              )
#     def test_one(self, x, y):
#         print("%s %s" % (x, y))
#         pass
import uiautomator
from uiautomator import device
# driver = uiautomator.connect("1181cef8")
# driver(resourceId="button1").click()
# device = device("1181cef8")
# device(resourceId="button1").click()
device.press.home()