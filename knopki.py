import psycopg2
from telebot import types

class Knopki:
    def __init__(self):
        self.conn = psycopg2.connect("postgres://mininuser:bGwT4IaNI2fagmpDr3i9o1xpGtWDzwPj@dpg-chqlnaqk728ivvu8etjg-a.frankfurt-postgres.render.com/users_6mql")
        self.cursor = self.conn.cursor()

    def knobut(self)-> dict:
        sql = """SELECT facultet, socr FROM facult"""
        self.cursor.execute(sql)
        result = dict()
        for socr, facultet in self.cursor.fetchall():
            result[socr] = facultet
        return result

    def inform(self, socr: str):
        sql = f"""SELECT opis FROM facult f, opis o WHERE f.facultet = %s AND f.socr LIKE o.socr"""
        self.cursor.execute(sql, (socr,))
        result = self.cursor.fetchall()
        print('result')
        return result

    def create_menu(self) -> types.ReplyKeyboardMarkup:
        btn_list = self.knobut()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for element in btn_list.items():
            markup.add(element[0])
        back = types.KeyboardButton('Назад')
        markup.add(back)
        return markup

    def infnapr(self, name: str) -> dict:
        sql = f"""SELECT n.name, n.socr FROM naprav n, cafedri c WHERE c.name = %s AND c.name_key LIKE n.cafedra"""
        self.cursor.execute(sql, (name,))
        result = dict()
        for name, socr in self.cursor.fetchall():
            result[socr] = name
        return result

    def create_napr(self, type_menu: str) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup()
        btn_list = self.infnapr(type_menu)
        for element in btn_list.items():
            btn = types.InlineKeyboardButton(text=element[1], callback_data=element[0])
            markup.add(btn)
        return markup

    def naprltinf(self, name_kay: str):
        sql = f"""SELECT o.opis FROM opis_napr o, naprav n WHERE n.socr = %s AND o.socr LIKE n.socr"""
        self.cursor.execute(sql, (name_kay,))
        result = self.cursor.fetchall()
        print('opis')
        return result

    def naprav(self, name_kay: str) -> dict:
        sql = """SELECT n.name, n.socr FROM naprav n, cafedri c WHERE c.name_key = %s AND n.cafedra LIKE c.name_key"""
        self.cursor.execute(sql, (name_kay,))
        result = dict()
        for socr, facultet in self.cursor.fetchall():
            result[socr] = facultet
        return result

    def create_naprav(self, type_menu: str) -> types.ReplyKeyboardMarkup:
        btn_list = self.naprav(type_menu)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for element in btn_list.items():
            markup.add(element[0])
        back = types.KeyboardButton('Вернуться')
        markup.add(back)
        return markup

    def faceltet(self, name_kay: str) -> dict:
        sql = """SELECT c.name, c.name_key FROM facult f, cafedri c WHERE f.facultet = %s AND f.socr LIKE c.socr"""
        self.cursor.execute(sql, (name_kay,))
        result = dict()
        for socr, facultet in self.cursor.fetchall():
            result[socr] = facultet
        return result

    def create_faceltet(self, type_menu: str) -> types.ReplyKeyboardMarkup:
        btn_list = self.faceltet(type_menu)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for element in btn_list.items():
            markup.add(element[0])
        back = types.KeyboardButton('Вернуться')
        markup.add(back)
        return markup

    def inforcafedr(self, socr: str):
        sql = f"""SELECT f.opis FROM cafedri c, facultopis f WHERE c.name = %s AND c.name_key LIKE f.name"""
        self.cursor.execute(sql, (socr,))
        result = self.cursor.fetchall()
        return result








