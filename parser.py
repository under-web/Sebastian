import os

import requests
from PIL import Image
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from views import get_interface

class Spider:
    def __init__(self, url):
        self.url = url
        ua = UserAgent()
        self.agent = {'User-agent': ua.firefox}
        res = requests.get(url, headers=self.agent).text
        self.soup = BeautifulSoup(res, 'lxml')

    def get_status(self):
        r = requests.get(self.url, headers=self.agent)
        return int(r.status_code)

    def get_html(self):
        return self.soup

def safe_image(src):
    p = requests.get(src)
    out = open("img.jpg", "wb")
    out.write(p.content)
    out.close()

def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    # print('The original image size is {wide} wide x {height} '
    #       'high'.format(wide=width, height=height))

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    # print('The resized image size is {wide} wide x {height} '
    #       'high'.format(wide=width, height=height))
    # resized_image.show()
    resized_image.convert('RGB').save(output_image_path)


if __name__ == '__main__':

    lvl_scare = Spider('https://profinvestment.com/fear-greed-index-bitcoin-cryptocurrency/')
    safe_image(lvl_scare.get_html().find('div', "entry-content clearfix single-post-content").find('img').get('data-src'))



    bit_url = Spider('https://www.rbc.ru/crypto/currency/btcusd')
    price_bitcoin =  bit_url.get_html().find('div', class_="chart__subtitle js-chart-value").text.replace(' ', '').split(',')[0].strip() + '$'

    resize_image('img.jpg', 'new_img.png', (200,200))
    os.remove('img.jpg')


    get_interface(price_bitcoin)
