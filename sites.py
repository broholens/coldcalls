# 会主动给电话号码打电话的网站
call_list = [
    {
        'url': 'https://www.liuxue86.com/',
        'iframe': 'LR_miniframe',  # id or name contains
        'phone_xp': '//input[@id="tel"]',
        'submit_xp': '//input[@id="telbtn"]'
    },
    {
        'url': 'http://www.wangxiao.cn/',
        'iframe': 'setFrame',  # id or name
        'phone_xp': '//div[@class="chat-view-window-editor"]/textarea',
        'text_f': '您好,我是{},想咨询二建,这是我的手机号{},您可以直接打我手机联系'
    },
    {
        'url': 'http://www.beimu.com/school/',
        'phone_xp': '//div[@class="jesong_chat_bottom"]/textarea',
        'text_f': '您好,我是{},想咨询雅思,这是我的手机号{},您可以直接打我手机联系'
    },
    {
        'url': 'https://www.zgjhjy.com/',
        'phone_xp': '//div[@class="jesong_chat_bottom"]/textarea',
        'text_f': '您好,我是{},想为孩子咨询数学,这是我的手机号{},您可以直接打我手机联系'
    },
    {
        'url': 'https://m.hbcjw.com/hncj/',
        'iframe': 'setFrame',  # id or name
        'phone_xp': '//div[@class="chat-view-window-editor"]/textarea',
        'text_f': '您好,我是{},想咨询成教,这是我的手机号{},您可以直接打我手机联系',
        # iframe之前要执行的js
        'before': "NTKF.im_openInPageChat('kf_10365_1539068284078')"
    },
    {
        'url': 'https://m.hbcjw.com/hncj/',
        'iframe': 0,  # 第一个
        'name_xp': '//input[@id="userName"]',
        'phone_xp': '//input[@id="tel"]',
        'submit_xp': 3  # enter 3 次
    },
    {
        'url': 'http://www.gemstonecn.com/consociation.php',
        'iframe': 'LR_miniframe',  # id or name contains
        'phone_xp': '//input[@id="tel"]',
        'submit_xp': '//input[@id="telbtn"]'
    },
    {
        'url': 'http://bdzqc.zsld101.com/web/846/15538/23597/index_tpl.htm',
        'name_xp': '//input[@id="name"]',
        'phone_xp': '//input[@id="mobile"]',
        'submit_xp': '//input[@class="tj_ly"]'
    },
    # iframe 嵌套 写在body里面
    # {
    #     'url': 'https://m.hbcjw.com/hncj/',
    #     'iframe': 'ECHAT_mini_chat',  # id or name
    #     'phone_xp': '//div[@class="chat-view-window-editor"]/textarea',
    #     'text_f': '您好,我是{},想咨询成教,这是我的手机号{}',
    #     # iframe之前要执行的js
    #     'before': "return ECHAT.miniChat(this,2)"
    # },
    ###########################################
    # 此课程号可变化
    {
        'url': 'http://qy.thea.cn/nxk/51122.htm',
        'name_xp': '//input[@class="user-name"]',
        'phone_xp': '//input[@class="user-tel"]',
        'submit_xp': '//input[@class="submit"]'
    },
    {
        'url': 'https://www.zhangmen.org/lp/sem',
        'name_xp': '//input[@id="s-name"]',
        'phone_xp': '//input[@id="stu_mobile1"]',
        'submit_xp': '//button[@id="pcheaderbtn2"]'
    },
    {
        'url': 'http://bd.jiameng.cn/angli/',
        'iframe': 'iframeMessage',  # id or name contains
        'name_xp': '//input[@id="txtName"]',
        'phone_xp': '//input[@id="txtTel"]',
        'submit_xp': 'return jmpricemsgsubmit();'
    },
    {
        'url': 'http://fd1.qinxue100.com/index.html',
        'phone_xp': '//input[@class="lxb-cb-input"]',
        'submit_xp': '//input[@class="lxb-cb-input-btn"]'
    },
    {
        'url': 'http://www.risecenter.com/',
        'iframe': 'doyoo_f_work',  # id or name contains
        'phone_xp': '//textarea[@id="message"]',
        'text_f': '您好,我是{},想为孩子咨询英语,这是我的手机号{},您可以直接打我手机联系'
    },
]