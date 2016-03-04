def secret_n_guess(n):
    number = 275
    n = int(n)
    if n < number:
        return "Your guess is too low. Try again."
    elif n > number:
        return "Your guess is too high. Try again."
    else:
        return "Congratulations, you guessed the secret number!"