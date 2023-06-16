#from code import attach_content_to_element, build_element
#from quickLinks import build_and_attach_quick_links
import domControl
import quickLinks

header_el = domControl.build_element(
  type='div',
  id='pyscript-header',
)


quick_links_el = domControl.build_element(
  type='div',
  id='quick-links'
)

domControl.attach_content_to_element('quick-links', quick_links_el)

 

