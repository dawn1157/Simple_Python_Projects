what = input("0 for coding or 1 for decoding? ")   
inp = input("Enter the code: ")
codes = inp.split()
if what == '0': 
    few_code = []
    for code in codes:
        if (len(code) >= 3):
            ran1 = 'asd'
            ran2 = 'zxc'
            new_code = ran1 + code[1:] + code[0] + ran2
            few_code.append(new_code)
    
        else:
            few_code.append(code[::-1]) #reverses the string or the assinged value/type
    print(' '.join(few_code)) 
    '''print(' '.join(few_code)) --> helps the code to join again after 
    splitting, but remember the order of the the method'''


elif what == '1':
    willis = []
    for code in codes:
        if (len(code) >= 3):
            raw_code = code[3:-3]
            raw = raw_code[-1] + raw_code[:-1]
            willis.append(raw)
        else:
            willis.append(code[::-1]) #reverses the string or the assinged value/type
    print(' '.join(willis))
        
    