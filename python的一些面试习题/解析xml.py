# coding=utf-8
from xml.parsers.expat import ParserCreate
import urllib
import re

class BaiduWeatherXmlHandler(object):
    def __init__(self, xml):
        self.gdata = []
        self.wdata = ['currentCity', 'date', 'weather', 'wind', 'temperature']
        self.g = False
        self.parser = ParserCreate()
        self.parser.returns_unicode = True
        self.parser.StartElementHandler = self.start_element
        self.parser.EndElementHandler = self.end_element
        self.parser.CharacterDataHandler = self.char_data
        self.parser.Parse(xml)
    def start_element(self, name, attrs):
        #print 's' + name
        if name in self.wdata:
            self.g = True
    
    def end_element(self, name):
        #print 'e' + name
        if name == 'CityWeatherResponse':
            for x in self.gdata:
                print x

    def char_data(self, text):
        #print 'c' + text
        if self.g:
            self.gdata.append(text)
            self.g = False

#获取xml
try:
    page = urllib.urlopen('http://api.map.baidu.com/telematics/v2/weather?location=%E8%8D%86%E5%B7%9E&ak=B8aced94da0b345579f481a1294c9094')
    xml = page.read()
finally:
    page.close()

handler = BaiduWeatherXmlHandler(xml)
