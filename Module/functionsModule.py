def assignDict(listRows):
    student_data = {}  # Dictionary to store student data
    for i in listRows:
        words = i.strip().split(",")  # Remove newline characters and split the line by commas
        student_name = words[0]
        student_marks = [int(mark) for mark in words[1:]]  # Convert marks to integers
        student_data[student_name] = student_marks
    return student_data


def read_txt_data(txt_path):
    try:
        file_obj = open(txt_path, 'r')  # opening the file
        list_rows = file_obj.readlines()  # reading lines from a file
        file_obj.close()

        return assignDict(list_rows)
    except Exception as e:
        print(e)
        return None


def readFile(file_path):
    return read_txt_data(file_path)

def MaxAvgSTD(dict1):
    all_avgs_list = {}
    for student, marks_list in dict1.items():
        value = 0  # Reset the value for each student
        count = 0  # Reset the count for each student

        for num in marks_list:
            count += 1
            value += num

        avg = value / count
        all_avgs_list[student] = avg

    return all_avgs_list

def find_highest_value(data_dict):
    if not data_dict:
        return None

    highest_avg = 0
    highest_student = None

    for student, avg in data_dict.items():
        if avg > highest_avg:
            highest_avg = avg
            highest_student = student

    return {"student_name": highest_student, "value": highest_avg}


def find_lowest_value(data_dict):
    if not data_dict:
        return None

    lowest_avg = float("inf")
    lowest_student = None

    for student, avg in data_dict.items():
        if avg < lowest_avg:
            lowest_avg = avg
            lowest_student = student

    return {"student_name": lowest_student, "value": lowest_avg}

def find_highest_mark(dict2):
    highest_student = None
    final_mark = float('-inf')  
    for key, value in dict2.items():
        highest_mark = value[0]
        for mark in value:
            if mark > highest_mark:
                highest_mark = mark
        
        if highest_mark > final_mark:
            final_mark = highest_mark
            highest_student = key
    return {"student_name": highest_student, "value": final_mark}
        
def find_lowest_mark(dict3):
    lowest_student = None
    final_mark = float('inf')  
    for key, value in dict3.items():
        lowest_mark = value[0]
        for mark in value:
            if mark < lowest_mark:
                lowest_mark = mark
        
        if lowest_mark < final_mark:
            final_mark = lowest_mark
            lowest_student = key
    return {"student_name": lowest_student, "value": final_mark}

    
#the statistics part
#finding Q1, Q2, and Q3

def find_quartiles(data):
    def median(numbers):
        n = len(numbers)
        index = n // 2
        if n % 2 == 0:
            return (numbers[index - 1] + numbers[index]) / 2
        else:
            return numbers[index]

    merged_list = []
    for marks in data.values():
        merged_list.extend(marks)

    sorted_marks = sorted(merged_list)
    lower_half = sorted_marks[:len(sorted_marks) // 2]
    upper_half = sorted_marks[(len(sorted_marks) + 1) // 2:]

    q1 = median(lower_half)
    q2 = median(sorted_marks)
    q3 = median(upper_half)

    quartiles = {"Q1": q1, "Q2": q2, "Q3": q3}
    return quartiles

#finding std
import math
from collections import Counter
def calculate_mean(marks):
    return sum(marks) / len(marks)

def calculate_variance(marks, mean):
    squared_diff_sum = sum((mark - mean) ** 2 for mark in marks)
    return squared_diff_sum / len(marks)

def find_std(marks):
    mean = calculate_mean(marks)
    variance = calculate_variance(marks, mean)
    standard_deviation = math.sqrt(variance)
    return standard_deviation

#finding IQR
def find_IQR(data):
    n = len(data)
    q1_index = n // 4
    q3_index = q1_index * 3

    q1 = data[q1_index]
    q3 = data[q3_index]

    return q3 - q1

#finding the most frequent value
def find_common(data):
    merged_list = []
    for marks in data.values():
        merged_list.extend(marks)

    count_dict = Counter(merged_list)
    most_frequent_value = count_dict.most_common(1)[0][0]

    return most_frequent_value



    

        
        
    
    





