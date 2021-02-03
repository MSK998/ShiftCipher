import re


# Counts the occurences of each character in the string
def count_occurrences(encoded_string):

    # Creates a dictionary to record occurences
    occurrences = dict()
    # Sets the input string to input string
    input_string = encoded_string
    # Removes whitespace before counting
    formatted = re.sub(r'\W+', '', input_string)

    # Loops the string
    for i in formatted:
        # If the letter has already been counted at least once then add to count
        if i in occurrences.keys():
            occurrences[i] += 1
        # If not then add the count (This logic may be redundant)
        else:
            occurrences[i] = 1
            
    # Prints each letter in the dictionary
    for i in sorted(occurrences.keys()):
        print(i + "\t" + str(occurrences[i]))
     
    # Returns the most common character in ASCII format
    return ord(max(occurrences, key=occurrences.get))

# Shifts the ASCII to decode the character 
def decode_shift_ascii(ascii_min, shift_value, char):
    # If the difference between the character and the minimum ASCII value
    # is less than the shift then take the difference from the shift
    # and take away from the ASCII value of Z + 1
    if (ord(char) - ascii_min) < shift_value:
        return chr((ascii_min + 26) - (shift_value - (ord(char) - ascii_min)))
    # If the shift value will not spill over then take shift from character
    elif (ord(char) - ascii_min) >= shift_value:
        return chr((ord(char) - shift_value))

# Checks if the character is upper or lowercase and shifts it
def decode_iterator(char, shift):
    # If capital then use these values in the ASCII shift
    if (ord(char) < 91) & (ord(char) > 64):
        return decode_shift_ascii(65, shift, char)
    
    # If lowercase then use these values in the ASCII shift
    elif (ord(char) < 123) & (ord(char) > 96):
        return decode_shift_ascii(97, shift, char)

    # If the character is not a letter then just return the original value
    else:
        return char


# Decode method where all of the info about the string is gathered    
def decode():
    # Gets the encoded string, whether the shift is known and sets up an output string
    encoded_string = input("Please input the string you would like to decode\n")
    shift_known = int(input("Do you know the shift value?\n1. Yes\n2. No\n"))
    decoded_string = ""

    # If the shift value is known then ask for the value
    if shift_known == 1:
        shift = int(input("What is the shift value?"))

        # Pass each character through the decode methods
        for char in encoded_string:
            decoded_string += decode_iterator(char, shift)

    # If the shift is unknown        
    elif shift_known == 2:
        # Finds the most common char and subtracts the
        # ASCII value of 'E' to find the shift value
        common_char = count_occurrences(encoded_string.lower())
        shift = common_char - ord("e")
        print(abs(shift))

        # Pass each character through the decode methods
        for char in encoded_string:
            decoded_string += decode_iterator(char, shift)
            
    # If a valid choice is not picked then exit program
    else:
        print("Enter a valid choice")
        exit(0)

    # Print final result
    print(decoded_string)

# Shifts ASCII to encode the character
def encode_shift_ascii(ascii_max, shift_value, char):
    # If the shift value is greater than the max ASCII value
    if (ascii_max - ord(char)) <= shift_value:
        # Start back at 'A' with the remaining shift value
        return chr((ascii_max - 26) + (shift_value - (ascii_max - ord(char))))
    # If the value is less than the max ASCII
    elif (ascii_max - ord(char)) > shift_value:
        # Return the shifted character value
        return chr(ord(char) + shift_value)

# Iterates through the input string to construct the encoded string
def encode_string(input_string, shift_value):
    # Sets origin to the input string and sets an output string
    origin_string = input_string
    encoded_string = ""

    # Checks each character is upper or lower case
    for char in origin_string:
        # Shift using these values if upper case 
        if (ord(char) < 91) & (ord(char) > 64):
            encoded_string += encode_shift_ascii(91, shift_value, char)

        # shift using these values if lower case    
        elif (ord(char) < 123) & (ord(char) > 96):
            encoded_string += encode_shift_ascii(123, shift_value, char)

        # If the character is not a letter then skip
        else:
            encoded_string += char

    # Prints the encoded string
    print(encoded_string)


# Gathers the information required to create a cipher    
def encode():
    # Gets the cleartext and shift value from user
    string_to_encode = input("Enter the string you want to encode\n")
    shift_value = int(input("What is the shift value of the cypher\n"))

    # If the shift value is greater than 25 then ask again
    while shift_value > 25:
        shift_value = int(input("What is the shift value of the cypher\n"))
    
    # Passes information to encode the string to the encode methods
    encode_string(string_to_encode, shift_value)

# Start method determines which mode the user wants
def main():
    choice = int(input("Encode or Decode\n1. Encode\n2. Decode\n"))

    if choice == 1:
        encode()
    elif choice == 2:
        decode()
    else:
        print("Please pick a valid choice")
        exit(0)

# Calls the main method on program start
if __name__ == "__main__":
    main()
