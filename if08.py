from multiprocessing.connection import answer_challenge


def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    
    if number==1:
        print('Monday')

    if number==2:
        print('Tuesday')

    if number==3:
        print('Wednesday')

    if number==4:
        print('Thursday')
    
    if number==5:
        print('Friday')
    
    if number==6:
        print('Saturday')
    
    if number==7:
        print('Sunday')
        
    
    
print(main(4))
