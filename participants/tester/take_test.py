"""take test"""
import csv
from typing import List, Any
from tqdm import tqdm
from langchain_chroma import Chroma
from write_to_csv import write_to_csv
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

def take_test():
    """main"""
    test_name = input("The test you want to take: ")
    test_file = "../../answer/" + test_name + ".csv"
    k = int(input("Number of chunks you want to retrieve: "))

    fields = ["Question", "Chunks"]
    result_file = "result/" + test_name + ".csv"

    rows = []

    with open(test_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        first = True
        for row in reader:
            if first:
                first = False
                continue
            question = row[0]
            chunks = get_retrieval_result(question, k)
            row = []
            row.append(question)
            row.append('; '.join(chunk[0].page_content for chunk in chunks))
            rows.append(row)
    
    print("Writing the result to " + result_file)
    write_to_csv(result_file, fields, rows)
    print("Complete writing")


def get_retrieval_result(query_text: str, k: int) -> List[Any]:
    """get retrieval result"""
    embedding_function = get_embedding_function()

    db = Chroma(
      persist_directory=CHROMA_PATH,
      embedding_function=embedding_function
    )

    results = db.similarity_search_with_score(query_text, k=k)
    return results



if __name__ == "__main__":
    take_test()
