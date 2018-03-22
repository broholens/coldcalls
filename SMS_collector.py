from selenium import webdriver
from selenium.webdriver.common.by import By


class SMSCollector:

    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)
        self.driver.set_page_load_timeout(10)


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
    # TODO: http://zt.epwk.com/1607epzhelu/
    {
        'url': 'https://m.weibo.cn/reg/index',
        'phone': (By.ID, 'sms_phone_input'),
        'password': (By.ID, 'sms_pwd_input'),
        'register': (By.ID, 'sms_vcode_fetch')
    },
    {
        'url': 'https://weibo.com/signup/signup.php',
        'phone': (By.NAME, 'username'),
        'password': (By.NAME, 'passwd'),
        'register': (By.CLASS_NAME, 'W_btn_e')
    },
    {
        'url': 'https://ssl.zc.qq.com/v3/index-en.html',
        'phone': (By.ID, 'phone'),
        'register': (By.ID, 'get_acc')
    },
    {
        'url': 'https://www.cmpassport.com/umc/reg/alias/',
        'phone': (By.ID, 'txtPhone'),
        'register': (By.ID, 'btnGetSmsCode')
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
        'url': 'https://passport.17173.com/register',
        'phone': (By.XPATH, '//input[contains(@class, "input-passport valid")]'),
        'password': (By.XPATH, '//input[contains(@class, "input-pw valid")]'),
        'register': (By.CLASS_NAME, 'get-captcha')
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
        'url': 'https://passport.yhd.com/passport/register_input.do',
        'phone': (By.XPATH, '//input[@class="phone"]'),
        'password': (By.XPATH, '//input[@class="validPhoneCode"]'),
        'register': (By.CLASS_NAME, 'r_require_code')
    },
    {
        'url': 'http://jz.fkw.com/reg.html',
        'phone': (By.XPATH, '//input[@id="regAcct"]'),
        'register': (By.CLASS_NAME, 'item_code')
    },
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
    # TODO: http://www.pptv.com/
    # TODO: http://vip.iqiyi.com/
    # TODO: http://www.eqxiu.com/
    # TODO: https://accounts.douban.com/register
    # TODO: https://memberprod.alipay.com/account/reg/index.htm
]

