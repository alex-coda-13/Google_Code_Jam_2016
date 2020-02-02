###########
#   @Author: Alexandre Codaccioni
#   @Problem: Google Code Jam 2016 Qualification Round - Problem C
#   @Python: 3.7.4
#   @Date: 23/01/2020
##########

# Generate all binaries, use convert and prime functions
def generate_binaries_convert_div(binary_string, final_binary_string, case, J, o_f):

    #### Convert in bases and found divisors ####
    
    o_f.write('Case #' + str(case) + ':\n')
    # Number of jam coins found 
    count_J = 0

    # We test all combinations until we reach 111..11
    while binary_string != final_binary_string:

        # We stop if we have J jam coin
        if count_J >= J:
            return

        # We convert binary_string in bases (2 to 10)
        # We test if the number is prime
        one_is_prime = False

        # Prepare file output
        to_write = binary_string + ' '

        # Convert in base
        for base in range(2, 11):
            number = convert_base(binary_string, base)

            # We create object non trivial divisor nt_div, length 1
            # Remains -1 if it is prime
            # Passed by reference
            nt_div = [-1]

            # If the number is prime, it is not a jam coin, try an other one
            if is_prime(number, nt_div):
                one_is_prime = True
                break

            to_write += str(nt_div[0]) + ' '
        
        # If any of the number in bases were not prime then it is a jam coin
        # Add 1 to the number of jam coins stored
        if not one_is_prime:
            o_f.write(to_write + '\n')
            count_J += 1

        ######################################

        #### Creating binary combinations ####

        # First and last digit must remain 1
        idx_bin = 1
        # Loop into each binary string, from left to righ
        while idx_bin < (len(binary_string) - 1):
            # If we find a 0, we replace by 1 and exit "while"
            if binary_string[idx_bin] == '0':
                binary_string = binary_string[:idx_bin] + '1' + binary_string[idx_bin + 1:]
                # Break from "while", we have a new binary
                break
            # If we have 1 we replace by 0 and go to next digit
            else:
                binary_string = binary_string[:idx_bin] + '0' + binary_string[idx_bin + 1:]
            idx_bin += 1

        ######################################

# Convert binary in base
def convert_base(binary_string, base):

    number_int = 0
    # Convert from right to left, Big endian
    index_binary = len(binary_string) - 1

    for bin_char in binary_string:
        # If digit is 1, add to number
        if bin_char == '1':
            # Using built-in pyhton3 pow for interger bit management (hardware space)
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
    # We only look at number in [O, sqrt(N)] (cf. Math and prime numbers)
    while div * div <= number:

        # We stop execution if we don't find any number divisor before 100000
        # This number is probably prime and there is a lot of jam coin to test
        if div > 100000:
            # print("TIME OUT")
            return True

        if number % div == 0:
            nt_div[0] = div
            return False

        # We don't have to test pair numbers since they are factor of 2
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

                    # Calling function that generate all binaries, convert them and find divisor
                    generate_binaries_convert_div(binary_string, final_binary_string, case, J, o_f)


    except Exception as err:
        print(err)
        return str(err)


if __name__ == "__main__":
    main()
