import random


def get_string_input(inputs):
    u_input = input(inputs)
    return u_input
    # return input from user as a string


def random_number(min_value, max_value):
    return random.randint(min_value, max_value)


def get_random_number(num_1, num_2):
    random_int = random_number(num_1, num_2)
    return random_int