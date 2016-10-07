# -*- coding: utf-8 -*-
# 제작자 : 나종찬
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import os
import urllib
import urllib2
import time

from selenium import webdriver
headers = {
    'content-type' : 'application/x-www-form-urlencoded;charset=UTF-8;text/html',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

company_name_list =[]
def get_company_name(browser, url):
    browser.get(url)    #브라우저 켜기
    time.sleep(1)
    try:
        table_list = browser.find_element_by_class_name("table_list")
        tbody = table_list.find_element_by_tag_name("tbody")
        tr_list = tbody.find_elements_by_tag_name("tr")

        for tr in tr_list:
            a_list = tr.find_elements_by_tag_name("a")
            for a in a_list:
                f.write(a.text.lower() + "\n")

    except:             # 예외 처리
        return
if os.path.isdir("/dart") == 0:      # 저장용 폴더 생성
   os.mkdir("/dart")

f = open("/dart/company_list.txt", 'wt')

#browser = webdriver.Firefox()
browser = webdriver.PhantomJS(executable_path="C:\MyPython\phantomjs.exe" )
# range() page 까지 검색
for i in range(1, 1313):
    try:
        target_url = "http://dart.fss.or.kr/dsae001/search.ax?startDate=&endDate=&currentPage="\
                     + str(i) + "&maxResults=45&maxLinks=10&sort=&series=&selectKey=&searchIndex=&textCrpCik=&autoSearch=true&textCrpNm=&typesOfBusiness=all&corporationType=all"
        print target_url
        get_company_name(browser, target_url)       # html 링크 저장 함수
    except:         # 예외처리
        continue

browser.close()
f.close()