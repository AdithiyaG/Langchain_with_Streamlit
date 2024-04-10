from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import Chroma
from azureopenai import embedding_function

REVIEWS_CSV_PATH="data/reviews.csv"
REVIEWS_CHROMA_PATH="chroma_data"

loader=CSVLoader(file_path=REVIEWS_CSV_PATH,source_column="review")
reviews=loader.load()

reviews_vector_db = Chroma.from_documents(
    reviews,embedding_function, persist_directory=REVIEWS_CHROMA_PATH
)


