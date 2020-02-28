#!/usr/bin/env python
import xml.etree.ElementTree as ET
import lxml.etree as ET

doc = ET.parse('DATA/presidents.xml')

print(doc)

presidents = doc.getroot()

print(presidents)

for pres in presidents:
    name = pres.find('name')
    first_name = name.findtext('first')
    last_name = name.findtext('last')
    party = pres.findtext('party')
    print(first_name, last_name, party)


