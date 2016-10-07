# -*- coding: EUC-KR -*-
# 제작자 : 나종찬
#import sys
import re
import os
import urllib
import urllib2

from selenium import webdriver
# 조선일보 html 코드에서 텍스트를 가져오는 함수

link_list = []                      # 기사 링크 저장 리스트
title_list =[]
def get_html(browser, url):        # 기사의 링크를 가져오는 함수
    browser.get(url)                # 브라우저 켜기
    try:
        type_1 = browser.find_element_by_class_name("type_1")       # 기사 제목 찾기
        tr_list = type_1.find_elements_by_tag_name("tr")
        print ("test")
        for tr in tr_list:
            try:
                file_loc = tr.find_element_by_class_name("file")
                a = file_loc.find_element_by_tag_name("a")
                pdf_url = a.get_attribute('href')         # href의 주소를  title_url 로
                if ".pdf" in pdf_url :                     # biz.chosun 의 링크만
                    link_list.append(pdf_url)                 # 리스트에 추가
                stock_item = tr.find_element_by_class_name("stock_item")
                stock_item_text = stock_item.text
                date = tr.find_element_by_class_name("date")
                date_text = date.text
                title_text = stock_item_text +"_("+date_text+")"
                refined_title = re.sub("[*?<>\|/:]","",title_text)
                title_list.append(refined_title)
            except:
                continue
    except:     # 예외처리
        return

# 기사 본문 크롤링
def get_article(browser, url, title):
    browser.get(url)    #브라우저 켜기
    try:
        print(url)
        print (title)
        u = urllib2.urlopen(url)
        f = open("/report/stock_item/"+ title +".pdf", 'wb')
        f.write(u.read())
        #print(article.text)
        #proto_text = article.get_attribute('innerHTML')         # html 코드를 텍스트로 받기

        #text_fiㅣtered = re.sub("<(/)?([a-zA-Z1-9]*)(\s[a-zA-Z]*=[^>]*)*(/)?>", "",proto_text)   # html 코드에서 태그 제거
        #text_revised = re.sub("<!--(.*?)-->", "",text_fiㅣtered)     #   불필요한 부분 제거
        #text_revised = re.sub("\t\t", "", article.text)          # tab 제거
        #text_revised = re.sub("\n\n", "", text_revised)         # 줄바꿈 제거
        f.close()               # close

    except:             # 예외 처리
        return
if os.path.isdir("/report") == 0:      # 저장용 폴더 생성
   os.mkdir("/report")
if os.path.isdir("/report/stock_item") == 0:      # 저장용 폴더 생성
   os.mkdir("/report/stock_item")


# 검색할 내용을 입력
# 조선일보 검색
temp_url = "http://finance.naver.com/research/company_list.nhn?keyword=&searchType=brokerCode&brokerCode=57&writeFromDate=&writeToDate=&itemName=&itemCode=&x=35&y=7&page="
#browser = webdriver.Firefox()
browser = webdriver.PhantomJS(executable_path="C:\MyPython\phantomjs.exe" )
# range() page 까지 검색
for i in range(26):
    try:
        i += 1
        target_url = temp_url + str(i)      # url 페이지 이동
        get_html(browser, target_url)       # html 링크 저장 함수
    except:         # 예외처리
        continue

for j in range(len(link_list)):         # 링크의 리스트 크기만큼
    try:
        get_article(browser, link_list[j], title_list[j])      # 기사텍스트 저장 함수\
    except:
        continue
