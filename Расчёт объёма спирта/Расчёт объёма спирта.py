from tkinter import *

#Главное окно программы
root = Tk()
root.resizable(width=False, height=False)
root.geometry('450x325')
root.title('Расчёт объёма спирта 1.0')

try:
    #Ставим иконку для заголовка приложения
    root.iconbitmap(r'alc.ico')
except:
    #Если иконки в каталоге нет, то ничего не делаем
    pass

#Виртуальаня картинка для задания размера кнопок в пикселях
pixelVirtual = PhotoImage(width=1, height=1)

#Заголовок окна, не путать с заголовком программы
lable=Label(root, text='Расчёт объёма спирта', width=50, fg="red", bg="black", font="Atial 16")
lable.pack()

#Ввод данных
#Введите начальный объём Алкоголя в МЛ
lable1=Label(root, text='Введите начальный объём Алкоголя в МЛ', fg="black", font="Atial 14")
lable1.pack()
lable1.place(relx=0.01, rely=0.1)

EntryA = Entry(root, width=10, font='Arial 16')
EntryA.pack()
EntryA.place(relx=0.01, rely=0.19)

#Укажите текущую крепость
lable2=Label(root, text='Укажите текущую крепость', fg="black",font="Atial 14")
lable2.pack()
lable2.place(relx=0.01, rely=0.27)

EntryB = Entry(root, width=10, font='Arial 16')
EntryB.pack()
EntryB.place(relx=0.01, rely=0.37)

#Укажите, какую в итоге крепость хотите получить
lable3=Label(root, text='Укажите, какую в итоге крепость хотите получить', fg="black", font="Atial 14")
lable3.pack()
lable3.place(relx=0.01, rely=0.45)

EntryC = Entry(root, width=10, font='Arial 16')
EntryC.pack()
EntryC.place(relx=0.01, rely=0.55)

#Результат в МЛ (добавить\убавить)
lable4=Label(root, text="Результат в МЛ (добавить\убавить)", fg="black", font="Atial 14")
lable4.pack()
lable4.place(relx=0.01, rely=0.75)

EntryD = Entry(root, width=10, font='Arial 16')
EntryD.pack()
EntryD.place(relx=0.01, rely=0.85, width=200)

#Расчёт данных
def koef(event):
    a = EntryA.get() # берем текст из первого поля: Введите начальный объём Алкоголя в МЛ
    a = int(a) # преобразуем в число целого типа

    b = EntryB.get() # берем текст из второго поля: Укажите текущую крепость
    b = int(b) # преобразуем в число целого типа

    d = EntryC.get() # берем текст из второго поля: Укажите, какую в итоге крепость хотите получить
    d = int(d) # преобразуем в число целого типа

    result = int((((((a/100) * b) / d) * 100))-a) #Сама формула для разбавления спирта водой
    EntryD.delete(0, END) # очищаем текстовое поле полностью
    EntryD.insert(0, result) # вставляем результат в начало 

# Функция отчистки всех полей ввода
def clear(event):
    EntryA.delete(0, END) # берем текст из первого поля: Введите начальный объём Алкоголя в МЛ
    EntryB.delete(0, END) # берем текст из второго поля: Укажите текущую крепость
    EntryC.delete(0, END) # берем текст из второго поля: Укажите, какую в итоге крепость хотите получить
    EntryD.delete(0, END) # очищаем текстовое поле полностью

#Запуск окна справки
def reference(event):
    root1 = Tk()
    root1.resizable(width=False, height=False)
    root1.geometry('300x300')
    root1.title('Справка')
    root1.focus_force()

#Закрыть главное окно
def exit_root(event):
    root.quit()

#Расчёт по заданным параметрам
button=Button(root, text='Рассчитать', fg="black", font="Atial 10")
button.pack()
button.bind("<Button>", koef)
button.place(relx=0.01, rely=0.66)

#Привязываем кнопку Enter, чтобу запускать Расчёт.
root.bind('<Return>',koef)
#Привязываем кнопку Delete чтобы отчищать все строки
root.bind('<Delete>',clear)
#Вызов окна справки
root.bind('<F1>', reference)
#Закрыть главное окно и все дочерние окна через ESC
root.bind('<Escape>', exit_root)
#Закрыть главное окно и все дочерние окна через крестик на форме
root.bind('<Destroy>', exit_root)

#Отчистка всех полей
button1=Button(root, text='Очистить', fg="black", font="Atial 10")
button1.pack()
button1.bind("<Button>", clear)
button1.place(relx=0.2, rely=0.66)

#Справка
button2=Button(root, text='Справка', fg="black", font="Atial 10")
button2.pack()
button2.bind("<Button>", reference)
button2.place(relx=0.36, rely=0.66)

root.mainloop()
