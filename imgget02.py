import requests
from bs4 import BeautifulSoup
from PIL import Image
import io
import re

#対象のURL 毎回変わる
url = 'http://anacap.doorblog.jp/archives/57964364.html'
session = requests.session()
#sessionを変更する 必須ではない また効果も不明
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}
#通信してレスポンスを取得する
res = requests.get(url,headers = headers)
#レスパンスをパースする
soup = BeautifulSoup(res.text,'html.parser')
#末尾がjpgになるurlをさがす
pattern = re.compile(r'jpg$')
#対象のURLの構造からa hrefを取得する必要がある
img_tags = soup.find_all('a')
# print(img_tags)
for i,img_tag in enumerate(img_tags):
    #色々な構造からhrefのみを取り出す
    img_url = img_tag.get('href')
    #いろんなhrefタグの中から末尾がjpgのものをさがす
    if img_url is not None and pattern.search(img_url):
        #jpgとし保存する
        img = Image.open(io.BytesIO(requests.get(img_url).content))
        img.save(f'img/{(i+1800)+1}.jpg')
print('DL完了！')