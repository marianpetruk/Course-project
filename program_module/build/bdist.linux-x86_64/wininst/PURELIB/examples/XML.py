import xml.etree.ElementTree as etree


tree = etree.parse('files/feed.xml')
root = tree.getroot()

print(root)
print(root.tag)

print(len(root))

for child in root:
    print(child)

print(root.attrib)
print(root[4])
print(root[4].attrib)

tree.findall('{http://www.w3.org/2005/Atom}entry') 
new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed', 
     attrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en'})
print(etree.tostring(new_feed))
