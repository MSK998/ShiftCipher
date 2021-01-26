import re


def count_occurrences():

    occurrences = dict()
    input_string = input("Please input the string you would like to count\n").lower()
    formatted = re.sub(r'\W+', '', input_string)

    for i in formatted:
        if i in occurrences.keys():
            occurrences[i] += 1
        else:
            occurrences[i] = 1

    for i in sorted(occurrences.keys()):
        print(i + "\t" + str(occurrences[i]))

    print(max(occurrences, key=occurrences.get))


def decode():

    print("Not Implemented Yet")


def shift_ascii(ascii_max, shift_value, char):
    if (ascii_max - ord(char)) <= shift_value:
        return chr(65 + (shift_value - (90 - ord(char))))
    elif (ascii_max - ord(char)) > shift_value:
        return chr(ord(char) + shift_value)


def encode_string(input_string, shift_value):
    origin_string = input_string
    encoded_string = ""

    for char in origin_string:
        if (ord(char) < 91) & (ord(char) > 64):
            encoded_string += shift_ascii(90, shift_value, char)

        elif (ord(char) < 123) & (ord(char) > 96):
            encoded_string += shift_ascii(122, shift_value, char)

        else:
            encoded_string += char

    print(encoded_string)


def encode():
    string_to_encode = input("Enter the string you want to encode\n")
    shift_value = int(input("What is the shift value of the cypher\n"))

    while shift_value > 25:
        shift_value = int(input("What is the shift value of the cypher\n"))

    encode_string(string_to_encode, shift_value)


def main():
    choice = int(input("Encode or Decode\n1. Encode\n2. Decode\n"))

    if choice == 1:
        encode()
    elif choice == 2:
        count_occurrences()


if __name__ == "__main__":
    main()