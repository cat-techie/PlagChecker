import tokenize
import TokenDictionary
import AlgorithmHeckel

if __name__ == '__main__':
    file1 = 'tasks/checkers.py'
    file2 = 'tasks/King.py'
    file3 = 'tasks/K_checkers.py'

    with open(file1, 'rb') as f1:
        # print(f"{tokenize.tok_name[1]}")
        tokens1 = TokenDictionary.FormatTokenStr(tokenize.tokenize(f1.readline))
        # print(" ".join(map(str, tokens)))
        kGram1 = AlgorithmHeckel.GenerateKGram(tokens1)
    with open(file2, 'rb') as f2:
        tokens2 = TokenDictionary.FormatTokenStr(tokenize.tokenize(f2.readline))
        kGram2 = AlgorithmHeckel.GenerateKGram(tokens2)

    with open(file3, 'rb') as f3:
        tokens3 = TokenDictionary.FormatTokenStr(tokenize.tokenize(f3.readline))
        kGram3 = AlgorithmHeckel.GenerateKGram(tokens3)

    print("Приблизительная оценка плагиата: " + str(round(AlgorithmHeckel.rateHeckel(kGram1, kGram3), 2)))
        # tokens = zip(*[iter(tokens)] * 2)
        # print(" ".join(map(str, tokens)))
