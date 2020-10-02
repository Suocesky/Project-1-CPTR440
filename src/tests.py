from set_one import a_one, b_two, c_three, d_four, e_five, f_six, g_seven, h_eight
from set_two import i_nine, j_ten, k_eleven, l_twelve, m_thirteen, n_fourteen, o_fifteen, p_sixteen
from set_three import q_seventeen, r_eighteen, s_nineteen, t_twenty, u_twentyone, v_twentytwo, w_twentythree, x_twentyfour


#Problem Set 1 - Basics

def testQuestion1():
    input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    functionResult = a_one.hex_to_base64(input)
    answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    if functionResult == answer:
        print("Question 1 Passed")
    else:
        print("Qustion 1 Failed")
        print("Your Result: ", functionResult)
        print("Actual Answer: ", answer)
    

def testQuestion2():
    input1 = "1c0111001f010100061a024b53535009181c"
    input2 = "686974207468652062756c6c277320657965"
    functionResult = b_two.fixedXOR(input1, input2)
    answer = "746865206b696420646f6e277420706c6179"
    if functionResult == answer:
        print("Question 2 Passed")
    else:
        print("Qustion 2 Failed")
        print("Your Result: ", functionResult)
        print("Actual Answer: ", answer)

def testQuestion3():
    input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    functionResult = c_three.decode(input)
    print("Question 3 Printed: ", functionResult)

def testQuestion4():
    input = ''
    with open('set_one/d_four.txt', 'r') as file:
        input = file.read().replace('\n', '')
    functionResult = d_four.solution(input)
    print("Question 4 returned: ", functionResult)

def testQuestion5():
    #First part of question 5
    firstString = "Burning 'em, if you ain't quick and nimble"
    firstResult = e_five.solution(firstString)
    firstAnswer = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
    if firstResult == firstAnswer:
        print("Part 1 of Question 5 Passed")
    else:
        print("Qustion 5 Part 1 Failed")
        print("Your Result: ", firstResult)
        print("Actual Answer: ", firstAnswer)

    #Second part of question 5
    secondString = "I go crazy when I hear a cymbal"
    secondResult = e_five.solution(secondString)
    secondAnswer = "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    if secondResult == secondAnswer:
        print("Part 2 of Question 5 Passed")
    else:
        print("Qustion 5 Part 2 Failed")
        print("Your Result: ", secondResult)
        print("Actual Answer: ", secondAnswer)

def testQuestion6():
    input = ''
    with open('set_one/f_six.txt', 'r') as file:
        input = file.read().replace('\n', '')
    functionResult = f_six.solution(input)
    print("Question 6 Returns: ", functionResult)

def testQuestion7():
    input = ''
    with open('set_one/g_seven.txt', 'r') as file:
        input = file.read().replace('\n', '')
    functionResult = g_seven.solution(input)
    print("Question 7 Returns: ", functionResult)

def testQuestion8():
    input = ''
    with open('set_one/h_eight.txt', 'r') as file:
        input = file.read().replace('\n', '')
    functionResult = h_eight.solution(input)
    print("Question 8 Returns: ", functionResult)

#Problem Set 2 - Block and Crypto

def testQuestion9():
    input = "Hello"
    functionResult = i_nine.solution(input)
    print("Test Not Set Up")
    

def testQuestion10():
    input = "Hello"
    functionResult = j_ten.solution(input)
    print("Test Not Set Up")

def testQuestion11():
    input = "Hello"
    functionResult = k_eleven.solution(input)
    print("Test Not Set Up")

def testQuestion12():
    input = "Hello"
    functionResult = l_twelve.solution(input)
    print("Test Not Set Up")

def testQuestion13():
    input = "Hello"
    functionResult = m_thirteen.solution(input)
    print("Test Not Set Up")

def testQuestion14():
    input = "Hello"
    functionResult = n_fourteen.solution(input)
    print("Test Not Set Up")

def testQuestion15():
    input = "Hello"
    functionResult = o_fifteen.solution(input)
    print("Test Not Set Up")

def testQuestion16():
    input = "Hello"
    functionResult = p_sixteen.solution(input)
    print("Test Not Set Up")

#Problem Set 3 - Block & Stream Crypto

def testQuestion17():
    input = "Hello"
    functionResult = q_seventeen.solution(input)
    print("Test Not Set Up")
    

def testQuestion18():
    input = "Hello"
    functionResult = r_eighteen.solution(input)
    print("Test Not Set Up")

def testQuestion19():
    input = "Hello"
    functionResult = s_nineteen.solution(input)
    print("Test Not Set Up")

def testQuestion20():
    input = "Hello"
    functionResult = t_twenty.solution(input)
    print("Test Not Set Up")

def testQuestion21():
    input = "Hello"
    functionResult = u_twentyone.solution(input)
    print("Test Not Set Up")

def testQuestion22():
    input = "Hello"
    functionResult = v_twentytwo.solution(input)
    print("Test Not Set Up")

def testQuestion23():
    input = "Hello"
    functionResult = w_twentythree.solution(input)
    print("Test Not Set Up")

def testQuestion24():
    input = "Hello"
    functionResult = x_twentyfour.solution(input)
    print("Test Not Set Up")