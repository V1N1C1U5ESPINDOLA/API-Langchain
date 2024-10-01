from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(api_key=key)

prompt_template = PromptTemplate(
    input_variables=["input_text"],
    template="Voce e um assistente que responde perguntas: {input_text}"
)

chain = LLMChain(llm=llm, prompt=prompt_template)

while True:
    user_message = input("Digite sua pergunta (ou 'sair' para encerrar): ")
    if user_message.lower() == 'sair':
        break
    response = chain.run(input_text=user_message)
    print("Resposta:", response)
