#https://rosalind.info/problems/iprb/
def probability (dom, hetero, rec):
    sum = 0
    for i in range (0, 9):
        if (i == 0):
            sum = sum + (dom / (dom + hetero + rec)) * ((dom - 1) / (dom + hetero + rec - 1))
        elif (i == 2):
            sum = sum + (dom / (dom + hetero + rec)) * (hetero / (dom + hetero + rec - 1))
        elif (i == 3):
            sum = sum + (dom / (dom + hetero + rec)) * (rec / (dom + hetero + rec - 1))
        elif (i == 4):
            sum = sum + (hetero / (dom + hetero + rec)) * (dom / (dom + hetero + rec - 1))
        elif (i == 5):
            sum = sum + (hetero / (dom + hetero + rec)) * ((hetero - 1) / (dom + hetero + rec - 1)) * 0.75
        elif (i == 6):
            sum = sum + (hetero / (dom + hetero + rec)) * (rec / (dom + hetero + rec - 1)) * 0.5
        elif (i == 7):
            sum = sum + (rec / (dom + hetero + rec)) * (dom / (dom + hetero + rec - 1))
        elif (i == 8):
            sum = sum + (rec / (dom + hetero + rec)) * (hetero / (dom + hetero + rec - 1)) * 0.5
    return sum

print(probability(17,21,18))