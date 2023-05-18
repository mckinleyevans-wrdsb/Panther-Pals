#from code import attach_content_to_element, build_element
import code 

#Builds the quicklink element 

def build_and_attach_quick_links(quick_links_list):
  for i, (link_label, link_url) in enumerate(quick_links_list.items()):
    link_el = code.build_element(
      type ='a', 
      id ='quick-link-'+str(i),
      class_name ='quick-link',
      content = link_label,
      attributes = {
        'href': link_url,
        'target=': '"blank"'
      }  
    )
  #Add the quicklink content to the quicklink element 
    code.attach_content_to_element('quick-links', link_el)