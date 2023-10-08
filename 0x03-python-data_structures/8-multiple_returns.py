#!/usr/bin/python3
def multiple_returns(sentence):
    leta = len(sentence)
    return (leta, sentence[0] if leta > 0 else None)
