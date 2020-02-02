/////////////
//  @Author: Alexandre Codaccioni
//  @Problem: Google Code Jam 2016 Qualification Round - Problem B
//  @G++: 4.2.1
//  @Date: 27/01/2020
////////////


#include <iostream>
#include <fstream>

using namespace std;


int get_index_grouped(string pattern);
string flip_at_index(string pattern, int index);
bool verify_pattern(string pattern);
int resolve_flip(string pattern);

//// Main Function ////


// Method explanantion :
// Consider a pattern made of '+' and '-', the idea is to take the first same elements (either '+' and '-') and flip them
// Repeat this operation until we have a pattern like +++...+

// Ex: ++--+- => take '++', since we have to flip all the first elements, we have ----+-
// We repeat this operation by taking '----' and we flip them, we have +++++-
// And again, we take +++++, flip them, we have ------
// We finally take ------ and we have ++++++

int main() {

    // Input file name
    string input_name = "B-large-practice.in.txt";
     
    // Open intput and output files
    ifstream i_file(input_name);
    ofstream o_file("Output_" + input_name);

    if (i_file.is_open() && o_file.is_open()) {

        string line;
        int test_case = 0;
        // Skip first line
        getline(i_file, line);
        // Read line by line
        while (getline(i_file, line)) {
            int nb_flip = 0;
            nb_flip = resolve_flip(line);
            test_case++;
            o_file << "Case #"<< test_case << ": " << nb_flip << '\n';
        }

    i_file.close();
    o_file.close();
    return 0;

    } else {
        cerr << "Error open input file" << endl; 
        return -1;
    }

}


//// Helper functions ////

// Function that flips the top elements of the stack from an index
string flip_at_index(string pattern, int index) {
    while (index >= 0) {
        if (pattern[index] == '+') {
            pattern[index] = '-';
        } else {
            pattern[index] = '+';
        }
        index--;
    }
    return pattern;
}

// Function that gets the index of the last similar elements in the the string
int get_index_grouped(string pattern) {

    // Get the index of last item with same pattern (e.g. --- or ++ )
    int last_index = pattern.length();
    int index_last_grouped;
    for(index_last_grouped = 0; index_last_grouped < last_index; index_last_grouped++) {
        if (index_last_grouped != last_index -1 && pattern[index_last_grouped] != pattern[index_last_grouped + 1]) {
            break;
        }
    }
    return index_last_grouped;
}

// Function that defines the stop condition when the string is +++..++
bool verify_pattern(string pattern) {

    for (int idx_pat = 0; idx_pat < pattern.length(); idx_pat++) {
        if (pattern[idx_pat] != '+') {
            return false;
        }
    }
    return true;
}

// Function taht executes the flips until we reach the stop condition and return the number of flip
int resolve_flip(string pattern) {

    int nb_flip = 0;
    while (verify_pattern(pattern) == false) {
        int index_grouped = get_index_grouped(pattern);
        pattern = flip_at_index(pattern, index_grouped);
        nb_flip ++;
    }
    return nb_flip;
}