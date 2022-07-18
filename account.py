def display():
    name = str(input('Enter your name : '))
    year = int(input('Which year you were born ? '))

    age = 2022 - year
    
    text = 'Hi, {} your age is {}'.format(name, age)

    print(text)

display()