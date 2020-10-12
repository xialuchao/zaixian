from android.page.BasePage import BasePage
from android.page.LoginPage import LoginPage


class ProfilePage(BasePage):
    def gotoLogin(self):
        #self.findByText("点击登录").click()
        self.loadSteps("../data/ProfilePage.yaml", "gotoLogin")
        return LoginPage()