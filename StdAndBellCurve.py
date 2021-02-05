import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
math_score_list = df["math score"].to_list()
reading_score_list = df["reading score"].to_list()
writing_score_list = df["writing score"].to_list()

math_score_mean = statistics.mean(math_score_list)
reading_score_mean = statistics.mean(reading_score_list)
writing_score_mean = statistics.mean(writing_score_list)

math_score_median = statistics.median(math_score_list)
reading_score_median = statistics.median(reading_score_list)
writing_score_median = statistics.median(writing_score_list)

math_score_mode = statistics.mode(math_score_list)
reading_score_mode = statistics.mode(reading_score_list)
writing_score_mode = statistics.mode(writing_score_list)

print("Mean, Median and Mode of math is {}, {} and {} respectively".format(math_score_mean, math_score_median, math_score_mode))
print("Mean, Median and Mode of reading is {}, {} and {} respectively".format(reading_score_mean, reading_score_median, reading_score_mode))
print("Mean, Median and Mode of writing is {}, {} and {} respectively".format(writing_score_mean, writing_score_median, writing_score_mode))

math_std_deviation = statistics.stdev(math_score_list)
reading_std_deviation = statistics.stdev(reading_score_list)
writing_std_deviation = statistics.stdev(writing_score_list)

math_first_std_deviation_start, math_first_std_deviation_end = math_score_mean-math_std_deviation, math_score_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_score_mean-(2*math_std_deviation), math_score_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_score_mean-(3*math_std_deviation), math_score_mean+(3*math_std_deviation)

reading_first_std_deviation_start, reading_first_std_deviation_end = reading_score_mean-reading_std_deviation, reading_score_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_score_mean-(2*reading_std_deviation), reading_score_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_score_mean-(3*reading_std_deviation), reading_score_mean+(3*reading_std_deviation)

writing_first_std_deviation_start, writing_first_std_deviation_end = writing_score_mean-writing_std_deviation, writing_score_mean+writing_std_deviation
writing_second_std_deviation_start, writing_second_std_deviation_end = writing_score_mean-(2*writing_std_deviation), writing_score_mean+(2*writing_std_deviation)
writing_third_std_deviation_start, writing_third_std_deviation_end = writing_score_mean-(3*writing_std_deviation), writing_score_mean+(3*writing_std_deviation)

math_list_of_data_within_1_std_deviation = [result for result in math_score_list if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_list_of_data_within_2_std_deviation = [result for result in math_score_list if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_list_of_data_within_3_std_deviation = [result for result in math_score_list if result > math_third_std_deviation_start and result < math_third_std_deviation_end]

reading_score_list_of_data_within_1_std_deviation = [result for result in reading_score_list if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_score_list_of_data_within_2_std_deviation = [result for result in reading_score_list if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_score_list_of_data_within_3_std_deviation = [result for result in reading_score_list if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]

writing_score_list_of_data_within_1_std_deviation = [result for result in writing_score_list if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_score_list_of_data_within_2_std_deviation = [result for result in writing_score_list if result > writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_score_list_of_data_within_3_std_deviation = [result for result in writing_score_list if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]

print("{}% of data for math lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_score_list)))
print("{}% of data for math lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(math_score_list)))
print("{}% of data for math lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(math_score_list)))

print("{}% of data for reading lies within 1 standard deviation".format(len(reading_score_list_of_data_within_1_std_deviation)*100.0/len(reading_score_list)))
print("{}% of data for reading lies within 2 standard deviations".format(len(reading_score_list_of_data_within_2_std_deviation)*100.0/len(reading_score_list)))
print("{}% of data for reading lies within 3 standard deviations".format(len(reading_score_list_of_data_within_3_std_deviation)*100.0/len(reading_score_list)))

print("{}% of data for reading lies within 1 standard deviation".format(len(writing_score_list_of_data_within_1_std_deviation)*100.0/len(writing_score_list)))
print("{}% of data for reading lies within 2 standard deviations".format(len(writing_score_list_of_data_within_2_std_deviation)*100.0/len(writing_score_list)))
print("{}% of data for reading lies within 3 standard deviations".format(len(writing_score_list_of_data_within_3_std_deviation)*100.0/len(writing_score_list)))