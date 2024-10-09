import xml.etree.ElementTree as ET


# def parse_xml(fn):
#     tree = ET.parse(fn)
#     root = tree.getroot()
#     print(tree.parse)
#     print(root.attrib["name"], root.tag)
#     for child in root:
#         print("\t" + child.attrib["name"], child.tag)


# parse_xml("C:\\Users\\ankit.yadav2\\OneDrive - S&P Global\\Desktop\\Untitled-1.xml")


# def write_xml(fn, el, attr, val):
#     tree = ET.parse(fn)
#     root = tree.getroot()
#     child = ET.Element(el)
#     child.attrib[attr] = val
#     root.append(child)
#     tree.write(fn)


# write_xml(
#     "C:\\Users\\ankit.yadav2\\OneDrive - S&P Global\\Desktop\\Untitled-1.xml",
#     "domain",
#     "name",
#     "hah",
# )


# def parse_xml(fn):
#     tree = ET.parse(fn)
#     root = tree.getroot()
#     print(root.tag)
#     for child in root:
#         print("\t" + child.tag)

# parse_xml("C:\\inetpub\\EDM\\Web.config")


def change_xml(fn):
    tree = ET.parse(fn)
    root = tree.getroot()
    appSettings = root.find("appSettings")
    for add in appSettings:
        if add.attrib["key"] == "Server":
            print(add.attrib["value"])
            server = input("New Server Name:")
            add.attrib["value"] = server
            print(add.attrib["value"])
        tree.write(fn)


change_xml("C:\\Users\\ankit.yadav2\\OneDrive - S&P Global\\Desktop\\Web.config")
