i = 1
def attach_content_to_element(id, content):
  Element(id).element.innerHTML = Element(id).element.innerHTML + content

def build_element(
  type='div',
  class_name='',
  id='', 
  content='',
  attributes={}
):
  class_string = f' class={class_name}' if class_name else ''
  id_string = f' id={id}' if id else ''
  attributes_string = ''
  for attribute_key, attribute_value in attributes.items():
    attributes_string+= f' {attribute_key}={attribute_value}'
  print(attributes_string)
  return f'''
    <{type}{class_string}{id_string}{attributes_string}>
      {content}
    </{type}>
  '''


quick_links_el = build_element(
  type = 'div',
  class_name = 'quick-links', 
  id = 'quick-links'
)

print(quick_links_el)
attach_content_to_element(quick_links_el, 'quick-links')

# itemize
for link in quick_links_list:
  link_el = build_element(
    type='a', 
    id='quick-link-'+i,
    class_name='quick-link',
    content='display link name',
    attributes={
      'href': 'https://phs.wrdsb.ca/'
    }  
  )
  i+=1
  attach_content_to_element(quick_links, link_el)
                          
  #<a href = 'https://phs.wrdsb.ca/', target = 'blank',> Preston Highschool)


