from bs4 import BeautifulSoup
import requests


# 单页的电影名 + 链接
def alone_page(soup):
    # 处理网页信息
    # 电影名1
    # content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)
    # 超链接地址1
    # content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a

    # 电影名2
    # content > div > div.article > ol > li:nth-child(2) > div > div.info > div.hd > a > span:nth-child(1)
    # 超链接地址2
    # content > div > div.article > ol > li:nth-child(2) > div > div.info > div.hd > a
    for i in range(1, 26):
        movie_name = soup.select("#content > div > div.article > ol > li:nth-child({}) > div > div.info > div.hd > a > span:nth-child(1)".format(i))
        # 注意此处是数组形式，因此不能用get_text()方法直接获取文本信息
        for j in movie_name:
            print(j.get_text())
        movie_url = soup.select("#content > div > div.article > ol > li:nth-child({}) > div > div.info > div.hd > a".format(i))
        # 同上，由于url不属于文本内容，因此使用get()方法获取url，否则会获取到url链接上面的文本
        for k in movie_url:
            print(k.get("href"))


def all_page():
    # https://movie.douban.com/top250
    # https://movie.douban.com/top250?start=25
    # https://movie.douban.com/top250?start=50
    # https://movie.douban.com/top250?start=75
    # https://movie.douban.com/top250?start=100
    soup_list = []
    for page in range(0, 226, 25):
        # 定制请求信息
        url = "https://movie.douban.com/top250?start={}".format(page)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'
        }
        # 获取响应数据
        response = requests.get(url=url, headers=headers)
        # 使用bs4进行解析
        soup = BeautifulSoup(response.text, "html.parser")
        # 调用获取单页数据的方法
        print("正在下载第{}页".format(page/25+1))
        soup_list.append(soup)
    return soup_list



if __name__ == '__main__':
    soup_list=all_page()
    for each_page in soup_list:
        alone_page(each_page)
