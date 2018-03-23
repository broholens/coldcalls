import time
import random
from itertools import count
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
d = webdriver.Firefox(options=options)

url = 'https://ppss.xdf.cn/h5/2-teacher/index.html?userId=gaoxiang15@xdf.cn&schoolId=6&teacherCode=TC1540&source=woxueTeacher&sourceExt=TC1540&from=groupmessage&isappinstalled=0'

for i in count():
    print(i)
    try:
        d.get(url)
        d.find_element_by_class_name('js-like').click()
        time.sleep(random.randrange(1, 3))
    except:
        pass