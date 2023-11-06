from models import Base, session, Book, engine

import datetime
import csv

def menu():
    while True:
        print('''
              \nPROGRAMMING BOOKS
              \r1) Add book
              \r2) View all books
              \r3) Search for book
              \r4) Book Analaysis
              \r5) Exit''')
        choice = input('What would you like to do? ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            input('''
                  \rPlease choose one of the options above.
                  \rA number from 1 - 5.
                  \rpress enter to try again.''')
                  

def add_csv():
    with open('suggested_books.csv', newline='') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title==row[0]).one_or_none()
            if book_in_db == None:
                 title = row[0]
                 author = row[1]
                 date = clean_date(row[2])
                 price = clean_price(row[3])
                 new_book = Book(title=title, author=author, published_date=date, price=price)
                 session.add(new_book)
        session.commit()

def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # add book
            pass
        elif choice == '2':
            # View all Books
            pass
        elif choice == '3':
            # Search for book
            pass
        elif choice == '4':
            # Display Book anaylsis
            pass
        else:
            print('GOODBYE')
            app_running = False


            

# import models
# main menu - add, search, analysis, exit, view
# add books to the database
# edit books
# delete books
# search books
# data cleaning
def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return_date = datetime.date(year, month, day)
    return return_date

def clean_price(price_str):
    price_float = float(price_str)
    return int(price_float * 100)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()
    add_csv()
    

    for book in session.query(Book):
        print(book)
    
    