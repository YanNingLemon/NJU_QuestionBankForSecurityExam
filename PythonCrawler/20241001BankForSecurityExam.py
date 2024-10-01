# 从20200928爬取南京大学实验室安全考试题库_02多个题目for循环.py修改而来
# 2024年，学校改用统一身份认证并且添加了全部题目分类，所以无需再手动修改题目种类分段爬取，可以一次将全部题库爬取下来
# 同时题库也增删到了1745题

import requests
from bs4 import BeautifulSoup # 借助BeautifulSoup包解析
import os # 用于文件目录操作

# 头部
headers = {
    "Accept":"",
    "Accept-Encoding":"",
    "Accept-Language":"",
    "Cache-Control":"",
    "Connection":"",
    "Content-Length":"",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie":"", # 请使用自己的header
    "Host":"",
    "Origin":"",
    "Sec-Fetch-Dest":"",
    "Sec-Fetch-Mode":"",
    "Sec-Fetch-Site":"",
    "Sec-Fetch-User":"",
    "Upgrade-Insecure-Requests":"",
    "User-Agent":"",
}



# 最终成果文本
resultStr=""

# 从第1题循环到第1040题
for i in range(1, 1746):
    print(i)
    # url = "http://aqks.nju.edu.cn/pc/PersonInfo/StartExercise_Mobile.aspx?TestNum=1&SelTestNum=170&SelectTest=yes"
    # TestNum含义不明，值为1，好像是题目种类，好像又不是
    # SelTestNum表示题号
    url = "https://aqks.nju.edu.cn/PersonInfo/StartExercise.aspx"
    # url = "http://aqks.nju.edu.cn/pc/PersonInfo/StartExercise_Mobile.aspx"
    d={'TestNum':'1','SelectTest':'yes'} # 这里修改了data的内容，为了适配从全部题目中爬取
    # 修改题号
    d['TestNum']=str(i) # 这里修改了data的内容，为了适配从全部题目中爬取
    # post获取网页
    response=requests.post(url,data=d,headers=headers)
    # 解析网页
    soup=BeautifulSoup(response.text)
    # 构造id
    idStr='trTestTypeContent'+str(i)
    # 找到id为idStr的table标签
    QuestionTable=soup.find_all('table',{'id':'trTestTypeContent1'}) # 实践发现所有的题目都是id为trTestTypeContent1
    # QuestionTable=soup.find_all('table',{'id':idStr})
    # 打印，查看信息
    # QuestionTable

    # 题目类型 单选题/判断题/多选题
    resultStr=resultStr+'题目类型：'+QuestionTable[0].find('input')["value"]+'\n'

    # 题目、答案和解析
    QuestionStr=QuestionTable[0].find_all('td')
    # for i in range(len(test)):
    for i in QuestionStr:
        if(i.text!=''):
            print(i.text)
            # resultStr+=i.text+'\n'
    resultStr+='\n'

# 查看成果文本
# 结果文本中出现选项的重复，但是不影响使用不是吗
resultStr

# 打开文件夹
dataFolder=r"D:\workspace\ybj"
os.chdir(dataFolder) # 打开文件目录，相当于cd
os.getcwd() # 返回当前工作目录，显示当前文件目录

# 写入文本文件
a= open('20241001BankForSecurityExam.txt','w',encoding='UTF-8')
a.write(resultStr)
a.close()