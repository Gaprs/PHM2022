import os
import pandas as pd
import time

path = r"D:\Pycharm\Python_Porject\2023\data\Data_Challenge_PHM2022_training_data"

p1 = {"DATA_C":0, "REF_C":0}
p2 = {"DATA_C":0, "REF_C":0}
p4 = {"DATA_C":0, "REF_C":0}
p5 = {"DATA_C":0, "REF_C":0}
p6 = {"DATA_C":0, "REF_C":0}
person = [p1, p2, p4, p5, p6]
def read_data():
    for dict in os.listdir(path):
        file_path = os.path.join(path, dict)

        for file in os.listdir(file_path):
            t = time.time()
            large_columns = 0
            with open(os.path.join(file_path, file), 'r') as f:
                lines = f.readlines()
                for line in lines:
                    column_count = len(line.split(','))
                    if column_count > large_columns:
                        large_columns = column_count
            f.close()
            columns_name = ["Target"] + ["data" + str(i) for i in range(0, large_columns)]
            data = pd.read_csv(os.path.join(file_path, file), header=None, delimiter=',', names=columns_name)
            data.to_csv(os.path.join(r"D:\Pycharm\Python_Porject\2023\data\Organized_training_data", file), index=False)
            print(file + " save done!")
            print(time.time() - t)


read_data()
