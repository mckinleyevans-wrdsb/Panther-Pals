import domControl


domControl.build_element('div', 'announcement','announcement')

announcement = input('What announcment do you want to make')

domControl.attach_content_to_element('pyscript-announcements','<h4>  </h4>'+announcement)