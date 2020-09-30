import base64
# Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.
# If your function works properly, then when you feed it the string:
# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:
# 686974207468652062756c6c277320657965
# ... should produce:
# 746865206b696420646f6e277420706c6179

def fixedXOR(input1, input2):
    #Solution:
    hex_string1 = bytes.fromhex(input1)
    hex_string2 = bytes.fromhex(input2)

    #XOR byte strings and place in result_byte_array, the convert back to hex
    result_byte_array = bytearray(len(hex_string1))
    for i in range(len(result_byte_array)):
        result_byte_array[i] = hex_string1[i] ^ hex_string2[i]
    print("Easter Egg: XORed bytes of two hex strings are ", bytes(result_byte_array))
    return result_byte_array.hex()
