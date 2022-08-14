def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a == b:
        return (0)
    if  a > b:
        return a
    elif b > a:
        return b
    
    return a , b
print(main(3,4))
