def anagram_checker(words_a, words_b, is_case_sensitive):
    # Modify your existing code here
    result = []
    for w_a in words_a: #get 1 word from words_a
        if (not is_case_sensitive): #if case sensitive FALSE change the words to lower case
            w_a=w_a.lower()
        
        for w_b in words_b: #get 1 work from words_b
            anagram = True
            if (not is_case_sensitive): #if case sensitive FALSE change the words to lower case
                w_b=w_b.lower()
            
            for c in w_a: #compare the characters to check if anagram
                if c not in w_b:
                    anagram = False
                    break
            
            result.append(anagram) #save if anagram or not

    #reference: True + True = 2 / True + False = 1 / False + False = 0
    if (result[0] + result[1] > 0) and (result[2] + result[3] > 0):
        return True
    else:
        return False


print ("a", anagram_checker(["Slient", "night"], ["thing", "listen"], False) ) # True

print ("b", anagram_checker(["Slient", "thing"], ["night", "slient"], True)) # False