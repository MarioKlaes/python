all_paths = [
  "../05_data/assignment_2_data/inflammation_01.csv",
  "../05_data/assignment_2_data/inflammation_02.csv",
  "../05_data/assignment_2_data/inflammation_03.csv",
  "../05_data/assignment_2_data/inflammation_04.csv",
  "../05_data/assignment_2_data/inflammation_05.csv",
  "../05_data/assignment_2_data/inflammation_06.csv",
  "../05_data/assignment_2_data/inflammation_07.csv",
  "../05_data/assignment_2_data/inflammation_08.csv",
  "../05_data/assignment_2_data/inflammation_09.csv",
  "../05_data/assignment_2_data/inflammation_10.csv",
  "../05_data/assignment_2_data/inflammation_11.csv",
  "../05_data/assignment_2_data/inflammation_12.csv",
]

# 
# how the WITH command works?
# remember syntax of readline()
# 

with open( all_paths[0], 'r') as f:
    # YOUR CODE HERE: Use the readlines() method to read the .csv file into 'contents'
    contents = f.readlines()

    for index, patinence in enumerate(contents):
        print (f'Patient # {index+1}:' , patinence)
        
    f.close()


"""
    contents = f.readlines()

    for index, patinence in enumerate(contents):
        print (f'Patient # {index+1}:' , patinence)
        
    f.close()
  """