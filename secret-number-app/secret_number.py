def secret_n_guess(n):
    number = 275
    if n == "":
        return 0
    n = int(n)
    if n == number:
        return 1
    elif n >= 300:
        return 2
    elif (n >= 277 and n <= 299) or (n >= 251 and n <= 273):
        return 3
    elif n == 274 or n == 276:
        return 4
    elif n <= 250:
        return 5