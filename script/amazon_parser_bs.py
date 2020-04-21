# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import URLError, HTTPError
import re
import csv
import time
import sys
import requests
import hmac
import hashlib
import base64
import urllib.parse
from datetime import datetime
from bs4 import BeautifulSoup


class AmazonProductAdvertisingAPI:

    def __init__(self, associate_id='researchatf04-22'):
        """ 初期化処理 """
        # ハッシュ関数とエンコードをset
        self.hash_func = hashlib.sha256
        self.encode_func = base64.b64encode
        #id,keyのset
        self.ACCESS_KEY = 'AKIAIL7AYT2Z43TYXGOA'
        self.SECRET_KEY = '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'
        self.ASSOCIATE_ID = associate_id

    def get_info(self, asin_code = 'B07K84PQJN'):
        api_domain = 'webservices.amazon.co.jp'
        api_page = '/onca/xml'
        # 商品のASINコード、ASINコードがない場合はISBN-10
        asin_code = asin_code
        # パラメーター用のタイムスタンプを生成
        time_stamp = urllib.parse.quote(datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))
        # URLパラメータのセット
        query='AWSAccessKeyId=' + self.ACCESS_KEY + \
            '&AssociateTag=' + self.ASSOCIATE_ID + \
            '&ItemId=' + asin_code + \
            '&Operation=ItemLookup' + \
            '&ResponseGroup=Images%2CItemAttributes%2COffers%2CReviews' + \
            '&Service=AWSECommerceService' + \
            '&Timestamp=' + time_stamp + \
            '&Version=2013-08-01'
        message = '\n'.join(['GET', api_domain, api_page, query])
        # HMACのSignature生成（ハッシュ値を算出）
        sing_gen = hmac.new(self.SECRET_KEY.encode('utf8'), message.encode('utf8'), self.hash_func)
        raw_sign = sing_gen.digest()
        sign = urllib.parse.quote(self.encode_func(raw_sign))

        # API用URLの生成
        url = 'http://' + api_domain + api_page + '?' + query + '&Signature=' + sign

        res = requests.get(url)
        print(res.text)
        soup = BeautifulSoup(res.text,'lxml')

        # 商品情報を取得
        productgroup = self.get_productgroup(soup)
        detailpageurl = self.get_url(soup)
        largeimage = self.get_largeimage(soup)
        title = self.get_title(soup)
        price = self.get_price(soup)
        amount = self.get_amount(soup)
        price_time = datetime.now().strftime('%Y年%m月%d日 %H時%M分時点')
        author = self.get_author(soup)
        brand = self.get_brand(soup)
        link_text = 'Amazon 詳細ページへ'


        result = {'productgroup':productgroup, 'asin_code':asin_code, 'detailpageurl':detailpageurl, 'largeimage':largeimage, 'title':title, 'price':price, 'amount':amount, 'author':author, 'brand':brand, 'price_time':price_time, 'link_text':link_text}

        return result

    def get_productgroup(self, soup):
        return soup.find('itemattributes').find('productgroup').text.strip()

    def get_url(self, soup):
        return soup.find('item').find('detailpageurl').text.strip()

    def get_largeimage(self, soup):
        return soup.find('largeimage').find('url').text.strip()

    def get_title(self, soup):
        return soup.find('itemattributes').find('title').text.strip()

    def get_price(self, soup):
        return soup.find('offersummary').find('formattedprice').text.strip()

    def get_amount(self, soup):
        return soup.find('offersummary').find('amount').text.strip()

    def get_brand(self, soup):
        return soup.find('itemattributes').find('publisher').text.strip()

    def get_author(self, soup):
        return soup.find('itemattributes').find('author').text.strip()

print ("|  名前  |  画像 | 既刊 | 完結済み | 紹介エピソード|")
print ("| ------ | ----- | ---- | -------- | ------------- |")
 
tsvFile = open("../reference/manga_db.tsv")
tsv = csv.reader(tsvFile, delimiter = '\t')
for i, s in enumerate(tsv):
    if i == 0:
        continue
    url = s[2]
    request = urllib.request.Request(url)
    sss = False
    while True:
        try:
            htmldata = urllib.request.urlopen(request)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        else:
            sss = True
        if sss:
            break
        time.sleep(1)

    status = htmldata.getcode() # ステータスコード
    #print(status)
    if status != 200:
        raise

    html = htmldata.read().decode('utf-8')
    bs = BeautifulSoup(html, "lxml")
    collection_size = bs.find("span",id="collection-size")
    if collection_size:
        match = re.search(r'\d+',collection_size.text)
        kansuu = match.group()

        ikkan_jouhou = bs.find('div', id='series-childAsin-item_1')
    #    print(ikkan_jouhou)
        ikkan_link = ikkan_jouhou.find("a").get("href")
        match2 = re.search('\/gp\/product\/([^?]+)',ikkan_link)
        #print(ikkan_link)
        ikkan_link = ikkan_jouhou.find("img").get("src")
        imglink = ikkan_link
        amazonid = match2.groups()[0]
    #    amazonaf = AmazonProductAdvertisingAPI()
    #    amazonaf.get_info()
    #    print(amazonaf.get_title())
        #print(create_amazon_imagelink(match2.groups()))

        print ("|" + s[0] + '|' + '[![{}]({})]({})'.format(s[0],imglink,s[2]) + "|" + kansuu + "|" + s[3] + "|" + "[{}](episode/{})".format(s[1],s[1]) + "|")

    else:
        ikkan_link = bs.find("img",id="ebooksImgBlkFront")

        if ikkan_link:
            imglink = ikkan_link.get("src")
            print ("|" + s[0] + '|' + '[![{}]({})]({})'.format(s[0],imglink,s[2]) + "|" + "1" + "|" + s[3] + "|" + "[{}](episode/{})".format(s[1],s[1]) + "|")
        else:
            book_div = bs.find("div",id="booksImageBlock_feature_div")
            imglink = book_div.find("img").get("src")
            print ("|" + s[0] + '|' + '[![{}]({})]({})'.format(s[0],imglink,s[2]) + "|" + "1" + "|" + s[3] + "|" + "[{}](episode/{})".format(s[1],s[1]) + "|")
    time.sleep(1)

