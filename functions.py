def my_function(fname):
    print(fname + "references")
my_function ("email")
my_function ("tokens")
my_function ("linus")

def greet_username(name):
    print(f"hello {name}")

name=input('enter your name:')
greet_username(name)


def number_even_odd(num):
    if (num % 2) == 0:
        print('{0} is even'.format(num))
    else:
        print('{0} is odd'.format(num))


number_even_odd(5)