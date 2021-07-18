import telebot
import config
import requests
from datetime import datetime
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.KeyboardButton("🇷🇺Рубль🇷🇺")
    i2 = types.KeyboardButton("💲Доллар💲")
    i3 = types.KeyboardButton("🆙Биткоин🆙")
    i4 = types.KeyboardButton("🌯Эфириум🌯")
    i5 = types.KeyboardButton("🤑Tether🤑")
    i6 = types.KeyboardButton("✡Binance Coin✡")
    i7 = types.KeyboardButton("🐕Dogecoin🐕")
    i8 = types.KeyboardButton("🪙Litecoin🪙")
    markup.add(i1, i2, i3, i4, i5, i6, i7, i8)

    bot.send_message(message.chat.id, "Приветствую тебя, {0.first_name}! Меня зовут Дуболом. Я бот, созданный, чтобы помочь тебе упростить слежение за курсом криптовалют.\nВыбери имеющуюся валюту:".format(
        message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🇷🇺Рубль🇷🇺':
            markup = types.InlineKeyboardMarkup(row_width=2)
            i2 = types.InlineKeyboardButton("Доллар", callback_data='usd_rur')
            i3 = types.InlineKeyboardButton("Биткоин", callback_data='btc_rur')
            i4 = types.InlineKeyboardButton("Эфириум", callback_data='eth_rur')
            i5 = types.InlineKeyboardButton("Tether", callback_data='rur_usdt')
            i6 = types.InlineKeyboardButton(
                "Binance Coin", callback_data='bnb_rur')
            i7 = types.InlineKeyboardButton(
                "Dogecoin", callback_data='doge_rur')
            i8 = types.InlineKeyboardButton(
                "Litecoin", callback_data='ltc_rur')
            markup.add(i2, i3, i4, i5, i6, i7, i8)

            bot.send_message(
                message.chat.id, 'Теперь выбери из списка ниже вторую валюту. Я отправлю курс 🇷🇺Рубль🇷🇺? к этой валюте.', reply_markup=markup)
        elif message.text == '💲Доллар💲':
            markup = types.InlineKeyboardMarkup(row_width=2)
            i1 = types.InlineKeyboardButton("Рубль", callback_data='usd_rur')
            i3 = types.InlineKeyboardButton("Биткоин", callback_data='btc_usd')
            i4 = types.InlineKeyboardButton("Эфириум", callback_data='eth_usd')
            i5 = types.InlineKeyboardButton("Tether", callback_data='usd_usdt')
            i6 = types.InlineKeyboardButton(
                "Binance Coin", callback_data='bnb_usd')
            i7 = types.InlineKeyboardButton(
                "Dogecoin", callback_data='doge_usd')
            i8 = types.InlineKeyboardButton(
                "Litecoin", callback_data='ltc_usd')
            markup.add(i1, i3, i4, i5, i6, i7, i8)

            bot.send_message(
                message.chat.id, 'Теперь выбери из списка ниже вторую валюту. Я отправлю курс 💲Доллар💲 к этой валюте.', reply_markup=markup)
        elif message.text == '🆙Биткоин🆙':
            markup = types.InlineKeyboardMarkup(row_width=2)
            i1 = types.InlineKeyboardButton("Рубль", callback_data='btc_rur')
            i2 = types.InlineKeyboardButton("Доллар", callback_data='btc_usd')
            i4 = types.InlineKeyboardButton("Эфириум", callback_data='eth_btc')
            i5 = types.InlineKeyboardButton("Tether", callback_data='btc_usdt')
            i6 = types.InlineKeyboardButton(
                "Binance Coin", callback_data='bnb_btc')
            i7 = types.InlineKeyboardButton(
                "Dogecoin", callback_data='doge_btc')
            i8 = types.InlineKeyboardButton(
                "Litecoin", callback_data='ltc_btc')
            markup.add(i1, i2, i4, i5, i6, i7, i8)

            bot.send_message(
                message.chat.id, 'Теперь выбери из списка ниже вторую валюту. Я отправлю курс 🆙Биткоин🆙 к этой валюте.', reply_markup=markup)
        elif message.text == '🌯Эфириум🌯':
            markup = types.InlineKeyboardMarkup(row_width=2)
            i1 = types.InlineKeyboardButton("Рубль", callback_data='eth_rur')
            i2 = types.InlineKeyboardButton("Доллар", callback_data='eth_usd')
            i3 = types.InlineKeyboardButton("Биткоин", callback_data='eth_btc')
            i5 = types.InlineKeyboardButton("Tether", callback_data='eth_usdt')
            i6 = types.InlineKeyboardButton(
                "Binance Coin", callback_data='bnb_eth')
            i7 = types.InlineKeyboardButton(
                "Dogecoin", callback_data='eth_doge')
            i8 = types.InlineKeyboardButton(
                "Litecoin", callback_data='ltc_eth')
            markup.add(i1, i2, i3, i5, i6, i7, i8)

            bot.send_message(
                message.chat.id, 'Теперь выбери из списка ниже вторую валюту. Я отправлю курс 🌯Эфириум🌯 к этой валюте.', reply_markup=markup)
        elif message.text == '🤑Tether🤑':
            markup = types.InlineKeyboardMarkup(row_width=2)
            i1 = types.InlineKeyboardButton("Рубль", callback_data='usdt_rur')
            i2 = types.InlineKeyboardButton("Доллар", callback_data='usdt_usd')
            i3 = types.InlineKeyboardButton(
                "Биткоин", callback_data='usdt_btc')
            i4 = types.InlineKeyboardButton(
                "Эфириум", callback_data='usdt_eth')
            i6 = types.InlineKeyboardButton(
                "Binance Coin", callback_data='bnb_usdt')
            i7 = types.InlineKeyboardButton(
                "Dogecoin", callback_data='usdt_doge')
            i8 = types.InlineKeyboardButton(
                "Litecoin", callback_data='ltc_usdt')
            markup.add(i1, i2, i3, i4, i6, i7, i8)

            bot.send_message(
                message.chat.id, 'Теперь выбери из списка ниже вторую валюту. Я отправлю курс 🤑Tether🤑 к этой валюте.', reply_markup=markup)
        elif message.text == '✡Binance Coin✡':
            markup = types.InlineKeyboardMarkup(row_width=2)
            i1 = types.InlineKeyboardButton("Рубль", callback_data='bnb_rur')
            i2 = types.InlineKeyboardButton("Доллар", callback_data='bnb_usd')
            i3 = types.InlineKeyboardButton("Биткоин", callback_data='bnb_btc')
            i4 = types.InlineKeyboardButton("Эфириум", callback_data='bnb_eth')
            i5 = types.InlineKeyboardButton("Tether", callback_data='bnb_usdt')
            i7 = types.InlineKeyboardButton(
                "Dogecoin", callback_data='bnb_doge')
            markup.add(i1, i2, i3, i4, i5, i7)

            bot.send_message(
                message.chat.id, 'Теперь выбери из списка ниже вторую валюту. Я отправлю курс ✡Binance Coin✡ к этой валюте.', reply_markup=markup)
        elif message.text == '🐕Dogecoin🐕':
            markup = types.InlineKeyboardMarkup(row_width=2)
            i1 = types.InlineKeyboardButton("Рубль", callback_data='doge_rur')
            i2 = types.InlineKeyboardButton("Доллар", callback_data='doge_usd')
            i3 = types.InlineKeyboardButton(
                "Биткоин", callback_data='doge_btc')
            i4 = types.InlineKeyboardButton(
                "Эфириум", callback_data='doge_eth')
            i5 = types.InlineKeyboardButton(
                "Tether", callback_data='doge_usdt')
            i6 = types.InlineKeyboardButton(
                "Binance Coin", callback_data='bnb_doge')
            i8 = types.InlineKeyboardButton(
                "Litecoin", callback_data='ltc_doge')
            markup.add(i1, i2, i3, i4, i5, i6, i8)

            bot.send_message(
                message.chat.id, 'Теперь выбери из списка ниже вторую валюту. Я отправлю курс 🐕Dogecoin🐕 к этой валюте.', reply_markup=markup)
        elif message.text == '🪙Litecoin🪙':
            markup = types.InlineKeyboardMarkup(row_width=2)
            i1 = types.InlineKeyboardButton("Рубль", callback_data='ltc_rur')
            i2 = types.InlineKeyboardButton("Доллар", callback_data='ltc_usd')
            i3 = types.InlineKeyboardButton("Биткоин", callback_data='ltc_btc')
            i4 = types.InlineKeyboardButton("Эфириум", callback_data='ltc_eth')
            i5 = types.InlineKeyboardButton("Tether", callback_data='ltc_usdt')
            i7 = types.InlineKeyboardButton(
                "Dogecoin", callback_data='ltc_doge')
            markup.add(i1, i2, i3, i4, i5, i7)

            bot.send_message(
                message.chat.id, 'Теперь выбери из списка ниже вторую валюту. Я отправлю курс 🪙Litecoin🪙 к этой валюте.', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Что-то пошло не так...")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            slovarik = {
                "usd": "💲Доллар💲",
                "rur": "🇷🇺Рубль🇷🇺",
                "btc": "🆙Биткоин🆙",
                "eth": "🌯Эфириум🌯",
                "usdt": "🤑Tether🤑",
                "bnb": "✡Binance Coin✡",
                "doge": "🐕Dogecoin🐕",
                "ltc": "🪙Litecoin🪙"
            }
            flex = call.data
            if flex[3] == '_':
                flex1 = flex[:3]
                flex2 = flex[4:]
            else:
                flex1 = flex[:4]
                flex2 = flex[5:]
            req = requests.get("https://yobit.net/api/3/ticker/" + flex)
            response = req.json()
            sell_price = response[flex]["sell"]
            buy_price = response[flex]["buy"]
            average_price = response[flex]["avg"]
            bot.send_message(
                call.message.chat.id,
                f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nСтоимость продажи валюты " + slovarik[flex1] + f": {buy_price} " + slovarik[flex2] + ".\nСтоимость покупки валюты " + slovarik[
                    flex1] + f": {sell_price} " + slovarik[flex2] + ".\nСредняя стоимость покупки валюты " + slovarik[flex1] + f" за всё время: {average_price} " + slovarik[flex2] + "."
            )
            if sell_price / average_price < 0.99:
                bot.send_message(
                    call.message.chat.id,
                    "Стоит задуматься над покупкой валюты " +
                    slovarik[flex1] +
                    ", так как прямо сейчас валюта продаётся по заниженной цене!"
                )
            elif buy_price / average_price > 0.99:
                bot.send_message(
                    call.message.chat.id,
                    "Решать, конечно, тебе, но я бы не упустил момент и продал " +
                    slovarik[flex1] +
                    ", так как прямо сейчас валюта взлетела в цене. А может, это "
                )
            bot.send_message(
                call.message.chat.id,
                "Что-то ещё?"
            )
        # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Понял!",
                                  reply_markup=None)

    except Exception as e:
        print(repr(e))
        print("sis")


bot.polling(none_stop=True)
