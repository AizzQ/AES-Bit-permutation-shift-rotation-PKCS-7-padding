from Crypto.Cipher import AES


def decrypt_aes(decrypt_aes, key, iv):
    """
>>> key = bytes([57, 226, 240, 61, 125, 240, 75, 68, 22, 35, 124, 205, 144, 27, 118, 220])
>>> iv = bytes([241, 147, 66, 129, 194, 34, 37, 51, 236, 69, 188, 205, 64, 140, 244, 204])
>>> decrypt_aes(bytes([255, 18, 67, 115, 172, 117, 242, 233, 246, 69, 81, 156, 52, 154, 123, 171]),key,iv)
b'hello world 1234'
>>> decrypt_aes(bytes([171, 218, 160, 96, 193, 134, 73, 81, 221, 149, 19, 180, 31, 247, 106, 64]),key,iv)
b'lovecryptography'
    """

    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = cipher.decrypt(decrypt_aes)
    return pt


def bit_permutation(input1, my_order):
    """
>>> bit_permutation("101",[1,2,3])
'101'
>>> bit_permutation("101",[3,2,1])
'101'
>>> bit_permutation("101",[1,3,2])
'110'
>>> bit_permutation("101",[3,2,1])
'101'
>>> bit_permutation("1010",[3,4,1,2])
'1010'
>>> bit_permutation("1010",[1,3,2,4])
'1100'
>>> bit_permutation("11110000",[5,6,7,8,1,2,3,4])
'00001111'
>>> bit_permutation("0001001100110100010101110111100110011011101111001101111111110001",[57,49, 41,33, 25, 17, 9,1,58, 50,42, 34, 26,18,10, 2, 59,51, 43, 35,27,19,11,  3,60, 52, 44,36,63,55, 47,39, 31, 23,15,7,62, 54,46, 38, 30,22,14, 6, 61,53, 45, 37,29,21,13,  5,28, 20, 12, 4])
'11110000110011001010101011110101010101100110011110001111'
    """
    ret0 = []
    output1 = []
    for i in input1:
        output1.append(i)
    for i in my_order:
        ret0.append(i - 1)
    mylist = output1
    mylist = [mylist[i] for i in ret0]
    xx = "".join(mylist)
    x1 = f'{xx}'
    return x1


def left_shift_rot(x, y=None):
    """

>>> left_shift_rot('010')
'100'
>>> left_shift_rot('111')
'111'
>>> left_shift_rot('1010111001')
'0101110011'
>>> left_shift_rot('0101110011')
'1011100110'
>>> left_shift_rot('1010111001',2)
'1011100110'
>>> left_shift_rot('0001',3)
'1000'
    """
    if y is None:
        SS = x[1:] + x[0: 1]
        return SS
    if y != 0:
        SS1 = x[y:] + x[0: y]
        return SS1


def PKCS7_pad(message, block_S):
    """
>>> PKCS7_pad('hello',6)
'hello\\x01'
>>> PKCS7_pad('hello',7)
'hello\\x02\\x02'
>>> PKCS7_pad('hello, how are you?',26)
'hello, how are you?\\x07\\x07\\x07\\x07\\x07\\x07\\x07'
>>> PKCS7_pad('hello, how are you?',55)
'hello, how are you?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
>>> PKCS7_pad('hello, how are you?',67)
'hello, how are you?000000000000000000000000000000000000000000000000'

    """
    message = message.encode("utf-8")
    padding_length = block_S - (len(message) % block_S)
    if padding_length == 0:
        padding_length = block_S
    padding = bytes([padding_length]) * padding_length
    a = message + padding
    a = a.decode("utf-8")
    return a
