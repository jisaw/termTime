import psycopg2


class db_wrangler(object):
    def __init__(self, dbname="", user=""):
        self.dbname = dbname
        self.user = user
        self.conn = psycopg2.connect("dbname=%s user=%s" % dbname, user)
        self.cur = self.conn.cursor()

    def initialize(self):
        self.cur.execute(
            "IF NOT EXISTS (SELECT * FROM projects) CREATE TABLE projects(id SERIAL, name varchar(64) not null, owner varchar(64) not null, pay money);"
        )
        self.cur.execute(
            "IF NOT EXISTS (SELECT * FROM tSheets) CREATE TABLE tSheets(id SERIAL, owner varchar(64), startDate date, endDate date, projectId int not null);"
        )
        self.cur.execute(
            "IF NOT EXISTS (SELECT * FROM workSessions) CREATE TABLE workSession(id SERIAL, date date not null, hours float8 not null, startTime time not null, endTime time not null, tSheetId int not null);"
        )

    def get_projects(self):
        self.cur.execute(
            "SELECT * FROM projects;"
        )
        return self.cur.fetchall()

    def print_projects(self):
        for i in self.get_projects():
            print("id: %s\nname: %s\nowner: %s\npay: %s" % (i[0], i[1], i[2]))
            print("*" * 10)

    def get_tSheets(self):
        self.cur.execute(
            "SELECT * FROM tSheets;"
        )
        return self.cur.fetchall()

    def print_tSheets(self):
        for i in self.get_tSheets():
            print("id: %s\nowner: %s\nstartDate: %s\nendDate: %s\nprojectId: %s" % (i[0], i[1], i[2], i[3], i[4]))
            print("*" * 10)

    def get_workSessions(self):
        self.cur.execute(
            "SELECT * FROM workSessions;"
        )
        return self.cur.fetchall()

    def print_workSessions(self):
        for i in self.get_workSessions():
            print("id: %s\ndate: %s\nhours: %s\nstartTime: %s\nendTime: %s\ntSheetId: %s" % (i[0], i[1], i[2], i[3], i[4], i[5]))
            print("*" * 10)