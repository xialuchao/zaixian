from android.page.App import App
import pytest, allure


class TestLogin(object):
    @classmethod
    def setup_method(self):
        self.loginPage=App.main().gotoMine()

    @allure.story("使用用户名密码登陆")
    def test_login_account_password(self):
        assert "客户编号" in self.loginPage.loginWithAccount("1000010", "admin123")
        # assert(self.loginPage.currentActivity ==".ui.MainActivity")

    # @pytest.mark.parametrize("user, pw, msg", [
    #     ("156005347600", "111111", "手机号码"),
    #     ("15600534760", "111111", "密码错误")
    # ])
    # def test_login_password(self, user, pw, msg):
    #     self.loginPage.loginByPassword(user, pw)
    #     assert msg in self.loginPage.getErrorMsg()

    def teardown_method(self):
        self.loginPage.logoutAccount()
