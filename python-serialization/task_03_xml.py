#!/usr/bin/env python3
import xml.etree.ElementTree as ET


"""function to serialize to xml"""


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    """goes to each item to make the conversion"""
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


"""function to deserialize"""


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}

    """goes to each item to make the conversion back"""
    for child in root:
        value_type = child.get("type")
        text = child.text or ""

        if value_type == "int":
            value = int(text)
        elif value_type == "float":
            value = float(text)
        elif value_type == "bool":
            value = text == "True"
        elif value_type == "NoneType":
            value = None
        else:
            value = text

        result[child.tag] = value

    return result
