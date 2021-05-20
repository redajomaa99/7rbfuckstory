import requests
import uuid
uid = str(uuid.uuid4())
r1 = requests.session()
import time
mid = None
coo = None
ds_user_id = None
see = None
Status_login = False
users = []
print('''
 _______                     _____ _______ 
|__   __|                   |  __ \__   __|
   | | ___  __ _ _ __ ___   | |__) | | |   
   | |/ _ \/ _` | '_ ` _ \  |  ___/  | |   
   | |  __/ (_| | | | | | | | |      | |   
   |_|\___|\__,_|_| |_| |_| |_|      |_|   
       Instagram : @givt_ops 
       telegtam  : t.me/Team_PT                                   
''')
class daddy_givt():
    def __init__(self):
        global Status_login
        self.username = input("[-] Username:")
        self.password = input("[-] Password:")
        if Status_login == False:
            self.login()
        else:
            self.get_user()
    def check(self):
        global users
        for username in users:
            time.sleep(4)
            url = f"https://instagram.com/{username}/?__a=1"
            headers = {
                "Host": "www.instagram.com",
                "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "DNT": "1",
                "Connection": "keep-alive",
                "Cookie": f"ig_cb=2; ig_did=4CA12CAF-9430-4ACF-80DA-7D64D33399D9; mid={mid}; shbid=482; shbts=1617918732.4239228; datr=azslYEfwg6RU7z0vwH_Rka-T; ig_nrcb=1; csrftoken=zPnq799h349OuQc1Ahuw4BH98BDPujEC; ds_user_id={ds_user_id}; sessionid={ds_user_id}; rur=RVA",
                "Upgrade-Insecure-Requests": "1",}
            r = r1.get(url,headers=headers)
            try:
                s = int(r.json()['graphql']['user']['edge_followed_by']['count'])
                s2 = int(r.json()['graphql']['user']['id'])
                if s<10:
                    url_block = f"https://www.instagram.com/web/friendships/{s2}/block/"
                    headers_block = {
                        "Host": "www.instagram.com",
                        "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
                        "Accept": "*/*",
                        "Accept-Language": "en-US,en;q=0.5",
                        "Referer": F"https://www.instagram.com/{username}/",
                        "X-CSRFToken": "zPnq799h349OuQc1Ahuw4BH98BDPujEC",
                        "X-Instagram-AJAX": "1e298a12d662",
                        "X-IG-App-ID": "936619743392459",
                        "X-IG-WWW-Claim": "hmac.AR12Fs18fzvYP9jCne1dhLjB5a8pdPtPh17yqrMQzdvWj1AN",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-Requested-With": "XMLHttpRequest",
                        "Origin": "https://www.instagram.com",
                        "DNT": "1",
                        "Connection": "keep-alive",
                        "Cookie": f"ig_cb=2; ig_did=4CA12CAF-9430-4ACF-80DA-7D64D33399D9; mid={mid}; shbid=482; shbts=1617918732.4239228; datr=azslYEfwg6RU7z0vwH_Rka-T; ig_nrcb=1; csrftoken=zPnq799h349OuQc1Ahuw4BH98BDPujEC; ds_user_id={ds_user_id}; sessionid={see}; rur=RVA",
                        "Content-Length": "0",
                        "TE": "Trailers"}
                    r2 = r1.post(url_block,headers=headers_block)
                    if r2.text.find('status	"ok"')>=0:
                        print(f"[+] Done Block:{username}")
                    else:
                        print(f"[-] Error block username:{username}")
                else:
                    print(f"[+] Its Good account:{username}")
            except:
                time.sleep(10)
        self.get_user()
    def get_user(self):
        global users
        users.clear()
        api = input("[?] Enter Story ID:")
        url = f"https://i.instagram.com/api/v1/media/{api}/list_reel_media_viewer/?include_blacklist_sample=true"
        headers = {
            "Host": "i.instagram.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": f"https://www.instagram.com/stories/{self.username}/{api}/",
            "X-IG-App-ID": "936619743392459",
            "X-IG-WWW-Claim": "hmac.AR12Fs18fzvYP9jCne1dhLjB5a8pdPtPh17yqrMQzdvWj7gE",
            "Origin": "https://www.instagram.com",
            "DNT": "1",
            "Connection": "keep-alive",
            "Cookie": f"ig_did=4CA12CAF-9430-4ACF-80DA-7D64D33399D9; mid={mid}; shbid=482; shbts=1617918732.4239228; datr=azslYEfwg6RU7z0vwH_Rka-T; ig_nrcb=1; csrftoken=zPnq799h349OuQc1Ahuw4BH98BDPujEC; ds_user_id={ds_user_id}; sessionid={see}; rur=RVA",
            "TE": "Trailers"}
        a = 0
        while True:
            r = r1.get(url,headers=headers)
            try:
                s1 = str(r.json()['users'][a]['username'])
                users.append(s1)
            except:
                if a == 0:
                    print('[-] No Found Any One .. We well Try After 100s')
                    time.sleep(120)
                    self.get_user()
                else:
                    break
        self.check()
    def login(self):
        global Status_login
        global coo, ds_user_id, see,mid
        url = "https://i.instagram.com/api/v1/accounts/login/"
        headers = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US",
            "X-IG-Capabilities": "3brTvw==",
            "X-IG-Connection-Type": "WIFI",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Host': 'i.instagram.com'}
        data = {
            '_uuid': uid,
            'password': self.password,
            'username': self.username,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_count': '0'}
        givt = r1.post(url, data=data, headers=headers, allow_redirects=True)
        if givt.text.find("is_private") >= 0:
            coo = givt.cookies
            ds_user_id = givt.cookies['ds_user_id']
            see = givt.cookies['sessionid']
            mid = givt.cookies['mid']
            Status_login = True
            self.__init__()
        else:
            print(f"[!] Error Login :{self.username}")
            Status_login = False
            self.__init__()




daddy_givt()


