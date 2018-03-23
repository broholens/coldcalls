import time
from random import choice
from itertools import cycle
from selenium import webdriver
from selenium.webdriver.common.by import By


class SMSBooming:

    names = ['李', '王', '赵', '刘']
    passwords = ['aiahdia6', 'akahoaw1', 'akxhk8as', 'ahfaxh0q']

    def __init__(self, phone_number):
        options = webdriver.FirefoxOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)
        self.driver.set_page_load_timeout(10)
        self.phone = phone_number

    def request(self, url):
        try:
            self.driver.get(url)
        except:
            self.driver.execute_script('window.stop()')

    def run(self):
        for platform in cycle(platforms):
            self.request(platform['url'])
            name, password = platform.get('name'), platform.get('password')
            phone, verify = platform['phone'], platform['register']
            try:
                if name is not None:
                    self.driver.find_element(name[0], name[1]).send_keys(choice(self.names))
                if password is not None:
                    self.driver.find_element(password[0], password[1]).send_keys(choice(self.passwords))
                time.sleep(1)
                self.driver.find_element(phone[0], phone[1]).send_keys(self.phone[:3])
                time.sleep(1)
                self.driver.find_element(phone[0], phone[1]).send_keys(self.phone[3:])
                time.sleep(1)
                self.driver.find_element(verify[0], verify[1]).click()
                print('ok', platform['url'])
            except:
                print('error', platform['url'])


platforms = [
    {
        'url': 'https://www.zhihu.com/signup',
        'phone': (By.NAME, 'phoneNo'),
        'register': (By.CLASS_NAME, 'SignFlow-smsInputButton')
    },
    {
        'url': 'https://login.zbj.com/register',
        'phone': (By.ID, 'sacc'),
        'register': (By.CLASS_NAME, 'btn-get-code')
    },
    {
        'url': 'http://zt.epwk.com/',
        'name': (By.ID, 'username'),
        'phone': (By.ID, 'mobile'),
        'register': (By.CLASS_NAME, 'button')
    },
    {
        'url': 'http://zt.epwk.com/1607epzhelu/',
        'phone': (By.ID, 'mobile2'),
        'register': (By.ID, 'verify2')
    },
    {
        'url': 'https://weibo.com/signup/signup.php',
        'phone': (By.NAME, 'username'),
        'password': (By.NAME, 'passwd'),
        'register': (By.CLASS_NAME, 'W_btn_e')
    },
    {
        'url': 'http://www.zhixue.com/container/reg/parent/reg',
        'phone': (By.ID, 'reg_txtMobile'),
        'password': (By.ID, 'reg_txtPwd'),
        'register': (By.ID, 'reg_btnCode')
    },
    {
        'url': 'https://om.qq.com/userReg/register?mediaType=1',
        'phone': (By.ID, 'phone'),
        'register': (By.CLASS_NAME, 'getAuthCode')
    },
    {
        'url': 'https://account.wps.cn/v1/signup',
        'phone': (By.ID, 'phone'),
        'password': (By.ID, 'phone_password'),
        'register': (By.ID, 'signupPhone')
    },
    {
        'url': 'http://www.zhangmen.com/lp/sem',
        'name': (By.ID, 's-name'),
        'phone': (By.ID, 'stu_mobile1'),
        'register': (By.ID, 'pcheaderbtn2')
    },
    {
        'url': 'http://passport.soufun.com/register.aspx',
        'phone': (By.ID, 'strMobile'),
        'register': (By.XPATH, '//input[@id="vcode"]')
    },
    # http://www.wanke001.com/Register/Register.aspx
]

special = [
    # frame
    {
        'url': 'http://i.xunlei.com/login.html',
        'frame': 'loginIframe',
        'click': (By.ID, 'ml_tab'),
        'phone': (By.XPATH, '//input[@id="ml_m"]'),
        'register': (By.ID, 'ml_gc')
    },
    {
        'url': 'http://i.xunlei.com/login.html',
        'frame': 'loginIframe',
        'click': (By.ID, 'turnRegister'),
        'phone': (By.XPATH, '//input[@id="pr_m"]'),
        'register': (By.ID, 'pr_gc')
    },
    {
        'url': 'http://jz.fkw.com/reg.html',
        'frame': 'regIframe',
        'phone': (By.XPATH, '//input[@id="regAcct"]'),
        'register': (By.CLASS_NAME, 'item_code')
    },
    # name after phone
    {
        'url': 'http://reg.jiayuan.com/signup/fillbasic.php',
        'phone': (By.ID, 'phoneNumber'),
        'name': (By.ID, 'mobile_vali'),
        'sleep': True,
        'register': (By.XPATH, '//a[@id="get"]')
    },
    # script
    {
        'url': 'http://music.163.com/#/login',
        'script': 'top.reg();return false;',
        'sleep': True,
        'phone': (By.CLASS_NAME, 'j-phone'),
        'password': (By.CLASS_NAME, 'j-pwd'),
        'register': (By.CLASS_NAME, 'j-btn')
    },
    # password confirm
    {
        'url': 'https://account.youku.com/register.htm',
        'phone': (By.ID, 'passport'),
        'password': (By.ID, 'password'),
        'password_confirm': (By.ID, 'repeatPsd'),
        'register': (By.ID, 'getMobileCode')
    },
    # click
    {
        'url': 'https://passport.17173.com/register',
        'click': (By.LINK_TEXT, '手机注册'),
        'phone': (By.XPATH, '//input[contains(@class, "input-passport valid")]'),
        'password': (By.XPATH, '//input[contains(@class, "input-pw valid")]'),
        'register': (By.CLASS_NAME, 'get-captcha')
    },
    # double click
    {
        'url': 'https://passport.yhd.com/passport/register_input.do',
        'phone': (By.XPATH, '//input[@class="phone"]'),
        'password': (By.XPATH, '//input[@class="validPhoneCode"]'),
        'register': (By.CLASS_NAME, 'r_require_code')
    },
    # TODO: http://www.pptv.com/
    # TODO: http://vip.iqiyi.com/
    # TODO: http://www.eqxiu.com/
    # TODO: https://accounts.douban.com/register
    # TODO: http://zt.epwk.com/1607epzhelu/
    # TODO: https://memberprod.alipay.com/account/reg/index.htm
]


if __name__ == '__main__':
    SMSBooming('').run()
