import xml.etree.ElementTree as ET
import os
import json
import re

from HTMLParser import HTMLParser

classes_data = []

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    class_name = ""
    studio_name = ""
    date = ""
    time = ""
    location = ""

    in_previous_class_li = False
    class_title_tag = False
    in_a = False

    p_count = 0
    br_count = 0
    data_count = 0

    def handle_starttag(self, tag, attrs):

        if tag == 'li' and ('class', 'media') in attrs:
            self.in_previous_class_li = True

        if tag == 'h3':
            if self.in_previous_class_li == True:
                self.class_title_tag = True

        if tag == 'a':
            self.in_a = True

        if tag == 'p' and self.in_previous_class_li == True:
            self.p_count += 1

        if tag == 'br':
            self.br_count += 1

    def handle_endtag(self, tag):
        if tag == "li":
            self.in_previous_class_li = False
            classes_data.append(ClassData(self.class_name, self.studio_name, self.date, self.time, self.location ))
            self.resetParser()

        if tag == 'h3':
            self.class_title_tag = False

        if tag == 'a':
            self.in_a = False

    def handle_data(self, data):

        if self.in_previous_class_li == True:
            if self.class_title_tag == True:
                if self.in_a == True:
                    self.class_name = data

            if self.p_count == 1:
                if self.in_a == True:
                    self.studio_name = data

            if self.p_count == 2:
                if self.br_count == 0:
                    self.date = data.strip()
                if self.br_count == 1:
                    self.time = data.strip()
                if self.br_count == 2:
                    self.location = data.strip()
                    self.br_count = -1

    def pretty_print(self):
        print "name " + self.class_name
        print "studio " + self.studio_name
        print "date " + self.date
        print "time " + self.time
        print "location " + self.location

    def print_state_info(self):
        print "in_previous_class_li " + str(self.in_previous_class_li)
        print "class_title_tag " + str(self.class_title_tag)
        print "in_a " + str(self.in_a)

        print "p_count " + str(self.p_count)
        print "br_count " + str(self.br_count)

    def resetParser(self):
        self.class_name = ""
        self.studio_name = ""
        self.date = ""
        self.time = ""
        self.location = ""

        self.class_title_tag = False
        self.in_a = False

        self.p_count = 0
        self.br_count = 0


class ClassData:
    def __init__(self, class_name, studio_name, date , time , location):
        self.class_name = class_name
        self.studio_name = studio_name
        self.date = date
        self.time = time
        self.location = location

    def get_json(self):
        data_as_json = {}
        data_as_json["class_name"] = self.class_name
        data_as_json["studio_name"] = self.studio_name
        data_as_json["date"] = self.date
        data_as_json["time"] = self.time
        data_as_json["location"] = self.location


        return data_as_json


dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'my_classes.htm')

parser = MyHTMLParser()

json_data = []

with open(filename, 'r') as content_file:
    content = content_file.read()

    parser.feed(content)


for class_data in classes_data:
    json_data.append(class_data.get_json())

with open("try1.json", 'w') as outfile:
    json.dump(json_data, outfile)
    outfile.close
