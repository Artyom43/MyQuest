import person
import room
import bathroom
import Kitchen

Locations = ['в комнату', 'в умывальную комнату', 'на кухню']
Loc = {
    0: room,
    1: bathroom,
    2: Kitchen
}
CurL = 0
WhatIDid = []

me = person.Person()
tasks = 0


def ItScenario():  # Собственно, сценарий
    global tasks
    if 'Взять ведро' in WhatIDid:
        text1.insert(1.0, 'Так, ведро есть. Но с пустым ведром полы не помоешь, так ведь?')
        bathroom.Doings.append('Набрать воду в ведро')
        Kitchen.Doings.append('Набрать воду в ведро')
        me.inventory.append('Ведро')
        WhatIDid.remove('Взять ведро')

    if 'Набрать воду в ведро' in WhatIDid and CurL == 2:
        text1.insert(1.0, 'Итак, ведро с водой у тебя есть, а швабра стоит в комнате - этого более чем достаточно,'
                          'чтобы вымыть полы!')
        room.Doings.append('Помыть полы')
        me.inventory.remove('Ведро')
        me.inventory.append('Ведро с водой')
        if 'Набрать воду в ведро' in bathroom.Doings:
            bathroom.Doings.remove('Набрать воду в ведро')
        WhatIDid.remove('Набрать воду в ведро')

    if 'Набрать воду в ведро' in WhatIDid and CurL == 1:
        text1.insert(1.0, 'Да что же такое, ни одной рабочей раковины в умывалке!'
                          'Придется набрать воду где-то еще.')

    if 'Помыть полы' in WhatIDid:
        text1.insert(1.0,'Впервые с твоего заселения в общежитие полы были вымыты.'
                         ' Они оказались светлее, чем ты думал')
        me.time -= 30
        WhatIDid.remove('Помыть полы')
        me.inventory.remove('Ведро с водой')
        me.tasks.remove('Помыть полы')
        tasks += 1

    if 'Подойти к столу' in WhatIDid:
        text1.insert(1.0, 'К твоему удивлению, на столе не стоит не одной грязной тарелки или чашки. Но не потому, что '
                          'ты моешь все сразу после еды - просто ты как обычно оставил все на кухне. Конечно, есть '
                          'вероятность, что при обходе это не заметят, но лучше не рисковать.')
        Kitchen.Doings.append('Помыть посуду')
        WhatIDid.remove('Подойти к столу')

    if 'Помыть посуду' in WhatIDid:
        text1.insert(1.0, "Так-то лучше. Теперь лучше перенести все в комнату, чтобы было видно, что я действительно"
                          " помыл посуду.")
        me.tasks.append('Принести посуду в комнату')
        room.Doings.append('Положить тарелку в шкаф')
        room.Doings.append('Поставить кружку на стол')
        me.tasks.remove('Помыть посуду')
        me.inventory.append('Тарелка')
        me.inventory.append('Кружка')
        WhatIDid.remove('Помыть посуду')
        me.time -= 10
        tasks += 1

    if 'Положить тарелку в шкаф' in WhatIDid and not 'Поставить кружку на стол' in WhatIDid:
        text1.insert(1.0, 'Давно, она тут не стояла. Надо потом не забыть, что она здесь.')
        me.inventory.remove('Тарелка')
        me.time -= 5

    if 'Поставить кружку на стол' in WhatIDid and not 'Положить тарелку в шкаф' in WhatIDid:
        text1.insert(1.0, 'Теперь нужно не пить из нее до обхода, чтобы не испортить видимость чистоты.')
        me.inventory.remove('Кружка')
        me.time -= 5

    if 'Поставить кружку на стол' in WhatIDid and 'Положить тарелку в шкаф' in WhatIDid:
        text1.insert(1.0, 'Ну, все на своих местах. в теории.')
        me.inventory.remove('Кружка')
        WhatIDid.remove('Поставить кружку на стол')
        WhatIDid.remove('Положить тарелку в шкаф')
        me.tasks.remove('Принести посуду в комнату')
        tasks += 1

    if me.time <= 0:
        text1.delete(1.0, END)
        button1.destroy()
        button2.destroy()
        text2.destroy()
        frame2.destroy()
        frame3.destroy()
        frame4.destroy()
        for item in Butt:
            item.destroy()
        for item in frame:
            item.destroy()
        text1.insert(1.0, 'Что ж, ты не успел убраться. Так бывает. В последние секунды перед парой '
                          'ты накинул куртку, схватил первые попавшиеся тетрадки и с надеждой на снисхождение побежал'
                          ' в ГК. Ты еще не знал, что коменда не прощает таких ошибок\n\n\nВЫ ПРОИГРАЛИ')

    if tasks == 3:
        text1.delete(1.0, END)
        button1.destroy()
        button2.destroy()
        text2.destroy()
        frame2.destroy()
        frame3.destroy()
        frame4.destroy()
        for item in Butt:
            item.destroy()
        for item in frame:
            item.destroy()
        text1.insert(1.0, 'Ты успешно справился с очисткой комнаты.В последние секунды перед парой '
                          'ты накинул куртку, схватил первые попавшиеся тетрадки и побежал в ГК с полной уверенностью'
                          ', что тебя не выселят. Хотя бы до следующего обхода.\n\n\nВЫ ВЫИГРАЛИ')


