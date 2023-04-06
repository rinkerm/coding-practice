import sys
import xml.etree.ElementTree as etree
 
def get_attr_number(node):
    if node is None:
        return 0
    else:
        a = len(node.attrib)
        for child in node:
            a+=get_attr_number(child)
        return a
    

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
