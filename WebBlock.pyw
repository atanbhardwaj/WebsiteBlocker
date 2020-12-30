import time
from datetime import datetime as dt
from config import websites_to_block
#host_path = r"C:\Windows\System32\drivers\etc\hosts"
host_path = "hosts"
redirect_ip = "127.0.0.1"
website_list = websites_to_block
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,18)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        with open(host_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect_ip+" "+website+"\n")
    else:
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)       