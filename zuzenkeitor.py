import glob
import os

from dotenv import load_dotenv
load_dotenv()

from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama



path = './submissions/2/'


model = ChatOllama(model="gemma2:2b",temperature=0)

prompt_template = PromptTemplate.from_file(os.path.join(path, "correctionprompttemplate.txt"))

def zuzendu(proposal, reference):
    prompt = prompt_template.invoke({"proposal": proposal, "reference": reference})
    return model.invoke(prompt)

    

def zuzendu_student(reference, student):
    tokens = student.split('_')
    
    izena_abizenak = tokens[0]
    student_id = tokens[1]

    student_path =  os.path.join(path, student)

    c_files = glob.glob(os.path.join(student_path,'*.c'))
    
    with open(c_files[0],"r") as c_file:
        proposal = c_file.read()
        result = zuzendu(proposal, reference)
        print(student_id, result)

                       
def main():

    with open(os.path.join(path,"reference.c"),"r") as file:
        reference = file.read()

    students = os.listdir(path)
    for student in students:
        if os.path.isdir(os.path.join(path,student)):
            zuzendu_student(reference, student)

if __name__=='__main__':
    main()