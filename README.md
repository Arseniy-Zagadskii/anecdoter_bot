# Автоматизированная отправка анекдотов по графику в телеграм канал или личный чат


## Зависимости

Для корректной работы кода рекомендуем 
использовать Python 3.9 и модули с их точными 
версиями указанными в `requirements.txt`.


## Установка

Данная инструкция предназначена для ОС Windows.
Советуем провести установку в виртуальной среде:

```
python -m venv C:\anecdoter_bot
source venv/bin/activate
pip install --require-hashes -r requirements.txt
```
Всё готово!


## Запуск

Нужно собрать своего бота для отладки и 
тестирования. Для этого перейдите в телеграме к 
`@BotFather` и следуйте инструкциям. После получения
токена бота скопируйте его значение в переменную
`bot_token` на 29 строчке и в параметр `Telebot` на 10 
строчке. После этого получите свой chatid, например 
у бота `@myidbot` и вставьте его значение в переменную 
`bot_chatID` на 30 строчке. Этот параметр настраивает, 
кому будут отправлены сообщения. В частности, это 
может быть канал. Запуск бота можно выполнить как из 
консоли, так и из IDE.


## Дисклеймер

Это код свободного доступа и никто не обязуется его 
поддерживать или обновлять. Код бота можно запустить
на удаленном сервере, возможно с некоторыми модификациями.
