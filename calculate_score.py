import csv
from evaluate_sentences_relevance import evaluate_sentences_relevance
def calulate_score():
    test_name = input("The test you want to calculate the score: ")
    participant = input("The participant you want to test: ")
    answer_file = "answer/" + test_name + ".csv"
    result_file = "participants/" + participant + "/result/" + test_name + ".csv"

    questions = []
    check_questions = []

    answers = []
    results = []

    with open(answer_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)

        first = True
        
        for row in reader:
            if first:
                first = False
                continue
            question = row[0]
            concatenated_strings = row[1]
            decomposed_list = concatenated_strings.split('; ')

            questions.append(question)
            answers.append(decomposed_list)

    with open(result_file, mode='r', encoding='utf-8') as file:
        
        reader = csv.reader(file)
        first = True
        
        for row in reader:
            if first:
                first = False
                continue
            question = row[0]
            concatenated_strings = row[1]
            
            decomposed_list = concatenated_strings.split('; ')

            check_questions.append(question)
            results.append(decomposed_list)
            

    if check_questions == questions:
        print("AC!!!")
    else:
        print("WA...")

    n = len(questions)
    MAP = 0
    for i in range(0, n):
        ap = 0
        rank = 0
        relevant_cnt = 0
        for chunk in results[i]:
            rank = rank + 1
            is_relevant = False
            for key_sentence in answers[i]:
                print("----------")
                print("Chunk: ")
                print(chunk)
                print("\nKey Sentence: ")
                print(key_sentence)
                relevance = evaluate_sentences_relevance(chunk, key_sentence)
                print("\nRelevance: ")
                print(relevance)

                if relevance[0] >= 0.5 and relevance[1] >= 0.5:
                    is_relevant = True
                    break

            if is_relevant:
                relevant_cnt = relevant_cnt + 1
                ap += relevant_cnt / rank 

        if relevant_cnt:
            ap = ap / relevant_cnt
        MAP += ap

    MAP = MAP / n

    print("==========")

    print(f"The final Mean Average Precision is: {MAP}")





if __name__ == "__main__":
    calulate_score()
