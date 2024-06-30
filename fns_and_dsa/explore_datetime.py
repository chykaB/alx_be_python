import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    year = current_date.year
    month = current_date.month
    day = current_date.day
    print(f"Current date and time: {year}-{month}-{day} {current_date.hour}:{current_date.minute}:{current_date.second}")
display_current_datetime()

def calculate_future_date():
    num_of_days = int(input("Enter the number of days to add to the current date:  "))
    current_date = datetime.date.today()
    print(current_date)
    future_date = timedelta(days=num_of_days )
    result = current_date + future_date
    print(f"Future date: {result}")
calculate_future_date()