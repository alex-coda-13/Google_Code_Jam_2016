###########
#   @Author: Alexandre Codaccioni
#   @Problem: Google Code Jam 2016 Qualification Round - Problem A
#   @Python: 3.7.4
#   @Date: 01/02/2020
##########

# Main function executed
def main():

    # Read input file
    input_file = "A-small-practice.in.txt"

    try : 
        with open(input_file, 'r') as i_f:
            with open("Output-" + input_file, 'w') as o_f: 
                # Skipping first line
                i_f.readline()
                case = 1
                for line in i_f:
                    # Get input number
                    N = int(line)

                    if N == 0:
                        o_f.write("Case #" + str(case) + ": INSOMNIA\n")
                    
                    else:                
                        # Variable definitions
                        mult = 1
                        tracker = []

                        # Counting process returning the last number seen
                        last_number = process_counting_and_tracking(N, mult, tracker)
                        o_f.write("Case #" + str(case) + ": "  + str(last_number)+ "\n")

                    case += 1

    except Exception as err :
        print(err)
        return str(err)

# Recursive function that multiplies N and keeps track of numbers
def process_counting_and_tracking(N, mult, tracker):

    # Multiplying N with mult
    M = mult * N
    # Converting M into string
    M = str(M)

    # Looking into each char number of M
    for char_num in M:
        
        if char_num not in tracker:
            # Keep tracks of numbers
            tracker.append(char_num)

    # Stop execution when we have the 10 numbers
    if len(tracker) == 10:
        return M

    # Recursive call with mult + 1 and tracker wich is an object, passed by reference (don't forget to return it)
    return process_counting_and_tracking(N, mult+1, tracker)
    
# Main() execution
if __name__ == "__main__":
    main()