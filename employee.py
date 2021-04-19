# to calculate dearness allowance

# class methods functions variables
def da(basic):
    da = basic * 0.8
    return da


def hra(basic):
    hra = basic * 0.15
    return hra


def pf(basic):
    pf = basic * 0.12
    return pf


def itax(gross):
    tax = gross * 0.10
    return tax


# structutal

# employee - file name ==

if __name__ == '__main__':
    print(hra(12000))
    print(__name__)
    print('Running from the original file')

else:
    print(__name__)
    print('call from the another programmmmm')

# basicSal = float(input('Enter the basic salry'))
# gross = hra(basicSal) + da(basicSal) + basicSal # total salary
# net = gross - pf(basicSal) - itax(gross)    # takeqaway
#
# print(f' my net salary is {net}')
