from selenium.webdriver.common.by import By
from android.page.BasePage import BasePage
from android.page.ProfilePage import ProfilePage
from android.page.SearchPage import SearchPage
from android.page.SelectedPage import SelectedPage
from android.page.LoginPage import LoginPage
from android.util.log_handle import LoggerHandler
import allure, time

log = LoggerHandler()

class MainPage(BasePage):
    _tool_icon = (By.ID, "m_tool_set_btn")
    _confirm_logout = (By.ID, "btn_logout_set")
    _button1 = (By.ID, "android:id/button1")  # 二次确认框的是
    _mine_icon = (By.ID, "rbtn_account")
    _profile_button=(By.ID, "user_profile_icon")
    _search_button = (By.ID, "home_search")
    _shopping_tab = (By.ID, "m_shopping_rb")
    _bidding_tab = (By.ID, "m_bidding_rb")
    _search_tab = (By.ID, "serach_img_btn")
    _search_blanket = (By.ID, "m_search_txt")
    _search_page_blanket = (By.ID, "m_search_et")
    # _bidding_button = (By.XPATH, "//")

    def gotoSelected(self):
        #调用全局的driver对象使用webdriver api操纵app
        #self.driver.find_element(By.xpath, "//*[@text='自选']")
        zixuan="自选"
        self.findByText(zixuan)
        #self.driver.find_element_by_xpath("//*[@text='自选']")
        self.findByText(zixuan).click()
        return SelectedPage()

    def gotoSearch(self) -> SearchPage:
        self.find(self._search_button).click()
        return SearchPage()

    def gotoProfile(self):
        #self.find(MainPage._profile_button).click()
        self.loadSteps("../data/MainPage.yaml", "gotoProfile")
        return ProfilePage()

    @allure.step("点击我的，跳转到登录页")
    def gotoMine(self):
        # 未登录，跳转到登陆页
        print(type(self._mine_icon))
        self.find(self._mine_icon).click()
        return LoginPage()

    @allure.step("点击首页的购物")
    def enterShopping(self):
        # 首页切换到购物tab
        self.find(self._shopping_tab).click()

    @allure.step("点击首页的竞买")
    def enterBidding(self):
        self.findByText("竞买").click()

    @allure.step("点击首页的购物")
    def enterBidding(self):
        # 首页切换到自营tab
        self.find(self._bidding_tab).click()

    # @allure.step("搜索页搜索 <{searchText}>")
    def enterSearch(self, searchText, category):
        # 进入搜索页面
        self.enterShopping()
        self.find(self._search_tab).click()
        time.sleep(2)
        print(22222)
        self.find(self._search_blanket).click()
        self.find(self._search_page_blanket).send_keys(searchText)
        print(33333)
        time.sleep(2)
        self.findByText(category).click()

    def logoutAccount(self):
        try:
            time.sleep(3)
            self.find(self._mine_icon).click()
            self.find(self._tool_icon).click()
            # 一定要sleep 不然会报错 Message: Swipe did not complete successfully
            time.sleep(1)
            self.swipes("up")
            self.find(self._confirm_logout).click()
            # time.sleep(3)
            # print(self.driver.page_source)
            self.find(self._button1).click()
            time.sleep(3)
        except Exception as e:
            log.info("tear down 退出登陆 失败：" + str(e))



    def back(self):
        self.driver.back()
