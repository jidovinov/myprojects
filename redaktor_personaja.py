import random
gender = ["Мужской", "Женский"]  # Пол персонажа
age = ["Подросток", "Взрослый", "Пожилой"]  # Возраст персонажа
body_type = ["Худой","Накаченный","Толстый","Дрищеватый"] # Телосложение
# 1-я трудность. Сделаем выбор телосложения неограниченным и заменяемым на любые значения # Done
skin_color = ["Светлый", "Смуглый", "Темный"] # Цвет кожи
hairstyle_female = ["Каре","Пикси","Кроп","Каскад"] # Прическа женская
hairstyle_male = ["Полубокс","Канадка","Ирокез","Гранж"] # Прическа мужская
haircolor = ["Блонд","Коричневый","Черный","Рыжий","Седой"] # Цвет волос
# 2-я трудность. В моей программе при выборе возраста - пожилой, цвет волос будет автоматически седым # Done
top_cloth_male = ["Футболка","Рубашка","Водолазка","Толстовка"] # Верх тела женская
top_cloth_female = ["Топик","Футболка","Майка","Худи"] # Верх тела мужская
middle_cloth_male = ["Спортивные штаны","Брюки","Шорты","Джинсы"] # Середина тела мужская
middle_cloth_female = ["Юбка","Джинсы","Легенсы","Брюки"] # Середина тела женская
shoes_male = ["Кеды","Ботинки","Тапки","Кроссовки"] # Обувь мужская
shoes_female = ["Басоножки","Туфли","Каблуки","Сандали"] # Обувь женская
accessories_male = ["Цепочка","Часы","Браслет"] # Аксессуары мужские
accessories_female = ["Очки","Ожерелье","Сережки"] # Аксессуры женские
# 3-я трудность. Постараюсь сделать так, что бы можно было выбрать несколько аксессуаров # Done
ready_check = ["Да","Нет"]
ready_check_first = ["Да", "Нет", "Сгенерировать случайно"]
haircolor_unlock = True
acc_check = False
choosing_acc_unclock = False
random_unlock = None
####################### КОД #######################
print("Привет, давай создадим с тобой персонажа!\nДля начала хорошо подумай, кого ты хочешь создать?")
print("Я буду набрасывать варианты, тебе остаётся выбрать, что ближе душе.")
print("Производи выбор при помощи цифр, этого будет достаточно.")
print("Ты готов?")
while True:
    print(ready_check_first)
    user_ready_check = input("")
    if user_ready_check == "1":
        random_unlock = False
        break
    elif user_ready_check == "2":
        print("Хорошо, как будешь готов - дай знать.")
        break
    elif user_ready_check == "3":
        random_unlock = True
        break
    else:
        print("Не могу понять, что ты выбрал, попробуй ещё раз")
