CommunityLink = "http://aminoapps.com/c/zerozero1"
#image_link = "pm1.aminoapps.com/8711/0cd560dddfa82c4544907298d53eedc0f9d79b23r1-1080-1080v2_128.jpg"


password = "moya12"
nickname = "𝐌𝐎𝐘𝐀 𝐒𝐓𝐎𝐑𝐄"

"""
@1secmail.com
@1secmail.org
@1secmail.net
@bheps.com
@dcctb.com
@kzccv.com
@qiott.com
@wuuvo.com
"""

EmailsName = "MOYA"
EmailsDomain = "@1secmail.com"


JsonFileName = "1-Store.json"
EmailsFileName = "1-Store.txt"


import os
import requests
import time


try:
	import colorama, pyfiglet, json, base64, hmac, hashlib, secmail, random, re, threading
except ModuleNotFoundError:
	os.system("pip install colorama pyfiglet json base64 hmac hashlib secmail random re threading")
os.system("clear")


from colorama import *
from pyfiglet import *


from time import sleep
from bs4 import BeautifulSoup
from random import choice


from urllib.request import ProxyHandler,urlopen,build_opener,install_opener
from base64 import b64encode


print(Fore.GREEN)
print("𝔴𝔞𝔡𝔢 𝔟𝔶 𝔪𝔥𝔞𝔱")
print("𝔞 𝔰𝔠𝔯𝔦𝔭𝔱 𝔣𝔬𝔯 𝔠𝔯𝔢𝔞𝔱𝔦𝔫𝔤 𝔞𝔠𝔠𝔬𝔲𝔫𝔱𝔰")
print("")
print(Fore.RED + Style.BRIGHT)
print(pyfiglet.figlet_format("AccGen", font="sblood"))
print(Fore.GREEN + Style.BRIGHT)
print("")
print("𝔧𝔬𝔦𝔫 𝔪𝔶 𝔱𝔢𝔩𝔢𝔤𝔯𝔞𝔪 𝔣𝔬𝔯 𝔪𝔬𝔯𝔢 𝔰𝔠𝔯𝔦𝔭𝔱𝔰")
print("[ https://t.me/mhat0 ]")
print(Fore.RED)


def deviceID():
	identifier = os.urandom(20)
	return ("19" + identifier.hex() + hmac.new(bytes.fromhex("E7309ECC0953C6FA60005B2765F99DBBC965C8E9"), b"\x19" + identifier, hashlib.sha1).hexdigest()).upper()


def NDCMSGSIG(mhat, data):
	return base64.b64encode(bytes.fromhex("19") + hmac.new(bytes.fromhex("DFA5ED192DDA6E88A12FE12130DC6206B1251E44"), data.encode("utf-8"),hashlib.sha1).digest()).decode("utf-8")


sec = secmail.SecMail()
device = deviceID()


headers = {"NDCDEVICEID": deviceID(),"Accept": "*/*","NDCLANG": "ar","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-GB,3n;q=0.9","Content-Type": "application/json","User-Agent":"Apple iPad6,12 iPadOS v15.4.1 Main/3.14.0","Connection":"keep-alive"}


def request_code(mhat ,email: str):
	data=json.dumps({"locale": "en_SE", "clientCallbackURL": "narviiapp://deafult","timestamp": (int(time.time() * 1000)), "retry": 0,"deviceID": deviceID(), "timezone": 60, "clientType": 100, "identity": email, "type": 1, "systemPushEnabled": 0, "bundleID": "com.narvii.master"})
	headers["NDC-MSG-SIG"] = NDCMSGSIG(mhat=NDCMSGSIG,data = data)
	headers["NDCDEVICEID"] = deviceID()
	req = requests.post(f"https://service.aminoapps.com/api/v1/g/s/auth/request-security-validation", data = data, headers = headers)
	if req.status_code!= 200:
		print(Fore.GREEN)
		print("="*63)
		print(Fore.RED)
		input("》")
		sleep(0.1)
		main()


