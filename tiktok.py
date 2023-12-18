import time
from meta import META,driver
import requests
from selenium.webdriver.common.by import By
from emoji import is_emoji
regex= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

import random
USERFILE="username.txt"
class TIKTOK:
    def __init__(self,username,password,url):
        self.useranme=username
        self.password=password
        self.url=url
        self.randomuser=random.choice(open(USERFILE,'r').readlines()).strip("\n")
       
    

    def login(self):
        driver.get(self.url)
        META.wait(By.XPATH,'//input[@name="username"]').send_keys(self.useranme)
        META.wait(By.XPATH,'//input[@type="password"]').send_keys(self.password)
        META.wait(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/button').click()
        try:
            d=META.wait(By.XPATH,'//*[@id="captcha_container"]/div/div[1]/div[2]/div')
            if d==None:
                d=""
                pass
            else:
                d=d.text
            META.log(d)
            if "puzzle" in d.lower():
                input("Press enter to continue if the recapture is done  ")
            pass
        except:
            status=META.wait(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[3]/span').text
            if "Username or password doesn't match our records. Try again.".lower()==status.lower():
                META.log(status)
                return False
            pass
        return True
    def genderize(self,name:str):
        f="".join([i for i in name.split(" ")[0] if not is_emoji(i) and not i.isdigit()])
        clasified=requests.get(f'https://api.genderize.io?name={f}').json()
        if clasified['gender']=='male':
            return True
        else:
            return False
    def gotouserfollower(self):
        i=META.wait(By.XPATH,'//*[@id="main-content-others_homepage"]/div/div[1]/h3/div[2]',50)
        if i==None:
            driver.back()
            time.sleep(3)
            driver.forward
        i.click()
        return True
    
    
    def autobomb(self):
        META.wait(By.XPATH,'//*[@id="app-header"]/div/div[2]/div/form/input').send_keys(self.randomuser)
        META.wait(By.XPATH,'//*[@id="app-header"]/div/div[2]/div/form/button').click()
        META.wait(By.XPATH,'//*[@id="tabs-0-panel-search_top"]/div/div/div[1]/div[2]/a[2]',50).click()
        
        con=True
        i=1
        self.gotouserfollower()
        doer=0
        while con:
            user=META.wait(By.XPATH,f'//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[{i}]')
            name=META.wait(By.XPATH,f'//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[{i}]/div/div/a/div/div/span').text
           
            if self.genderize(name=name):
                META.wait(By.XPATH,f'//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[{i}]/div/div/div/div/button').click()
                print(f"FOLLOW USER: {name.upper()}  SUCCESS")
                driver.execute_script("window.scrollBy(0,50)")
         
            else:
                doer+=1
            
            if  doer>=40:
                META.wait(By.XPATH,f'//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[{i}]/div/div/a').click()
                try:
                    d=META.wait(By.XPATH,'//*[@id="captcha_container"]/div/div[1]/div[2]/div')
                    if d==None:
                        d=""
                        pass
                    else:
                        d=d.text
                    META.log(d)
                    if "puzzle" in d.lower():
                        input("Press enter to continue if the recapture is done  ")
                    pass
                except:
                    pass
                try:
                    private=META.wait(By.XPATH,'//*[@id="main-content-others_homepage"]/div/div[2]/div[2]/p[1]')
                    if private !=None:
                        if "private"  in private.text.lower():
                            driver.back()
                            pass
                except:
                    pass
                doer=0
                i=0
                self.gotouserfollower()
                
                time.sleep(5)
            i+=1
          
            continue
