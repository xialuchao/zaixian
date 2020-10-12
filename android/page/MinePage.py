import time, allure
from selenium.webdriver.common.by import By
from android.page.BasePage import BasePage
from android.util.log_handle import LoggerHandler
# from android.page.MainPage import MainPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

log = LoggerHandler()

class MinePage(BasePage):
    _to_account=(By.ID, "m_to_other_btn")
    _fiter = (By.ID, "m_other_btn")
    _login_to_account = (By.ID, "rbtn_account")
    _account = (By.ID, "m_login_account_et")
    _password = (By.ID, "m_login_pwd_et")
    _login_button = (By.ID, "m_login_btn")
    _close_register_phone = (By.ID, "m_back_btn")
    _tool_icon = (By.ID, "m_tool_set_btn")
    _confirm_logout = (By.ID, "btn_logout_set")
    _button1 = (By.ID, "android:id/button1")  # 二次确认框的是
    _back_locator=(By.XPATH, "//*[contains(@resource-id, 'iv_close') or contains(@resource-id, 'iv_action_back')]")

    @allure.step('进入 我的-关注 页面')
    def enterMyAttention(self):
        # log.info("确保进入的页面是我的页面，点击我的")
        # self.find(self._to_account).click()
        log.info("点击 我的，关注")
        self.findByText("关注").click()
        log.info("点击 关注的 竞买")
        self.findByText("竞买").click()
        self.swipes("up")
        self.swipes("up")
        self.swipes("up")
        self.swipes("down")
        self.swipes("down")
        self.swipes("down")
        log.info("点击 筛选 ")
        self.find(self._fiter).click()
        time.sleep(1)
        self.swipes("up")
        self.swipes("down")
        self.driver.back()
        log.info("点击 关注的 购物")
        self.findByText("购物").click()
        self.swipes("up")
        self.swipes("up")
        self.swipes("up")
        self.swipes("down")
        self.swipes("down")
        self.swipes("down")
        self.driver.back()
        time.sleep(2)
        return self.driver.page_source

    @allure.step("进入 我的 已得标 进行操作")
    def enterMyGet(self):
        log.info("点击 我的 已得标")
        self.findByText("已得标").click()
        time.sleep(1)
        self.swipes("up")
        self.swipes("up")
        self.swipes("down")
        self.swipes("down")
        self.driver.back()
        time.sleep(2)
        return self.driver.page_source


    @allure.step('退出登陆')
    def logoutAccount(self):
        self.find(self._login_to_account).click()
        self.find(self._tool_icon).click()
        # 一定要sleep 不然会报错 Message: Swipe did not complete successfully
        time.sleep(1)
        self.swipes("up")
        self.find(self._confirm_logout).click()
        # time.sleep(3)
        # print(self.driver.page_source)
        self.find(self._button1).click()
        time.sleep(3)

