__author__ = 'sileix'
f = open('test_flowsheet.gpj', 'rb')

from io import StringIO
from xml.parsers.expat import ParserCreate
from xml.etree.cElementTree import parse
# from xml.etree.cElementTree import fromstring
# a  = '<?xml version="1.0" encoding="utf-8"?>\n<rootnode version="1.0" type="example">\n    <Package> xmlMetadata </Package>\n</rootnode>'
# project = fromstring(a)
#
# doc=parse('test_flowsheet.gPJ')
#
# root = doc.getroot()
# i = 0
# for item in project:
#     print(i, item.tag, item.attrib)
#     i=i+1
#
# root[9].attrib
# root[9]
#
# for model in root.findall('ModelReference'):
#     name = model.get('model')
#     print(name)
f = StringIO('Hello!\nHi!\nGoodbye!')
while 1:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
