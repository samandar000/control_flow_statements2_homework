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
    elif a==b or a==c:
        return (a or b or c) 
    
    if b > a and b < c:
        return b
    if b < a and b > c:
        return b
    elif b==a or b==c:
        return (b or a or c)
    
    
    if c > b and c < a:
        return c
    if c < b and c > a:
        return c
    elif c==a or c==b:
        return (c or a or b)

    return a ,b, c
print(main(6,5,5))