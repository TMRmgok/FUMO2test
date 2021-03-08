from django.shortcuts import get_object_or_404, render
from .models import Task, Globvar
# Create your views here.
from django.http import HttpResponse
from .forms import TaskForm
import random, sqlite3
import os.path


def index(request):
    tasks = Task.objects.all()
    print(tasks)
    vopr = 'Инструментальные стали'
    vopr2 = tasks[random.randint(0,2)]
    v1 = vopr2.v1
    o1 = vopr2.v2
    o2 = vopr2.v3
    o3 = random.randint(1,10)
    print(str(o3))
    print('Проверка печати')
    return render(request, 'main/index.html', {'title':vopr,'v1':v1,'o1':o1,'o2':o2,'o3':o3, 'vopr': vopr2})


def about(request):
    global i
    i=0
    print('Счетчик числа вопросов')
    return render(request, 'main/contact_form.html')

def create(request):
    global right_answer, count_right_answer, count_all_answer

# шаг 1.1 Проверяем, есть ли переменная "правильный ответ"
# шаг 1.2 Проверяем, есть ли переменная "количество правильных ответов"

    if 'right_answer' in globals():
        print('Есть правильный ответ')
    else:
        print('Нет правильного ответа')
        right_answer=1

    if 'count_right_answer' in globals():
        print('Есть правильный ответ')
    else:
        print('Нет правильного ответа')
        count_right_answer = 0

    if 'count_all_answer' in globals():
        print('Первый вопрос по списку')
    else:
        print('Уже были вопросы')
        count_all_answer = -1

    if count_all_answer==10:
        count_right_answer=0
        count_all_answer=-1

# шаг 2.1 Получаем запрос от текущей страницы "req"
# шаг 2.2 Выводим длину запроса в переменную (чтобы отобразить при проверке)
# шаг 2.3 Сравниваем данный ответ с правильным ответом

    req = request.POST
    print(req)
    length_post=len(req)
    if len(req)==1:
        print('Ответа нет ',len(req))
    if len(req)==2:
        if str(right_answer)==str(req['choice']):
            print('Ответ дан!!! ',req['choice'],'. Это правильно!')
            count_right_answer=count_right_answer+1

    count_all_answer=count_all_answer+1
# шаг 3.1 Подгружаем из базы данных из таблицы Tasks все вопросы
# шаг 3.2 Выбираем случайный номер вопроса, загружаем строку с данным номером в переменную vopr2
# шаг 3.3 Считываем значение правильного ответа из строки в переменную right_answer

    tasks = Task.objects.all()
    vopr = 'Инструментальные стали'
    num_vopr = random.randint(0,10)-1
    vopr2 = tasks[num_vopr]
    right_answer = vopr2.v6
    print('Новый правильный ответ -', right_answer)
    test_info={'length_post':length_post,'count_right_answer':count_right_answer,'count_all_answer':count_all_answer}


#шаг 4. Проверки на внесение данных в базу
    sqlite_file = '/home/TMRmgok/tmrmgok.pythonanywhere.com/db.sqlite3'
    #'C:/Users/Александр/PycharmProjects/FUMO2test/FUMO2site/db.sqlite3'
    if os.path.exists(sqlite_file):
        print('File exists')
    else:
        print('File NOT exists')


    conn = sqlite3.connect(sqlite_file)
    cur = conn.cursor()
    request1="UPDATE main_globvar SET prO = '"+str(right_answer)+"' WHERE id = 1"
    cur.execute(request1)
    cur.execute("SELECT * FROM main_globvar")

    results1 = cur.fetchall()
    results2 = results1[0]
    results3 = results2[1]
    print('Новый вопрос - ', num_vopr)
    print('Новый правильный ответ - ',results3)
    return render(request, 'main/index.html', {'title':vopr, 'vopr': vopr2, 'test_info':test_info})

def hello(request):
    return HttpResponse("Hello world")