# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# text_1 = 'She sells sea shells on the sea shore The shells'
# text_2 = text_1.lower()
# text_2 = text_2.replace(('.' and ';' ), '') 
# text_2 = text_2.split(' ' or '  ')
# text_2 = set(text_2)
# print(len(text_2))

# решение со второй группой:

text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
text_1 = text.lower().replace(".", "").split(' ' or '  ')
set_1 = set(text_1)
print(len(set_1))