if random_unlock == False:
    print("Давай определимся - какого пола будет твой персонаж")
    while True:
        print(gender)
        user_gender = input("")
        if user_gender == "1":
            hairstyle_female.clear()
            top_cloth_female.clear()
            middle_cloth_female.clear()
            shoes_female.clear()
            accessories_female.clear()
            break
        elif user_gender == "2":
            hairstyle_male.clear()
            top_cloth_male.clear()
            middle_cloth_male.clear()
            shoes_male.clear()
            accessories_male.clear()
            break
        else:
            print("Не могу понять, что ты выбрал, попробуй ещё раз")
    print("Определим возраст твоего персонажа")
    while True:
        print(age)
        user_age = input("")
        if user_age == "1" or user_age == "2":
            break
        elif user_age == "3":
            haircolor_unlock = False
            break
        else:
            print("Не могу понять, что ты выбрал, попробуй ещё раз")
    print("Выберем телосложение твоему персонажу")
    while True:
        print(body_type)
        user_body_type = input("")
        len_body_type = len(body_type)
        try:
            if int(user_body_type) <= int(len_body_type):
                break
            else:
                print("Не могу понять, что ты выбрал, попробуй ещё раз")
        except ValueError:
            print("Не могу понять, что ты выбрал, попробуй ещё раз")
    print("Нужно понять, какой цвет кожи будет у твоего персонажа?")
    while True:
        print(skin_color)
        user_skin_color = input("")
        if user_skin_color == "1" or user_skin_color == "2" or user_skin_color == "3":
            break
        else:
            print("Не могу понять, что ты выбрал, попробуй ещё раз")
    print("Давай выберем прическу твоему персонажу")
    while True:
        print(hairstyle_male + hairstyle_female)
        hairstyle = hairstyle_female + hairstyle_male
        user_hairstyle = input("")
        if user_hairstyle == "1" or user_hairstyle == "2" or user_hairstyle == "3" or user_hairstyle == "4":
            break
        else:
            print("Не могу понять, что ты выбрал, попробуй ещё раз")
    while haircolor_unlock == True:
        print("Теперь выберем цвет для волос")
        print(haircolor)
        user_haircolor = input("")
        if user_haircolor == "1" or user_haircolor == "2" or user_haircolor == "3" or user_haircolor == "4" or user_haircolor == "5":
            break
        else:
            print("Не могу понять, что ты выбрал, попробуй ещё раз")
    print("Теперь будем наряжать нашего персонажа")
    print("Выбирай, что будет сверху")
    while True:
        top_cloth = top_cloth_male + top_cloth_female
        print(top_cloth)
        user_top_cloth = input("")
        try:
            if int(user_top_cloth) <= 4:
                break
            else:
                print("Не могу понять, что ты выбрал, попробуй ещё раз")
        except ValueError:
            print("Не могу понять, что ты выбрал, попробуй ещё раз")
    print("Выбирай, что будет снизу?")
    while True:
        middle_cloth = middle_cloth_male + middle_cloth_female
        print(middle_cloth)
        user_middle_cloth = input("")
        try:
            if int(user_middle_cloth) <= 4:
                break
            else:
                print("Не могу понять, что ты выбрал, попробуй ещё раз")
        except ValueError:
            print("Не могу понять, что ты выбрал, попробуй ещё раз")
    print("Выбирай обувь?")
    while True:
        shoes = shoes_male + shoes_female
        print(shoes)
        user_shoes = input("")
        try:
            if int(user_shoes) <= 4:
                break
            else:
                print("Не могу понять, что ты выбрал, попробуй ещё раз")
        except ValueError:
            print("Не могу понять, что ты выбрал, попробуй ещё раз")
    print("Желаешь ли добавить аксессуары?")
    while True:
        print(ready_check)
        user_ready_check = input("")
        if user_ready_check == "1":
            choosing_acc_unclock = True
            acc_check = True
            acc = accessories_male + accessories_female
            choosing_acc = []
            break
        elif user_ready_check == "2":
            acc_check = False
            break
        else:
            print("Не могу понять, что ты выбрал, попробуй ещё раз")
    if acc_check == True:
        print("Выбирай:")
        while len(choosing_acc) < 3 and acc_check == True:
            print(acc)
            user_acc = input("")
            if user_acc == "1":
                a = (int(user_acc)-1)
                choosing_acc.append(acc[a])
                acc.pop(a)
                if len(choosing_acc) < 3:
                    print("Желаешь добавить ещё?")
                while len(choosing_acc) < 3:
                    print(ready_check)
                    user_ready_check = input("")
                    if user_ready_check == "1":
                        acc_check = True
                        break
                    elif user_ready_check == "2":
                        acc_check = False
                        break
                    else:
                        print("Не могу понять, что ты выбрал, попробуй ещё раз")
            elif user_acc == "2":
                a = (int(user_acc)-1)
                choosing_acc.append(acc[a])
                acc.pop(a)
                if len(choosing_acc) < 3:
                    print("Желаешь добавить ещё?")
                while len(choosing_acc) < 3:
                    print(ready_check)
                    user_ready_check = input("")
                    if user_ready_check == "1":
                        acc_check = True
                        break
                    elif user_ready_check == "2":
                        acc_check = False
                        break
                    else:
                        print("Не могу понять, что ты выбрал, попробуй ещё раз")
            elif user_acc == "3":
                a = (int(user_acc)-1)
                choosing_acc.append(acc[a])
                acc.pop(a)
                if len(choosing_acc) < 3:
                    print("Желаешь добавить ещё?")
                while len(choosing_acc) < 3:
                    print(ready_check)
                    user_ready_check = input("")
                    if user_ready_check == "1":
                        acc_check = True
                        break
                    elif user_ready_check == "2":
                        acc_check = False
                        break
                    else:
                        print("Не могу понять, что ты выбрал, попробуй ещё раз")
            else:
                print("Не понимаю, что происходит")
    print("Осталось назвать твоего персонажа:")
    user_name = input("")
