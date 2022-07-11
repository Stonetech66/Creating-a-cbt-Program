#

class cbt:
   def __init__(self, question , answer):
     self.question= question
     self.answer= answer
     

"""
override the question_part and input your own questions with the answers
"""     
  
question_part=[
"who is the  premier league winner of 2021/2022\n(a) chelsea\n(b) mancity\n(c) liverpool\n\n",
"who is the  champions league winner of 2021/2022\n(a) liverpool\n(b) mancity\n(c) realmadrid\n\n",
"who is the president of America\n(a) joe biden\n(b) donald trump\n(c)hillary clinton\n\n",
]

Answers=[
cbt(question_part[0],"b"),
cbt(question_part[1],"c"),
cbt(question_part[2],"a"),
]


def run_cbt(Answers):
   score=0
   for cbt in Answers:
     answer=input (cbt.question)
     if answer== cbt.answer:
       score += 1
   print("your score is ",score," / ",len(Answers))
run_cbt(Answers)
