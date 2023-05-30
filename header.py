from code import attach_content_to_element, build_element
from quickLinks import build_and_attach_quick_links

header_el = build_element(
  type='div',
  class_name='header',
  id='header',
  content=''
)

attach_content_to_element("pyscript-header", header_el)

quick_links_el = build_element(
  type='div',
  id='quick-links'
)
attach_content_to_element('pyscript-header', quick_links_el)

 #list of quick links
quick_links_list = {
  'Preston Website':'https://phs.wrdsb.ca/',
  'My Blueprint': 'https://app.myblueprint.ca/?sdid=wrdsb',
  'School Day':'https://www.school-day.com/',
  'Kahoot':'https://kahoot.it/'
}
build_and_attach_quick_links(quick_links_list)

