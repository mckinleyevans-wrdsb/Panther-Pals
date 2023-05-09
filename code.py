from pyscript import Element

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
  return f'''
    <{type}{class_string}{id_string}{attributes_string}>
      {content}
    </{type}>
  '''
