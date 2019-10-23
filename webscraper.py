from bs4 import BeautifulSoup
import requests
import json
import sys # prints python_script.property
# url =  "https://sicp-s1.mit.edu/fall19/psets"
# url to get access
# response = requests.get(url, timeout=5)
# print(response.content)
# function that returns the response from accessing a particular page
with open("lab.html") as page:
    content = BeautifulSoup(page)
    firstHalf = content.find("div", attrs={"id": "firstHalf"})
    psets = firstHalf.findAll("center")[1:]#prints all the pset bodies
    pset_scores = []
    for index,lab in enumerate(psets):
        # pset = lab.find("b")
        # print(pset)
        pset_info = lab.findAll("td", attrs = {"align":"center"})
# <td align="center" colspan="8"><b>Pset 0</b></td>, <td align="center"> <b>Pset submitted</b> Friday, September 06 at 09:35PM</td>, <td align="center">Checkoff Not Required for Pset 0!</td>        if pset_info:
        if pset_info:

            pset_number = float(pset_info[0].text[5:6])

            auto_grader = pset_info[1].text
            # 'auto_grader': '100.0% Thursday, September 19 at 11:31PM'
            index = auto_grader.find("%")

            auto_grader_score = auto_grader[:index] if index >= 0 else "0"
            auto_grader_score = float(auto_grader_score.replace(" ",""))/100
            checkoff = pset_info[2].text
            checkoff_score = [index for index,i in enumerate(checkoff) if i == ":" or i == "|"]
            style_score = checkoff[checkoff_score[0]+1:checkoff_score[1]].replace(" ","").split("/")
            discussion_score = checkoff[checkoff_score[2]+1:checkoff_score[3]].replace(" ", "").split("/")
            style_score = float(style_score[0])/float(style_score[1])
            discussion_score = float(discussion_score[0])/float(discussion_score[1])


            # 'checkoff': 'style: 9/10 | discussion: 10/10 | time: Tuesday, September 17 at 06:26PM'
            score_info = {i:globals()[i] for i in ("pset_number", "auto_grader_score", "style_score","discussion_score")}
            # {'pset_number': 'Pset 1', 'auto_grader': '100.0% Thursday, September 19 at 11:31PM', 'checkoff': 'style: 9/10 | discussion: 10/10 | time: Tuesday, September 17 at 06:26PM'}

            pset_scores.append(score_info)

with open('pset.json', 'w') as outfile:
    json.dump(pset_scores, outfile)

        #     pset_number = psetline.b.text[:6]
        #     autograder = lab.find()
        #     print(autograder)
            # autograder = lab.select("td td text", attrs = {"color":"rgb(0,200,0)","font-weight":"bolder"}).text
            # checkoff = lab.find("text", attrs = {"color": "green"}).text
            # result = dict([(i,globals()[i]) for i in ("pset_number", "autograder", "checkoff")])



         # labObject = {
         #    "pset": lab.find("b"),
         #    "autograder": lab.find("span", attrs={"style":"color:rgb(0,200,0);font-weight:bolder;"}).text,
         #    "checkoff": lab.find("text", attrs={"style": "colors:green"}).text
         #    }
         # print(labObject)


# print(psets)
# firstHalf["style"] = None
# labArr = []
# print(firstHalf)
# for index,lab in enumerate(firstHalf.findAll('center')):
#
#     # print("lab",lab)
#
#     labObject = {
#     "pset": lab.findAll("b"),
#     "autograder": lab.findAll("span", attrs={"style":"color:rgb(0,200,0);font-weight:bolder;"}).text,
#     "checkoff": lab.findAll("text", attrs={"style": "colors:green"}).text
#     }
#     # print("labObject",labObject)
#     labArr.append(labObject)
# with open('pset.json', 'w') as outfile:
#     json.dump(tweetArr, outfile)

# import pdfquery
# pdf = pdfquery.PDFQuery("60001.pdf")
# result = pdf.extract([("with_formatter", "Autograder")])
# print(result)
