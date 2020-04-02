from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus #한번 검색하면 ASCII 코드로 변환 된거 보여주기. 
#import ssl

#context = ssl.create_unverified_context()

baseUrl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
plusUrl = input("Write a topic that you want for your image training: ")
result = urlopen(baseUrl)
url = baseUrl + quote_plus(plusUrl)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')#html변수 에 저장했던 주소를 분석.
img = soup.find_all(class_="_img")

print(img[0])
folder = './' + plusUrl + '/'
n = 1
for i in img:
   # print(i["data-source"])
    imgUrl = i["data-source"]
    with urlopen(imgUrl) as f: #f = urlopen(imgUrl)
        with open(folder + plusUrl + str(n) + '.jpg', 'wb') as h: #image file = binary 0101010101000001010 
            img = f.read()
            h.write(img)
    print("Finished dowloading", n, "번째", imgUrl)
    n += 1
print('Downloaded all.')
