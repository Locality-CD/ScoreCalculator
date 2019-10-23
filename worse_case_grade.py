from webscraper import collect_lab_information
from total_worse_grade import calculate_total_grade
from parsedata import calculate_total_lab_score



result = collect_lab_information()
print(result)


# def calculate_total_grade(finger_score_percentage,test_score, microquiz_score):
#     lab_score = calculate_total_lab_score()
#     finger_score = 10 * finger_score_percentage/100
#     test_score = test_score/100.0 * 40
#     microquiz_score = 20 * microquiz_score/20
#     return lab_score + finger_score + test_score + microquiz_score
