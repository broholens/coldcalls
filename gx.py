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
    rs = (grequests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}) for url in urls)
    tasks = grequests.imap(rs, exception_handler=exception_handler)
    for task in tasks:
        print(task.json())
if __name__ =='__main__':
    while True:
        g_request() 
