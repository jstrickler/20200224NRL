#!/usr/bin/env python
import xml.etree.ElementTree as ET
import lxml.etree as ET

doc = ET.parse('DATA/presidents.xml')

for pres in doc.findall('.//president'):
    name = pres.find('name')
    first_name = name.findtext('first')
    last_name = name.findtext('last')
    party = pres.findtext('party')
    print(first_name, last_name, party)


