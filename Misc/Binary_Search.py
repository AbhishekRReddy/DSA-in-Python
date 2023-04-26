'''
Binary Search
'''

def locate_card(cards,query):
    for pos,elem in enumerate(cards):
        if elem==query:
            return pos
    return False

test_cases={'input':{'cards':[],
                     'query':4},
            'output':4
}
print(locate_card(**test_cases['input'])==test_cases['output'])