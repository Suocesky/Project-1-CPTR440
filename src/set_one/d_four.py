# Detect single-character XOR
# One of the 60-character strings in this file has been encrypted by single-character XOR.
# Find it.

# (Your code from #3 should help.)    
# return input

def solution(input):
    #Solution
    #The text file is called four.txt. The test file is reading it and putting it as input to this string so you shouldn't need to worry about it.

    #convert input to bytes (hex encoded like previous ones?), break into 60 character strings
    hex_string_in_bytes = bytes.fromhex(input)

    high_score = 0
    high_score_message = ''
    #I copied these character frequencies from http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html 
    #I couldn't find out why this didn't work for awhile, but eventually I realized it was because messages had spaces,
    #So I added a space and %10 seemed to work.
    character_frequencies = {
        'a': 8.12, 'b': 1.49, 'c': 2.71, 'd': 4.32,
        'e': 12.02, 'f': 2.30, 'g': 2.03, 'h': 5.92,
        'i': 7.31, 'j': 0.10, 'k': 0.69, 'l': 3.98,
        'm': 2.61, 'n': 6.95, 'o': 7.68, 'p': 1.82,
        'q': 0.11, 'r': 6.02, 's': 6.28, 't': 9.10,
        'u': 2.88, 'v': 1.11, 'w': 2.09, 'x': 0.17,
        'y': 2.11, 'z': 0.07, ' ': 10
    }

    
    start = 0
    for end in range (30, len(hex_string_in_bytes)):
        #Loop through all decimal 256 ascii charactersv
        for character in range(256):
            current_message = bytes()
            #XOR the decimal ascii character representation with every byte in range
            for byte in range(start, end):
                current_message += bytes([hex_string_in_bytes[byte] ^ character])

            #add the value of each character according to the character frequencies to the current score
            current_score = 0
            for byte in current_message:
                if chr(byte) in character_frequencies:
                    current_score += character_frequencies[chr(byte)]

            #Update message if current score is higher that highscore
            if current_score > high_score:
                high_score = current_score
                high_score_message = current_message
        start = start +1           

    return high_score_message.decode('ascii')