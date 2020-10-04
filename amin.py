import requests

import json

import time
def spam():

    a = 0

    username = input("[+] Enter username:")

    pasword = input("[+] Enter Pasword:")

    Target = input("[+] Enter Target:")

    r = requests.session()

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "accept": "*/*",

        "accept-encoding": "gzip, deflate,br",

        "accept-language": "ar,en-US;q=0.9,en;q=0.8",

        "content-length": "279",

        "content-type": "application/x-www-form-urlencoded",

        "origin": "https://www.instagram.com",

        "referer": "https://www.instagram.com/",

        "sec-fetch-dest": "empty",

        "sec-fetch-site": "same-origin",

        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",

        "x-csrftoken": "lih2ypMfhzdqwMbm5jIILqxZDj4zLeCW",

        "x-ig-app-id": "936619743392459",

        "x-ig-www-claim": "hmac.AR1_p9SjMFQF73bcZgzygDgxb9yBZUn83e69xoDD2qpSdmtW",

        "x-instagram-ajax": "901e37113a69",

        "x-requested-with": "XMLHttpRequest"

    }

    data = {"username": username, "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:" + pasword, "queryParams": "{}",

            "optIntoOneTap": "false"}

    login = r.post(url, headers=headers, data=data, allow_redirects=True)

    if login.text.find("userId") >= 0:

        print('[√] Done Login:', username)

        s = requests.get("https://instagram.com/" + Target + "/?__a=1")

        idinsta = str(s.json()["graphql"]["user"]["id"])

        print("[√] id Target:", idinsta)

        data1 = {

            "source_name": "", "reason_id": 2, "frx_context": ""

        }

        r.headers.update({'X-CSRFToken': login.cookies['csrftoken']})

        for cdref in range(1000000000000000000000000000000):

            reporturl = "https://www.instagram.com/users/" + idinsta + "/report/inappropriate"

            report = r.post(reporturl, data=data1)

            a +=1

            if report.text.find("We take your reports seriously. We look into every issue, and take action when people violate our                    >

                print("[√] Done Self:",a)

                time.sleep(10)

            else:

                print("[-] Error Self:")

                time.sleep(15)

    else:

        print('[-] Error Login')

        out3()
