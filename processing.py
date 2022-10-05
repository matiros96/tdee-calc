'''
Mifflin St Jeor forumula for calculating RDEE
Men:   (10 * W) + (6.25 * H ) - (5 * A) + 5
Women: (10 * W) + (6.25 * H ) - (5 * A) - 161
Variables: W=weight in kilograms, H=height in centimeters, A=age in years

https://www.sailrabbit.com/bmr/
'''

def do_calculation(weight, height, age, gender, algo):
    if gender == 'male':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        return bmr
    elif gender == 'female':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        return bmr