import dotenv
from langchain_openai import AzureChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings


dotenv.load_dotenv()

client=AzureChatOpenAI(
    azure_deployment="gpt-4-32k",
    openai_api_version="2023-07-01-preview")

embedding_function=AzureOpenAIEmbeddings(
    azure_deployment="text-embedding-ada-002",
    openai_api_version="2023-07-01-preview")