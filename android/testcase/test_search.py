
import pytest, allure,time

from android.page.App import App


class TestSearch(object):
    @classmethod
    def setup_method(self):
        self.MainPage = App.main()

    @allure.story("使用用户名密码登陆")
    # @pytest.mark.parametrize("searchText, category", [
    #     ("测试", "邮票")
    # ])
    def test_login_search(self, searchText="测试", category="邮票类"):
        self.MinePage = self.MainPage.gotoMine()
        self.MinePage.loginWithAccount("1000010", "admin123")
        self.MinePage.gotoMainPage()
        self.MainPage.enterSearch(searchText, category)
        self.MainPage.back()
        self.MainPage.back()
        self.MainPage.back()
        time.sleep(1)
        self.MainPage.enterBidding()

    def teardown_method(self):
        self.MainPage.logoutAccount()
