# from datetime import datetime as dt

# now = dt.now()
# year = now.year

# date_of_birth = dt(year=1995, month=5, day=7)

# print(year)
# print(date_of_birth)

import random
import smtplib
from datetime import datetime
day = datetime.now().weekday()

mail = "jmcvibes@yahoo.com"
my_password = "Wagzy17"

if day == 2:
    with open("./day32/quote.txt", encoding="utf-8") as file:
        content = file.read()
        list_content = content.splitlines()
        quote = random.choice(list_content)

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=mail, password=my_password)
        send = connection.sendmail(from_addr=mail, to_addrs="talktojmcvibes@jmail.com",
                                   msg=f"Subject:Monday motivation\n\n{quote}")
