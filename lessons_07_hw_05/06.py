import random


def pemrtuate(texts):
    text_fynal = []

    texts = texts.split()

    for text in texts:
        text_list = []
        if len(text) == 1:
            text_fynal.append(text)
        else:
            for symbol in text:
                text_list.append(symbol)

            first_symbol = text_list[0]
            last_symbol = text_list[- 1]

            del text_list[0]
            del text_list[- 1]

            random.shuffle(text_list)
            text_list = ''.join(text_list)
            my_text = first_symbol + text_list + last_symbol
            text_fynal.append(my_text)

    return ' '.join(text_fynal)


texts = str(input('Введите предложение: \n >>> '))
print(pemrtuate(texts))
