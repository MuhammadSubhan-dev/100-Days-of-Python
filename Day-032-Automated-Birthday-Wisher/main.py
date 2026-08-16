import pandas as pd
import datetime as dt
import random
import smtplib

MY_EMAIL = "t8045546@gmail.com"
MY_PASSWORD = "cemnqegvzmjxvfqc"

today_tuple = (dt.datetime.now().month, dt.datetime.now().day)    #Created tuple of todays month and day

data = pd.read_csv("./birthdays.csv")   #Dataframe

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}  #Stored in dictionary as tuples

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")