from tkinter import *
root = Tk()
root.title('my game')


root.geometry('900x600+200+0')

frame1 = Frame(root, bg='blue', bd=2)
frame2 = Frame(root, bg='red', bd=2)
frame3 = Frame(root, bg='green', bd=2)
frame4 = Frame(root, bg='green', bd=2)


text1 = Text(frame1, height=25, width=50, font='SemiBold 12', wrap=WORD)
text1.insert(1.0,"Проснувшись, ты выбрался из-под одеяла и горы вещей, которые тебе в очередной раз было лень убирать"
                 " в шкаф. Солнце стояло уже высоко, а ты чувствовал себя как никогда выспавшимся. Не успел ты"
                 " об этом подумать, как к тебе пришло понимание происходящего: ты проспал первые две пары. Хорошо, что"
                 " это были лекции, и ты ничего важного не пропустил. До следующей пары у тебя остается еще час - более"
                 ", чем достаточно, чтобы ещё чуть-чуть поспать. Но не успел ты лечь обратно под кучу одежды, как "
                 "в памяти возник образ коменды. Тон, с которым она говорила о состоянии вашей комнаты, "
                 "ясно давал понять: если во время сегодняшнего обхода комната будет выглядеть так же, то завтра "
                 "тебе придется искать новое место для жилья. И как на зло, обход начинался за 30 минут до окончания "
                 "последней пары. Значит, принимать меры стоит уже сейчас - одного часа должно хватить чтобы привести "
                 "все к состоянию хотя бы чуть ниже среднего.\n\n"
                 '*Звуки разрушения четвертой стены*\nОбрати внимание, на перемещение между локациями ты тратишь 5'
                 ' игровых минут. Сколько времени займут другие действия - загадка, призванная привнести хоть немного '
                 'интриги в игру :) \nОднако, действуй с умом, - времени очень и очень мало!')

i = 4.0
text2=Text(frame2, height=25, width=30, font='SemiBold 12', wrap=WORD)
text2.insert(2.0, 'оставшееся время: {} минут\n'.format(me.time))
text2.insert(3.0, 'задачи: \n')
for item in me.tasks:
    text2.insert(i, '           {}\n'.format(item))
    i += 1
text2.insert(i, 'инвентарь: \n')
for item in me.inventory:
    text2.insert(i, '           {}\n'.format(item))
    i += 1


Butt = []
frame = []


