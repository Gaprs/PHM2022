import os
import pandas as pd
import time

path = r"D:\Pycharm\Python_Porject\2023\data\Organized_training_data"

p1 = {"DATA_C":0, "REF_C":0}
p2 = {"DATA_C":0, "REF_C":0}
p4 = {"DATA_C":0, "REF_C":0}
p5 = {"DATA_C":0, "REF_C":0}
p6 = {"DATA_C":0, "REF_C":0}
person = [p1, p2, p4, p5, p6]
def read_data():
    for person_num, dict in enumerate(os.listdir(path)):
        file_path = os.path.join(path, dict)

        for file in os.listdir(file_path):
            t = time.time()
            data = pd.read_csv(os.path.join(file_path, file))
            if ("data_pdmp" in file):
                person[person_num]["DATA_C"] = len(data.columns)
            elif ("ref_pdmp" in file):
                person[person_num]["REF_C"] = len(data.columns)
            print(time.time() - t)


read_data()
print("done")
