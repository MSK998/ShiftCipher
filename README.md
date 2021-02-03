# ShiftCipher
A small console app that will encode and decode shift ciphers

## Usage
There are two modes that can be entered, encode and decode. Each one speaks for itself, encode will ask for a string to be entered and the shift value that you want. Decode will ask for the encoded string, it will then ask if you know the shift value. If you know the shift value then it will decode using the value that is supplied. However, if you don't know the shift value, a simple and basic form of frequency analysis will be conducted. Once the analysis has completed it will use the shift value that it believes is correct, it is important to note that this is not always going to be accurate. 

### Frequency Analysis
The frequency analysis is extremely simple and this technique has only been tested with english. In the english language the most common letter that is usually found in sentences is 'E'. After counting every letter in the sentence the frequency analysis will find the most common letter in the encoded text and will assume that it is the letter 'E'. The frequency analysis will then work out the difference between the most counted character and 'E', this difference is now the shift value that is going to get used in decoding.
