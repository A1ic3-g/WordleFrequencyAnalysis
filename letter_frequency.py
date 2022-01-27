from unittest import result
import pandas as pd
import numpy as np
import plotly.express as px


def main():
    letters = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    def count(word):
        for char in word:
            letters[char] += 1
    
    df = pd.read_csv("wordle.txt", sep = " ", header=None, names = ["word"])
    
    length = df.shape[0]
    result = [count(word) for word in df['word']]
    
    graph_data = pd.DataFrame.from_dict(letters, orient="index")
    print (graph_data)
    fig = px.bar(graph_data)
    fig.show()

if __name__ == "__main__":
    main()