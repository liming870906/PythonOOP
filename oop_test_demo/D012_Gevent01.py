import urllib
import urllib2
# 1. 导入Python SSL处理模块
import ssl

# 2. 表示忽略未经核实的SSL证书认证

context = ssl._create_unverified_context()

url = "https://www.tingtingfm.com/"  # 此处为没有经过CA认证的URL地址。
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
request = urllib2.Request(url, headers=headers)
# 3. 在urlopen()方法里 指明添加 context 参数
response = urllib2.urlopen(request, context=context)
print(response.read())