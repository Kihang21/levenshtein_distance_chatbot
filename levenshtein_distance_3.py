
"""
pip install python-Levenshtein
"""


import Levenshtein

# 학습 데이터 (질문과 답변)
training_data = [
    {"question": "저는 오늘 밥을 먹었습니다.", "answer": "오늘 무엇을 먹었나요?"},
    {"question": "저는 어제 밥을 먹었습니다.", "answer": "어제 무엇을 먹었나요?"},
]

# chat의 질문
chat_question = "나 아까 초밥 먹었어."

# 1. 학습 데이터의 질문과 chat의 질문의 유사도를 레벤슈타인 거리를 이용해 구하기
def calculate_similarity(question1, question2):
    levenshtein_distance = Levenshtein.distance(question1, question2)
    return levenshtein_distance

# 2. chat의 질문과 레벤슈타인 거리와 가장 유사한 학습 데이터의 질문의 인덱스를 구하기
distances = [calculate_similarity(chat_question, data["question"]) for data in training_data]
most_similar_index = distances.index(min(distances))

# 3. 학습 데이터의 인덱스의 답을 chat의 답변을 채택한 뒤 출력
best_answer = training_data[most_similar_index]["answer"]
best_distance = distances[most_similar_index]

# 결과 출력
print(f"두 문장의 Levenshtein 거리: {best_distance}")
print(f"가장 유사한 학습 데이터의 질문 인덱스: {most_similar_index}")
print(f"답변: {best_answer}")
