import datetime

# output content to the given element
def output_content(id, content):
  Element(id).element.innerHTML += content

# make element from given variables
def make_element(element_type, element_class, element_id, element_content):
  return f'''
  <{element_type} class='{element_class}' id='{element_id}'>
    {element_content}
  </{element_type}>
  '''
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

def make_day():
  day_content = f'''
  <div class='calendar-day'>
    <h4>'#'</h4>
  </div>
  '''
  return make_day()

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

# print each day in the month
for date in date_iterate(2023, 5):
  pass
  

output_content('pyscript-calendar', make_element(element_type='div', element_class='calendar', element_id='calendar', element_content=calendar_content))

