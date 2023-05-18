import os
from DolosAPI.dolos import dolos
import csv

path = input("Enter the submissions folder:")

with open("inputFiles.csv", "w") as file:
    file.write("filename"+'\n')
    for each_input_file in os.listdir(path):
        file.write(path + "\\"+each_input_file+'\n')


dolos.output_format = "csv"
dolos.output_destination = f"Dolos_Reports"
dolos.path = f"inputFiles.csv"
dolos.language = "cpp"
dolos.min_similarity = 0.5
dolos.sort_by = "similarity"
dolos.run()
