pw}

response = requests.post(url=login_url, data=data)

visit_url}

response = requests.post(url=login_url, data=data)

login_res = requests.post(url=login_url, data=data)

cookies = requests.utils.dict_from_cookiejar(login_res.cookies)

visit_res = requests.get(url=visit_url, cookies=cookies)

