import pandas as pd
import math

class Result(object):
    def __init__(self, output1, output2, output3):
        self.output1 = output1
        self.output2 = output2
        self.output3 = output3

class UserMainCode(object):
    @classmethod
    def age(cls, input1):
        # Read the CSV file
        data_frame = pd.read_csv(input1)
        
        # Calculate mean age rounded to 5 decimal places
        mean_age = round(data_frame['Age'].mean(), 5)
        
        # Count entries with age less than mean
        count_less_than_mean = len(data_frame[data_frame['Age'] < mean_age])
        
        # Calculate positive values after subtracting mean age
        positive_values = [round(age - mean_age, 3) for age in data_frame['Age'] if age > mean_age]
        
        return Result(mean_age, count_less_than_mean, positive_values)

# Example usage:
input1 = "URL of the dataset"
result = UserMainCode.age(input1)
print(result.output1)  # Output1: Mean age
print(result.output2)  # Output2: Number of entries with age less than mean
print(result.output3)  # Output3: List of positive values after subtracting mean age
