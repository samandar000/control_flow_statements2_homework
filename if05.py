def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1=n%10
    x2=n%100//10
    x3=n%1000//100
    x4=n%10000//1000
    x5=n%100000//10000
    if x1 > x2 and x1 > x3 and x1 >x4 and x1 > x5:
        return x1
    if x2 > x1:
        return x2
    if x3 > x1:
        return x3
    if x4 > x1:
        return x4
    if x5 > x1:
        return x5
    if x1==x2 or x3 or x4 or x5:
        return x1
    
print(main(14234))
    