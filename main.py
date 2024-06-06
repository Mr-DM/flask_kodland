from flask import Flask
import random

app = Flask(__name__)

fact_list = ["Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
             "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
             "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.",
             "Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.",
             "Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.",
             "Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.",
             "Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.",
             "Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.",]

@app.route("/")

        
def hello_world():
    return f"""<h1>Hello World</h1> 
      <h2> Добро пожалывать 😀</h2> 
      <a href="/random_fact">Посмотреть случайный факт!</a> <br>
        <a href="/flip_coin">Бросок монетки!❌/✔</a> <br> 
        <a href="/pass_generate">Генератор паролей 🔐</a> """
    
@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(fact_list)}</p>'

@app.route("/flip_coin")
def flip():
    chise = random.randint(0,5)
    if chise > 3:
        return f'<h1>True 🤑</h1>'
    else:
        return f'<h1>Flast 😓</h1>'
    
@app.route("/pass_generate")
def gen_pass():
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(8):
        password += random.choice(elements)
    return f'<h1>You pass 🔐 --> {password}</h1>'


app.run(debug=True)



