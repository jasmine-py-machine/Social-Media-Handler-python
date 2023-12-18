import sys
import os
import json
PATHSELENIUM=r"C:\\Program Files (x86)\\chromedriver.exe"
CHROMEDRIVERNAME=r"chromedriver.exe"
REQUIREMENTNAME=r"r.txt"
SETUPJSON=r"setup.json"
##check for setup
setup=json.load(open(SETUPJSON))["setup"]
g={
        "setup":"yes",
        "all":"ypu"
    }
def  converttojson(lst):
    with open(SETUPJSON, 'w') as json_file:
        json.dump(lst, json_file,indent=4,separators=(',',':'))
      
if setup=="yes":
   print("")
else:
    #install module first
    os.system(f"pip install -r {REQUIREMENTNAME}")
    if  os.path.exists(PATHSELENIUM):
        print(f"{PATHSELENIUM}=====> exist")
        converttojson(g)
        print("setup complete")
    else:
        print(f"{PATHSELENIUM}=====>  not exist\n adding it automathically")
        try:
            os.replace("chromedriver.exe",PATHSELENIUM)
        except Exception as e:
            print(e)
            pass
        if os.path.exists(PATHSELENIUM):
            print("file move successfully ")
            converttojson(g)
            print("setup complete")
            
        else:
            print("pls do it manually ")
            print(f"copy file {CHROMEDRIVERNAME} to path {PATHSELENIUM}")
    
    
    


