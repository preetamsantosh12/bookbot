def calculateWords(text):
    words = text.split()
    return len(words)

def createLetterFrequencyMap(text):
    dict = {}
    for letter in text:
        l = letter.lower()
        if l not in dict:
            dict[l] = 0
        dict[l] += 1
    return dict
