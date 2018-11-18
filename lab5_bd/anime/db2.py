from anime.connection import Connection


class Anime:

    def __init__(self, db_connection, name, description, author):
        self.db_connection = db_connection.connection
        self.name = name
        self.description = description
        self.author = author

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO anime (name, description, author) VALUES (%s, %s, %s);", (self.name, self.description, self.author))
        self.db_connection.commit()
        c.close()

con = Connection('dbuser', '123', 'anime')

with con:
    anime = Anime(con, 'Атака титанов', 'Второе, что вспомнила', 'Хадзимэ Исаяма')
    anime.save()