def attach_content_to_element(id, content):
  Element(id).element.innerHTML = Element(id).element.innerHTML + content

def build_element(type='div', class_name='', id='', content=''):
  class_string = f' class={class_name}' if class_name else ''
  id_string = f' id={id}' if id else ''
  return f'''
    <{type}{class_string}{id_string}>
      {content}
    </{type}>
  '''

print('Declan')
print("!!!")
print('!!!!!!!!!!!!!!')
print('Taiki')
  
print('!!!!!')
print('Numair')


print('!!!!!')
print("Jack is so cool and is the bestest")
print('this is so true - Aryan')
print('I lied aryan did not say that')
print('aryan')

print('Abeer')
print('Riley')
print('Hi')
print ('Eric')