def ButtGenerator():
    for frames in frame:
        frames.destroy()
    frame.clear()
    for button in Butt:
        button.destroy()
    Butt.clear()
    for it in range(len(Loc[CurL].Doings)):
        frame.append(Frame(root, bg='green', bd=2))

        def ButtClick(j):
            text1.delete(1.0, END)
            text2.delete(1.0, END)
            if not Loc[CurL].Doings[j] in WhatIDid:
                WhatIDid.append(Loc[CurL].Doings[j])
            Loc[CurL].Doings[j] = ''
            Butt[j].destroy()
            frame[j].destroy()
            j -= 1

            ItScenario()

            k = 4.0
            text2.insert(2.0, 'оставшееся время: {} минут\n'.format(me.time))
            text2.insert(3.0, 'задачи: \n')
            for item in me.tasks:
                text2.insert(k, '           {}\n'.format(item))
                k += 1
            text2.insert(k, 'инвентарь: \n')
            k += 1
            for item in me.inventory:
                text2.insert(k, '           {}\n'.format(item))
                k += 1
            print(room.Doings, bathroom.Doings, Kitchen.Doings, WhatIDid, me.inventory)

        Butt.append(Button(frame[it], text='{}'.format(Loc[CurL].Doings[it]), command=lambda j=it: ButtClick(j)))
        frame[it].grid(row=it + 3, column=0)
        Butt[it].grid(row=it + 4, column=0)


def button_clicked_1():
    text1.delete('1.0', END)
    text2.delete('1.0', END)
    global CurL
    ItScenario()
    ii = 0
    while ii < len(Loc[CurL].Doings):
        if Loc[CurL].Doings[ii] == '':
            del Loc[CurL].Doings[ii]
        else:
            ii += 1
    CurL = (CurL + 1) % 3
    button1['text'] = 'Пойти {}'.format(Locations[(CurL + 1) % 3])
    button2['text'] = 'Пойти {}'.format(Locations[(CurL + 2) % 3])

    ButtGenerator()
    me.time -= 5

    text1.insert(1.0, '{}'.format(Loc[CurL].Text))

    k = 4.0
    text2.insert(2.0, 'оставшееся время: {} минут\n'.format(me.time))
    text2.insert(3.0, 'задачи: \n')
    for item in me.tasks:
        text2.insert(k, '           {}\n'.format(item))
        k += 1
    text2.insert(k, 'инвентарь: \n')
    k += 1
    for item in me.inventory:
        text2.insert(k, '           {}\n'.format(item))
        k += 1
    print(room.Doings, bathroom.Doings, Kitchen.Doings, WhatIDid, me.inventory)


def button_clicked_2():
    text1.delete(1.0, END)
    text2.delete(1.0, END)
    global CurL
    ItScenario()
    ii = 0
    while ii < len(Loc[CurL].Doings):
        if Loc[CurL].Doings[ii] == '':
            del Loc[CurL].Doings[ii]
        else:
            ii += 1
    CurL = (CurL + 2) % 3
    ButtGenerator()
    button1['text'] = 'Пойти {}'.format(Locations[(CurL + 1) % 3])
    button2['text'] = 'Пойти {}'.format(Locations[(CurL + 2) % 3])

    text1.insert(1.0, '{}'.format(Loc[CurL].Text))

    me.time -= 5
    k = 4.0
    text2.insert(2.0, 'оставшееся время: {} минут\n'.format(me.time))
    text2.insert(3.0, 'задачи: \n')
    for item in me.tasks:
        text2.insert(k, '           {}\n'.format(item))
        k += 1
    text2.insert(k, 'инвентарь: \n')
    k += 1
    for item in me.inventory:
        text2.insert(k, '           {}\n'.format(item))
        k += 1

    print(room.Doings, bathroom.Doings, Kitchen.Doings, WhatIDid, me.inventory)


button1 = Button(frame3, text='Пойти в умывальную комнату', command=button_clicked_1)
button2 = Button(frame4, text='Пойти на кухню', command=button_clicked_2)
ButtGenerator()


frame1.grid(row=0, column=0)
frame2.grid(row=0, column=2)
frame3.grid(row=1, column=0)
frame4.grid(row=2, column=0)
text1.grid(row=0, column=0)
text2.grid(row=0, column=1)
button1.grid(row=2, column=0)
button2.grid(row=2, column=1)


root.mainloop()



