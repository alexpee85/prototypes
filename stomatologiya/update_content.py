import re

s = open("index.html", encoding="utf-8").read()

# Заменяем заголовок и описание
s = s.replace('<title>Vita-Den Lux — стоматология в Бишкеке, ул. Токтогула 165</title>',
              '<title>Стоматология — стоматология в Бишкеке, ул. Ивана Панфилова, 173</title>')
s = s.replace('<meta name="description" content="Vita-Den Lux — стоматология в Бишкеке, ул. Токтогула 165. Лечение, гигиена, имплантация, брекеты. Запись на приём.">',
              '<meta name="description" content="Стоматология — стоматология в Бишкеке, ул. Ивана Панфилова, 173. Лечение, гигиена, имплантация, брекеты. Запись на приём.">')

# Заменяем эмблему и заголовок
s = s.replace('<div class="emblem">V</div>', '<div class="emblem">С</div>')
s = s.replace('<div class="brand-t">VITA-DEN LUX<small>СТОМАТОЛОГИЯ · БИШКЕК</small></div>',
              '<div class="brand-t">СТОМАТОЛОГИЯ<small>СТОМАТОЛОГИЯ · БИШКЕК</small></div>')
s = s.replace('font-size:1.3rem">VITA-DEN LUX</span>', 'font-size:1.3rem">СТОМАТОЛОГИЯ</span>')
s = s.replace('<b>VITA-DEN LUX</b>', '<b>СТОМАТОЛОГИЯ</b>')
s = s.replace('© Vita-Den Lux. Демонстрационный концепт, не действующий сайт.',
              '© Стоматология. Демонстрационный концепт, не действующий сайт.')

# Телефон
s = s.replace('<a href="tel:+996775777773"', '<a href="tel:+996****1230"')
s = s.replace('+996 775 777 773', '+996 **** 1230')

# Яндекс.Карты ссылка
s = s.replace('https://ya.ru/vita_dent_lux/161052964652/', 'https://ya.ru/dental_office_of_koombaev_k_k_/220364869657/')

open("index.html", "w", encoding="utf-8").write(s)
print("Базовое наполнение готово")
