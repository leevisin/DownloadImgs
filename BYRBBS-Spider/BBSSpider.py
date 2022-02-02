from pyquery import PyQuery as pq
import requests
import time
import csv
import re

def article(pp,x_doc,session,my_header,writer,user):
    """
    对每个帖子进行数据获取
    :param pp: 版块的第几页
    :param x_doc: html的pyquery对象
    :param session: 会话对象
    :param my_header: 请求头
    :param writer: csv文件的指针
    :param user: 北邮人用户名
    """
    for tr in x_doc('tbody').children():
        link = 'https://bbs.byr.cn'+pq(tr).find('.title_9 a').attr('href')+'?_uid={usr}'.format(usr=user)+'&p={p}'
        title = pq(tr).find('.title_9 a').text()
        com_num = int(pq(tr).find('.title_11.middle').text())
        #计算该帖子有多少页回复
        article_pages = int(com_num/10)+1
    
        #翻页，获取每页的所有评论
        for p in range(1,article_pages+1):
            a_resp = session.get(link.format(p=p), headers=my_header)
            a_doc = pq(a_resp.text)
            com_texts = ''
            for com in a_doc.items('.a-content-wrap'):
                comment = str(com.children().eq(3)).replace('<br/>', '')
                #用正则剔除无效信息（只保留中文,。！？@等符号）
                comment = ''.join([x for x in re.findall(r'[\u4e00-\u9fa5A-Z0-9a-z\,，。！!@？\? \t\r]*', comment) if 'bd' not in x])
                if comment:
                    com_texts+=comment+'\r'
                print(pp,title,comment)
            #写入csv文件
            try:
                writer.writerow((title,com_texts))
            except:
                pass


def get_data(user, password, board,filename):
    """
    获取北邮人论坛考研版块的数据，保存到csv中
    :param user: 北邮人论坛账号
    :param password: 北邮人论坛密码
    :param board: 北邮人论坛子版块
    :param filename: 数据保存的文件名
    """
    
    #创建csv文件
    csvf = open('{}.csv'.format(filename),'a+',encoding='gbk',newline='')
    writer = csv.writer(csvf)
    #writer.writerow(('帖子名','回复'))
    
    #登录北邮人论坛，创建session会话
    my_header = {'x-requested-with': 'XMLHttpRequest'}
    byr_data = {'id': user, 'passwd': password}
    session = requests.Session()
    r_url = 'https://bbs.byr.cn/user/ajax_login.json'
    req = session.post(r_url, data=byr_data, headers=my_header)
    # 查看登录是否成功
    print(req.json())
    #开始在考研版块翻页，获取每页中的帖子信息
    first_page_url = 'https://bbs.byr.cn/board/{board}?p={page}&_uid={usr}'.format(board=board,page=1, usr=user)
    first_resp = session.get(first_page_url, headers=my_header)
    first_html = first_resp.text
    first_doc = pq(first_html)
    pages = int(first_doc('.page-main').children().eq(-2).find('a').text())
    for page in range(1, pages + 1): 
        if page == 1:
            #对该版块的第一页的所有帖子进行抓取
            article(page,first_doc, session, my_header, writer, user)
        else:
            x_page_url = 'https://bbs.byr.cn/board/{board}?p={page}&_uid={usr}'.format(board=board,page=page, usr=user)
            x_resp = session.get(x_page_url, headers=my_header)
            x_doc = pq(x_resp.text)
            #对该版块剩余页面的所有帖子进行抓取
            article(page,x_doc, session, my_header, writer, user)
    csvf.close()
    
    
user='userID'
password='yourPassword'
board = 'IWhisper' #信息社会>悄悄话
filename = 'data'

get_data(user,password,board,filename)
