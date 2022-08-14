def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a > b and a < c:
        return a
    if a < b and a > c:
        return a
    
    if b > a and b < c:
        return b
    if b < a and b > c:
        return b
    
    if c > b and c < a:
        return c
    if c < b and c > a:
        return c
    return a ,b, c
print(main(6,5,4))