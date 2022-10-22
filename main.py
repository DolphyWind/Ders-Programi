from PIL import Image, ImageDraw, ImageFont

lessons_per_day = 8
day_count = 5
mask = Image.open('mask.png')
cell_size = mask.size

table_size = (mask.size[0] * (lessons_per_day + 1), mask.size[1] * day_count)

table_img = Image.new('RGBA', table_size, (255, 255, 255))

font = ImageFont.truetype('times.ttf', 18)

lesson_data = {
    'tar':       ((0, 0, 0, 255),         'Tarih'),
    'star':      ((0, 0, 0, 255),         'Seçmeli\nTarih'),
    'day':       ((253, 138, 250, 255),   ''),
    'fel':       ((94, 174, 179, 255),    'Felsefe'),
    'biyo':      ((128, 50, 50, 255),     'Biyoloji'),
    'fiz':       ((255, 0, 0, 255),       'Fizik'),
    'tde':       ((18, 18, 254, 255),     'Edebiyat'),
    'stde':      ((18, 18, 254, 255),     'Seçmeli\nEdebiyat'),
    'alm':       ((226, 46, 164, 255),    'Almanca'),
    'reh':       ((199, 207, 44, 255),    'Rehberlik'),
    'bed':       ((0, 200, 0, 255),       'Beden'),
    'mat':       ((252, 20, 211, 255),    'Matematik'),
    'smat':      ((252, 20, 211, 255),    'Seçmeli\nMatematik'),
    'muz':       ((29, 163, 243, 255),    'Müzik'),
    'ing':       ((249, 119, 23, 255),    'İngilizce'),
    'kim':       ((6, 81, 125, 255),      'Kimya'),
    'din':       ((0, 108, 3, 255),       'Din'),
    'cog':       ((115, 115, 115, 255),   'Coğrafya'),
    'scog':      ((115, 115, 115, 255),   'Seçmeli\nCoğrafya'),
    'diks':      ((38, 165, 191, 255),    'Diksiyon'),
    'soset':     ((255, 0, 255, 255),     'Sosyal Etk.'),
    'ink':       ((0, 0, 0, 255),         'İnklap'),
}

def fill_image(im: Image, x, y, w, h, color):
    for j in range(h):
        for i in range(w):
            pass
            im.putpixel((x + i, y + j), color)

def main():
    days = ('Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma')
    draw = ImageDraw.Draw(table_img)

    lessons = list()
    fname = input('Dosya Adı: ')
    with open(fname, 'r') as f:
        for line in f:
            for x in line.replace('\n', '').split():
                lessons.append(x)

    for i in range(day_count):
        fill_image(table_img, 0, i * cell_size[1], cell_size[0], cell_size[1], lesson_data['day'][0])
        table_img.paste(mask, (0, i * cell_size[1], cell_size[0], (i + 1) * cell_size[1]), mask)
        draw.text(((cell_size[0] - draw.textsize(days[i], font=font)[0]) / 2, i * cell_size[1] + (cell_size[1] - draw.textsize(days[i], font=font)[1]) / 2), days[i], font=font, fill=(255, 255, 255, 255))

    index = 0
    for i in range(day_count):
        for j in range(lessons_per_day):
            inp = lessons[index]
            index += 1
            fill_image(table_img, (j + 1) * cell_size[0], i * cell_size[1], cell_size[0], cell_size[1], lesson_data[inp][0])
            table_img.paste(mask, ((j + 1) * cell_size[0], i * cell_size[1], (j + 2) * cell_size[0], (i + 1) * cell_size[1]), mask)
            text_size = draw.textsize(lesson_data[inp][1], font=font)
            draw.text(((j + 1) * cell_size[0] + cell_size[0] / 2 - text_size[0] / 2, i * cell_size[1] + cell_size[1] / 2 - text_size[1] / 2), lesson_data[inp][1], font=font, fill=(255, 255, 255, 255))

    table_img.save('Ders Programı_{}.png'.format(''.join(fname.split('.')[:-1])))



if __name__ == '__main__':
    main()
