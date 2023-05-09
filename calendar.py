import datetime

# get the amount of days in a given month
def get_days_in_month(month, is_leap_year):
  month_days = 0
  
  if(month % 2 == 0):
    month_days = 30
  else:
    month_days = 31

  if(month == 2 and is_leap_year):
    month_days = 28
  elif (month == 2):
    month_days = 29
  
  return month_days

# iterate through the days in a month
def date_iterate(year, month):
    for i in range(1, get_days_in_month(month, year % 4 == 0) + 1):
        yield datetime.date(year, month, i)
      
# print each day in the month
for date in date_iterate(2022, 5):
    print(date)


