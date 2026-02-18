// функция, срабатывающая при нажатии на кнопку
function changeAll() {
    // через console.log, console.error можно выводить сообщения в консоль браузера - аналог print
    console.log("На кнопку нажали!!!")
    console.error("Изменения необратимы...")

    // получаем плашки по их id
    const group = document.getElementById('group');
    const place = document.getElementById('place');
    const teacher = document.getElementById('teacher');

    // получаем форму по её классу. С помощью querySelector можно получить элемент через его id ('#id-name') или класс ('.class-name')
    const form = document.querySelector('.jsForm');

    // получаем данные полей формы - доступно c name-атрибутами инпутов
    const formData = new FormData(form);

    const groupValue = formData.get('groupInput');
    const placeValue = formData.get('placeInput');
    const teacherValue = formData.get('teacherInput');

    // изменяем текст в полях
    group.textContent = `Ваша группа - ${groupValue}!`;
    place.textContent = `Площадка - ${placeValue}`;

    // условный оператор. скобки в условии обязательны, кавычки тоже. Это вам не питон.
    if (teacherValue !== "Слободянюк Анастасия Андреевна" && teacherValue !== "") {
        // alert - всплывающее окно вверху браузера
        alert("Нельзя изменить преподавателя!😈")
    }
    else {
        teacher.textContent = `Преподаватель - Слободянюк Анастасия Андреевна`;
    };

    // сброс полей формы
    form.reset();
}