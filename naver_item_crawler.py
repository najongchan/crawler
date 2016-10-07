# -*- coding: EUC-KR -*-
# ������ : ������
#import sys
import re
import os
import urllib
import urllib2

from selenium import webdriver
# �����Ϻ� html �ڵ忡�� �ؽ�Ʈ�� �������� �Լ�

link_list = []                      # ��� ��ũ ���� ����Ʈ
title_list =[]
def get_html(browser, url):        # ����� ��ũ�� �������� �Լ�
    browser.get(url)                # ������ �ѱ�
    try:
        type_1 = browser.find_element_by_class_name("type_1")       # ��� ���� ã��
        tr_list = type_1.find_elements_by_tag_name("tr")
        print ("test")
        for tr in tr_list:
            try:
                file_loc = tr.find_element_by_class_name("file")
                a = file_loc.find_element_by_tag_name("a")
                pdf_url = a.get_attribute('href')         # href�� �ּҸ�  title_url ��
                if ".pdf" in pdf_url :                     # biz.chosun �� ��ũ��
                    link_list.append(pdf_url)                 # ����Ʈ�� �߰�
                stock_item = tr.find_element_by_class_name("stock_item")
                stock_item_text = stock_item.text
                date = tr.find_element_by_class_name("date")
                date_text = date.text
                title_text = stock_item_text +"_("+date_text+")"
                refined_title = re.sub("[*?<>\|/:]","",title_text)
                title_list.append(refined_title)
            except:
                continue
    except:     # ����ó��
        return

# ��� ���� ũ�Ѹ�
def get_article(browser, url, title):
    browser.get(url)    #������ �ѱ�
    try:
        print(url)
        print (title)
        u = urllib2.urlopen(url)
        f = open("/report/stock_item/"+ title +".pdf", 'wb')
        f.write(u.read())
        #print(article.text)
        #proto_text = article.get_attribute('innerHTML')         # html �ڵ带 �ؽ�Ʈ�� �ޱ�

        #text_fi��tered = re.sub("<(/)?([a-zA-Z1-9]*)(\s[a-zA-Z]*=[^>]*)*(/)?>", "",proto_text)   # html �ڵ忡�� �±� ����
        #text_revised = re.sub("<!--(.*?)-->", "",text_fi��tered)     #   ���ʿ��� �κ� ����
        #text_revised = re.sub("\t\t", "", article.text)          # tab ����
        #text_revised = re.sub("\n\n", "", text_revised)         # �ٹٲ� ����
        f.close()               # close

    except:             # ���� ó��
        return
if os.path.isdir("/report") == 0:      # ����� ���� ����
   os.mkdir("/report")
if os.path.isdir("/report/stock_item") == 0:      # ����� ���� ����
   os.mkdir("/report/stock_item")


# �˻��� ������ �Է�
# �����Ϻ� �˻�
temp_url = "http://finance.naver.com/research/company_list.nhn?keyword=&searchType=brokerCode&brokerCode=57&writeFromDate=&writeToDate=&itemName=&itemCode=&x=35&y=7&page="
#browser = webdriver.Firefox()
browser = webdriver.PhantomJS(executable_path="C:\MyPython\phantomjs.exe" )
# range() page ���� �˻�
for i in range(26):
    try:
        i += 1
        target_url = temp_url + str(i)      # url ������ �̵�
        get_html(browser, target_url)       # html ��ũ ���� �Լ�
    except:         # ����ó��
        continue

for j in range(len(link_list)):         # ��ũ�� ����Ʈ ũ�⸸ŭ
    try:
        get_article(browser, link_list[j], title_list[j])      # ����ؽ�Ʈ ���� �Լ�\
    except:
        continue
