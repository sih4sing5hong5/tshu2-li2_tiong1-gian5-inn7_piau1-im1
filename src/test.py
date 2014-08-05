import xml.etree.ElementTree as ET

tree = ET.parse('123.xml')
root = tree.getroot()

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)