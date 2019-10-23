import json
worse_case = 3
# [{"pset_number": 1.0, "auto_grader_score": 1.0, "style_score": 0.9, "discussion_score": 1.0}, {"pset_number": 2.0, "auto_grader_score": 1.0, "style_score": 0.9, "discussion_score": 1.0}, {"pset_number": 3.0, "auto_grader_score": 0.875, "style_score": 0.9, "discussion_score": 1.0}, {"pset_number": 4.0, "auto_grader_score": 0.93, "style_score": 1.0, "discussion_score": 1.0}, {"pset_number": 5.0, "auto_grader_score": 0.0, "style_score": 1.0, "discussion_score": 1.0}]

def calculate_score(pset,auto,style,discussion):
    #auto/100
    low = 3
    high = 7
    total_points = 5 if pset != 5 else 10
    #the lowest and highest range that a pset score can be assigned

    #(style + discussion)/2
    checkoff_normalized = (style + discussion)/2

    # sum of scores/ max * number osc scores
    if auto or pset != 5:
        if auto > checkoff_normalized:
            auto_points =  low * auto
            checkoff_points = high * checkoff_normalized
        else:
            auto_points =  high * auto
            checkoff_points = low * checkoff_normalized

        percent_score = (auto_points + checkoff_points)/10
    else:
        auto_points = 0
        checkoff_points = checkoff_normalized * 10


    percent_score = (auto_points + checkoff_points)/10

    #(auto_points + checkoff_point)/ 10

    return total_points * percent_score

def calculate_total_lab_score():
    with open('pset.json') as json_data:
        total_score = 0
        jsonData = json.load(json_data)
        print(jsonData)
        worse_case_score = dict() #key is pset and value is the wrose case score
        for pset in jsonData:
            pset_number,auto_grader_score,style_score,discussion_score = pset["pset_number"], pset["auto_grader_score"], pset["style_score"],pset["discussion_score"]
            points =  calculate_score(pset_number,auto_grader_score,style_score,discussion_score)
            total_score += points
        return total_score

def calculate_total_grade(finger_score_percentage,test_score, microquiz_score):
    lab_score = calculate_total_lab_score()
    finger_score = 10 * finger_score_percentage/100
    test_score = test_score/100.0 * 40
    microquiz_score = 20 * microquiz_score/20
    return lab_score + finger_score + test_score + microquiz_score

print(calculate_total_grade(88.8, 81, 20))








# [{"pset_number": "Pset 1", "auto_grader_score": "100.0%", "style_score": ": 9/10 ", "discussion_score": ": 10/10 "}, {"pset_number": "Pset 2", "auto_grader_score": " 100.0%", "style_score": ": 9/10 ", "discussion_score": ": 10/10 "}, {"pset_number": "Pset 3", "auto_grader_score": " 87.5%", "style_score": ": 9/10 ", "discussion_score": ": 10/10 "}, {"pset_number": "Pset 4", "auto_grader_score": " 93.0%", "style_score": ": 10/10 ", "discussion_score": ": 10/10 "}, {"pset_number": "Pset 5", "auto_grader_score": "", "style_score": ": 10/10 ", "discussion_score": ": 10/10 "}]
