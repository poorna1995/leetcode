


def PowerofNumber(number,power):
    if power ==0:
        return 1
    print(power)
    return number * PowerofNumber(number,power-1)


number =2
power=3

print(PowerofNumber(number,power))