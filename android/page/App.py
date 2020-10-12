from android.driver.Client import AndroidClient
from android.page.BasePage import BasePage
from android.page.MainPage import MainPage


class App(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().restart_app()
        return MainPage()