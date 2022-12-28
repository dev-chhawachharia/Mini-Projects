
#Mini Project :- Monday Motivational Quote via email
import random
import datetime as dt
import smtplib
#get quotes:
list1 = []
with open("quotes.txt") as file1:
    for line in file1:
        list1.append(line)

# print(list1)

todayQuote = list1[random.randint(0,102)]
# print(todayQuote)

now = dt.datetime.now()
day_of_week= now.weekday()
# print(day_of_week)
if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=<enter your email-id> , password =<enter your app password> )
        connection.sendmail(from_addr=<sender email id> , to_addrs=<reciever email id> , msg=f"Subject:Today's Motivational Quote\n\n{todayQuote}")

