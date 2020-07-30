import threading, cloudscraper, time, re, string, os, random, sys
from sty import fg, bg, ef, rs
from bs4 import BeautifulSoup

class Autoclaim(threading.Thread):
    def __init__(self, site, token, phpsessid, delay):
        threading.Thread.__init__(self)
        self.site = site
        self.PHPSESSID = phpsessid
        self.Token = token
        self.delay = delay
        
    def run(self):
        if str(self.site).find("?coin=BCH") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, BCHToken=self.Token, Ref='EC-UserId-26314',)
        elif str(self.site).find("?coin=BCN") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, BCNToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=BTC") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, BTCToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=ADA") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, ADAToken=self.Token, Ref='EC-UserId-26314')      
        elif str(self.site).find("?coin=DASH") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, DASHToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=DGB") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, DGBToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=DOGE") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, DOGEToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=ETC") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, ETCToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=ETH") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, ETHToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=EXG") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, EXGToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=EXS") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, EXSToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=LSK") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, LSKToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=LTC") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, LTCToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=NEO") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, NEOToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=POT") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, POTToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=RDD") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, RDDToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=PPC") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, PPCToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=STRAT") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, STRATToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=XTZ") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, XTZToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=TRX")   > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, TRXToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=WAVES") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, WAVESToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=XMR") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, XMRToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=XRP") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, XRPToken=self.Token, Ref='EC-UserId-26314')
        elif str(self.site).find("?coin=ZEC") > 0:
            cookies = dict(PHPSESSID=self.PHPSESSID, ZECToken=self.Token, Ref='EC-UserId-26314')
        else:
            pass
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        scraper = cloudscraper.create_scraper()
        while True:
            try:
                r = scraper.post(self.site, headers=headers, cookies=cookies)
            except Exception as e:
                print("Connection Error ")
            soup = BeautifulSoup(r.text, "html.parser")
            succ = soup.find("div", {"class": "alert alert-success"})
            a = random.randint(77, 87)
            if soup.find("div", {"class": "alert alert-danger"}) is not None:
                print(fg(160) + soup.find("div", {
                    "class": "alert alert-danger"}).text + fg.rs)
            elif soup.find("div", {"class": "alert alert-success"}) is not None:
                if succ.text.find('EC-UserId') > 0:
                    try:
                        print(fg(a) + soup.find("div", {
                            "class": "alert alert-success"}).text + fg.rs)
                    except Exception as e:
                        print(fg(160) + soup.title.text + "  " + str(e))
                else:
                    print(fg(a) + soup.title.string + "  Success Claim                              " + fg.rs)
            elif soup.find("div", {"class": "card center-align green darken-4 white-text z-depth-5 faa-horizontal animated"}) is not None:
                print(fg(a) + soup.find("div", {"class": "card center-align green darken-4 white-text z-depth-5 faa-horizontal animated"}.text+ fg.rs))
            else:
                print(fg(a) + soup.title.string + "  Success Claim                              " + fg.rs)
            time.sleep(self.delay)

if __name__ == '__main__':

    def logo():
        os.system("cls||clear")
        x = random.randint(16, 224)
        print("\033[1;0H")
        print(fg(x) +  "███▄▄▄▄      ▄████████    ▄█   ▄█▄  ▄██████▄  ████████▄   ▄██████▄   ▄█        ▄█      "+ fg.rs)
        print(fg(x+1) +"███▀▀▀██▄   ███    ███   ███ ▄███▀ ███    ███ ███   ▀███ ███    ███ ███       ███       "+ fg.rs)
        print(fg(x+1) +"███   ███   ███    █▀    ███▐██▀   ███    ███ ███    ███ ███    ███ ███       ███       "+ fg.rs)
        print(fg(x+2) +"███   ███  ▄███▄▄▄      ▄█████▀    ███    ███ ███    ███ ███    ███ ███       ███       "+ fg.rs)
        print(fg(x+3) +"███   ███ ▀▀███▀▀▀     ▀▀█████▄    ███    ███ ███    ███ ███    ███ ███       ███       "+ fg.rs)
        print(fg(x+4) +"███   ███   ███    █▄    ███▐██▄   ███    ███ ███    ███ ███    ███ ███       ███       "+ fg.rs)
        print(fg(x+5) +"███   ███   ███    ███   ███ ▀███▄ ███    ███ ███   ▄███ ███    ███ ███▌    ▄ ███▌    ▄ "+ fg.rs)
        print(fg(x+4) +" ▀█   █▀    ██████████   ███   ▀█▀  ▀██████▀  ████████▀   ▀██████▀  █████▄▄██ █████▄▄██ "+ fg.rs)
        print("")
        print(fg(x + 2) + 'Express Crypto autoclaim create by Nekodoll ' + fg.rs)
        print(fg(x + 1) + '-' * 90 + fg.rs)

    def rest_time():
        for i in range(50, 0, -1):
            x = random.randint(16, 224)
            sys.stdout.write(fg(x) + "\rrest for {} seconds ".format(i))
            time.sleep(1)
            sys.stdout.flush()
            
    f = open('Data.txt','r').readlines()
    for x in range(len(f)):
        data = f[x].split(",")
        Autoclaim(data[0],data[1],data[2],int(data[3])).start()      
    while True:
        logo()
        time.sleep(10)
        rest_time() 