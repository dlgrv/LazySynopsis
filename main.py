from PIL import Image, ImageDraw, ImageFont
import docx
import random

sets = {0: [0,  1,   2,        3,     4,   5,  6,  7, 8],
      1: [28, 61, '#05045c', 20.55, 125, 50, 30, 39, 100],
      2: [28, 55, '#05045c', 20.55, 121.5, 50, 30, 39, 100]}

alphabet = ["й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "ф", "ы", "в", "а", "п",
            "р", "о", "л", "д", "ж", "э", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", "ё"]

# START CONST
number_file = 1
number_paper = 11
enter = 0
additional_indent = 0
indent = 0

fonts_numb = 1

doc = docx.Document('text.docx')
text = []
for paragraph in doc.paragraphs:
    text.append(paragraph.text)

imag = Image.open('paper/11.png')
font = ImageFont.truetype(f'fonts/{fonts_numb}.ttf', size=sets[fonts_numb][0])

for i in range(len(text)):
    if len(text[i]) < sets[fonts_numb][1]:
        indent = sets[fonts_numb][5] + random.randint(-2,2)
        draw_text = ImageDraw.Draw(imag)
        draw_text.text((indent, sets[fonts_numb][4] + sets[fonts_numb][3]*enter),
                       text[i],
                       font=font,
                       fill=(sets[fonts_numb][2]))
        enter+=1
    else:
        # ДЕЛИМ ТЕКСТ НА СТРОКИ
        temporary_text = text[i]
        temporary_text = [temporary_text[g:g + sets[fonts_numb][1]] for g in range(0, len(temporary_text), sets[fonts_numb][1])]
        # ДОБАВЛЯЕМ '-'
        for j in range(len(temporary_text)-1):
            if temporary_text[j][-1].lower() in alphabet \
                    and temporary_text[j][-2].lower() in alphabet \
                    and temporary_text[j + 1][0].lower() in alphabet:
                if temporary_text[j + 1][1].lower() in alphabet:
                    temporary_text[j] += '-'
                elif temporary_text[j + 1][1] == ' ':
                    temporary_text[j] += temporary_text[j + 1][0]
                    temporary_text[j + 1] = temporary_text[j + 1].replace(temporary_text[j + 1][0], '', 1)
        # НАННОСИМ ТЕКСТ НА ЛИСТ
        draw_text = ImageDraw.Draw(imag)
        for j in range(len(temporary_text)):
            # ОПРЕДЕЛЯЕМ ЕСТЬ ЛИ ЕЩЕ СВОБОДНОЕ МЕСТО НА ЛИСТКЕ
            if enter >= sets[fonts_numb][7]:
                enter = 0
                if number_paper == 11:
                    number_paper = 12
                    #------------------------------------------------------------------
                    offset = {1: -7, 1.3: -10, 1.5: -11,
                              -1: -7, -1.3: -10, -1.5: -11}
                    offset_list = []
                    for i in offset.keys():
                        offset_list.append(i)
                    offset_real = random.choice(offset_list)
                    #print(offset_real)
                    imag = imag.rotate(offset_real)

                    watermark = imag
                    imag = Image.open('background/1.png')
                    imag.paste(watermark, (offset[offset_real], 0), watermark)

                    # МЕНЯЕМ ПЕРСПЕКТИВУ
                    width, height = imag.size
                    temporary = random.randint(7, 12) / 100000
                    imag = imag.transform((width, height), Image.PERSPECTIVE, (1, 0, 0, 0, 1, 50, 0, temporary), fill=1)

                    # ДОБАВЛЯЕМ ТЕНИ И СВЕТ
                    watermark = Image.open('trash/1.png')
                    imag.paste(watermark, (random.randint(-730, 0), 0), watermark)
                    #------------------------------------------------------------------
                    imag.save(f"{number_file}.png")
                    imag = Image.open('paper/12.png')
                    number_file += 1
                    additional_indent = sets[fonts_numb][8]
                    enter = 0
                else:
                    number_paper = 11
                    # ------------------------------------------------------------------
                    offset = {0: 0, 0: 0, 0: 0}
                    offset_list = []
                    for i in offset.keys():
                        offset_list.append(i)
                    offset_real = random.choice(offset_list)
                    #print(offset_real)
                    imag = imag.rotate(offset_real)

                    watermark = imag
                    imag = Image.open('background/1.png')
                    imag.paste(watermark, (offset[offset_real], 0), watermark)

                    # МЕНЯЕМ ПЕРСПЕКТИВУ
                    width, height = imag.size
                    #temporary = random.randint(7, 12) / 100000
                    temporary = 0
                    imag = imag.transform((width, height), Image.PERSPECTIVE, (1, 0, 0, 0, 1, 50, 0, temporary), fill=1)

                    # ДОБАВЛЯЕМ ТЕНИ И СВЕТ
                    watermark = Image.open('trash/1.png')
                    imag.paste(watermark, (random.randint(-730, 0), 0), watermark)
                    # ------------------------------------------------------------------
                    imag.save(f"{number_file}.png")
                    imag = Image.open('paper/11.png')
                    number_file += 1
                    additional_indent = 0
            # ОПРЕДЕЛЯЕМ КРАСНАЯ СТРОКА ИЛИ НЕ ОЧЕНЬ ;)
            if j == 0:
                indent = sets[fonts_numb][5] + additional_indent + random.randint(-2, 2)
            else:
                indent = sets[fonts_numb][6] + additional_indent + random.randint(-2, 2)
            draw_text = ImageDraw.Draw(imag)
            draw_text.text((indent, sets[fonts_numb][4] + sets[fonts_numb][3] * enter),
                           temporary_text[j],
                           font=font,
                           fill=(sets[fonts_numb][2]))
            enter += 1


if number_file % 2 == 0:
    offset = {0: 0, 0: 0, 0: 0}
    offset_list = []
    for i in offset.keys():
        offset_list.append(i)
    offset_real = random.choice(offset_list)
    temporary = 0
else:
    offset = {1: -7, 1.3: -10, 1.5: -11,
              -1: -7, -1.3: -10, -1.5: -11}
    offset_list = []
    for i in offset.keys():
        offset_list.append(i)
    offset_real = random.choice(offset_list)
    temporary = random.randint(7, 12) / 100000

#print(offset_real)
imag = imag.rotate(offset_real)

watermark = imag
imag = Image.open('background/1.png')
imag.paste(watermark, (offset[offset_real], 0), watermark)

# МЕНЯЕМ ПЕРСПЕКТИВУ
width, height = imag.size
imag = imag.transform((width, height), Image.PERSPECTIVE, (1, 0, 0, 0, 1, 50, 0, temporary), fill=1)

# ДОБАВЛЯЕМ ТЕНИ И СВЕТ
watermark = Image.open('trash/1.png')
imag.paste(watermark, (random.randint(-730, 0), 0), watermark)
imag.save(f"{number_file}.png")