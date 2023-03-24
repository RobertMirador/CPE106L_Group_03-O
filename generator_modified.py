import random

"""Functions"""

def getWords(fileName):
    with open(fileName) as fN:
        wordType = [line.rstrip() for line in fN]
    return tuple(wordType)

def sentence():
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    genArticle = random.choice(articles)
    genNoun = random.choice(nouns)
    if genArticle != "THE":
        vowel = 'aeiou'
        if genNoun[0].lower() in vowel:
            return "AN " + genNoun
        else:
            return "A " + genNoun
    else:
        return genArticle + " " + genNoun

def prepoPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepoPhrase()

"""Vocabulary"""

articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
prepositions = getWords("prepositions.txt")
verbs = getWords("verbs.txt")

"""Program"""

def main():
    senCount = int(input("Enter the number of sentences to be generated: "))
    for count in range(senCount):
        print("\nSentence",count + 1,"-",sentence())

if __name__ == "__main__":
    main()
