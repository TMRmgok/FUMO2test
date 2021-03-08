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
    #print('Ответ:')
    req = request.POST
    print(req)
    #print(len(req))
    if len(req)==1:
        print('Ответа нет ',len(req))
    # else:
    #     if str(2)==str(req['choice']):
    #           print('Ответ дан!!! ',req['choice'],'. Это правильно!')
    #     else:
    #           print('Ответ дан!!! ', req['choice'], '. Это неправильно!')


    #print('Следующие проверки')
    form = TaskForm
    tasks = Task.objects.all()
    prO1 = Globvar.objects.get(pk=1)
    prOtv = prO1.prO

    #print(prOtv)
    vopr = 'Инструментальные стали'
    num_vopr = random.randint(0,10)
    vopr2 = tasks[num_vopr]
    v1 = vopr2.v1
    o1 = vopr2.v2
    o2 = vopr2.v3
    o3 = vopr2.v4
    o4 = vopr2.v5
    prOTTT = vopr2.v6
    print('Новый правильный ответ',prOTTT)

    sqlite_file = '/home/TMRmgok/tmrmgok.pythonanywhere.com/db.sqlite3'
    if os.path.exists(sqlite_file):
        print('File exists')
    else:
        print('File NOT exists')


    conn = sqlite3.connect(sqlite_file)
    cur = conn.cursor()
    request1="UPDATE main_globvar SET prO = '"+str(prOTTT)+"' WHERE id = 1"
    #print(request1)
    cur.execute(request1)
    cur.execute("SELECT * FROM main_globvar")

    results1 = cur.fetchall()
    results2 = results1[0]
    results3 = results2[1]
    print('Новый вопрос - ', num_vopr)
    print('Новый правильный ответ - ',results3)
    #i=prO
    #print('Правильный ответ - ',i)
    return render(request, 'main/index.html', {'title':vopr, 'vopr': vopr2})

def hello(request):
    return HttpResponse("Hello world")