# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import keyword
import tokenize
import TokenDictionary


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file1 = 'tasks/checkers.py'
    file2 = 'tasks/King.py'
    file3 = 'tasks/K_checkers.py'

    with open(file1, 'rb') as f1:
        #print(f"{tokenize.tok_name[1]}")
        var = TokenDictionary.FormatTokenStr(tokenize.tokenize(f1.readline))
        print(" ".join(map(str, var)))
        #for t in tokenize.tokenize(f1.readline):
            #print(t)

        #tokens = zip(*[iter(tokens)] * 2)
        #print(" ".join(map(str, tokens)))
