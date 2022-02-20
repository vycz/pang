import pickle
import os
class Istore:
    #<string,list>
    data = {}
    ext = {}
    db_file = '～/.pangtemp/'
    db_name = 'dbase'

    def __init__(self) -> None:
        if not os.path.isfile(self.get_file_path()):
            if not os.path.exists(self.db_file):
                os.makedirs(self.db_file)
                mydb  = open(self.get_file_path(), 'wb')  
                pickle.dump(self, mydb)
                return
        mydb  = open(self.get_file_path(), 'rb')
        table = pickle.load(mydb)
        self.data = table.data
        self.ext = table.ext
    
    def get_data_items(self):
        return self.data.items()

    def add_data(self,alias,codes_str):
        self.data[alias] = codes_str.split(',')
        mydb  = open(self.db_file, 'wb') 
        pickle.dump(self, mydb)
    
    def del_data(self,alias):
        del self.data[alias]
        mydb  = open(self.db_file, 'wb') 
        pickle.dump(self, mydb)    
    
    def list_data(self):
        for key,value in self.data.items():
            print(key+'|'+value)
    
    def get_signal_data_code(self,alias):
        return self.data[alias]
    
    def get_file_path(self):
        return self.db_file + self.db_name

if __name__ == '__main__':
    istore = Istore()