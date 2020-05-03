import time
from datetime import datetime as dt

host_path = r"C:\Windows\System32\drivers\etc\hosts"
host_temp = r"C:\Users\wojte\Documents\progamowanie python\web_blocker\hosts"
redirect = "127.0.0.1"
website_list = ["facebook.com", "www.facebook.com",
                "www.youtube.com", "youtube.com"]

# code in comments - triple quotes is my way to delete IP
# of blocked websites - finally method from course is applied
"""bare_hosts_file = ""

with open(host_temp) as f:
    content = f.readlines()
    for i in range(21):
        bare_hosts_file += content[i]"""

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 15) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("blocked time")
        with open(host_temp) as f:
            content = f.read()
            for i in website_list:
                if i in content:
                    pass
                else:
                    f.write(redirect+" "+i+"\n")

    else:
        print("free time")
        """with open(host_temp, "w") as f:
            #f.write(bare_hosts_file)"""
        with open(host_temp, "r+") as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(i in line for i in website_list):
                    f.write(line)
                f.truncate()
                # truncate() function deletes text from cursor and below
    time.sleep(5)


