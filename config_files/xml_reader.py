import xml.etree.ElementTree as Et
from datetime import datetime


class XMLReader:
    path = '/Users/jaimegonzalezquirarte/Desktop/App/XML_Files/summary_a01260410.xml'
    def pull_info(tree):
        for section in tree:
            if section.tag == "info":
                for elementary in section:
                    if elementary.tag == "essentials":
                        for data in elementary:
                            print(data.tag, data.text)
                    elif elementary.tag == "basics":
                        for data in elementary:
                            print(data.tag, data.text)
            elif section.tag == "allergies":
                for allergy in section:
                    for element in allergy:
                        print(element.tag, element.text)
            elif section.tag == "background":
                for category in section:
                    # to be reviewed
                    if section.tag == "hereditary":
                        print(category.text)
                    elif section.tag == "pathological":
                        print(category.text)
            elif section.tag == "immunizations":
                for immunization in section:
                    print(immunization.text)
            elif section.tag == "tags":
                for element in section:
                    for event in element:
                        print(event.tag, event.text)
            elif section.tag == "statuses":
                for group in section:
                    for element in group:
                        for detail in element:
                            print(detail.tag, detail.text)

    try:
        tree = Et.parse(path).getroot()
        pull_info(tree)

    except FileNotFoundError:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"{dt_string} - File {path} not found!")

    except PermissionError:
        print(f"{datetime.now()} Insufficient permission to read {path}!")

    except IsADirectoryError:
        print(f"{datetime.now()} {path} is a directory!")
    except OSError as e:
        print(f"Unable to open {path}: {e}")
