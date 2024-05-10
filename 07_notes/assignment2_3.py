#
# Alternative solution for the Assignment 02
#

import numpy as np
import sys

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

class ArthritisDrugStudy:
    '''
    The class will store the results on MEAN, MAX, and MIN for future use.
    '''
    def __init__(self, file_path):
            self.file_path = file_path
            self.axis = 1 # row
            self.patience_mean = None
            self.patience_max = None
            self.patience_min = None
            self.patients_data = []
            self.check_zeros_mean = None

            #try open the data file
            self.read_patient_data()
    
    def read_patient_data (self):
        #load patient's data in the class
        try: #try open the file
            self.patients_data = np.loadtxt(fname = self.file_path, delimiter = ',')

        except FileNotFoundError: #if file not fouund raise error
            raise FileNotFoundError ("File not found.")
        
        except Exception: # if any other error occur, raise error
            raise Exception ("File cannot be opened.")
    
    def min (self):
        if len(self.patients_data) == 0:
            raise ValueError ("No data available for MIN.")
        else:
            self.patience_min = self.patients_data.min(axis = self.axis)

    def max (self):
        if len(self.patients_data) == 0:
            raise ValueError ("No data available for MAX.")
        else:
            self.patience_max = self.patients_data.max(axis = self.axis)
    
    def mean (self):
        if len(self.patients_data) == 0:
            raise ValueError ("No data available for MEAN.")
        else:
            self.patience_mean = self.patients_data.mean(axis = self.axis)
            self.check_zeros()

    def check_zeros(self):
        '''
        Given an array, x, check whether any values in x equal 0.
        Return True if any values found, else returns False.
        '''
         # np.where() checks every value in x against the condition (x == 0) and returns a tuple of indices where it was True (i.e. x was 0)
        flag = np.where(self.patience_mean == 0)[0]

        # Checks if there are any objects in flag (i.e. not empty)
        # If not empty, it found at least one zero so flag is True, and vice-versa.
        self.check_zeros_mean = len(flag) > 0


try:
    p = ArthritisDrugStudy(all_paths[0])
    p.max()
    print (f'Max: {p.patience_max}')
    print (f'Len: {len(p.patience_max)}')
    p.mean()
    print (f'Check Zeros: {p.check_zeros_mean}')

except Exception:
    ex_type, ex_value, traceback = sys.exc_info()
    # the latst exception raised will be stored in "ex_value"
    #  useful when the class or funcion can raise more than one exception
    print (ex_value) 
