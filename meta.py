
try:
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    import time,sys, traceback,re,os
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    import colorama
except:
    import os
    os.system(f"pip install -r r.txt")
    
path =r"C:\Program Files (x86)\chromedriver.exe"
s=Service(executable_path=path)
driver=webdriver.Chrome(service=s)   
class META: 
    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
    def wait(by,element,time=15):
        try:
            wait=WebDriverWait(driver,time)
            return wait.until(EC.visibility_of_element_located((by,element)))
        except Exception as e:
            print(e)
    def waits(by,element,time=15):
        try:
            wait=WebDriverWait(driver,time)
            return wait.until(EC.visibility_of_all_elements_located((by,element)))
        except  Exception as e:
            META.log(e)
    def error():
        traceback_template = '''Traceback (most recent call last):
        File "%(filename)s", \nline %(lineno)s, in %(name)s
        %(type)s: %(message)s\n'''
        exc_type, exc_value, exc_traceback = sys.exc_info() 
        traceback_details = {
                                'filename': exc_traceback.tb_frame.f_code.co_filename,
                                'lineno'  : exc_traceback.tb_lineno,
                                'name'    : exc_traceback.tb_frame.f_code.co_name,
                                'type'    : exc_type.__name__,
                                'message' : exc_value,
                                }

        del(exc_type, exc_value, exc_traceback) # So we don't leave our local labels/objects dangling
        r=f"{traceback.format_exc()},{traceback_template % traceback_details}"
        return str(r)
    def exit():
        driver.quit()
        sys.exit()
    def log(txt):
        with open('logs.txt',"a+") as file:
            file.write(f"[{time.ctime()}]==>{txt}\n")
        print(txt)
        file.close()
