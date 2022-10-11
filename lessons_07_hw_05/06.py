import random


def pemrtuate(texts):
    text_fynal = []
    texts = texts.split()

    for text in texts:
        text_list = []
        if len(text) <= 2:
            text_fynal.append(text)
        else:
            for symbol in text:
                text_list.append(symbol)

        first_symbol = text_list[0]
        last_symbol = text_list[- 1]

        text_list.pop(0)
        text_list.pop(-1)

        my_text = []
        while len(text_list) != 0:
            b = text_list[:3]
            random.shuffle(b)
            my_text = ''.join(b)
            del text_list[:3]
            pass




texts = str(input('Enter text\n>>>>> '))
pemrtuate(texts)

