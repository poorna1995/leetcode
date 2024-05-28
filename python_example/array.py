# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190

# Create a list to store these monthly expenses and using that find out
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this


expenses = [2200, 2350, 2600, 2130, 2190]
# print(expenses[1])


class solution:
    def month_expense(self, expenses):
        return expenses[1] - expenses[0]


print(solution().month_expense(expenses))


class solution:
    def first_quarter(self, expenses):
        return sum(expenses[0:3])


print(solution().first_quarter(expenses))


class solution:
    def spend_twothousand(self, expenses):
        for i in expenses:
            if i == 2000:
                return True
        return False


print(solution().spend_twothousand(expenses))


class solution:
    def jun_month(self, expenses):
        expenses.append(1980)
        return expenses


print(solution().jun_month(expenses))


class solution:
    def refund(self, expenses):
        expenses[3] = expenses[3] - 200
        return expenses


print(solution().refund(expenses))
