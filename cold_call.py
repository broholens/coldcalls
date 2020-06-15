import random
import time
import json
import pathlib

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def make_driver(driver="chrome", load_img=False):
    """只支持chrome和phantomjs"""
    driver = driver.lower()
    ua = Faker().user_agent()
    if driver == "phantomjs":
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = ua
        dcap["phantomjs.page.settings.loadImages"] = load_img
        d = webdriver.PhantomJS(desired_capabilities=dcap)
    elif driver == "chrome":
        # 创建chrome并配置
        ops = webdriver.ChromeOptions()
        # ops.add_argument("--headless")
        ops.add_argument("--no-sandbox")
        ops.add_argument("--disable-gpu")
        ops.add_argument("--start-maximized")
        # ops.add_argument('--incognito')
        ops.add_argument("lang=zh_CN")
        if load_img is False:
            prefs = {"profile.managed_default_content_settings.images": 2}
            ops.add_experimental_option("prefs", prefs)
        # 解决window.navigator.webdriver=True的问题
        # https://wwwhttps://www.cnblogs.com/presleyren/p/10771000.html.cnblogs.com/presleyren/p/10771000.html
        ops.add_experimental_option("excludeSwitches", ["enable-automation"])
        ops.add_argument(f'user-agent={Faker().user_agent()}')
        try:
            # selenium兼容问题
            d = webdriver.Chrome(options=ops)
        except:
            d = webdriver.Chrome(chrome_options=ops)
    else:
        raise ValueError("Unknown argument %s. Support chrome and phantomjs only." % driver)
    d.maximize_window()
    return d


class ColdCall:
    # 密码只要符合网站注册密码要求即可
    password = 'aiahdia6'
    # 映射配置文件中定位元素的模式
    mode_map = {
        'id': By.ID,
        'xpath': By.XPATH,
        'name': By.NAME,
        'class_name': By.CLASS_NAME,
        'link_text': By.LINK_TEXT
    }

    def __init__(self, phone_number):
        self.driver = make_driver()
        self.phone_number = phone_number
        self.name = Faker('zh_CN').name()
        self.sites = self.load_sites()

    def tease_site(self, site):
        """根据配置点击网站进行注册"""
        self.driver.get(site['url'])
        # 获取site字段
        username, password = site.get('username_path'), site.get('password_path')
        phone_path, submit_path = site['phone_path'], site.get('submit_path')
        iframe, password_confirm = site.get('iframe'), site.get('password_confirm_path')
        sleep_time, message = float(site.get('sleep_time', 0)), site.get('message_path')
        # 不填写留言内容默认使用手机号
        message_content = message and message.get('msg', self.phone_number)
        preset, postset = site.get('preset'), site.get('postset')
        # 等待表单页面加载完全
        sleep_time and time.sleep(sleep_time)
        iframe and self.driver.switch_to.frame(iframe)
        preset and self._parse_type(preset)
        # 填写表单
        self._send_optional_value(username, self.name)
        self.send_phone_number(phone_path)
        self._send_optional_value(password, self.password)
        self._send_optional_value(password_confirm, self.password)
        self._send_optional_value(message, message_content)
        submit_path and self._find_element(submit_path).click()
        postset and self._parse_type(postset)

    def send_phone_number(self, phone_path):
        """逐个字符输入手机号"""
        time.sleep(1)
        self._find_element(phone_path).clear()
        for i in range(11):
            self._find_element(phone_path).send_keys(self.phone_number[i])
            self.random_sleep(0.3)

    def _parse_type(self, item):
        """解析preset和postset字段，执行点击命令/脚本"""
        set_type = item.get('type', 'click')
        if set_type == 'click':
            self._find_element(item).click()
        elif set_type == 'script':
            self.driver.execute_script(item['value'])
        time.sleep(0.2)

    def _parse_mode(self, item):
        """解析配置文件中的mode,默认为xpath"""
        mode = item.get('mode', 'xpath')
        return self.mode_map[mode]

    def _find_element(self, item):
        """对driver.find_element的封装"""
        return self.driver.find_element(self._parse_mode(item), item['value'])

    def _send_optional_value(self, key, value):
        """对于可能存在的值进行填写"""
        if key:
            self._find_element(key).send_keys(value)

    @staticmethod
    def load_sites():
        content = pathlib.Path('sites.json').read_text()
        return json.loads(content)

    @staticmethod
    def random_sleep(max_sleep_time):
        time.sleep(random.random()*max_sleep_time)

    def run(self):
        # for site in self.sites:
        #     self.tease_site(site)
        self.tease_site(self.sites[-1])


if __name__ == '__main__':
    cc = ColdCall("17719674031")
    cc.run()