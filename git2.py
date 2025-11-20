def sasa(*args):
    res=0
    sib=[]
    for i in args:
        if  i % 2 == 0:
            sib.append(i)
        else:
            print(f"mn argam zoj peyda nakardam")        
    return sib            
    


zoj=sasa(10,5,8,16,9,7,88,74,99,126,33,43)
print( f"list adad hay zoj be sharh zir mibashd {zoj}")