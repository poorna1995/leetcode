# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function


class solution:
    def oddnumber(self, num):
        odd = []
        for i in range(num + 1):
            if i % 2 != 0:
                odd.append(i)
        return odd


print(solution().oddnumber(1000))
