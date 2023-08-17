def stringer(input_list):
    if not input_list:
        return 'List is empty!'
    new_string=''
    try:
        for i in range(0,len(input_list)-1):
            new_string += str(input_list[0]) + ', '
        new_string += 'and ' + str(input_list[-1])
    except TypeError:
        print("kurwa coś nie ten")
    except IndexError:
        print("coś tam przejebałeś")
    return new_string

spam = ['apples', 'bananas', 'tofu', 'cats']
empty = []

print(stringer(spam))
print(stringer(empty))
