from banner import banner
from colorama import Fore,Back,Style
import os
from time import sleep
import json
FILENAME='data.json'

info=f"{Fore.GREEN}Email:{Fore.RESET}{Style.BRIGHT}adeyemidiamond5@gmail.com{Fore.RESET}"
s=["Facebook unfriend all friend","Instagram unfollow all Following","Twitter unfollow all Following","for tiktok Service [AUTO BOMB]","Twitter Auto Bomb","Use last  Data"]
urls=[r"https://m.facebook.com/login.php",r"https://www.instagram.com/",r"https://twitter.com/i/flow/login",r"https://www.tiktok.com/login/phone-or-email/email",r"https://twitter.com/i/flow/login",r"https://www.tiktok.com/login/phone-or-email/email"]

def service_info(s:list[str])->str:
    for i,d in enumerate(s):
        print(f"{Style.BRIGHT}{Fore.YELLOW}[{Fore.WHITE}{i+1}{Fore.YELLOW}]  {Fore.CYAN}{d}{Fore.RESET}{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.YELLOW}[{Fore.WHITE}0{Fore.YELLOW}]  {Fore.CYAN}Exit{Fore.RESET}{Style.RESET_ALL}")
def  converttojson(lst):
    with open(FILENAME, 'w') as json_file:
        json.dump(lst, json_file,indent=4,separators=(',',':'))
                                
def main()->str:
    while True:
        try: 
            ans=int(input("Choose the option you want: "))
        except Exception as e:
            print(e)
            continue
        if ans==0:
            break
        if ans>len(s) or ans<0:
            print(f"it out of range")
            continue
        if ans==len(s):            
            ck=json.load(open(FILENAME))
            url=ck["url"]
            useraname=ck["username"]
            password=ck["password"]
            ans=ck["ans"]
        else:
            url=urls[ans-1]
            print(f"{Style.BRIGHT}You are to enter useranme/email for {url}") 
            useraname=str(input(f"{Fore.LIGHTBLUE_EX}Username/Email: {Fore.RESET}"))
            password=str(input(f"{Fore.LIGHTBLACK_EX}Password: {Fore.RESET}"))
            if useraname=="" or password=="":
                print("can;t be empty") 
                continue
            lst={
                "url":url,
                "username":useraname,
                "password":password,
                "ans":ans

            }
            converttojson(lst=lst)
            
        if ans==1:
            from facebook import Facebook
            fb=Facebook(url=url,username=useraname,password=password)
            fb.login()
            fb.gotofriendlist(True)
            break
        if ans==2:
            from instagram import instagram
            ig=instagram(url=url,username=useraname,password=password)
            ig.login()
            ig.profile()
            ig.unfollow("following")
            break

        if ans==3:
            from x import Twitter
            x=Twitter(url=url,usernam=useraname,password=password)
            x.login()
            x.goto_profile()
            x.find_following(True)
            break
        if ans==4:
            from tiktok import TIKTOK
            tiktok=TIKTOK(username=useraname,password=password,url=url)
            tiktok.login()
            tiktok.autobomb()
        #twitter bomber
        if ans==5:
            from  x import Twitter
            x=Twitter(url=url,usernam=useraname,password=password)
            x.login()
            x.autobomb()
            
        
if __name__=="__main__":
    try:
        os.system("cls")
        banner(info=info)
        service_info(s=s)
        main()
    except KeyboardInterrupt:
        
        print("\n Keyboard Interrupt")