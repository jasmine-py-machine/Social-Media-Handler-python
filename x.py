
import time
from meta import META,driver
from selenium.webdriver.common.by import By
import random,requests
from emoji import is_emoji
USERLIST=random.choice(["AlesaRusel"])
URL=r"https://twitter.com/"
regex= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
class Twitter():

    def __init__(self,url,usernam,password):
        self.username=usernam
        self.password=password
        self.url=url
    def login(self):
        driver.get(self.url)
        META.wait(By.XPATH,"//input[@name='text']").send_keys(self.username)
        META.wait(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        META.wait(By.XPATH,'//input[@name="password"]').send_keys(self.password)
        META.wait(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]').click()
        time.sleep(1)
        try:
            check=driver.find_element(By.XPATH, "/html/body").text
            if "Wrong password" in check:
                META.log(f"your username: {self.username} and password: {self.password} isn't correct ")
                driver.quit()
            else:
                pass
        except:
            META.log("no error")
            pass
    def goto_profile(self):
        #click profile
        META.wait(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[9]').click()
        META.log("successfully in profile now ")
    def find_following(self,unfollow=False):
        find=META.wait(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span')
        
        META.log(f"You have {find.text} following")
    
        if unfollow:
            no=[i for i in find.text if i.isdigit()]
            f_no=int("".join(no))+1
            
            META.wait(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[1]/a').click()
            META.log("in following session")
            con=True
            c=1
            while con:
                for i in range(1,36):
                    name=META.wait(By.XPATH,f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/a/div/div/span')
                    o=META.wait(By.XPATH,f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div[1]/div[2]')
                    f_no-=1
                    print(f_no)
                    if f_no<=1 or f_no==0 :
                        META.log("Done")

                        driver.quit()
                        break
                    o.click()
                    META.wait(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]').click()
                    doer="[{}]  Unfollow user: {} successfully".format(c,name.text)
                    if i>10:
                        driver.execute_script("window.scrollBy(0,100)")
                    META.log(doer)
                    c+=1
                f_no=f_no-i
                driver.refresh()

                
                continue
        print(i,f_no)          
        driver.quit()
    def verified_followers(self):
        k,m,b=1000,1000000,1000000000
        try:
            vfollowers=META.wait(By.XPATH,'//a[contains(@href,"/verified_followers")]').text
        except:
            vfollowers="27followers"
            pass
        #print(vfollowers)
        strob=vfollowers.lower()
        f_no=int("".join([i for i in strob if i.isdigit()]))
        if "k" in strob:
            f_no=f_no*k
        elif "m" in strob:
            f_no=f_no*m
        elif "b" in strob:
            f_no=f_no*b
        else:
            f_no=f_no*1
        
        if f_no>=2000:
            META.log("more than 1k followers")
            driver.back()
            return False
        else:
            return True
    def genderize(self,name:str):
        f="".join([i for i in name.split(" ")[0] if not is_emoji(i) and not i.isdigit()])
        clasified=requests.get(f'https://api.genderize.io?name={f}').json()
        if clasified['gender']=='male' or clasified['gender']=="null":
            return True
        else:
            return False
    def autobomb(self):
        META.wait(By.XPATH,'//a[@href="/explore"]').click()
        META.wait(By.XPATH,'//input[@placeholder="Search"]').send_keys(USERLIST)
        driver.get(f'{URL}{USERLIST}/followers')
        META.log("in user profile")
        
        i=1
        while True:
            button=META.wait(By.XPATH,f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div/div[2]')
            if button.text.lower()!="following" or button.text.lower()!="pending":
                profile=META.wait(By.XPATH,f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/a').click()
                #button=META.wait(By.XPATH,f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div/div[2]')
                confirm=self.verified_followers()
               
                if confirm:
                    driver.back()
                    name=META.wait(By.XPATH,f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]').text
                    #print(name)
                    #print(i)
                    #time.sleep(600)
                    if self.genderize(name=name):
                        button=META.wait(By.XPATH,f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div/div[2]')
                        button.click()
                        print(f"follow user {name}")
                        
                    #driver.back()
                        
            i+=1
            driver.execute_script("window.scrollBy(0,30)")
                

       # time.sleep(30)
            
        