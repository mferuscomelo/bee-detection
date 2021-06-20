# Adapted from: https://github.com/datitran/raccoon_dataset/blob/master/xml_to_csv.py

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + "/*.xml"):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall("object"):
            width = int(root.find("size")[0].text)
            height = int(root.find("size")[1].text)

            # According to: https://cloud.google.com/vision/automl/object-detection/docs/csv-format
            value = (
                # TODO: Need to change UNASSIGNED to TRAIN/VALIDATION/TEST randomly. Common ratios: 80/10/10, 70/15/15, 60/20/20
                "UNASSIGNED", # set
                root.find("path").text.replace("\\", "/").replace("C:/Users/milanfc/OneDrive/Documents/Programming/bee-detection/", ""), # path
                member[0].text, # label
                int(member[4][0].text) / width, # x_min (normalized => x_min / width)
                int(member[4][1].text) / height, # y_min (normalized => x_min / height)
                "",
                "",
                int(member[4][2].text) / width, # x_max (normalized => x_max / width)
                int(member[4][3].text) / height, # y_max (normalized => x_max / height)
                "",
                ""
            )
            xml_list.append(value)
    column_name = ["set", "path", "label", "x_min", "y_min", "", "", "x_max", "x_max", "", ""]
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    image_path = "./../annotations/"
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv("./../data/bee_labels.csv", index=None, header=None)
    print("Successfully converted xml to csv.")


main()

# root.find("path").text.replace("\\", "/").replace("C:/Users/milanfc/OneDrive/Documents/Programming/bee-detection", "."), # path
#                 int(root.find("size")[0].text), # label
#                 int(root.find("size")[1].text), #x_min
#                 member[0].text,
#                 int(member[4][0].text),
#                 int(member[4][1].text),
#                 int(member[4][2].text),
#                 int(member[4][3].text)