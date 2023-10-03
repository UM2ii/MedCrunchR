## MedCruncher - Simplify the processing of reports and documents using LLMs (Large Language Models)

### About
MedCruncher is a python based a wrapper to process the medical literature using Large Language Models. 

![image](https://github.com/UM2ii/wordscruncher/assets/49832962/80681d03-1a1a-46ce-b268-82c69a2cf381)
Figure 1.0 MedCruncher takes multiple reports and prompt in form of excel sheet and processes the reports and prompts resepectively and saves the results into excel format

### Instructions

#### Step 1: Install MedCruncher using pip

`pip install medcruncher`

#### Step 2: Install Fastchat for LLM inference
'pip install fschat'

#### Step 3: Follow the Fastchat's documentation Open-AI compatible api
`https://github.com/lm-sys/FastChat/blob/main/docs/openai_api.md#restful-api-server`


#### step 4: Example code to use MedCruncher module:

`from wordscruncher import Cruncher
instance = Cruncher("reports.xlsx", "EMPTY", "http://localhost:8000/v1", "vicuna-7b-v1.5-16k", "final_results")
instance.crunch_data()`

