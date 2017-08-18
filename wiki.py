import wikipedia as wk


def wiki(text):
   try:
    answer = wk.summary(text,1)
    return answer
   except:
       return "Error"

