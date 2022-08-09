from datetime import datetime


user_input = input("Enter a Deadline Date : ")

input_list = user_input.split(":")

deadline = input_list[1]

print(input_list)

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()

time_remaining = deadline_date - today_date

print(f"Time Remaining for  {input_list[0]} is {time_remaining.days} days")
