import random
import time
import urllib.request

urls = [
    # This is my website
    "https://genshin-card.littlebell.top/",
    "https://count.littlebell.top/"
]
for url in urls:
    req = urllib.request.Request(url)
    req.add_header(
        'User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54',
    )
    req.add_header(
    'Accept-Language','zh-CN,zh;q=0.9'
    )
    data = urllib.request.urlopen(req).read()
    print(data)
    time.sleep(random.randint(5,10))
