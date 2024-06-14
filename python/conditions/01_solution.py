# 
# if age<13 
# print(child)
# elseif if age<20 
# print(teenager)
# elseif age <60 
# print(adult)
# else age>60
# print(senior)



class solution:
    def age_category(self, age):
        if age<16 :
            print('child')
        elif age<20:
            print('Teenager')
        elif age<60:
            print('Adult')
        else:
            print('Senior')

print(solution().age_category(12))
     

    


        