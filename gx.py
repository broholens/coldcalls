import grequests

urls = [
    'https://ppssp.xdf.cn/Mobile_Teacher_Home/like?u=gaoxiang15%40xdf.cn&protocol=https%3A',
    'https://ppssp.xdf.cn/Mobile_Teacher_Home/like?u=weiyunpeng%40xdf.cn&protocol=https%3A',
    'https://ppssp.xdf.cn/Mobile_Teacher_Home/like?u=hanyang%40xdf.cn&protocol=https%3A',
    'https://ppssp.xdf.cn/Mobile_Teacher_Home/like?u=liuchongyou%40xdf.cn&protocol=https%3A',
    'https://ppssp.xdf.cn/Mobile_Teacher_Home/like?u=lichen44%40xdf.cn&protocol=https%3A',
    'https://ppssp.xdf.cn/Mobile_Teacher_Home/like?u=shangguanhe%40xdf.cn&protocol=https%3A',
    'https://ppssp.xdf.cn/Mobile_Teacher_Home/like?u=wangqisong%40xdf.cn&protocol=https%3A'
]


def exception_handler(request, exception):
    print('error')


def g_request():
    rs = (grequests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'}) for url in urls)
    tasks = grequests.imap(rs, exception_handler=exception_handler)
    for task in tasks:
        print(task.json())

        
if __name__ =='__main__':
    while True:
        g_request() 
