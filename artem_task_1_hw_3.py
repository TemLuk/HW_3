year_of_birth = input("What year were you born?:")
if year_of_birth != int(year_of_birth):
    year_of_birth = int(input("Please, write your birth in numbers:"))
    if year_of_birth == 2001:
        print('You should visit Holland.')
    elif 2001 > year_of_birth:
        print('You should visit Vietnam.')
    else:
        print("Travel everywhere!")
