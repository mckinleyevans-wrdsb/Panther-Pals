import datetime
import domControl 

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
      
# create calendar element
calendar_content = ''''''
rows = 5
columns = 5

# return a day and its content
def make_day():
  day_content = f'''
  <div class='calendar-day'>
    <h5>#</h5>
  </div>
  '''
  return day_content

# return a row and loop through/add days per column
def make_row():
  global columns
  column_content = ''''''
  for i in range(columns):
    column_content += make_day()
  
  row_content = f'''
  <div class='calendar-row'>
    {column_content}
  </div>
  '''

  return row_content


for i in range(rows):
  calendar_content += make_row()

# print each day in the month ( use this later )
for date in date_iterate(2023, 5):
  pass

# make the calendar content on the html
domControl.attach_content_to_element(id='pyscript-calendar', 
               content=domControl.build_element(
                 type='div', 
                 class_name='calendar',
                 id='calendar', 
                 content=calendar_content
               )
              )

