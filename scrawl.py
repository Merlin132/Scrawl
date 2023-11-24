# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 18:37:15 2023

@author: 92188
"""

import requests
import re
import json


#产品网站：https://item.jd.com/100049336402.html

#—————————————————————————————————预处理得到url—————————————————————————————————

headers = {#伪装自己
    #哪个页面发出的数据，在检查-Network-Header里看
    'referer': 'https://h5.m.taobao.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'cookie': 'lLtC1_=1; t=c3def3054a290285b2765d025589a9b5; xlly_s=1; thw=us; hng=GLOBAL%7Czh-CN%7CUSD%7C999; sgcookie=E100qzDc%2FA18p6QbXk3jiCk1HQ1ihshKHwqWf5Aw8ZfuqdlC1KQbdMaoLWzH2tKT3W49Vc3iVY%2FLiKAtBFyNCR7%2BS%2Fvq3ZG%2B1MTEoaCdZu6iwQ%2F30AtmbtIHBtuDN4w6sf%2BC; mt=ci=0_0; tracknick=; cna=9NYjHWTZKXsBASQJiR79cmYb; _uetsid=3bfeaed0892411ee924a657c1fc340c2; _uetvid=3bfec0e0892411ee971d01631b68c3a5; _m_h5_tk=37bf6ad606318807bc2b16b239ffd1eb_1700672609184; _m_h5_tk_enc=10e142ecd5e2ebc77449764af186df2e; cookie2=1396a7c02d24ff65b0e8b35760538869; _tb_token_=5ae4bef8ef157; _samesite_flag_=true; isg=BIaGbQMTH8_RHMoHFhBVkqLV13wI58qhIfMRK3CvRqmFcyaN2HUasYoSSa-_XsK5; l=fBgIBtZnNdmjZtNdBOfaFurza77OSIRYSuPzaNbMi9fP9MCB5VxlW1eUif86C3GVF6WHR3RxBjFXBeYBqQd-nxvO6cSB23HmndLHR35..; tfstk=dVtvrTMDbbc0OQEvLS3o_-G6AZMoxnp2UIJQj1f05QdJZCBGmx5MyhCJdx5m7qR9yCOPosgVjdOJTIQi3KYc6Qp6p1YcSASO1p5yjEfiucH9PQY0s1v_BOs2qEqGijS9CBjttXmnxKJV7GGntcH63KJQ8iy-xDv23GSstXmn3UxmAT87_xz-GoxDktgg7rRYwFOFHZCLj_ETXAXAk69fwfhOQlxHv9rUt6BgkYH87P7fUcwkSL1..'
}

url=[]
#网址，方法略蠢，需要改良
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671477099&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671550344&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671556337&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=2&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671559110&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=3&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671562310&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=4&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671567548&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=5&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671571331&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=6&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671574297&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=7&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671576993&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=8&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671579290&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=9&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671582810&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=10&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671587286&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=11&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671591702&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=12&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671601815&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=13&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671610431&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=14&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671612778&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=15&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671614668&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=16&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671617571&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=17&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671619604&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=18&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671621754&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=19&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671625880&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=20&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671628230&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=21&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671630458&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=22&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671633056&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=23&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671635533&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=24&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671645379&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=25&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671649435&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=26&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671657855&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=27&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671660522&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=28&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671663709&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=29&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671712497&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=30&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671715164&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=31&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671716892&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=32&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671720753&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=33&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700671725134&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=34&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700672066238&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=35&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700672105088&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=36&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700672117538&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=37&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700672130964&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=38&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')
url.append('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1700672136958&loginType=3&uuid=122270672.1700649984143202373630.1700649984.1700668734.1700671455.3&productId=100049336402&score=0&sortType=5&page=39&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=')

#—————————————————————————————————数据请求&处理—————————————————————————————————
#texts用于存储评论
texts = []
num=0

import time
for ui in url:
    #增加延时，不易触发反爬
    time.sleep(3)
    r = requests.get(ui,headers=headers)
    data = r.text
    
    #数据解析：发现规律，"content":"想要的评论内容","creationTime"
    #利用正则
    pat = re.compile('"content":"(.*?)","creationTime"')
    texts.extend(pat.findall(data))#列表拼接
    num=num+1
    print(num,len(texts))

#———————————————————————————————————存储评论————————————————————————————————————
df = pd.DataFrame()
df['comments'] = texts
df.to_excel('Comments of ikan CGM.xlsx')

#———————————————————————————————————词云制作————————————————————————————————————
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import jieba

#合并字符串，方便切割和词云
text_merge = " ".join(texts)
#使用 jieba 进行分词，将中文文本切分为单词
words = jieba.cut(text_merge, cut_all=False)
word_string = " ".join(words)

#删除不需要的词汇
stopwords = STOPWORDS
stopwords.add('的')
stopwords.add('很')
stopwords.add('非常')
stopwords.add('也')
stopwords.add('在')
stopwords.add('还是')
stopwords.add('会')
stopwords.add('我')
stopwords.add('可以')
stopwords.add('看到')
stopwords.add('这个')
stopwords.add('不错')
stopwords.add('给')
stopwords.add('都')
stopwords.add('又')
stopwords.add('了')
stopwords.add('血糖')
stopwords.add('对')
stopwords.add('后')
stopwords.add('是')
stopwords.add('好')
stopwords.add('用')
stopwords.add('买')
stopwords.add('有')
stopwords.add('使用')
stopwords.add('能')
stopwords.add('还')
stopwords.add('就')
stopwords.add('真的')
stopwords.add('动态')
stopwords.add('血糖仪')
stopwords.add('产品')
stopwords.add('没有')
stopwords.add('特别')
stopwords.add('第一次')
stopwords.add('而且')
stopwords.add('自己')
stopwords.add('和')
stopwords.add('感觉')
stopwords.add('一个')
stopwords.add('一直')
stopwords.add('监测')
stopwords.add('检测')

#创建WordCloud对象
wordcloud = WordCloud(font_path="simhei.ttf", width=800, height=400, max_words=200, background_color="white", stopwords = stopwords).generate(word_string)

# 绘制词云
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()