def get_code_link(email):
    print(Fore.GREEN)
    print("="*63)
    print(Fore.RED)
    print(f"𝔰𝔢𝔫𝔡𝔦𝔫𝔤 𝔠𝔬𝔡𝔢 𝔱𝔬 [ {email} ] ...")
    sleep(3.5)
    return BeautifulSoup(sec.read_message(email, sec.get_messages(email).id[-1]).htmlBody, "html.parser").find_all("a")[0]["href"]






class CaptchaSolver:
    def __init__(self, proxy=None):
        self._s = requests.Session()
        if proxy:
            self._s.proxies.update({'http': proxy, 'https': proxy})
        self.__event_validation = None
        self.__view_state = None
        self.__save_data(self._s.get('https://cloudmersive.com/ocr-api').text)

    def __save_data(self, text):
        self.__event_validation = re.findall(r'__EVENTVALIDATION".*value="(.*)"', text)[0]
        self.__view_state = re.findall(r'__VIEWSTATE".*value="(.*)"', text)[0]

    @staticmethod
    def __get_captcha_result(text):
        result = re.findall(f'TextResult":.*"(.*)"', text)
        if result:
            return result[0].replace('\\n', '')
        return ''

    def solve(self, image: open) -> str:
        """
        Method for solving regular text captcha.
        :param image: open(file, 'rb')
        """
        data = {
            '__EVENTVALIDATION': self.__event_validation,
            '__VIEWSTATE': self.__view_state,
            'ctl00$MainContent$LanguageSelector': 'eng',
            'ctl00$MainContent$btnUpload2': 'Photos of Docs to Text'
        }

        r = self._s.post('https://cloudmersive.com/ocr-api', data=data, files={'ctl00$MainContent$FileUploadBox': image})
        if not r.ok:
            return ''
        self.__save_data(r.text)
        return self.__get_captcha_result(r.text)






def check_code(mhat, code:str,email: str):
    data = json.dumps({'locale': 'en_SE','clientCallbackURL': 'narviiapp://default','deviceID': deviceID(),'timezone': 60,'validationContext': {'level': 1,'type': 1,'identity': email,'data': {'code': code,},},'clientType': 100,'systemPushEnabled': 0,'timestamp':(int(time.time() * 1000)),
    'bundleID': 'com.narvii.master'})
    headers["NDC-MSG-SIG"] = NDCMSGSIG(mhat=NDCMSGSIG,data = data)
    headers["NDCDEVICEID"] = deviceID()
    req = requests.post('https://service.aminoapps.com/api/v1/g/s/auth/check-security-validation', headers=headers, data=data)


def register(mhat, password: str, email: str, code: str, nickname: str):
    data = json.dumps({'secret': '0 '+password,'timezone': 60,'clientType': 100,'systemPushEnabled': 0,'timestamp': (int(time.time() * 1000)),'locale': 'en_SE','bundleID': 'com.narvii.master','validationContext': {'identity': email,'data': {'code': code,},'level': 1,'type': 1,},'nickname': nickname,'deviceID': deviceID(),'email': email,'clientCallbackURL': 'narviiapp://default'})
    headers["NDC-MSG-SIG"] = NDCMSGSIG(mhat=NDCMSGSIG,data = data)
    headers["NDCDEVICEID"] = deviceID()
    req = requests.post('https://service.aminoapps.com/api/v1/g/s/auth/register', headers=headers, data=data)
    if req.status_code!=200:
    	print("𝔦𝔫𝔠𝔬𝔯𝔯𝔢𝔠𝔱 𝔳𝔢𝔯𝔦𝔣𝔦𝔠𝔞𝔱𝔦𝔬𝔫 𝔠𝔬𝔡𝔢 !")


def login(mhat ,email: str, password: str):
	data=json.dumps({"secret": f"0 {password}","clientType": 100,"systemPushEnabled": 0,"timestamp": (int(time.time() * 1000)),"locale": "en_SE","action": "normal","bundleID": "com.narvii.master","timezone": 60,"deviceID":deviceID(),"email": email,"v": 2,"clientCallbackURL": "narviiapp://deafult"})
	headers["NDC-MSG-SIG"] = NDCMSGSIG(mhat=NDCMSGSIG,data = data)
	req = requests.post(f"https://service.aminoapps.com/api/v1/g/s/auth/login", data = data, headers = headers)
	if req.status_code!= 200:
		sleep(0.1)
		main()
		print(req.json()["api:message"])
	try:mhat.sid, mhat.userId = req.json()["sid"], req.json()["account"]["uid"]
	except:pass

