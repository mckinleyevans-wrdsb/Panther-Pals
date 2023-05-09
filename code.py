
def attach_content_to_element(id, content):
  print(Element(id).element)
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

quick_links_list = {
  'Preston Website':'https://phs.wrdsb.ca/',
  'Google': 'https://www.google.com/'
  }



# itemize
for i, (link_label, link_url) in enumerate(quick_links_list.items()):
  
  link_el = build_element(
    type ='a', 
    id ='quick-link-'+str(i),
    class_name ='quick-link',
    content = link_label,
    attributes = {
      'href': link_url
    }  
  )

  
  attach_content_to_element('quick-links', link_el)
                          
  #<a href = 'https://phs.wrdsb.ca/', target = 'blank',> Preston Highschool)


