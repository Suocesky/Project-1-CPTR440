import a_one, b_two, c_three, d_four, e_five, f_six, g_seven, h_eight
import i_nine, j_ten, k_eleven, l_twelve, m_thirteen, n_fourteen, o_fifteen, p_sixteen
import q_seventeen, r_eighteen, s_nineteen, t_twenty, u_twentyone, v_twentytwo, w_twentythree, x_twentyfour


#Problem Set 1 - Basics

def testQuestion1():
    input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    functionResult = a_one.hexToBase64(input)
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
        print("Question 1 Passed")
    else:
        print("Qustion 2 Failed")
        print("Your Result: ", functionResult)
        print("Actual Answer: ", answer)

def testQuestion3():
    input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    functionResult = c_three.decode(input)
    print("Question 3 Printed: ", functionResult)

def testQuestion4():
    input = "Hello"
    functionResult = d_four.solution(input)
    print("Test Not Set Up")
def testQuestion5():
    input = "Hello"
    functionResult = e_five.solution(input)
    print("Test Not Set Up")

def testQuestion6():
    input = "Hello"
    functionResult = f_six.solution(input)
    print("Test Not Set Up")

def testQuestion7():
    input = "Hello"
    functionResult = g_seven.solution(input)
    print("Test Not Set Up")

def testQuestion8():
    input = "Hello"
    functionResult = h_eight.solution(input)
    print("Test Not Set Up")

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