
import pytest

from android.page.App import App
from android.page.MainPage import MainPage


class TestSelected(object):
    @classmethod
    def setup_class(cls):
        cls.MinePage=App.main().gotoMine()

    def test_price(self):
        self.MinePage.loginByPassword("1000010", "admin123")
        assert self.mainPage.gotoSelected().gotoHS().getPriceByName("科大讯飞")==28.83
