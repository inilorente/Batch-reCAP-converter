# -*- coding: utf-8 -*-

import os

#Path to Autodesk reCap installation folder
decap_path = r"C:\Program Files\Autodesk\Autodesk ReCap"
#Path to folder containing the point clouds
origins_folder = r'"REPLACE THIS TEXT BETWEEN QUOTATION MARKS WITH FOLDER PATH"'
#Path to folder where the resulting reCap projects will be saved
destination_folder = r'"REPLACE THIS TEXT BETWEEN QUOTATION MARKS WITH FOLDER PATH"'

os.chdir(decap_path)

origins = os.listdir(origins_folder)

for file in origins:
    os.system(r"decap.exe" + r" --importWithLicense " + destination_folder + " " + file + " " + origins_folder + "\\" + file)
