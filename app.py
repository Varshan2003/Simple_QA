from langchain_google_genai import GoogleGenerativeAI
import config as cfg

llm = GoogleGenerativeAI(model="gemini-pro",google_api_key=cfg.key)
while True:
    question = input("Enter a query")
    answer = llm.invoke(question)
    print(answer)