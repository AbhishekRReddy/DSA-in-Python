'''


'''

def locate_card(cards,query):
    for pos,elem in enumerate(cards):
        if elem==query:
            return pos





output=3

test_cases={'input':{'cards':[13,11,10,7,4,3,1,0],
                     'query':7},
            'output':3
}
print(locate_card(**test_cases['input'])==output)