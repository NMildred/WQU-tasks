def describe(key):
    
    list_1= [(script[key]) for script in scripts]
    total = sum (list_1)
    avg = total/len (list_1)
    
    variance = []
    for x in range(len(scripts)):
        variance.append((list_1[x] - avg)**2)
    s = (sum(variance)/len(scripts))**0.5
        
    list = sorted ([(script[key]) for script in scripts])
    for n in range (0, len (list)):
        median = 1/2*(n+1)
        Q1 = 1/4*(n+1)
        Q3 = 3/4*(n+1)
        med = list [int (median)]
        q25 = list [int (Q1)]
        q75 = list [int (Q3)]

    return (total, avg, s, q25, med, q75)
