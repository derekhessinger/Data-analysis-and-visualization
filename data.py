'''data.py
Reads CSV files, stores data, access/filter data by variable name
Derek Hessinger
CS 251 Data Analysis and Visualization
Spring 2023
'''
import csv
import numpy as np

class Data:

    ''' Constructor for the data object'''
    def __init__(self, filepath=None, headers=None, data=None, header2col=None):

        
        self.filepath = filepath
        self.headers = headers
        self.data = data
        self.header2col = header2col

        if self.filepath != None:   # if filepath is there, call read
            self.read(filepath)

        return

    ''' Method to read in .csv file and convert to numpy array'''
    def read(self, filepath):

        with open(filepath, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)  # create reader object

            self.filepath = filepath    # set file path
            line = 0                    # initialize line
            colNum = []                 # create column set
            self.header2col = {}        # create header2col dictionary to store headers and corresponding column nums
            self.data = []              # create data set to hold data entries
            list = []                   # create list set to hold headers

            for row in reader:
                if line == 0:   # For the first row (headers)
                    list = row  # take the headers from the first row and store in a set
                    line+=1 # increment to next row

                elif line == 1: # grab header datatype and indices
                    if "numeric" and "string" not in row:   # check to ensure csv file has data type row and raise error if not
                        raise Exception("FileError: CSV file is missing data type row. Must contain data type row.")
                    idx = self.rowIndices(row)  # use helper function to get row indices
                    self.headers = self.headerIndices(idx, list) # set header and corresponding indices with helper function
                    line+=1     # increment to next row

                else:           # for remaining rows, add data points to newRow set, then add newRows to data set
                    dataRow = [] # create empty set for data rows
                    for i in idx:   # for each element in each column, add data from row into set
                        dataRow.append(float(row[i]))
                    self.data.append(dataRow)   # add new set to data

            self.makeDict() # use helper function to make a dictionary of cols to headers

            self.data = np.array(self.data) # create np array of data
        return

    '''Helper function that returns indices of headers within a set'''
    def headerIndices(self, indices, arr):
        headers = []    # create set to hold headers
        for i in indices:   # for each index, add header to set
            x = arr[i].rstrip() # remove whitespace
            headers.append(x)   # add string to headers
        return headers

    '''Helper function that returns indices of rows within a set'''
    def rowIndices(self, row):
        indices = []    # create empty set to hold indices
        for i in range(len(row)):   # for the number of elements in the row
            if row[i] == 'numeric': # if the datum is a numeric element
                indices.append(i)   # add to set
        return indices

    '''Helper function that makes a dictionary of column indices and their corresponding headers'''
    def makeDict(self):
        for i in range(len(self.headers)):  # for the number of headers
            self.header2col[self.headers[i]] = i    # cast the header index to the header
        return

    '''Method to convert data object to string'''
    def __str__(self):

        result = str(self.filepath) + " (" + str(self.data.shape[0]) + "x" + str(self.data.shape[1]) + ") \n"   # add filepath and shape to string
        result += "Headers: \n" 
        for header in self.headers: # add headers to string
            result += header + "    "

        result += "\n-------------------------------\n"

        for i in range(5):  # add first five rows to string
            for data in self.data[i]:
                result += str(data) + "     "
            result += "\n"
            
            if i >= (np.ma.size(self.data, axis = 0)) -1:   # if i is greater than 5, break elements are not printed further
                break

        return result

    '''Method to return headers in data'''
    def get_headers(self):
       return self.headers

    '''Method to return mappings of headers to indices in data'''
    def get_mappings(self):
        return self.header2col

    '''Method to return the number of variables in data'''
    def get_num_dims(self):
        return len(self.headers)
    
    '''Method to return the number of samples in data'''
    def get_num_samples(self):
        return self.data.shape[0]

    '''Method to return rowInd-th data sample'''
    def get_sample(self, rowInd):
        return self.data[rowInd]

    '''Method to return the variable (column) indices of the str variable names in headers'''
    def get_header_indices(self, headers):
        indices = []
        for head in headers:
            indices.append(self.header2col[head])

        return indices

    def get_all_data(self):
        '''Gets a copy of the entire dataset

        (Week 2)

        Returns:
        -----------
        ndarray. shape=(num_data_samps, num_vars). A copy of the entire dataset.
            NOTE: This should be a COPY, not the data stored here itself.
            This can be accomplished with numpy's copy function.
        '''
        pass

    def head(self):
        '''Return the 1st five data samples (all variables)

        (Week 2)

        Returns:
        -----------
        ndarray. shape=(5, num_vars). 1st five data samples.
        '''
        pass

    def tail(self):
        '''Return the last five data samples (all variables)

        (Week 2)

        Returns:
        -----------
        ndarray. shape=(5, num_vars). Last five data samples.
        '''
        pass

    def limit_samples(self, start_row, end_row):
        '''Update the data so that this `Data` object only stores samples in the contiguous range:
            `start_row` (inclusive), end_row (exclusive)
        Samples outside the specified range are no longer stored.

        (Week 2)

        '''
        pass

    def select_data(self, headers, rows=[]):
        '''Return data samples corresponding to the variable names in `headers`.
        If `rows` is empty, return all samples, otherwise return samples at the indices specified
        by the `rows` list.

        (Week 2)

        For example, if self.headers = ['a', 'b', 'c'] and we pass in header = 'b', we return
        column #2 of self.data. If rows is not [] (say =[0, 2, 5]), then we do the same thing,
        but only return rows 0, 2, and 5 of column #2.

        Parameters:
        -----------
            headers: Python list of str. Header names to take from self.data
            rows: Python list of int. Indices of subset of data samples to select.
                Empty list [] means take all rows

        Returns:
        -----------
        ndarray. shape=(num_data_samps, len(headers)) if rows=[]
                 shape=(len(rows), len(headers)) otherwise
            Subset of data from the variables `headers` that have row indices `rows`.

        Hint: For selecting a subset of rows from the data ndarray, check out np.ix_
        '''
        pass