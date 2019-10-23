





def calculate_total_grade(lab_score,finger_score_percentage,test_score, microquiz_score):

    finger_score = 10 * finger_score_percentage/100
    test_score = test_score/100.0 * 40
    microquiz_score = 20 * microquiz_score/20
    return lab_score + finger_score + test_score + microquiz_score
