# Password Genarator
#
# 5/15/2021
# @author Jack Hangen
# Incomplete
# given certain inputs will create a password around those parameters

# import statments
import random

running_string = ""
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters = ['a','b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [1,2,3,4,5,6,7,8,9,0]
sped_char = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '=']

def cap_qu():
    cap_letters = input("Does it need to have a captial letter (y/n): ")
    if (cap_letters == 'y'):
        return True
    elif (cap_letters == 'n'):
        return False
    else:
        print("please enter 'y' or 'n'")
        cap_qu()

def lett_qu():
    lett = int(input("How many letters: "))
    if (lett > len(letters)):
        print(f"That number is to high, enter one under {len(letters)}")
        lett_qu()
    else:
        return lett

def nums_qu():
    nums = int(input("How many numbers: "))
    if (nums > len(numbers)):
        print(f"That number is to high, enter one under {len(numbers)}")
        nums_qu()
    else:
        return nums

def char_qu():
    char = int(input("How many special characters : "))
    if (char > len(sped_char)):
        print(f"That number is to high, enter one under {len(sped_char)}")
        char_qu()
    else:
        return char


cap_letters = cap_qu()
lett = lett_qu()
nums = nums_qu()
char = char_qu()

if (cap_letters == True):
    place = random.randrange(0, len(sped_char) - 1, 1)
    running_string = (f"{upper_letters[place]}")

for i in range(lett):
    place = random.randrange(0, len(letters) - 1, 1)
    running_string = (f"{running_string}{letters[place]}")
    letters.remove(letters[place])

for i in range(nums):
    place = random.randrange(0, len(numbers) - 1, 1)
    running_string = (f"{running_string}{numbers[place]}")
    numbers.remove(numbers[place])

for i in range(char):
    place = random.randrange(0, len(sped_char) - 1, 1)
    running_string = (f"{running_string}{sped_char[place]}")
    sped_char.remove(sped_char[place])

print(f"Your password is: {running_string}")