if random_unlock == True:
    while True:
        len_gender = len(gender)
        random_gender = random.randint(1, int(len_gender))
        if random_gender == 1:
            hairstyle_female.clear()
            top_cloth_female.clear()
            middle_cloth_female.clear()
            shoes_female.clear()
            accessories_female.clear()
            break
        elif random_gender == 2:
            hairstyle_male.clear()
            top_cloth_male.clear()
            middle_cloth_male.clear()
            shoes_male.clear()
            accessories_male.clear()
            break
    while True:
        len_age = len(age)
        random_age = random.randint(1, int(len_age))
        if random_age == 1:
            break
        elif random_age == 2:
            break
        elif random_age == 3:
            haircolor_unlock = False
            break
    while True:
        len_body_type = len(body_type)
        random_body_type = random.randint(1, int(len_body_type))
        if int(random_body_type) <= int(len_body_type):
            break
    while True:
        len_skin_color = len(skin_color)
        random_skin_color = random.randint(1, int(len_skin_color))
        if random_skin_color == 1 or random_skin_color == 2 or random_skin_color == 3:
            break
    while True:
        hairstyle = hairstyle_female + hairstyle_male
        len_hairstyle = len(hairstyle)
        random_hairstyle = random.randint(1, int(len_hairstyle))
        if random_hairstyle <= len_hairstyle:
            break
    while haircolor_unlock == True:
        len_haircolor = len(haircolor)
        random_haircolor = random.randint(1, int(len_haircolor))
        if random_haircolor <= 5:
            break
    while True:
        top_cloth = top_cloth_male + top_cloth_female
        len_top_cloth = len(top_cloth)
        random_top_cloth = random.randint(1, int(len_top_cloth))
        if random_top_cloth <= 4:
            break
    while True:
        middle_cloth = middle_cloth_male + middle_cloth_female
        len_middle_cloth = len(middle_cloth)
        random_middle_cloth = random.randint(1, int(len_middle_cloth))
        if random_middle_cloth <= 4:
            break
    while True:
        shoes = shoes_male + shoes_female
        len_shoes = len(shoes)
        random_shoes = random.randint(1, int(len_shoes))
        if random_shoes <= 4:
            break
    while True:
        random_ready_check = random.randint(1, 2)
        if random_ready_check == 1:
            choosing_acc_unclock = True
            acc_check = True
            acc = accessories_male + accessories_female
            choosing_acc = []
            break
        elif random_ready_check == 2:
            acc_check = False
            break
    if acc_check == True:
        while len(choosing_acc) < 3 and acc_check == True:
            len_acc = len(acc)
            random_acc = random.randint(1, int(len_acc))
            if random_acc == 1:
                a = (int(random_acc) - 1)
                choosing_acc.append(acc[a])
                acc.pop(a)
                while len(choosing_acc) < 3:
                    random_ready_check = random.randint(1, 2)
                    if random_ready_check == 1:
                        acc_check = True
                        break
                    elif random_ready_check == 2:
                        acc_check = False
                        break
            elif random_acc == 2:
                a = (int(random_acc) - 1)
                choosing_acc.append(acc[a])
                acc.pop(a)
                while len(choosing_acc) < 3:
                    random_ready_check = random.randint(1, 2)
                    if random_ready_check == 1:
                        acc_check = True
                        break
                    elif random_ready_check == 2:
                        acc_check = False
                        break
            elif random_acc == 3:
                a = (int(random_acc) - 1)
                choosing_acc.append(acc[a])
                acc.pop(a)
                while len(choosing_acc) < 3:
                    random_ready_check = random.randint(1, 2)
                    if random_ready_check == 1:
                        acc_check = True
                        break
                    elif random_ready_check == 2:
                        acc_check = False
                        break
################## ИТОГО ##################
if random_unlock == False:
    print("Давай покажу характеристика твоего персонажа:")
    print("Имя:", user_name)
    print("Пол:", gender[int(user_gender)-1])
    print("Возраст:", age[int(user_age)-1])
    print("Телосложение:", body_type[int(user_body_type)-1])
    print("Цвет кожи:", skin_color[int(user_skin_color)-1])
    print("Прическа:", hairstyle[int(user_hairstyle)-1])
    if haircolor_unlock == True:
        print("Цвет волос:", haircolor[int(user_haircolor)-1])
    else:
        print("Цвет волос:", haircolor[4])
    print("  Одежда\nСверху:", top_cloth[int(user_top_cloth)-1],"\nСнизу:", middle_cloth[int(user_middle_cloth)-1])
    print("Обувь:", shoes[int(user_shoes)-1])
    if choosing_acc_unclock == True:
        print("  Аксессуары", *choosing_acc, sep="\n")
if random_unlock == True:
    print("Давай покажу характеристика твоего персонажа:")
    print("Пол:", gender[int(random_gender)-1])
    print("Возраст:", age[int(random_age)-1])
    print("Телосложение:", body_type[int(random_body_type)-1])
    print("Цвет кожи:", skin_color[int(random_skin_color)-1])
    print("Прическа:", hairstyle[int(random_hairstyle)-1])
    if haircolor_unlock == True:
        print("Цвет волос:", haircolor[int(random_haircolor)-1])
    else:
        print("Цвет волос:", haircolor[4])
    print(" ~Одежда~")
    print("Сверху:", top_cloth[int(random_top_cloth) - 1])
    print("Снизу:", middle_cloth[int(random_middle_cloth)-1])
    print("Обувь:", shoes[int(random_shoes) - 1])
    if choosing_acc_unclock == True:
        print(" ~Аксессуары~", *choosing_acc, sep="\n")