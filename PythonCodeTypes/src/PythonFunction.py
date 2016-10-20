'''
Created on Feb 19, 2016

@author: rduvalwa2
'''
import shelve

def high_score(player, score):
    dataBase = 'scores'
    shelf = shelve.open(dataBase)
    if player in shelf:
        if score > shelf[player]:
            shelf[player] = score
    else:
        shelf[player] = score
    highscore = shelf[player]
    shelf.close()
    return highscore

if __name__ == "__main__":
    team = high_score()
    