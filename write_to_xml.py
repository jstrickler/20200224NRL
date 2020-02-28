#!/usr/bin/env python
import xml.etree.ElementTree as ET
import lxml.etree as ET

vehicle_data = [
    ('wind', '0468', 'leo', 2003),
    ('ust', '4090', 'geo', 2006),
    ('cn', '9', 'leo', 2014),
]

root = ET.Element('vehicles')

for name, number, orbit, year in vehicle_data:
    v = ET.SubElement(root, 'vehicle', name=name)
    ET.SubElement(v, 'number').text = number
    ET.SubElement(v, 'orbit').text = orbit
    ET.SubElement(v, 'year').text = str(year)

print(ET.tostring(root, pretty_print=True).decode())

doc = ET.ElementTree(root)

doc.write('vehicles.xml', pretty_print=True, xml_declaration=True)

