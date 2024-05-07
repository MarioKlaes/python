def anagram_checker(words_a, words_b, is_case_sensitive):
    # Modify your existing code here
    l_w_a = []
    l_w_b = []

    #take 1 work from each WORDS
    if len(words_a) > 0:
        w_a = words_a[0]
        l_w_a = list(w_a)
        del words_a[0]
        print (words_a, words_b, is_case_sensitive)
        anagram_checker(words_a, words_b, is_case_sensitive)
    else:
        return
    
    if len(words_b) > 0:
        w_b = words_b[0]
        l_w_b = list(w_b)
        del words_b[0]
        print (words_a, words_b, is_case_sensitive)
        anagram_checker(words_a, words_b, is_case_sensitive)
    else:
        return
    
    l_w_a.sort()
    l_w_b.sort()
    print (l_w_a,"---",l_w_b)
    return


print ("a", anagram_checker(["Slient", "night"], ["thing", "listen"], False) ) # True

# print ("b", anagram_checker(["Slient", "thing"], ["night", "slient"], True)) # False