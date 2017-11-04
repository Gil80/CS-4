#  Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
#  Write a program to prompt for a score between 0.0 and 1.0.
#  If the score is out of range, print an error message.
#  If the score is between 0.0 and 1.0,
#  print a grade using the following table:
#  Score   Grade
#  >= 0.9     A
#  >= 0.8     B
#  >= 0.7     C
#  >= 0.6     D
#  < 0.6      F


def computegrade(score):
    if score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            return 'A'
        elif score >= 0.8:
            return 'B'
        elif score >= 0.7:
            return 'C'
        elif score >= 0.6:
            return 'D'
        else:
            return 'F'
    else:
        return 'Please enter positive values within range 0.0 and 1.0'


input_score = input("Enter Score Between 0.0 and 1.0: ")
try:
    float_score = float(input_score)
except:
    print('bad score')
    exit()

print(computegrade(float_score))
