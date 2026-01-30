This assignment works to implement Caesar and Vigenere Ciphers through Python.

Part1.py successfully takes a message in plaintext, then encrypts and decrypts the text using
the ASCII charcacter subset. I implemented either a shift or key to iterate through the selected range,
and covert the strings accordingly.

Part 2 of this assignment is found in the following files:
2.1 Simple Cracks by Hand
CSC348Assignment2_2 (2.2)
CSC348Assignment2_3 (2.3)
CSC348Assignment2_4 (2.4)
CSC348Assignment2_5 (2.5)

2.1 Simple Cracks by Hand: By-hand cracking of an encrypted string using Caesar cipher

CSC348Assignment2_2 (2.2): Calculates frequency analysis by analyzing the length of the message, then dividing the count of each symbol by the total message length.
I added a upper conversion in order to test my original message from Part 1.

CSC348Assignment2_3 (2.3): Correlation is found among sets 1 and 2, then sets 1 and 3 through normalization: means are calculated, then a numerator and "denominator" is 
established. The numerator is found by subtracting to find the distance of x and y from the average, deviations are calculated, then summed. For the denominator, the squared 
deviations of the means are found then summed together. Finally, the numerator is divided by the square roots of the x and y frequencies. Cross_correlations is then called 
to compute specific calculations between the sets.

CSC348Assignment2_4 (2.4): Previous frequency analysis is employed to create an expected list of frequencies. The highest correlation is stored and the corresponding shift location, 
I initialized it at -2 to have a higher calculation than the minimum. Every shift is tried for all 27 symbols. When the best shifted pattern with the highest correlation is found,
it's returned.

CSC348Assignment2_5 (2.5): This Vigenere Cipher builds on the previous functions and the act of columinizing ciphertext to create tables where the shift digit converts to a character based on
the key size. The key is generated through converting Caesar shifts into characters, then the key is used to decrypt the ciphertext into plaintext by reversing the Vigenere. While my code has
no run errors, I was unable to successfully find the correct key length to generate a key word to decrypt. I tested lengths 2 through 12 and I believe the error lies in my decryption function 
or the ability of my correalation function to properly work on large sets of texts.
