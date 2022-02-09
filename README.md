# AutoClick
Click, double-click, right-click, type, wait, scroll wheel functions can be repeatedly completed in your thought.

Author: [@不高兴就喝水](https://space.bilibili.com/412704776/?spm_id_from=333.999.0.0)

Source Code: 链接：https://pan.baidu.com/s/1Gu8NbGlysaxMTdDKIHOabg 提取码：gcrr

Environment Requirement:
- python 3.4+ (My environment is 3.8, author's environment is 3.7.6, and 3.9 may have error)

In cmd use pip command to install environment below:
- pip install pyperclip
- pip install xlrd
- pip install pyautogui==0.9.50
- pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
- pip install pillow

**python exe must be root(Administer)**, else click will not be triggered.

Method: 
- run cmd by administer, in cmd is `C:\Windows\system32>` not `C:\Users\UserName>`
- Put whole directory in `C:` or its subdirectory, and use `cd` to the path you put
- Enter `python waterRPA.py` to run as 使用说明书1.docx

# BYRBBS Spider

### 2022-02-10: Add User Name and Comment Time Attributes.

There are four columns in data csv file: title, user, time, comment. And each first comment of new title is the context of the title.

---

In cmd use pip command to install environment below:
- pip install requests
- pip install pyquery

If Warning:
`Could not find a version that satisfies the requirement  XXX (from versions: )`
`No matching distribution found for XXX`

- Method 1: Update npm `python -m pip install --upgrade pip`
- Method 2: Use DouBan Source `pip install XXX -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com`
    - Such as `pip install requests -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com`

Change to your ID and Password in line 84 & line 85

Use Python to login BYRBBS Code Part（Python模拟登录北邮人论坛）
```python
import requests

r_url = 'https://bbs.byr.cn/user/ajax_login.json'
my_header = {'x-requested-with': 'XMLHttpRequest'}
byr_data = {'id': 'userId', 'passwd': 'userPswd'}
session = requests.Session()
req = session.post(r_url, data=byr_data, headers=my_header)
print(req.text)
```
**Please Do Not Use Proxy（不要使用代理！不然会报错！**
If success, there will be no error.

# Download Image
Download images from url that likes http://avatar.csdn.net/1/3/B/1_li1325169021.jpg

Thanks for 小光Y, he/she's code can run correctly. And it reduces the duplicate operations. 
You can use for loop to download database that can read from web like the link above simply.

>[java根据图片路径下载图片并保存到本地目录](https://www.cnblogs.com/xiaoguangy/p/11497700.html)


# Generate Image
Generate images by Strings read data from txt file

CommonUtil.java class is the util to control image's style, such as background's length and height, font style, font color, etc.

Test.java class is to generate images, pathname should be changed accordingly, I have no idea about relative pathname, 
so please change to absolute pathname if you have no idea.

In Test class, it reads one line each. There are two items in one line and seperate by '\t'(i.e tab), you can change them according to your txt file.
