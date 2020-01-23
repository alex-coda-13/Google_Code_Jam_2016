###########
#   @Author: Alexandre Codaccioni
#   @Problem: Google Code Jam 2016 Qualification Round -  Problem C
#   @Python: 3.7.4
#   @Date: 23/01/2020
##########

# Generate all binaries, use convert and prime functions
def generate_binaries_convert_div(binary_string, final_binary_string, case, J, o_f):

    #### Convert into base and found divisors ####
    
    o_f.write('Case #' + str(case) + ':\n')
    # Number of jam coins found 
    count_J = 0

    # We test all combination until we reach 111..11
    while binary_string != final_binary_string:

        # We stop if we have found J jam coin
        if count_J >= J:
            return

        # We convert binary_string into base (2 to 10)
        # And we test if the number is prime
        one_is_prime = False

        # Prepare what we will store in the output
        to_write = binary_string + ' '

        # Convert into base
        for base in range(2, 11):
            number = convert_base(binary_string, base)

            # We create object containing non trivial divisor nt_div
            # Remain -1 if it is prime
            # Passed by reference
            nt_div = [-1]

            # If the number is prime, it is not a jam coin, try other one
            if is_prime(number, nt_div):
                one_is_prime = True
                break

            to_write += str(nt_div[0]) + ' '
        
        # If any of the number in bases were not prime then it is a jam coin
        # Add 1 to the number of jam coins founded
        if not one_is_prime:
            o_f.write(to_write + '\n')
            count_J += 1

        ######################################

        #### Creating binary combinations ####

        # First and last digit must remain 1
        idx_bin = 1
        # Loop into each binary string, from left to righ
        while idx_bin < (len(binary_string) - 1):
            # If we found a 0 we replace by 1 and exit while
            if binary_string[idx_bin] == '0':
                binary_string = binary_string[:idx_bin] + '1' + binary_string[idx_bin + 1:]
                # Break from while, we have found a new binary
                break
            # If we found 1 we replace by 0 and go next digit
            else:
                binary_string = binary_string[:idx_bin] + '0' + binary_string[idx_bin + 1:]
            idx_bin += 1

        ######################################

# Convert binary into number base
def convert_base(binary_string, base):

    number_int = 0
    # Convert from right to left, little endian
    index_binary = len(binary_string) - 1

    for bin_char in binary_string:
        # If digit is 1, add to number
        if bin_char == '1':
            # Using built-in pyhton3 for interger bit management (hardware space)
            number_int += int(pow(base, index_binary))
        index_binary -= 1
    
    return number_int

# Return number is prime and add divisor to object nt_div
def is_prime(number, nt_div):

    if (number <= 3) : 
        return True

    if number % 2 == 0:
        nt_div[0] = 2
        return False

    if number % 3 == 0:
        nt_div[0] = 3
        return False
    
    div = 5
    # We look at number in [O, sqrt(N)] only (cf. Math and prime numbers)
    while div * div <= number:

        # We stop execution early if we don't find any number divisor
        # Number must be prime and there is a lot jamcoin to test
        if div > 100000:
            # print("TIME OUT")
            return True

        if number % div == 0:
            nt_div[0] = div
            return False

        # we don't have to pair numbers since it's factor of 2
        div = div + 2

    return True

# Main function executed
def main():

    input_file = "C-small-practice.in.txt"

    try:
        # Test cases
        case = 0
        # Open input file
        with open(input_file, 'r') as i_f:
            # Open / Create output file
            with open('Output_' + input_file, 'w') as o_f:
                # Skipping first line since its the number of test case
                i_f.readline()
                for line in i_f:
                    # Test cases
                    case += 1

                    # Initialize N and J
                    split_line = line.split(' ')
                    N = int(split_line[0])
                    J = int(split_line[1])

                    # Create first and last binary with N bits
                    # 10000..1 and 1111...11
                    # Big endian reading but constructed from left to right
                    binary_string = '1' + '0' * (N-2) + '1'
                    final_binary_string = '1' * N

                    # Calling finction that generate all binaries, convert them and find divisor
                    generate_binaries_convert_div(binary_string, final_binary_string, case, J, o_f)


    except Exception as err:
        print(err)
        return str(err)


if __name__ == "__main__":
    main()
