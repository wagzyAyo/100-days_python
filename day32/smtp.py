import smtplib

my_email = "jmcvibes@yahoo.com"
password = "wagzy17"

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="classiccybertech@yahoo.com", msg="subject:Hello\n\nHow are You doing")
