import time
from random import choice
from itertools import cycle
from datetime import datetime
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.common.by import By


class SMSBooming:

    names = ['李先生', '王女士', '赵先生', '刘先生']
    passwords = ['aiahdia6', 'akahoaw1', 'akxhk8as', 'ahfaxh0q']

    def __init__(self, phone_number):
        self.phone = phone_number

    def create_driver(self):
        options = webdriver.FirefoxOptions()
        # options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        driver.set_page_load_timeout(10)
        return driver

    def request(self, d, url):
        try:
            d.get(url)
        except:
            try:
                d.execute_script('window.stop()')
            except:
                pass

    def boom(self, driver, platform):
        self.request(driver, platform['url'])
        name, password = platform.get('name'), platform.get('password')
        phone, verify = platform['phone'], platform['register']
        password_confirm = platform.get('password_confirm')
        _password = choice(self.passwords)
        try:
            if name is not None:
                driver.find_element(name[0], name[1]).send_keys(
                    choice(self.names))
            time.sleep(1)
            driver.find_element(phone[0], phone[1]).send_keys(self.phone[:3])
            time.sleep(1)
            driver.find_element(phone[0], phone[1]).send_keys(self.phone[3:7])
            time.sleep(1)
            driver.find_element(phone[0], phone[1]).send_keys(self.phone[7:])
            if password is not None:
                driver.find_element(password[0], password[1]).send_keys(
                    _password)
            if password_confirm is not None:
                driver.find_element(password_confirm[0],
                                    password_confirm[1]).send_keys(_password)
            driver.find_element(verify[0], verify[1]).click()
        except:
            pass

    def timer(self, start_time, platform):
        sleep = True
        while True:
            if datetime.now().hour != start_time or sleep is True:
                time.sleep(60 * 60)
                sleep = False
                continue
            driver = self.create_driver()
            for tel in platform:
                self.boom(driver, tel)
                time.sleep(5)
            driver.close()
            sleep = True

    def run_telephone(self):
        """10点开刷　刷一次"""
        self.timer(10, telephone)

    def run_daily(self):
        self.timer(12, daily)

    def run_constantly(self):
        driver = self.create_driver()
        for platform in cycle(constantly):
            self.boom(driver, platform)
            time.sleep(10)

    def run(self):
        p1 = Process(target=self.run_constantly)
        p2 = Process(target=self.run_daily)
        p3 = Process(target=self.run_telephone)
        p1.start()
        p2.start()
        p3.start()


