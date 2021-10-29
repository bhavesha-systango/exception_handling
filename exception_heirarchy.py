print(IndexError.__mro__)
print(KeyError.__mro__)

def loopups():
    s = [1, 4, 6]
    try:
        item = s[5]
    except IndexError:
        print("handled index error")

    d = dict(a=65,b=66,c=67)
    try:
        value = d['x']
    except KeyError:
        print("handled key error")

loopups()
def loopups():
    s = [1, 4, 6]
    try:
        item = s[5]
    except LookupError:
        print("handled index error")

    d = dict(a=65,b=66,c=67)
    try:
        value = d['x']
    except LookupError:
        print("handled key error")

loopups()
