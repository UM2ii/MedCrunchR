import os
import pandas as pd
from tqdm import tqdm
import openai


class Cruncher():
    def __init__(self, file_name: str , key:str , url:str, model: str):
        openai.api_key = key
        openai.api_base = url
        self.model= model 
        self.extension = os.path.splitext(file_name)[1]
        try:
            if self.extension == ".xlsx":
                self.reports = pd.read_excel(file_name, sheet_name="Reports")
                print("Data Loaded..\n", self.reports.columns)
        
        
        except Exception as Error:
            print("Error: Only xlsx file format is supported. Error:", Error)

        try:
            if self.extension == ".xlsx":
                self.prompts = pd.read_excel(file_name, sheet_name="Prompts")
                print("Data Loaded..\n", self.prompts.columns)
        
        
        except Exception as Error:
            print("Error: Only xlsx file format is supported. Error:", Error)

    def show_data(self):
        print(self.reports.head(), self.reports.shape)
        print(self.prompts.head(), self.prompts.shape)

    def crunch_data(self):
        for report_id in tqdm(range(self.reports.shape[0])):
            for prompt_id in range(self.prompts.shape[0]):
                column_index = str(prompt_id)+'_'+str(self.prompts.iloc[prompt_id,1]-1)
                if column_index not in self.reports:
                    self.reports[column_index]=''

                #print(report_id,self.prompts.iloc[prompt_id,1]-1)
                query= self.prompts.iloc[prompt_id,0] + '''. report: ''' + self.reports.iloc[report_id, self.prompts.iloc[prompt_id,1]] 
                try:
                    completion = openai.ChatCompletion.create(
                    model=self.model,
                    max_tokens= 800,
                    temperature= 0.0,
                    messages=[{
                        "role": "assistant",
                        "content": "Hi there! I'm Dolphin, an AI assistant. I can help you with things like answering questions, providing information, and helping with tasks. How can I help you?"
                        },
                        {"role": "user", "content": query }
                    ]
                    )

                    answer = completion.choices[0].message.content
                except Exception as e:
                    print(e)
                    answer= "error"
                
                self.reports[column_index]=answer
                print(answer)
        self.reports.to_excel('file_final.xlsx', index=False)