"""
def change_global_picture():
	global image_link
	data = json.dumps({"icon":f"{image_link}","timestamp":int(time.time()*1000)})
	headers["NDC-MSG-SIG"] = NDCMSGSIG(mhat=NDCMSGSIG,data=data)
	headers["NDCAUTH"] = f"sid={login.sid}"
	req = requests.post(f"https://service.aminoapps.com/api/v1/g/s/user-profile/{login.userId}", data=data,headers = headers)
	if req.status_code!= 200:
		print(req.json()["api:message"])
"""

def get_cid(mhat):
	global CommunityLink
	return requests.get(f"https://service.aminoapps.com/api/v1/g/s/link-resolution?q={CommunityLink}",headers = headers).json()


Community=get_cid(mhat=get_cid)
LinkInfo = Community['linkInfoV2']['extensions']
ComId = int(LinkInfo["community"]['ndcId'])


def join_community(mhat):
	global ComId
	data = json.dumps({"timestamp" : int(time.time()*1000)})
	headers["NDC-MSG-SIG"] = NDCMSGSIG(mhat=NDCMSGSIG,data = data)
	headers["NDCAUTH"] = f"sid={login.sid}"
	req = requests.post(f"https://service.aminoapps.com/api/v1/x{ComId}/s/community/join", data = data, headers = headers)
	if req.status_code!=200:
		print(req.json()["api:message"])


def save(email, password, device):
    global JsonFileName
    global EmailsFileName
    try:
        with open(JsonFileName, 'a') as x:
            acc = f'{{"email": "{email}","password": "{password}","device": "{device}"}},\n'
            x.write(acc)
            xr=open(EmailsFileName,"a")
            xr.write(f"{email}\n")
            print(f"𝔰𝔞𝔳𝔢𝔡 𝔰𝔲𝔠𝔠𝔢𝔰𝔰𝔣𝔲𝔩𝔩𝔶 !")
    except Exception as m:
        print(m)


def ms(email):
	request_code(mhat=request_code,email=email)
	link = get_code_link(email)
	print(f"𝔩𝔦𝔫𝔨 : [ {link} ]")
	image = urlopen(link).read()
	try:
		remove('captcha.png')
	except:
		pass
	file = open('captcha.png','wb')
	file.write(image)
	captcha_solver = CaptchaSolver()
	predictCode = captcha_solver.solve(open('captcha.png', 'rb'))
	predictCode = ''.join(predictCode.split())
	print(f"𝔠𝔬𝔡𝔢 : [ {predictCode} ]")
	check_code(mhat=check_code,code=predictCode,email=email)
	register(mhat=register,password=password,email=email,nickname=nickname,code=predictCode)
	login(mhat=login,email=email,password=password)
	print(f"𝔩𝔬𝔤𝔤𝔢𝔡 𝔦𝔫 𝔰𝔲𝔠𝔠𝔢𝔰𝔰𝔣𝔲𝔩𝔩𝔶 𝔴𝔦𝔱𝔥 [ {email} ]")
	save(email, password, device)
	#change_global_picture()
	join_community(mhat=join_community)
	print(f"𝔧𝔬𝔦𝔫𝔢𝔡 𝔰𝔲𝔠𝔠𝔢𝔰𝔰𝔣𝔲𝔩𝔩𝔶 𝔴𝔦𝔱𝔥 [ {email} ]")
	print(f"𝔡𝔬𝔫𝔢 𝔴𝔦𝔱𝔥 [ {email} ] !")


def main():
	while True:
		times=int("5")
		for mhat in range(int(times)):
			characters = 12
			chose = "".join(choice("abcdefghijklmnopqrstuvwxyz1234567890")for i in range(characters))
			email_generation = f"{EmailsName}-{chose}"
			ms(f"{email_generation}{EmailsDomain}")


main()