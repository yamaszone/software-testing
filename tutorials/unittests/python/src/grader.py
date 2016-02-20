
def calculate(grade):
    if grade > 90:
        return 'A'
    elif 80 < grade <= 90:
        return 'B'
    elif 70 < grade <= 80:
        return 'C'
    else:
        return 'F'