from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QHBoxLayout, QWidget,QPushButton,QLabel,QVBoxLayout,QMessageBox,QRadioButton,QGroupBox,QButtonGroup
app =  QApplication([])
main_win = QWidget()
from random import *
question = QLabel("Какого цвета нет на флаге РФ?")
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton("Красный")
rbtn_2 = QRadioButton("Зеленый")
rbtn_3 = QRadioButton("Белый")
rbtn_4 = QRadioButton("Синий")
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
button = QPushButton("Ответить")
label1 = QLabel("Правильно/Не правильно")
label2 = QLabel("Правильный:")
layout_ans5 = QVBoxLayout()
layout_ans5.addWidget(label1)
layout_ans5.addWidget(label2)
answergroupbox = QGroupBox("Результат теста")
answergroupbox.setLayout(layout_ans5)
mainlayout = QVBoxLayout()
mainlayout.addWidget(question)
mainlayout.addWidget(RadioGroupBox)
mainlayout.addWidget(answergroupbox)
mainlayout.addWidget(button)
main_win.setLayout(mainlayout)
answergroupbox.hide()
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
def show_result():
    RadioGroupBox.hide()
    answergroupbox.show()
    button.setText("Следущий вопрос")
def show_question():
    RadioGroupBox.show()
    answergroupbox.hide()
    button.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
q1 = Question("Кто быстрее передвигается","Гепард","Змея","Лев","Мышь")
q2 = Question("Кто выиграл последний чемпионат мира по футболу","Франция","Россия","Германия","Бразилия")
q3 = Question("Как назывался мультфильм с синими человечками","Смурфики","Лунтик","Смешарики","Барбоскины")
q4 = Question("Какая самая большая река","Амазонка","Нил","Лена","Ока")
q5 = Question("Какого цвета елка?","Зеленого","Красного","Желтого","Синего")
q6 = Question("Кто главный герой игры майнкрафт?","Стив", "Карась","Орк","Кракин")
q7 = Question("Как звали самого главного автобота в фильме Трансформеры?","Оптимус", "Шун","Рэд","Грэган")
q8 = Question("В каком виде не может быть вода?","Мягкий", "Газообразный","Жидкий","Застывший")
q9 = Question("Кто выиграл последний мажор в кс го?","Нави", "Виртус про","Гамбит","Хероик")
q10 = Question("Кто нынешний президент РФ?","Путин", "Майкл Джордан","Симпл","Медведев")
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)
question_list.append(q9)
question_list.append(q10)
answers=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    label2.setText(q.right_answer) 
    show_question() 

def show_correct(res):
    label1.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print("Статистика:",main_win.score,"\nРейтинг",main_win.score/main_win.total*100)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            print("Статистика:",main_win.score,"\nРейтинг",main_win.score/main_win.total*100)
            show_correct('Неверно!')


def next_question():
    main_win.total += 1
    print("Всего Вопросов:",main_win.total)
    cur_question = randint(0,len(question_list)-1)
    
    if cur_question >= len(question_list):
        cur_question = 0
    q = question_list[cur_question]
    ask(q)    

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()       




main_win.total = 0
main_win.score = 0



button.clicked.connect(click_OK)


next_question()    

main_win.show()
app.exec_()