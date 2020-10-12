
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from android.driver.Client import AndroidClient
from android.util.log_handle import LoggerHandler
from android.util.config_path import screenshots_path
import yaml, os
import allure
import time

log = LoggerHandler()

class BasePage(object):

    element_black=[
        (By.XPATH, "ddd")
    ]
    def __init__(self):
        self.driver: WebDriver = self.getDriver()

    @classmethod
    def getDriver(cls):
        try:
            cls.driver = AndroidClient.driver
            log.info("driver 创建成功：" + str(cls.driver))
            return cls.driver
        except Exception as e:
            log.info("创建driver失败")
            raise e

    @classmethod
    def getClient(cls):
        return AndroidClient

    def find(self, kv) -> WebElement:
        #todo: 处理各类弹框
        try:
            log.info("在页面查找元素:"+ kv.__str__())
            return self.driver.find_element(*kv)
        except Exception as e:
            log.info("页面元素未找到,如图" + kv.__str__())
            self.get_pic()
            raise e

    def get_pic(self):
        picname = os.path.join(screenshots_path, str(int(time.time()*1000))) + ".png"
        self.driver.get_screenshot_as_file(picname)
    # def find_all(self, by, value):
    #     element: WebElement
    #     #加上重试机制
    #     for i in range(3):
    #         try:
    #             element=self.driver.find_element(by ,value)
    #             return element
    #         except:
    #             #找到页面的最顶层元素进行点击
    #             #动态变化位置的元素
    #
    #             #黑名单
    #             ##//*[@text='弹框']/..//*[@text='确认']
    #             for e in BasePage.element_black:
    #                 elements=self.driver.find_elements(*e)
    #                 if(elements.__sizeof__()>0):
    #                     elements[0].click()

    def elementExists(self, kv):
        try:
            self.driver.find_element(*kv)
            log.info("判断元素是否存在：" + kv.__str__() + "元素存在,截图")
            self.get_pic()
            return True
        except Exception as e:
            log.info("判断元素是否存在：" + kv.__str__() + "元素不存在，截图")
            self.get_pic()
            return False

    def swipes(self, dir):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        if dir == "up":
            log.info("向上滑一次")
            self.driver.swipe(x * 0.5, y * 4 / 5, x * 0.5, y * 1 / 5)
        elif dir == "left":
            log.info("向左滑一次")
            self.driver.swipe(x * 4 / 5, y * 0.5, x * 1/5, y * 0.5)
        elif dir == "right":
            log.info("向右滑一次")
            self.driver.swipe(x * 1 / 5, y * 0.5, x * 4 / 5, y * 0.5)
        elif dir == "down":
            log.info("向下滑一次")
            self.driver.swipe(x * 0.5, y * 1 / 5, x * 0.5, y * 4 / 5)

    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" %text))

    def getCurrentActivity(self):
        return self.driver.current_activity

    def getResouce(self):
        # print(type(self.driver.page_source))
        # print(self.driver.page_source)
        return self.driver.page_source

    def loadSteps(self, po_path, key, **kwargs):
        file=open(po_path, 'r')
        po_data=yaml.load(file)
        po_method=po_data[key]
        po_elements=dict()
        if po_data.keys().__contains__("elements"):
            po_elements=po_data['elements']
        #po_elements=yaml.load(open('xxx.yaml'))['elements']

        for step in po_method:
            step: dict
            element_platform=dict()
            if step.keys().__contains__("element"):
                element_platform=po_elements[step['element']][AndroidClient.platform]
            else:
                element_platform={"by": step['by'], "locator": step['locator']}
            element: WebElement=self.find(by=element_platform['by'], value=element_platform['locator'])
            action=str(step['action']).lower()

            #todo: 定位失败，多数是弹框，try catch后进入一个弹框处理 元素智能等待
            if action=="click":
                element.click()
            elif action=="sendkeys":
                text=str(step['text'])
                for k,v in kwargs.items():
                    origin=text
                    text=text.replace("$%s" %k, v)
                    print("update text: %s %s" % (origin, text))
                element.send_keys(text)
            else:
                print("UNKNOW COMMAND %s" % step)

