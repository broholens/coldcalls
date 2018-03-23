from itertools import count
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
d = webdriver.Firefox(options=options)

urls = [
    # 'https://ppss.xdf.cn/h5/2-teacher/index.html?userId=gaoxiang15@xdf.cn&schoolId=6&teacherCode=TC1540&source=woxueTeacher&sourceExt=TC1540&from=groupmessage&isappinstalled=0',
    'https://ppss.xdf.cn/h5/2-teacher/index.html?userId=weiyunpeng@xdf.cn&schoolId=6&teacherCode=TC1537&source=woxueTeacher&sourceExt=TC1537&from=groupmessage&isappinstalled=0'
    'https://ppss.xdf.cn/h5/2-teacher/index.html?userId=hanyang9@xdf.cn&schoolId=6&teacherCode=TC1539&source=woxueTeacher&sourceExt=TC1539&from=groupmessage&isappinstalled=0',
    'https://ppss.xdf.cn/h5/2-teacher/index.html?userId=liuchongyou@xdf.cn&schoolId=6&teacherCode=TC1546&source=woxueTeacher&sourceExt=TC1546&from=groupmessage&isappinstalled=0',
    'https://ppss.xdf.cn/h5/2-teacher/index.html?userId=lichen44@xdf.cn&schoolId=6&teacherCode=TC1553&source=woxueTeacher&sourceExt=TC1553&from=groupmessage&isappinstalled=0',
    'https://ppss.xdf.cn/h5/teacher/index.html?userId=shangguanhe@xdf.cn&schoolId=6&teacherCode=TC1556&source=woxueTeacher&sourceExt=TC1556&from=singlemessage&isappinstalled=0',
    'https://ppss.xdf.cn/h5/2-teacher/index.html?userId=wangqisong@xdf.cn&schoolId=6&teacherCode=TC1511&source=woxueTeacher&sourceExt=TC1511&from=singlemessage&isappinstalled=0'
]

for i in count():
    print(i)
    for url in urls:
        try:
            d.get(url)
            d.find_element_by_class_name('js-like').click()
        except:
            pass
