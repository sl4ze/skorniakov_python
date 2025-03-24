
def run():
    while True:
        print('enter a number or name, ctrl+c to exit')
        var = input()
        try: 
            numeric_var = int(var)
            if numeric_var > 7:
                print('Hello')
        except:
            
            if var == 'John':
                print('Hello, John')
            else:
                print('There is no such name')
        print('enter a numeric array, numbers are separated by space only')
        
        mltpls3 = []
        while True:
            numlist = input().split()
            try:
                for number in set((numlist)):
                    number = float(number)
                    if number % 3 == 0:
                        mltpls3.append(number)
                print('ay elements that are multiples of 3 : ', mltpls3)
                break
            except Exception as e:
                print('Wrong input: ', e)





if __name__ == '__main__':
    run()