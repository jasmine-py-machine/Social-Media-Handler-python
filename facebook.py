
import re,os
from meta import META,driver
from selenium.webdriver.common.by import By
from colorama import Fore,Back,Style,reinit
regex= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
class Facebook:
        def __init__(self,username,password,url) -> None:
            self.url=url
            self.username=username
            self.password=password

        def login(self):
            META.log(f"opening url====> {self.url}")
            driver.get(self.url)
            META.log("done")
            META.wait(By.XPATH,'//*[@name="email"]').send_keys(self.username)
            META.wait(By.XPATH,'//*[@name="pass"]').send_keys(self.password)
            META.wait(By.XPATH,'//*[@name="login"]').click()
            try:
                try:

                    ck=META.wait(By.XPATH,'//*[@id="page"]/div[7]/div[1]/div/div[2]/div')
                except:
                    ck=META.wait(By.XPATH,'//*[@id="login_error"]')
                #META.log(f"{Style.DIM}{Back.RED}{Style.RESET_ALL}{Back.RESET}{Fore.RED}{ck.text}{Fore.RESET}")
                META.log(f"{Style.DIM}{Back.RED}{Style.RESET_ALL}{Back.RESET}{Fore.RED}{ck.text}{Fore.RESET}")
                driver.quit()
                exit()
            except:
                pass
            try:
                d=META.wait(By.XPATH,'//*[@id="approvals_code"]')
                d.send_keys(str(input("auth code: ")))
                META.wait(By.XPATH,'//*[@id="checkpointSubmitButton"]').click()
                META.wait(By.XPATH,'//*[@id="checkpointSubmitButton"]').click()
                META.wait(By.XPATH,'//*[@id="checkpointSubmitButton"]').click()
                META.wait(By.XPATH,'//button[@value="This was me"]').click()
                META.wait(By.XPATH,'//*[@id="checkpointSubmitButton"]').click()
            except:
                pass
            try:
                META.wait(By.XPATH,'//*[@id="root"]/div[1]/div/div/div[3]/div[2]/form/div/button').click()
            except:
                pass
            META.log(f"{Style.DIM}{Back.GREEN}{Style.RESET_ALL}{Back.RESET}{Fore.GREEN}LOGIN SUCCESS{Fore.RESET}")
        
        def gotofriendlist(self,unfriend:bool):
           
            META.wait(By.XPATH,'//*[@id="mJewelNav"]/div[2]').click()
            META.waits(By.XPATH,'//a[@role="tab"]')[1].click()
            find=META.wait(By.XPATH,'//header[@class="_5lm6 _8xxc"]')
            META.log(f"{Fore.MAGENTA}You have {Fore.WHITE}{Style.BRIGHT}{find.text}{Style.RESET_ALL}")
            no=[i for i in find.text if i.isdigit()]
            f_no=int("".join(no))
            if unfriend:
                track=0
                #action=ActionChains(driver)
                total=0
                while f_no!=0:
                    threedot=META.waits(By.XPATH,'//i[@class="img _71t _8yzt img _2sxw"]')
                    for i in threedot:
                        i.click()
                        #action.click(i).perform()
                        try:
                            META.waits(By.XPATH,'//a[@class="_54k8 _55i1 _58a0 touchable"][2]',4)[0].click()
                        except:
                            META.waits(By.XPATH,'//a[@class="_54k8 _55i1 _58a0 touchable"][2]',4)[1].click()
                            pass
                        track+=1
                    total+=len(threedot)
                       
                    f_no=f_no-track
                    track=0
                    META.log(total)
                    driver.refresh()
                    


           
                META.log("done")