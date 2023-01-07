def duzlestirme(k):

    for x in k:
        if isinstance(x,list):
            duzlestirme(x)
        else:
            boskume.append(x)
            

k =[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

boskume=[]

duzlestirme(k)



print(boskume)

