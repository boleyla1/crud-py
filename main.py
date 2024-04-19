
from tkinter import *
import messagebox
from tkinter import ttk

from result import result
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()
session = sessionmaker(bind=engine)
session = session()
# window
Window = Tk()
Window.title('resgister')
Window.geometry('700x700')
Window.resizable(False, False)
Window.config(bg='darkgray')

class human(Base):
    __tablename__ = 'human'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    family = Column(String)
    age = Column(Integer)
    def __init__(self, name="", family="", age=''):
        self.name = name
        self.family = family
        self.age = age
Base.metadata.create_all(engine)
def onClickRegister(e):
    human1 = human( name=TxtName.get(), family=TxtFamily.get(), age=TxtAge.get())
    register(human1)
    loadData()
def insertTable(human):
    Table.insert('', 'end', values=[human.name, human.family, human.age])

def register(human):
    session.add(human)
    session.commit()
def onClickSearch(e):
    dialog = TxtSearch.get()
    result = Search(dialog)
    CleanTable()
    if dialog == '':
        loadData()
    else:
        for item in result:
            insertTable(item)

def Search(dialog):
    alldata = session.query(human).all()
    resultList=[]
    for data in alldata:
        if data.name == dialog or data.family == dialog or data.age == dialog:
            resultList.append(data)
    return resultList
def CleanTable():
    for item in Table.get_children():
        Table.delete(item)
def loadData():
    CleanTable()
    alldata = session.query(human).all()
    for item in alldata:
        insertTable(item)


TxtName = Entry(Window)
TxtName.place(x=100, y=100)
TxtFamily = Entry(Window)
TxtFamily.place(x=100, y=140)
TxtAge = Entry(Window)
TxtAge.place(x=100, y=180)
TxtSearch = Entry(Window, width=25)
TxtSearch.place(x=130, y=270)
#lable
LblName = Label(Window, text='Name')
LblName.place(x=30, y=100)
LblFamily = Label(Window, text='Family')
LblFamily.place(x=30, y=140)
lblAge = Label(Window, text='Age')
lblAge.place(x=30, y=180)

#table
colums = ['name','family','age']
Table = ttk.Treeview(Window, columns=colums, show='headings')
Table.heading(colums[0], text='Name')
Table.heading(colums[1], text='Family')
Table.heading(colums[2], text='Age')
Table.column(colums[0], width=120)
Table.column(colums[1], width=120)
Table.column(colums[2], width=120)
Table.place(x=30, y=300)

#buttons
btnSearch = Button(Window, text='Search')
btnSearch.bind('<Button-1>', onClickSearch)
btnSearch.place(x=30, y=270)
btnGet = Button(Window, text='register', )
btnGet.bind('<Button-1>', onClickRegister)
btnGet.place(x=120, y=230)


# run window with loop
loadData()
Window.mainloop()
