from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms import PetitionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very-very-secret-key'  # Ключ конфигурации
csrf = CSRFProtect(app)


@app.route('/')
def page():
    navigation = [
        {'name': 'Главная', 'url': '/'},
        {'name': 'Форма', 'url': '/form'},
        {'name': 'О нас', 'url': '#'}
    ]

    footer_data = {
        'show_copyright': True,
        'year': 2026,
        'company': 'Яндекс Лицей',
        'version': '1.0.0'
    }

    # можно передавать данные в шаблон
    page_title = "Привет, Яндекс!"
    return render_template('index.html', title=page_title, navigation=navigation, footer_data=footer_data)


@app.route('/hello/<string:username>')
def hello(username):
    age = request.args.get('age', 16)

    navigation = [
        {'name': 'Главная', 'url': '/'},
        {'name': 'Форма', 'url': '/form'},
        {'name': 'О нас', 'url': '#'}
    ]

    footer_data = {
        'show_copyright': True,
        'year': 2026,
        'company': 'Яндекс Лицей',
        'version': '1.0.0'
    }

    return render_template('hello.html',
                           username=username,
                           age=age,
                           navigation=navigation,
                           footer_data=footer_data)


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = PetitionForm()

    navigation = [
        {'name': 'Главная', 'url': '/'},
        {'name': 'Форма', 'url': '/form', 'active': True},
        {'name': 'О нас', 'url': '#'}
    ]

    footer_data = {
        'show_copyright': True,
        'year': 2026,
        'company': 'Яндекс Лицей',
        'is_form_page': True
    }

    if form.validate_on_submit():
        print(f"Имя: {form.name.data}")
        print(f"Фамилия: {form.surname.data}")
        print(f"Пол: {form.sex.data}")
        print(f"Подпись: {'да' if form.sign.data else 'нет'}")
        return "Форма успешно отправлена!"

    return render_template('form.html',
                           form=form,
                           navigation=navigation,
                           footer_data=footer_data)


if __name__ == '__main__':
    app.run(port=8083, host='127.0.0.1', debug=True)