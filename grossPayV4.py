# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime
# and create a function called computepay which takes two parameters (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

inputHours = input('Please enter amount of hours: ')
try:
    float_hours = float(inputHours)
except:
    print('Error, please enter numeric input')
    exit()
inputRate = input('Please enter rate per hour: ')
try:
    float_rate = float(inputRate)
except:
    print('Error, please enter numeric input')
    exit()


def computepay(hours, rate):
    if hours > 40:
        extraTime = hours - 40.0
        extraTimeRate = extraTime * 1.5 * rate
        grossPay = 40.0 * rate + extraTimeRate
    else:
        grossPay = hours * rate
    return grossPay


totalPay = computepay(float_hours, float_rate)
print('The Gross Pay Amount is:', "$"+str(round(totalPay, 2)))