import base64
import binascii
# The string:
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Should produce:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
# So go ahead and make that happen. You'll need to use this code for the rest of the exercises.
#
# Cryptopals Rule
# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

def hex_to_base64(input):
    # Do Calculations and return answer
    # Solution Here:

    #Convert Hex to bytes as it says in directions
    hex_string_in_bytes = bytes.fromhex(input)
    print("Easter Egg after converting hex to bytes: ", hex_string_in_bytes)

    #Convert the Hex Byte String to a base64 byte string
    base64_byte_string = base64.b64encode(hex_string_in_bytes)

    #Convert the base64 byte string to base64 binary  ascii characters
    base64_ascii_characters = binascii.b2a_base64(base64_byte_string)

    # Decode the base64 byte string
    decoded_base64_characters = base64.b64decode(base64_ascii_characters)

    #Convert decoded_base64_characters to utf-8 string and return
    return decoded_base64_characters.decode('utf-8')
    