from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def page():
    url_style = url_for('static', filename='css/style.css')
    return f'''
    <!doctype html>
       <html lang="en">
         <head>
           <meta charset="utf-8">
           <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
           <link rel="stylesheet" type="text/css" href="{url_style}">
           <title>Привет, Яндекс!</title>
         </head>
         <body>
            <p><i>Добро пожаловать в Яндекс Лицей!</i></p>
            <img src="{url_for('static', filename='img/yal.png')}" alt="Добро пожаловать в Яндекс Лицей!">
         </body>
       </html>
    '''


@app.route('/hello/<string:username>')
def hello(username):
    age = request.args.get('age', 16)
    return f'''
    <! doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
        </head>
        <body>
            <h1>Добрый день, {username}, {age}!</h1>
            <h2 class="alert alert-primary d-flex align-items-center">Ваша группа - 5!</h1>
            <h3 class="alert alert-success d-flex align-items-center">Площадка - ДТ "Альтаир"</h2>
            <h4 class="alert alert-info d-flex align-items-center">Преподаватель - Слободянюк Анастасия Андреевна</h3>
        </body>
    </html>
    '''


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return f'''
            <!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form.css')}" /> 
                        <title>Вы не могли бы подписать мою петицию?</title>
                    </head>
                    <body>
                        <div class="container">
                            <h1>Вы не могли бы подписать мою петицию?</h1>
                            <form class="yalForm" method="post">
                                <div class="mainInfo">
                                    <input type="text" id="name" placeholder="Введите имя" name="name">
                                    <input type="text" id="surname" placeholder="Введите фамилию" name="surname">
                                </div>
                
                                <div class="formGroup">
                                    <label for="gender">Укажите пол</label>
                                    <div class="gender">
                                        <input type="radio" name="sex" id="male" value="male">
                                        <label for="male" style="color: blue">мужской</label>
                                    </div>
                                    <div class="gender">
                                        <input type="radio" name="sex" id="female" value="female" checked>
                                        <label for="female" style="color: violet">женский</label>
                                    </div>
                                </div>
                
                                <div>
                                    <input type="checkbox" checked name="sign" id="sign">
                                    <label for="sign">Подписать</label>
                                </div>
                
                                <button type="submit" class="formBtn">Подтвердить</button>
                            </form>
                        </div>
                    </body>
                </html>'''
    elif request.method == 'POST':
        print(request.form.get('name', ""))
        print(request.form.get('surname', ""))
        print(request.form.get('sex', ""))
        print(request.form.get('sign', "no"))
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8083, host='127.0.0.1')
