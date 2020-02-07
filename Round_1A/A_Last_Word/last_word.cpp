/////////////
//  @Author: Alexandre Codaccioni
//  @Problem: Google Code Jam 2016 Round 1A - Problem A
//  @G++: 4.2.1
//  @Date: 07/02/2020
////////////

#include <iostream>
#include <fstream>
using namespace std;


//// Main Function ////

string process_last_word(string word);

int main() {

    string input_name = "A-large-practice.in.txt";
     
    // Open intput and output files
    ifstream i_file(input_name);
    ofstream o_file("Output-" + input_name);

    if (i_file.is_open() && o_file.is_open()) {

        string line;
        int test_case = 0;
        // Skip first line
        getline(i_file, line);
        // Read line by line
        while (getline(i_file, line)) {

            string word = line;
            string last_word = process_last_word(word);
            
            test_case++;
            o_file << "Case #"<< test_case << ": " << last_word << '\n';
        }

    i_file.close();
    o_file.close();
    return 0;

    } else {
        cerr << "Error open file" << endl; 
        return -1;
    }
}


//// Helper functions ////

// Function that takes a word and return the last_word needed
string process_last_word(string word) {

    // We first copy the input word into the output word
    string last_word = word;

    for(int idx_w = 1; idx_w < word.length(); idx_w++) {
        // If the letter is smaller than the first one, we simply add it at the end
        if (word[idx_w] < last_word[0]) {
            last_word[idx_w] = word[idx_w];
        } else {
            // If the letter is greater, we move each char to the next index
            for (int idx_lw = idx_w; idx_lw > 0; idx_lw--) {
                last_word[idx_lw] = last_word[idx_lw - 1];
            }
            // We add the letter in the first index
            last_word[0] = word[idx_w];
        }
    }
    return last_word;
}