import numpy as np

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

def patient_summary(file_path, operation):
    # load the data from the file
    data = np.loadtxt(fname=file_path, delimiter=',')
    ax = 1  # this specifies that the operation should be done for each row (patient)
    
    # implement the specific operation based on the 'operation' argument
    summary_values = []

    if operation == 'mean':
        # YOUR CODE HERE: calculate the mean (average) number of flare-ups for each patient
        print (f"Mean: {data.mean(axis = ax)}")
        summary_values = data.mean(axis = ax)

    elif operation == 'max':
        # YOUR CODE HERE: calculate the maximum number of flare-ups experienced by each patient
        print (f"Max: {data.max(axis = ax)}")
        summary_values = data.max(axis = ax)
            
    elif operation == 'min':
        # YOUR CODE HERE: calculate the minimum number of flare-ups experienced by each patient
        print (f"Min: {data.min(axis = ax)}")
        summary_values = data.min(axis = ax)
    
    else:
        # if the operation is not one of the expected values, raise an error
        raise ValueError("Invalid operation. Please choose 'mean', 'max', or 'min'.")

    return summary_values



data_min = patient_summary(all_paths[0], 'min')
print(len(data_min))