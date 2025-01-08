# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.


def fizz_buzz(number):
    """Returns Fizz if number is divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both 3 and 5.
    If not divisible by either 3 or 5, returns the number itself.
    >>> fizz_buzz(3)
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(15)
    'FizzBuzz'
    """

    if (number % 3 == 0) & (number % 5 == 0):
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'

    return


# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.


def sum_of_squares(numbers):
    """Returns the sum of the squares of all the numbers in a list.
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([2, 4, 6])
    56
    """

    sum_of_squares = 0
    for each in numbers:
        squared  = each ** 2
        sum_of_squares += squared
    return sum_of_squares




# Question 3

# Write a function that counts the number of vowels in a string.


def count_vowels(string):
    """Returns the number of vowels in a string.
    >>> count_vowels("hello")
    2
    >>> count_vowels("aeiou")
    5
    """
    vowels_list = 'aeiou'
    vowels_count = 0
    for each in string:
        if each in vowels_list:
            vowels_count += 1
    
    return vowels_count


# Question 4

# Write a function that counts the number of repeated characters in a string.


def count_repeats(string):
    """Returns the number of repeated characters in a string.
    >>> count_repeats("hello")
    2
    >>> count_repeats("aeiou")
    0
    """
    """
    Thomas Tay Note:
    The test example above did not consider multiple repeated characters such as "heello"
    Will interpret the requirement as below:
    - Count repeated characters for each character.
    - If a character is repeated more than once, count as 1.
    - Store all chracters and its count in a dictionary.
    - Will return the count of the character that is repeated the most.
    """
    repeated_dic = {}
    most_repeated_count = 0
    # Count each chracter and store the counts in a dictionary
    for each_character in string:
        if each_character in repeated_dic:
            repeated_dic[each_character] += 1
        else:
            repeated_dic[each_character] = 1

    # Find the character count that is repeated the most
    for key,value in repeated_dic.items():
        if value > 1:
            if value > most_repeated_count:
                most_repeated_count = value 

    return most_repeated_count



if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
