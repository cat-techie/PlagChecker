# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import keyword
import tokenize


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    tokens = []


    with open('tests.py', 'rb') as f:
        for token in tokenize.tokenize(f.readline):
            #print(token)
            if token.string in tokenDict or keyword.iskeyword(token.string):
                tokens.append(token.type)
                print(token)

        tokens = zip(*[iter(tokens)] * 2)
        print(" ".join(map(str, tokens)))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
