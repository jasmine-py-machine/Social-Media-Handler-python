import re,os
from meta import META,driver
from selenium.webdriver.common.by import By
regex= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
class instagram:
    def __init__(self,url,username,password):
        self.url=url
        self.username=username
        self.password=password
    def login(self):
        driver.get(self.url)
        META.wait(By.XPATH,"//input[@name='username']").send_keys(self.username)
        META.wait(By.XPATH,"//input[@name='password']").send_keys(self.password)
        META.wait(By.XPATH,"//button[@type='submit']").click()
        try:
            error=META.wait(By.XPATH,'//*[@id="loginForm"]/span/div').text
            if "password was incorrect" in error:
                print("your password is incorrect..")
                error_code=403
                return error_code
            else:
                print("successfully login")
                try:
                    META.wait(By.XPATH,"//button[text()='Not Now']").click()
                    print("your login info does not save on this broswer")
                    META.wait(By.XPATH,"//button[text()='Not Now']").click()
                    print("notification turn off")
                    error_code =200
                    META.log("error_code=200 successfully login")
                    return error_code
                except Exception as e:
                    META.log(e)
                    pass
                
        except:
            pass
    
    def profile(self):
        #click profile
        #find username
        global user
        if re.match(regex,self.username):
            f=str(driver.find_element_by_xpath('//*[@id="mount_0_0_8L"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a').get_attribute("href"))
            f=f.strip(self.url)
            user=f.strip(r"/")
        else:
            user=self.username
        try:
            META.wait(By.XPATH,f"//a[contains(@href,'/{user}')]").click()
            print("successfully in  profile now ")
            META.log(f"error_code=200 successfully in  profile now ")
        except Exception as e:
            META.log(e)
            pass
    
    
    
    def unfollow(self,action:str):
        retry=0
        if action=="following":
            doer=r"following"
        else:
            doer=r"followers"
        f_number=META.wait(By.XPATH,f"//a[contains(@href, '/{doer}')]").text.strip(f"{doer}")
        f_number=int("".join( i for i in f_number if i!=','))
        try:
            META.wait(By.XPATH,f"//a[contains(@href, '/{doer}')]").click()
            META.log(f"clicking on {doer}")
            print(f"clicking on {doer} now")
        except Exception as e:
            META.log(f"{e},no 87")
            pass
        c=0
        os.system("cls")
        for i in range(f_number):
            try:
                if action=="following":
                    META.wait(By.XPATH,"//button[@class='_acan _acap _acat _aj1-']").click()
                else:
                    META.wait(By.XPATH,"//div[text()='Remove']").click()
                buttn=META.wait(By.XPATH,"//button[@class='_a9-- _a9-_']")
                if "Report a problem" in buttn.text:
                    print("""Try Again Later
We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake""")
                    
                else:
                    buttn.click()
                    c+=1
                    print("you have unfollow {} out of {} {}".format(c,f_number,doer),end="\r")
                    
                    driver.execute_script("window.scrollBy(0,100)")
            except Exception as e:
                
                META.log(META.error())
                if retry==1:
                    print(f"hey {user} you don't want to get your account banned try again in 1 hour or 24 hour pls..".upper())
                    driver.quit()
                    quit(0)
                os.system("cls")
                print("your account it's on limit \nyou have unfollow {} out  of {} {}\n pls. wait for 10 minutes".format(c,f_number,doer,int(f_number)-int(c)))
                META.countdown(600)
                print("count down finish work begin.............")
                retry+=1
                

                os.system("cls")
    def profile_info(self):
        try:
            name=META.wait(By.XPATH,'//*[@id="mount_0_0_T/"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div[1]')
            bio=META.wait(By.XPATH,'//*[@id="mount_0_0_8L"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/h1')
            followers=META.wait(By.XPATH,f"//a[contains(@href, '/followers')]")
            following=META.wait(By.XPATH,f"//a[contains(@href, '/following')]")
            post=META.wait(By.XPATH,'//*[@id="mount_0_0_8L"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]')
            print(f"""
            YOUR PROFILE INFO
                NAME: {name}
                FOLLOWERS: {followers}
                FOLLOWING: {following}
                POST: {post}
                BIO: {bio}
                                    """)
        except:
            META.log(META.error())
            return 300
