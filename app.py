from xml.dom import minidom


def read_xml(line):
    mydoc = minidom.parse('C:\\Users\\MarcoCalzada\\OneDrive - KS Soluciones\\Python\\flaskTest\\docs\\layout.xml')
    layout_fields = mydoc.getElementsByTagName("field")
    write_file = open("C:\\Users\\MarcoCalzada\\OneDrive - KS Soluciones\\Python\\flaskTest\\docs\\parsed",
                      "a")
    for field in layout_fields:
        length = field.attributes['length'].value
        data = line[:int(length)]
        line = line[int(length):]
        write_file.write(field.firstChild.data.ljust(30, ' ') + '\t||' + data + "\n")
    write_file.write("\n\n")


def main():
    for line in open("C:\\Users\\MarcoCalzada\\OneDrive - KS Soluciones\\Python\\flaskTest\\docs\\transactions", "r"):
        read_xml(line)
        print("\n")
        print("\n")


if __name__ == '__main__':
    main()
