import time, allure
from selenium.webdriver.common.by import By
from android.page.BasePage import BasePage
from android.page.MinePage import MinePage
# from android.page.MainPage import MainPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):
    _to_account=(By.ID, "m_to_other_btn")
    _login_to_account=(By.ID, "rbtn_account")
    _account=(By.ID, "m_login_account_et")
    _password=(By.ID, "m_login_pwd_et")
    _login_button=(By.ID, "m_login_btn")
    _close_register_phone=(By.ID, "m_back_btn")
    _tool_icon=(By.ID, "m_tool_set_btn")
    _confirm_logout=(By.ID, "btn_logout_set")
    _button1=(By.ID, "android:id/button1") #二次确认框的是
    _back_locator=(By.XPATH, "//*[contains(@resource-id, 'iv_close') or contains(@resource-id, 'iv_action_back')]")
    _hunt_icon = (By.ID, "rbtn_hunt")

    @allure.step('输入用户名，密码')
    def loginWithAccount(self, account, password):
        self.find(self._to_account).click()
        self.find(self._account).send_keys(account)
        self.find(self._password).send_keys(password)
        self.find(self._login_button).click()
        if self.elementExists(self._close_register_phone):
            self.find(self._close_register_phone).click()
        time.sleep(2)
        print(self.driver.page_source)
        return self.driver.page_source

    @allure.step('公用部分：输入用户名，密码')
    def loginWithAccountSetUp(self, account, password):
        if self.elementExists(self._close_register_phone):
            self.find(self._to_account).click()
            self.find(self._account).send_keys(account)
            self.find(self._password).send_keys(password)
            self.find(self._login_button).click()
            time.sleep(1)
            # if self.elementExists(self._close_register_phone):
            #     self.find(self._close_register_phone).click()
        return MinePage()

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
        # print(self.driver.current_activity)
    #
    # def currentActivity(self):
    #     return self.driver.current_activity()

    #  ##############################################

    def loginByWX(self):
        return self
    def loginByMSG(self, phone, code):
        return self

    def loginByPassword(self, account, password):
        # self.find(self._other_locator).click()
        # self.find(self._tv_login_with_account).click()
        # self.find(self._login_account).send_keys(account)
        # self.find(self._login_password).send_keys(password)
        # self.find(self._button_next).click()

        self.loadSteps("../data/LoginPage.yaml", "loginByPassword", var1=account, var2=password)
        return self
    def loginSuccessByPassword(self, account, password):
        from android.page.MainPage import MainPage
        return MainPage()

    def back(self):
        self.find(self._back_locator).click()
        #WebDriverWait(self.driver, 2).until(expected_conditions.presence_of_element_located(self._close_locator))
        from android.page.ProfilePage import ProfilePage
        return ProfilePage()

    def getErrorMsg(self):
        msg=self.find(self._error_msg).text
        self.findByText("确定").click()
        return msg

    def gotoMainPage(self):
        time.sleep(5)
        self.find(self._hunt_icon).click()
    #     return MainPage()


