import re
with open('par.txt', 'r') as text:
    passage = text.read()
    sentences = re.split("(?<=[.!?]) +", passage)
    words = [sentence.split() for sentence in sentences]
    numberSentences = len(sentences)
    numberWords = sum([len(i) for i in words])
    numberLetters = len(passage) - numberWords
    avgSentence = numberWords/numberSentences
    avgLetter = numberLetters/numberWords
    print("Paragraph Analysis\n-----------------")
    print(f"Approximate Word Count: {numberWords}")
    print(f"Approximate Sentence Count: {numberSentences}")
    print(f"Approximate Letter Count: {avgLetter}")
    print(f"Average Sentence Length: {avgSentence}")