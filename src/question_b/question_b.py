'''
For some reson this environment behaves differenlty and wants some comments at top of each folde
'''

#write functions here, don't add input('') statements here!

def get_day_of_week(day):

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    if 1 <= day <= 7:
        return days[day - 1]
    else:
        return "Invalid number. Please enter a number in the range of 1 through 7."