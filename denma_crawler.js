/*
 * phantomjs�� Ȱ���� �� ��ũ������ 0.1, 2013-11-30
 * http://start.goodtime.co.kr
 * (c) 2013 �̵���
 * MIT ���̼���
 */
 
/********** ���� ����. �Ʒ� ���� ������ ������ �����ؾ� �� ***********/
 
// ���� ���������� URL. �� �ּҺ��� �����ؼ� ����Ʈ�� ��ũ�������Ѵ�.
var index = 1;
var url = 'http://comic.naver.com/webtoon/detail.nhn?titleId=119874&no='+ index+'&weekday=sun';
 
// ������������ � ����Ʈ�� ��ũ���������� �����ϴ� CSS ������
var contentSelectors = ['.wt_viewer #content_image_0', '.wt_viewer #content_image_1', '.wt_viewer #content_image_2',
			'.wt_viewer #content_image_3', '.wt_viewer #content_image_4'];
 
// ���� �������� ��ũ�� ã�� �� �ִ� CSS ������
var nextLinkSelector = '.btn_area .next a';
 
// �ִ�� ������ �������� ��
var maxPages = 890;
 
// ������ ����Ʈ ĸó �̹����� ������ ����
var saveTo = './captures';
 
/********** �� ���ϴ� ��ũ������ ���� �ڵ� ***************/
var webpage = require('webpage');
var page = webpage.create();
 
page.open(url, scrape);
 
function scrape(status) {
    if (status != 'success') {
        console.log('�������� ���� ����: ' + url);
        phantom.exit();
    }
 
    console.log(++index + ': ' + url);
 
    for (var i = 0; i < contentSelectors.length;) {
        var clipRect = page.evaluate(function (selector) {
            var o = document.querySelector(selector);
            return o ? o.getBoundingClientRect() : null;
        }, contentSelectors[i]);
 
        ++i;
        if (clipRect) {
            page.clipRect = clipRect;
	    if(index < 10){
		if( i < 10){
            		page.render(saveTo + '/' + "000"+index + '-' +"0"+ i + '.png');
		}
		else {
			page.render(saveTo + '/' + "000"+index + '-' + i + '.png');
		}
	    }
	    else if(index < 100 && index > 10){
            	if( i < 10){
            		page.render(saveTo + '/' + "00"+index + '-' +"0"+ i + '.png');
		}
		else {
			page.render(saveTo + '/' + "00"+index + '-' + i + '.png');
		}
	    }
	    else if(index < 1000 && index > 100){
            	if( i < 10){
            		page.render(saveTo + '/' + "0"+index + '-' +"0"+ i + '.png');
		}
		else {
			page.render(saveTo + '/' + "0"+index + '-' + i + '.png');
		}
	    }
	    else{
     	    	if( i < 10){
            		page.render(saveTo + '/' +index + '-' +"0"+ i + '.png');
		}
		else {
			page.render(saveTo + '/' + index + '-' + i + '.png');
		}
	    }
        }
    }
 
    url = page.evaluate(function(selector) {
        var o = document.querySelector(selector);
        return o ? o.href : null;
    }, nextLinkSelector);
 
    if (index >= maxPages || !url) {
        phantom.exit();
    }
 
    page.open(url, scrape);
}