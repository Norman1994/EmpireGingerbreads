label atlantic_city:

    scene atlantic_city

    "Нда... Что и говорить, это явно не тот ресторан, куда меня посылала Рита."

    "Да что уж, даже если зайду туда и скажу, что на моё имя заказано мероприятие мне дадут пинка и даже не извинятся."

    if varvara_scores > 0:

        show Varvara with dissolve

        varvara "Ну вот, ваш ресторан. Как всегда хорош!"

        varvara "Эй, а вы чего такой кислый? Не тот ресторан?"

        me "Да нет, тот. Просто... А, чего я ждал..."

        varvara "Простите?"
        
        me "Не важно. В любом случае, спасибо. Буду думать, что делать дальше."

        varvara "Вы разве не зайдете?"

        me "Да, зайду. Потом. Сейчас только отдохну после путешествия..."

        varvara "Ну ладно, пожалуйста."

        varvara "А, да, кстати: приходите сегодня на ужин к графу Зареченскому. Не пожалеете."

        if eva_scores > 0:

            me "Вообще то меня уже туда пригласили..."

            varvara "Ух ты, как здорово! Ну ладно, мне пора. До свидания, Сударь!"

        else:

            me "Эм... Не знаю..."

            varvara "Ну ладно, мне пора. До встречи, Сударь!"

        hide Varvara with dissolve

    else: 

        "Я чувствовал себя идиотом. Хуже того - потерянным идиотом."

        "Но паники почему-то не было. Да, к горлу подкатывала тошнота, да, кружилась голова и гулко билось сердце, но не более."

        "И на что я надеялся? Что меня встретит тот же самый ресторан из 21 века с тем же персоналом?"

        "Хотя скорее я просто хотел убедиться, что все происходящее - не мой воспаленный бред, а новая реальность."

        "Что ж. Лучше мне от этого не стало."

    jump empire_city_second

    return