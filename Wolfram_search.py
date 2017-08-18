import wolframalpha as wa
from ibmkeys import *


def wolfsearch(text):
    try:
        client = wa.Client(wolf_id)
        res = client.query(text)
        return next(res.results).text
    except:
        return "Wolfram error"