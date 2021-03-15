from time import sleep

def fizzbuzz(elements):
    if type(elements) != int: raise ValueError
    fizzbuzz = []
    for i in range(1,elements+1):
        if i%15 == 0:
            fizzbuzz.append('FizzBuzz')
        elif i%3 == 0:
            fizzbuzz.append('Fizz')
        elif i%5 == 0:
            fizzbuzz.append('Buzz')
        else:
            fizzbuzz.append(i)
    return fizzbuzz

def colorprint(fizzbuzz_item):
    if fizzbuzz_item in ['Fizz','Buzz','FizzBuzz']:
        print(fizzbuzz_item)
    else:
        print(fizzbuzz_item)

if __name__ == '__main__':
    while True:
        print("Welcome to FizzBuzz. Choose how many elements do you want:")
        try:
            elements = int(input())
            if elements <=0: raise ValueError
        except:
            print(f"You must inform a positive number!\n")
            continue
        break
    for i in range (4):  
        msg = f"Generating {elements} elements of FizzBuzz" + "." * i
        print ('\r' + msg, end='')
        sleep(1)
    print(" Done!")
    
    for item in fizzbuzz(elements):
        isfizzbuzz = item in ['Fizz','Buzz','FizzBuzz']
        print(item + ' (*)' if isfizzbuzz else item)
        sleep(.1)