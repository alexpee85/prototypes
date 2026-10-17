import re

s = open("index.html", encoding="utf-8").read()

# Заменяем заголовок и описание
s = s.replace('<title>Dental Plus — стоматология в Бишкеке, ул. Горького, 51А</title>',
              '<title>Голливуд — стоматология в Бишкеке, ул. 7 Апреля, 1/1</title>')
s = s.replace('<meta name="description" content="Dental Plus — стоматология в Бишкеке, ул. Горького, 51А. Лечение, гигиена, имплантация, брекеты. Запись на приём.">',
              '<meta name="description" content="Голливуд — стоматология в Бишкеке, ул. 7 Апреля, 1/1. Лечение, гигиена, имплантация, брекеты. Запись на приём.">')

# Заменяем эмблему и заголовок
s = s.replace('<div class="emblem">D</div>', '<div class="emblem">Г</div>')
s = s.replace('<div class="brand-t">DENTAL PLUS<small>СТОМАТОЛОГИЯ · БИШКЕК</small></div>',
              '<div class="brand-t">ГОЛЛИВУД<small>СТОМАТОЛОГИЯ · БИШКЕК</small></div>')
s = s.replace('font-size:1.3rem">DENTAL PLUS</span>', 'font-size:1.3rem">ГОЛЛИВУД</span>')
s = s.replace('<b>DENTAL PLUS</b>', '<b>ГОЛЛИВУД</b>')
s = s.replace('© Dental Plus. Демонстрационный концепт, не действующий сайт.',
              '© Голливуд. Демонстрационный концепт, не действующий сайт.')

# Телефон
s = s.replace('<a href="tel:+996708526677"', '<a href="tel:+996705609262"')
s = s.replace('+996 708 52 66 77', '+996 705 60 92 62')

# WhatsApp
s = s.replace('https://wa.me/996708526677', 'https://wa.me/996705609262')

# Яндекс.Карты ссылка
s = s.replace('https://ya.ru/dental_plus/94403781252/', 'https://ya.ru/gollivud/144133783135/')

open("index.html", "w", encoding="utf-8").write(s)
print("Голливуд контент обновлён")