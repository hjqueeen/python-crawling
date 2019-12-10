import urllib.request as req

#파일 URL
img_url = 'http://www.picturebook-museum.com/uploads/books/02_1654.jpg'
html_url = 'http://google.com'

#다운받을 경로
save_path1 = 'C:/test1.jpg'
save_path2 = 'C:/index.html'

#예외 처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download failed')
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)
    
    #다운로드 파일 정보
    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))
    print()

    #성공
    print('Download Succeed')

    