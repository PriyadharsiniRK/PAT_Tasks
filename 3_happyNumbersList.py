def happyNumber_Check(n):
    happyNumbersSet = set()

    while n != 1 and n not in happyNumbersSet:
        happyNumbersSet.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))

    return n == 1

def find_happyNumbers(numbers):
    happyNumbersList = []
    for num in numbers:
        if happyNumber_Check(num):
            happyNumbersList.append(num)
    return happyNumbersList

# Example usage
if __name__ == "__main__":
    # Replace this list with your input of numbers
    number_list = [10,501,22,37,100,999,87,351]

    happy_numbers = find_happyNumbers(number_list)
    print("Happy Numbers in the given List: ",happy_numbers)