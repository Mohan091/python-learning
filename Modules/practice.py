import random 
import string 


start_random_words = random.choices(string.ascii_letters, k=4)
end_random_words = random.choices(string.ascii_letters, k=4)

inpt = input("Enter the words: ")
new_inpt_encoding = inpt.split(" ")
coding = input("Enter the choice of 'coding' or 'decoding': ")
coding = True if coding == "coding" else False
if(coding):
    new_list = []
    for word in new_inpt_encoding:
        if(len(word) >=3):
            inpt_new = "".join(start_random_words) + word[1:] + word[0] +"".join(end_random_words)
            new_list.append(inpt_new)
        else:
            new_list.append(word[::-1])
    print(f'The encrypted message is: {" ".join(new_list)}')

else:
    new_list = []
    for word in new_inpt_encoding:
        if(len(word) >=3):
            inpt_new = word[4:-4]
            inpt_new = inpt_new[-1] + inpt_new[:-1]
            new_list.append(inpt_new)
        else:
            new_list.append(word[::-1])

    print(f'Decrypted message is: {" ".join(new_list)}')
