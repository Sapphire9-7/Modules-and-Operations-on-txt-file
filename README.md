# Modules-and-Operations-on-txt-file
This Python program first reads the txt file as a dictionary, the keys are the student names, and the values are a list of the students' marks. Operations such as finding the highest average, the highest mark, IQR, standard deviation.. etc are performed on the formed dictionary. This is a practice of modules, statistics, and dictionary operations.
# In more detail
The program first extracts the contents of the txt file and assigns the first element after splitting the contents as the key value of the dictionary and the remaining values are the values of each key and they are grouped as a list. Then operations on the original dictionary are performed, each operation can be found in the "Module" folder in the "functionsModule" Python file. Operations include:
- Finding the Max/Min average of the values and printing a dictionary pair of the key and the highest/lowest average.
- Finding the highest/lowest value of each list of each key and comparing the highest/lowest values, and finally printing a dictionary pair of the key and the highest/lowest value.
- Finding the Q1, Q2, Q3, and IQR of the merged lists.
- Finding the standard deviation of the merged lists.
- Finding th emost frequent element (mark) of the merged list.

The resulting dictionary is then exported as a json file.
