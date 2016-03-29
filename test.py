__author__ = "Silei Xiong"

import xml.etree.ElementTree as ET
import string
# from collections import namedtuple
# from urllib.request import urlopen
# from xml.etree.cElementTree import parse
import csv

def read_data(model):
    with open('Icon_size_data_base.csv') as f:
        f_csv = csv.reader(f, delimiter=',')
        # headers = next(f_csv)
        #
        # ftab_csv = csv.reader(f)
        # next(ftab_csv)
        # next(ftab_csv)
        # for row in ftab_csv:
        #     print(row)
        #     [a, b, c, d] = row
        # print(a, '\n', b, '\n', c, '\n', d)

# open file or read to string
project_file = open('Buhler_mill_layout1.gPJ', 'r')
file_str = project_file.read()
project_file.close()
# file_str.encode(encoding='utf-8')
root = ET.fromstring(file_str)

# tree = ET.parse("test_flowsheet.gPJ")
# root = tree.getroot()

ModelReferenceCache = root.find('ModelReferenceCache')
ModelReference = ModelReferenceCache.findall('ModelReference')
# ModelEntity = root.find('ModelEntity')
for it in root.iter('Group'):
    if it.attrib['name'] == 'Models':
        Group_Models = it
        ModelEntity = it.findall('ModelEntity')
        break

# ModelEntity[0].attrib['name'] = 'mod_test'
a = ET.tostring(root)
new_file = open('new', 'wb')
new_file.write(a)
new_file.close()
# tree.write('output', encoding="us-ascii")
# models = namedtuple('models', 'port')
# ports = namedtuple('ports', 'name content subType Transform Labels')
#Transform = namedtuple('Transform', 'ScaleX ScaleY ScaleX ScaleY TranslateX TranslateY')

class Port:
    def __init__(self, it):
        self.name = it.get('name')
        self.content = it.get('content')
        self.subType = it.get('subType')
        if 'layer' in it.keys():
            self.layer = it.get('layer')
        self.Transform = it.find('Transform').attrib
        self.Labels = [i.attrib for i in it.iter('Transform')]

    def write(self, it):
        pass


class Unit:
    def __init__(self, it):
        self.name = it.get('name')
        self.model = it.get('model')
        self.layer = it.get('layer')
        self.Transform = it.find('Transform').attrib
        self.Labels = [i.attrib for i in it.iter('Transform')]
    def write(self, it):
        pass

class Connection:
    def __init__(self, it):
        if 'unit_1' in it.keys():
            self.unit_1 = it.get('unit_1')
        else:
            self.unit_1 = it.get('port_1')
        if 'unit_2' in it.keys():
            self.unit_2 = it.get('unit_2')
        else:
            self.unit_2 = it.get('port_2')
        self.point_1 = it.get('point_1')
        self.point_2 = it.get('point_2')
        self.points = [float(i) for i in it.find('LineSegment').get('points').split(',')]

    def write(self, it):
        pass

class Model:
    def __init__(self, it):
        self.name = it.get('model')
        self.port = {i.get('name'):Port(i) for i in it.findall('Port')}
        # self.port = dict()
        # for it2 in it.findall('Port'):
        #     self.port[it2.get('name')] = Port(it2)

    def write(self, it):
        pass

class Flowsheet:
    def __init__(self, it):
        self.name = it.get('name')
        self.layer = [i.get('name') for i in it.find('FlowsheetLayers').findall('Layer')]
        # self.Layer = list()
        # for it2 in it.find('FlowsheetLayers').findall('Layer'):
        #     self.Layer = it2.get('name')
        self.unit = {i.get('name'):Unit(i) for i in it.findall('Unit')}
        self.port = {i.get('name'):Port(i) for i in it.findall('Port')}
        self.all_unit = dict(self.unit, **self.port)
        self.connection = [Connection(i) for i in it.findall('Connection')]
        # self.unit = dict()
        # for it2 in it.findall('Unit'):
        #     self.unit[it2.get('name')] = Unit(it2)
        # for it2 in it.findall('Port'):
        #     self.unit[it2.get('name')] = Port(it2)
        # self.connection = list()
        # for it2 in it.findall('Connection'):
        #     self.connection.append(Connection(it2))

    def write(self, it):
        pass


models = dict()
flowsheets = list()
for it in ModelReference:
    models[it.get('model')] = Model(it)
for it in ModelEntity:
    flowsheets.append(Flowsheet(it))


