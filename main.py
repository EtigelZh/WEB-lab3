from jinja2 import Template
f_template = open('primer.html','r', encoding ='utf-8-sig')
html = f_template.read()
color = {
    1: "синий",
    2: "зеленый",
    3: "красный"
}
fio = {
    1: "Иван",
    2: "Иванов",
    3: "Иванович"
}
f_template.close()
template = Template(html)
result_html = template.render(name = 'color', dictionary = color, key=1)
f = open('test.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()