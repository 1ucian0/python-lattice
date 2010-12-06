#!/usr/bin/python

import urllib
import lxml.html as html
import textwrap

source=urllib.urlopen('http://code.google.com/p/python-lattice/').read()
doc = html.document_fromstring(source)

title=doc.get_element_by_id('project_summary_link').text_content()
wikicontent=doc.get_element_by_id('wikicontent')
body_text='''
python-lattice
==============
'''
body_text+=title+'\n\n'
for child in wikicontent.iterdescendants():
    text=child.text_content().replace(u'\xb6','')
    if child.tag == 'h2':
        body_text+='\n'+text+'\n'+'-'*len(text)
    elif child.tag == 'pre':
        body_text+='\n\t'+text.replace('\n','\n\t')+'\n'
    elif child.tag == 'p':
        body_text+='\n'+textwrap.fill(text, width=80)
    else:
        pass
print body_text
