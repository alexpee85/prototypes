import re

s = open("index.html", encoding="utf-8").read()

# Заменяем заголовок и описание
s = s.replace('<title>Стоматология — стоматология в Бишкеке, ул. Ивана Панфилова, 173</title>',
              '<title>Dental Plus — стоматология в Бишкеке, ул. Горького, 51А</title>')
s = s.replace('<meta name="description" content="Стоматология — стоматология в Бишкеке, ул. Ивана Панфилова, 173. Лечение, гигиена, имплантация, брекеты. Запись на приём.">',
              '<meta name="description" content="Dental Plus — стоматология в Бишкеке, ул. Горького, 51А. Лечение, гигиена, имплантация, брекеты. Запись на приём.">')

# Заменяем эмблему и заголовок
s = s.replace('<div class="emblem">С</div>', '<div class="emblem">D</div>')
s = s.replace('<div class="brand-t">СТОМАТОЛОГИЯ<small>СТОМАТОЛОГИЯ · БИШКЕК</small></div>',
              '<div class="brand-t">DENTAL PLUS<small>СТОМАТОЛОГИЯ · БИШКЕК</small></div>')
s = s.replace('font-size:1.3rem">СТОМАТОЛОГИЯ</span>', 'font-size:1.3rem">DENTAL PLUS</span>')
s = s.replace('<b>СТОМАТОЛОГИЯ</b>', '<b>DENTAL PLUS</b>')
s = s.replace('© Стоматология. Демонстрационный концепт, не действующий сайт.',
              '© Dental Plus. Демонстрационный концепт, не действующий сайт.')

# Телефон
s = s.replace('<a href="tel:+996****1230"', '<a href="tel:+996708526677"')
s = s.replace('+996 **** 1230', '+996 708 52 66 77')

# WhatsApp
s = s.replace('https://wa.me/996775777773', 'https://wa.me/996708526677')

# Яндекс.Карты ссылка
s = s.replace('https://ya.ru/dental_office_of_koombaev_k_k_/220364869657/', 'https://ya.ru/dental_plus/94403781252/')

open("index.html", "w", encoding="utf-8").write(s)
print("Dental Plus контент обновлён")
