import json
from collections import defaultdict, Counter
import random
import pandas as pd


# อ่านข้อมูลจากไฟล์ raw_data.json
def load_data():
    try:
        with open("data/raw_data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        try:
            with open("raw_data.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return None


# แปลงข้อมูลให้อยู่ในรูปแบบข้อความ
def get_text(data):
    if isinstance(data, str):
        return data

    if isinstance(data, list):
        result = []
        for item in data:
            result.append(get_text(item))
        return " ".join(result)

    if isinstance(data, dict):
        if "text" in data:
            return get_text(data["text"])

        result = []
        for value in data.values():
            result.append(get_text(value))
        return " ".join(result)

    return ""


# สร้าง Transition Probability Matrix
def build_matrix(text):
    words = text.split()
    transitions = defaultdict(Counter)

    for i in range(len(words) - 1):
        current = words[i]
        next_word = words[i + 1]
        transitions[current][next_word] += 1

    matrix = {}

    for current, next_words in transitions.items():
        total = sum(next_words.values())

        matrix[current] = {}

        for word, count in next_words.items():
            matrix[current][word] = count / total

    return matrix


# หาคำที่มีโอกาสเป็นคำถัดไปมากที่สุด
def predict_word(matrix, word):
    if word not in matrix:
        return []

    result = sorted(
        matrix[word].items(),
        key=lambda x: x[1],
        reverse=True
    )

    return result


# สร้างประโยคจากคำเริ่มต้น
def generate_text(matrix, start, amount):
    words = start.split()

    for i in range(amount):
        current = words[-1]

        predictions = predict_word(matrix, current)

        if not predictions:
            break

        next_words = [x[0] for x in predictions]
        probabilities = [x[1] for x in predictions]

        next_word = random.choices(
            next_words,
            weights=probabilities,
            k=1
        )[0]

        words.append(next_word)

    return " ".join(words)


def build_matrix_table(matrix):
    df = pd.DataFrame(matrix).T.fillna(0)

    return df


def get_last_word(start):
    current = start.split()[-1]

    return current


def build_prediction_table(result):
    prediction_df = pd.DataFrame(
        result,
        columns=["คำถัดไป", "Probability"]
    )

    prediction_df["Probability (%)"] = (
        prediction_df["Probability"] * 100
    ).round(2)

    return prediction_df[
        ["คำถัดไป", "Probability (%)"]
    ]
