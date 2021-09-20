import random
import validators


def generate_short():
    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    short = "".join(random.choices(char_set, k=10))
    return short


def check_url(url):
    return validators.url(url)
