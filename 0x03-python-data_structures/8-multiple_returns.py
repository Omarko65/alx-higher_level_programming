#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    if lent < 1:
        return(lent, None)
    else:
        return(lent, sentence[0])
