# Importing libraries
import datetime
import hashlib
import time
from urllib.request import urlopen, Request

from send import send_email

# setting the URL you want to monitor
# url = Request('https://www.union.ic.ac.uk/acc/badminton/sessions/view/index.php?sid=89603',
#               headers={'User-Agent': 'Mozilla/5.0'})
url = Request("https://www.union.ic.ac.uk/acc/badminton/sessions/view/index.php?sid=89606",
              headers={'User-Agent': 'Mozilla/5.0'})

# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("running")

to = ["carl.yifeng.li@outlook.com", "lixt2002@gmail.com", "leo.liu20@imperial.ac.uk"]
time_interval = 300

while True:
    try:
        # perform the get request and store it in a var
        response = urlopen(url).read()

        # create a hash
        currentHash = hashlib.sha224(response).hexdigest()

        # wait for 30 seconds
        time.sleep(time_interval)

        # perform the get request
        response = urlopen(url).read()

        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()

        # Present time
        time_now = "[{}]".format(datetime.datetime.now())

        # check if new hash is same as the previous hash
        if newHash == currentHash:
            print(" ".join([time_now, "No change"]))
            continue

        # if something changed in the hashes
        else:
            # notify
            print(" ".join([time_now, "Something changed"]))

            # Send the email to notify me
            send_email(to)

            # again read the website
            response = urlopen(url).read()

            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()

            # wait for 30 seconds
            time.sleep(time_interval)
            continue

    # To handle exceptions
    except Exception as e:
        print("error")
