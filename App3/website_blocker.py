
import time

from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

hosts_temp = r".\App3\hosts"

redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.bbc.com"]

while True:
    if  8 <= dt.now().hour and dt.now().hour <= 16:

        with open(hosts_temp, "r+") as file:
            content = file.read()
            print(content)

            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")


    else:
        with open(hosts_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

            file.truncate()


    time.sleep(5)
