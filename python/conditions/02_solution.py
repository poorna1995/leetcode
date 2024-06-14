
# days=['Monday', 'Tuesday','Wednesday','Thursday']

# class solution:
#     def movie_discount(self,age,days):
#         for day in days:
#             if day== 'wednesday' & age<18:
#                 price = 8
#                 print(price)
#             else:
#                 price=12
#                 print(price)


# print(solution().movie_discount(24))

age =9
day='wednesday'

price =12 if age>=18 else 8
if day=='wednesday':
   price-=2
   
print('ticket price for you is $',price)


