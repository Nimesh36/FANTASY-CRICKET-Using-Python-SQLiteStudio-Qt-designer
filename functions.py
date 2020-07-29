def score(d):
    sco=int(d[1]/2)
    if d[1]>=50: sco+=5
    if d[1]>=100: sco+=10
    if d[2]>0:
        sr=d[1]*100/d[2]
        if sr>=80 and sr<100: sco+=2
        if sr>=100:sco+=4
    sco += d[3]
    sco += 2*d[4]
    sco += d[8] * 10
    if d[8] >= 3: sco = sco + 5
    if d[8] >= 5: sco = sco + 10
    if d[5]>0:
        er = d[7]*6/ d[5]
        if er <= 2: sco = sco + 10
        if er > 2 and er <= 3.5: sco = sco + 7
        if er > 3.5 and er <= 4.5: sco = sco + 4
    sco = sco + 10*(d[9]+d[10]+d[11])
    return sco