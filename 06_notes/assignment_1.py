# This is a function, which we will learn more about next week. For testing purposes, we will write our code in the function
def anagram_checker(word_a, word_b):

  if 'str' not in str(type(word_a)):
    print('strings A is NOT valid')
    return
  elif 'str' not in str(type(word_b)):
    print('string B is NOT valid.')
    return
  else:
    temp_a = word_a.lower() #eliminate upper case
    list_a = list(temp_a) #make a list of characters
    list_a.sort() #sort the list
    temp_a = "" #clear the orignal string
    temp_a.join(list_a) #create a new string with the same characters ordered

    temp_b = word_b.lower() #eliminate upper case
    list_b = list(temp_b) #make a list of characters
    list_b.sort() #sort the list
    temp_b = "" #clear the orignal string
    temp_b.join(list_b) #create a new string with the same characters ordered

    print("Result:", temp_a in temp_b)

def anagram_checker2(word_a, word_b):

  if 'str' not in str(type(word_a)):
    print('strings A is NOT valid')
    return
  elif 'str' not in str(type(word_b)):
    print('string B is NOT valid.')
    return
  else:
    temp_a = word_a.lower() #eliminate upper case
    temp_b = word_b.lower() #eliminate upper case

    for c in temp_a:
        if c not in temp_b:
          print("Not an anagram")
          return
    
    print("It is an anagram")

# Run your code to check using the words below:
anagram_checker("Slient", "listen")

anagram_checker2("Slient", "listen")