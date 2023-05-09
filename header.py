from code import attach_content_to_element, build_element

# <div class='header', id='header'>
#   Panther Pals
# </div

header_el = build_element(
  type='div',
  class_name='header',
  id='header',
  content='Panther Pals'
)

attach_content_to_element("pyscript-header",header_el)