voted =  {'johnny' : 31 , 'adem' : 0 , 'david' : 1}
def checkvote(name):
    if voted.get(name):
        print('kicked out!')

    else:
        voted[name] = True
        print('Hi there!')