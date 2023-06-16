import datetime
import domControl

def monthly_calendar():
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
      <h4>#</h4>
    </div>
    '''
    return day_content
  
  # return a row and loop through/add days per column
  def make_row():
    columns = 5
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
  domControl.attach_content_to_element(id='monthly-calendar', 
                 content=domControl.build_element(
                   type='div', 
                   class_name='calendar',
                   id='calendar', 
                   content=calendar_content
                 )
                )

def weekly_calendar():
  all_day_containers = ''
  day_list = ['Monday','Tuesday','Wednesday','Thursday','Friday']
  
  for i in day_list:
    box_info = domControl.build_element(
      type = 'div',
      class_name = 'box-info',
      id = 'weekly',
      content = f'''Info'''
    )
    
    day_name = domControl.build_element(
      type = 'div',
      class_name = 'day-name',
      id = 'weekly',
      content = f'''{i}'''
    )
    
    day_container = domControl.build_element(
      type = 'div',
      class_name = 'day-container',
      id = 'weekly',
      content = f'''{day_name}{box_info}'''
    )
    
    all_day_containers += day_container

  month_name = domControl.build_element(
    type = 'div',
    class_name = 'month-name',
    id = 'weekly',
    content = f'''September'''
  )
  
  weekly_calendar = domControl.build_element(
    type = 'div',
    class_name = 'weekly-calendar',
    id = 'weekly',
    content = f'''{month_name}{all_day_containers}'''
  )
  
  domControl.attach_content_to_element(
    id = 'pyscript-weekly-calendar', 
    content = weekly_calendar
  )


monthly_calendar()

weekly_calendar()