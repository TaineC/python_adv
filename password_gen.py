from pip._vendor.colorama import Fore
import random
import string

pw_length = input('Enter Password Length: ')
pw_length = int(pw_length)

def pw_gen(chars = string.ascii_letters+string.digits+string.punctuation):
    return ''.join([random.choice(chars) for n in range(pw_length)])
    
result = pw_gen()
print(Fore.LIGHTMAGENTA_EX + result)