constantly = [
    {
        'url': 'https://www.zhihu.com/signup',
        'phone': (By.NAME, 'phoneNo'),
        'register': (By.CLASS_NAME, 'SignFlow-smsInputButton')
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
    {
        'url': 'http://wuhan.bdcgw.cn/pctg/2345/2961/?A',
        'phone': (By.XPATH, '//input[@name="tgMobile1"]'),
        'register': (By.ID, 'btnTg1')
    },
    {
        'url': 'http://www.wanke001.com/Register/Register.aspx',
        'phone': (By.ID, 'txtMobile'),
        'register': (By.ID, 'sendCode')
    },
    {
        'url': 'http://passport.cnmo.com/register/',
        'phone': (By.XPATH, '//input[@id="m_mobile"]'),
        'name': (By.XPATH, '//input[@id="m_uname"]'),
        'password': (By.XPATH, '//input[@id="m_password"]'),
        'password_confirm': (By.XPATH, '//input[@id="m_confirm"]'),
        'register': (By.XPATH, '//input[@id="m_getcode"]')
    },
    {
        'url': 'https://my.22.cn/register.html',
        'phone': (By.XPATH, '//input[@id="iphoneCode"]'),
        'register': (By.XPATH, '//input[@id="iphone-code-get"]'),
    },
    {
        'url': 'http://www.888v666.com/zzsq/',
        'phone': (By.XPATH, '//input[@id="mobile"]'),
        'register': (By.XPATH, '//span[@class="item_code"]')
    },
    {
        'url': 'http://u.tiandaoedu.com/register.html',
        'phone': (By.ID, 'u_phone'),
        'password': (By.ID, 'p_verify'),
        'register': (By.CLASS_NAME, 'w_inp_yzm')
    }
]


telephone = [
    {
        'url': 'http://www.taisha.org/',
        'phone': (By.XPATH, '//input[@class="lxb-cb-input"]'),
        'register': (By.XPATH, '//input[@class="lxb-cb-input-btn"]')
    },
    {
        'url': 'http://www.xinquanedu.com/zt/2017/xinquan/',
        'phone': (By.XPATH, '//input[@class="lxb-cb-input"]'),
        'register': (By.XPATH, '//input[@class="lxb-cb-input-btn"]')
    },
    {
        'url': 'http://sg.ivygate.info/',
        'phone': (By.XPATH, '//input[@class="lxb-cb-input"]'),
        'register': (By.XPATH, '//input[@class="lxb-cb-input-btn"]')
    },
    {
        'url': 'https://www.liuxue86.com/',
        'phone': (By.XPATH, '//form[@class="guestbook-fixed"]/input'),
        'register': (By.XPATH, '//form[@class="guestbook-fixed"]/button')
    },
    {
        'url': 'http://lp.liuxue.com/usa/hot/home/#/',
        'phone': (By.XPATH, '//input[@class="lxb-cb-input"]'),
        'register': (By.XPATH, '//input[@class="lxb-cb-input-btn"]')
    },
    {
        'url': 'http://liuxue.xdf.cn/',
        'phone': (By.ID, 'stu_Phone'),
        'name': (By.ID, 'stu_Name'),
        'register': (By.ID, 'dosubmit')
    },
    {
        'url': 'http://liuxue.shciic.com/',
        'name': (By.NAME, 'UserName'),
        'phone': (By.NAME, 'Phone'),
        'register': (By.XPATH, '//form[@id="submitform"]/div/input')
    },
    {
        'url': 'http://liuxue.fm/',
        'phone': (By.XPATH, '//input[@class="lxb-cb-input"]'),
        'register': (By.XPATH, '//input[@class="lxb-cb-input-btn"]')
    },
    {
        'url': 'http://yingguo.liuxue86.com/',
        'name': (By.NAME, 'uname'),
        'phone': (By.NAME, 'telephone'),
        'register': (By.CLASS_NAME, 'btn-assertive')
    },
    {
        'url': 'http://xa.jiajiaoban.cn/pc/izk/index.html',
        'phone': (By.ID, 'studentname2'),
        'name': (By.ID, 'mobilephone2'),
        'register': (By.CLASS_NAME, 'xes-btn1')
    },
    {
        'url': 'http://xa.zgjhjy.com/',
        'name': (By.ID, 'name'),
        'phone': (By.ID, 'phone'),
        'register': (By.ID, 'btn')
    },
    {
        'url': 'http://ruishi.liuxue86.com/',
        'name': (By.NAME, 'uname'),
        'phone': (By.NAME, 'telephone'),
        'register': (By.CLASS_NAME, 'btn-assertive')
    },
]

daily = [
    {
        'url': 'http://longmenedu.com.cn/baoming.asp',
        'name': (By.NAME, 'UserName'),
        'phone': (By.NAME, 'Mtel'),
        'register': (By.NAME, 'Submit')
    },
    {
        'url': 'http://www.xascedu.com/',
        'name': (By.XPATH, '//input[@id="msgLeft_senderName"]'),
        'phone': (By.XPATH, '//input[@id="msgLeft_telephone"]'),
        'register': (By.XPATH, '//img[@id="msgLeft_Btn"]')
    },
    {
        'url': 'https://h5.ele.me/login/',
        'phone': (By.XPATH, '//section[@class="MessageLogin-FsPlX"]/input'),
        'register': (By.XPATH, '//section[@class="MessageLogin-FsPlX"]/button')
    },
    {
        'url': 'https://passport.womai.com/register/redirect.do',
        'phone': (By.XPATH, '//input[@id="Email"]'),
        'name': (By.XPATH, '//input[@id="loginId"]'),
        'password': (By.XPATH, '//input[@id="password"]'),
        'password_confirm': (By.XPATH, '//input[@id="password2"]'),
        'register': (By.XPATH, '//input[@id="validBtn"]')
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
]

special = [
    # alert
    {
        'url': 'https://liuxue.bfsu.edu.cn/apply/index.php/welcome',
        'name': (By.NAME, 'name'),
        'phone': (By.NAME, 'tel'),
        'register': (By.ID, 'sendEmail')
    },
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
    # 获取不到
    {
        'url': 'http://www.lofter.com/phoneAccount/register',
        'phone': (By.XPATH, '//input[@id="phone-num"]'),
        'register': (By.LINK_TEXT, '获取验证码')
    },

    # TODO: http://www.pptv.com/
    # TODO: http://vip.iqiyi.com/
    # TODO: http://www.eqxiu.com/
    # TODO: http://www.baixing.com/oz/verify/reg
    # TODO: https://www.a5.net/member.php?mod=register
    # TODO: https://accounts.douban.com/register
    # TODO: http://zt.epwk.com/1607epzhelu/
    # TODO: http://www.liuxue51.net/user/register
    # TODO: https://memberprod.alipay.com/account/reg/index.htm
]


if __name__ == '__main__':
    SMSBooming('13909188482').run()
