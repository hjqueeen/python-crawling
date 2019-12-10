# section 02-2
# 파이썬 크롤링 기초
# urlopen 함수 기초 사용법

import urllib.request as req 
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명
path_list = ["c:/test1.jpg", "c:/index.html"]

# 다운로드 리소스 url
target_url = ["http://www.picturebook-museum.com/uploads/books/20191125_01.jpg",
 "http://google.com"]
 

for i, url in enumerate(target_url):
    #예외 처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        #수신 내용
        contents = response.read()

        print("----------------------------")

        #t상태 정보 중간 출력
        print('Header Info-{} : {} '.format(i, response.info()))
        print('HTTP Status Code: {}'.format(response.getcode()))
        print()
        print('---------------------------')






    except HTTPError as e:
        print("Dowmloead failed.")
        print("HTTPError code : ", e.code)
    except URLError as e:
        print("Download failed.")
        print("URL Error Reason : ", e.reason)

    #성공
    else:
        print()
        print("Download Succeed.")






