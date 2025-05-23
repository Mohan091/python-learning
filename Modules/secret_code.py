# # secret code language 
# encoding rule : 
# 1. if a word contain atleast 3 characters , remove the first letter  and append it at the end 
# 2. now append 4 randon characters at the start and the end of the word 
# 3. else 
# 4. simply reverse the string 

# Decoding rule: 
# 1. if the word contain 3 letters reverse it
# 2. else 
# 3. remove 3 random character from start and end. now remove the last letter and append it to the beginning

import random 
import string

word_msg_encode = input("Enter the word to be encoded: ")

def word_encoding(word_msg_encode):
    start_random_characters = random.choices(string.ascii_letters, k=4)
    end_random_characters = random.choices(string.ascii_letters, k=4)
    print("Message encoding started")
    if len(word_msg_encode) > 3:
        encode_rule_1 = word_msg_encode[1:] + word_msg_encode[0]
        encode_rule_2 = ''.join(start_random_characters) + encode_rule_1 + ''.join(end_random_characters)
        print(f"encoded message is: {encode_rule_2}")
    else:
        print("Message encoding started")
        encode_rule_2 = word_msg_encode[::-1]
        print(f"encoded message is: {encode_rule_2}")   
    print("Message encoding completed") 
    return encode_rule_2


def word_decoding(encode_rule_2):
    print("Message decoding started")
    if len(word_msg_encode) > 3:
        decode_rule_1 = encode_rule_2[4:-4] 
        decode_rule_2 = decode_rule_1[-1] + decode_rule_1[:-1] 
        print(f"Decoded message is: {decode_rule_2}")        
    else:
        decode_rule_3 = word_msg_encode[::-1]
        print(f"Decoded message is: {decode_rule_3}")
    print("Message decoded successfully")


encoded_msg = word_encoding(word_msg_encode)
word_decoding(encoded_msg)  
