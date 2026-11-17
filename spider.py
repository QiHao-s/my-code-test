import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    # 1. 目标网址（这是一个专门给新手练爬虫的合法网站）
    url = 'http://quotes.toscrape.com/'
    
    # 2. 发送请求，获取网页源代码
    print("正在拜访网站...")
    # 加上 headers 伪装成浏览器，更礼貌也不容易被拦截
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)
    
    # 检查一下有没有连上
    if response.status_code == 200:
        print("连接成功，开始解析代码！")
    else:
        print("连接失败，状态码：", response.status_code)
        return

    # 3. 把网页源代码交给 BeautifulSoup 去解析
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 4. 找到所有包含名言的区块
    quotes = soup.find_all('div', class_='quote')
    
    # 5. 准备一个列表存数据
    data_to_save = []
    
    # 6. 循环提取每一句名言和作者
    for q in quotes:
        text = q.find('span', class_='text').text # 提取名言内容
        author = q.find('small', class_='author').text # 提取作者名字
        
        print(f"抓取到: [{author}] - {text}")
        data_to_save.append([author, text])
        
    # 7. 把所有数据保存到 CSV 表格里
    with open('quotes.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['作者', '名言']) # 表头
        writer.writerows(data_to_save)    # 写入数据
        
    print("\n🎉 抓取完毕！所有名言已保存到 quotes.csv 文件中。")

if __name__ == "__main__":
    scrape_quotes()