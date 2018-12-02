import os
import shutil
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
genuine_dir = dir_path + '\\sample_Signature333593f\\sample_Signature\\genuine\\'
lookup_dir = dir_path + '\\sample_Signature333593f\\sample_Signature\\forged\\'
move_dir =  dir_path + '\\sample_Signature333593f\\sample_Signature\\forged_classification\\'

def create_forged_subfolders():
    for i in range(1,31):
        id = '';
        if i > 9:
            id = '0' + str(i);
        else:
            id = '00' + str(i);
        os.makedirs(os.path.join(move_dir,'NFI-XXXYY' + id))

def arrange_forged():
    for folderName, subfolders, filenames in os.walk(lookup_dir):
        for i,filename in enumerate(filenames):
            f = filename[9:12]
            print f
            shutil.copy(lookup_dir+filename,move_dir+'NFI-XXXYY'+f)

def create_dataset():
    for folderName, subfolders, filenames in os.walk(genuine_dir):
        for filename in filenames:
            


create_dataset()
