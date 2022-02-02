# BYRBBS Spider
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
