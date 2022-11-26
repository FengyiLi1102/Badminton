# Importing libraries
import datetime
import hashlib
import time
from urllib.request import urlopen, Request

from send import send_email


def read_hash(url):
    response = urlopen(url).read()
    return hashlib.sha224(response).hexdigest()


# setting the URL you want to monitor
url_Tues = Request('https://www.union.ic.ac.uk/acc/badminton/sessions/view/index.php?sid=89603',
                   headers={'User-Agent': 'Mozilla/5.0'})
url_Mon = Request("https://www.union.ic.ac.uk/acc/badminton/sessions/view/index.php?sid=89602",
                  headers={'User-Agent': 'Mozilla/5.0'})

# to create the initial hash
currentHash_Tue = read_hash(url_Tues)
currentHash_Mon = read_hash(url_Mon)
print("running")

to = ["carl.yifeng.li@outlook.com", "lixt2002@gmail.com", "leoliu4720@gmail.com"]
time_interval = 120

while True:
    try:
        # create a hash
        currentHash_Tues = read_hash(url_Tues)
        currentHash_Mon = read_hash(url_Mon)

        # wait for 30 seconds
        time.sleep(time_interval)

        # perform the get request
        newHash_Mon = read_hash(url_Mon)
        newHash_Tue = read_hash(url_Tues)

        # Present time
        time_now = "[{}]".format(datetime.datetime.now())

        # check if new hash is same as the previous hash
        if (newHash_Mon == currentHash_Mon) and (newHash_Tue == currentHash_Tue):
            print(" ".join([time_now, "No change"]))
            continue

        # if something changed in the hashes
        else:
            # notify
            print(" ".join([time_now, "Something changed"]))

            # Send the email to notify me
            send_email(to)

            # again read the website
            currentHash_Tue = read_hash(url_Tues)
            currentHash_Mon = read_hash(url_Mon)

            # wait for 30 seconds
            time.sleep(time_interval)
            continue

    # To handle exceptions
    except Exception as e:
        print("error")
