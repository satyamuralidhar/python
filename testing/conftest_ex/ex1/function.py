import json 

#create a class for private data using _

class StudentDB:
    def __init__(self):
        self.__data = None
    
    #create connection string
    
    def connection(self,std_data):
        """
        opening a file using with open and store into private data
        """
        with open(std_data) as json_data:
            self.__data = json.load(json_data)

    # create a method for for get data

    def get_data(self,name):
        for student in self.__data['students']:
            # student['name'] = 'ram'
            if student['name'] == name:
                return student

    # create a sample DB close with out any funtionality

    def close(self):
        pass
