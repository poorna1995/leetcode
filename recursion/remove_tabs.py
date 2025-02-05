def RemoveTabs(string):
    if len(string)==0:
        return ""
    print(string)
    firstString = string[0]
    if firstString == " " or firstString == "\t":
        return RemoveTabs(string[1:])
        
    return string[0] + RemoveTabs(string[1:])
    
    

string = "poorna poraneesha \t"
print(RemoveTabs(string))
    