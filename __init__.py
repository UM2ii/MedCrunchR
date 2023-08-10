
class Cruncher():
   def __init__(self, file_name: str):
      import os
      import pandas as pd
      self.extension = os.path.splitext(file_name)[1]
      try:
         if self.extension == ".xlsx":
            self.data_frame = pd.read_excel(file_name)
            
         if self.extension == "csv":
            self.data_frame = pd.read_csv(file_name)
            
         print("Data Loaded..\n", self.data_frame.columns)
         
      except Exception as e:
         print("Error: Only xlsx and csv file format is supported.", e)
            
      
   def show_data(self):
      print(self.data_frame.head())

   def query(self, Query:str):
      print(Query)