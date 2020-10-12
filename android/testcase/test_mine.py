from android.page.App import App
import pytest, allure


class TestMine(object):
    @classmethod
    def setup_method(self):
        self.MinePage=App.main().gotoMine().loginWithAccountSetUp("1000010", "admin123")

    @allure.story("进入我的-关注-竞买、购物切换")
    def test_my_attention(self):
        # self.Mine = self.loginPage.loginWithAccountSetUp("1000010", "admin123")
        assert "客户编号" in self.MinePage.enterMyAttention()

    @allure.story("进入我的-已得标")
    def test_my_get(self):
        # self.Mine = self.loginPage.loginWithAccountSetUp("1000010", "admin123")
        assert "客户编号" in self.MinePage.enterMyGet()

    # @pytest.mark.parametrize("user, pw, msg", [
    #     ("156005347600", "111111", "手机号码"),
    #     ("15600534760", "111111", "密码错误")
    # ])
    # def test_login_password(self, user, pw, msg):
    #     self.loginPage.loginByPassword(user, pw)
    #     assert msg in self.loginPage.getErrorMsg()

    def teardown_method(self):
        self.MinePage.logoutAccount()
