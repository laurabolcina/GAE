def calculate(no1, no2, operator):
    """Takes two numbers and an operator and executes operation."""
    no1 = float(no1)
    no2 = float(no2)
    result = eval("{0} {1} {2}".format(no1, operator, no2))
    return result