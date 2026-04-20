import wikipedia 
import re
from typing import List

def tokenize(text: str) -> List[str]:
        """Splits given text into a list of the individual tokens in order

        Args:
            text - text to tokenize

        Returns:
            tokens of given text in order
        """
        tokens = []
        token = ""
        for c in text:
            if (
                re.match("[a-zA-Z0-9]", str(c)) != None
                or c == "'"
                or c == "_"
                or c == "-"
            ):
                token += c
            else:
                if token != "":
                    tokens.append(token.lower())
                    token = ""
                if c.strip() != "":
                    tokens.append(str(c.strip()))

        if token != "":
            tokens.append(token.lower())
        return tokens

    for word in words:
        if word in self.pos_freqs:
            self.pos_freqs[word] += 1
        else:
            self.pos_freqs[word] = 1
    #print(freqs)

    #print out the number of unique words
    total_unique_words = len(freqs)
    print(f"Total unique words: {total_unique_words}")

# Print out the total number of words
total_words = sum(freqs.values())
print(f"Total words: {total_words}")

#Print the top 20 words
top_words = sorted(freqs.items(), key=lambda x: x[1], reverse=True) 

article = wikipedia.page("Artemis II", auto suggest=False)
print(article)
tokens = tokenize(article)
print(tokens)

