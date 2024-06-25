
# import mysql.connector

# mydata =  mysql.connector.connect (
#     host="localhost",
#     user="root",
#     password="Lebohang2007@" ,
#     database="libraries"
# )
# my_cursor = mydata.cursor();
# # my_cursor.execute("CREATE DATABASE libraries;")
# # my_cursor.execute("SHOW DATABASES")
# # showing = my_cursor.fetchall()
# # for data in showing:
# #     print(data)


#     # def create_tables(self):
#         # self.my_cursor.execute("CREATE TABLE library_books (book_id INT auto_increment PRIMARY KEY, name VARCHAR(255) NOT NULL,author VARCHAR(255) NOT NULL,description varchar(255) , is_available BOOLEAN DEFAULT TRUE)")
#         # self.my_cursor.execute("CREATE TABLE  checkouts (c_out_id INT auto_increment PRIMARY KEY,book_id INT,c_date DATE,FOREIGN KEY (book_id) references library_books(book_id))")

#         # self.mydata.commit()
#        # print("table added successfully.")
# # class Library:

# def view_all_book():
#     my_cursor.execute("select * from library_books");
#     result = my_cursor.fetchall()

#     for books in result :
#         print(books)

# def add_book():
#         print("Book added successfully.")
#         my_cursor.execute("INSERT INTO library_books (name, author, description) VALUES ('life', 'nombuso', 'djfhfufhuefefe'),('yesyes', 'mr frica', 'kjeereuiuf') ")
#         mydata.commit()


# def checkout_books():
#     success = False
#     book_checkout = int(input())
#     # my_cursor.execute("Select (book_id) from library_books")
#     my_cursor.execute("Select * from library_books")
#     available_books = my_cursor.fetchall()

#     print(available_books)
#     for books in available_books:
#         # print(books[0])
#         # print(books[4])
#         if books[0] == book_checkout and books[4] == 1:
#             my_cursor.execute("INSERT INTO checkouts (book_id, c_date) VALUES (%s, CURDATE())", (book_checkout,  ))
#             my_cursor.execute("UPDATE library_books SET is_available = FALSE WHERE book_id = %s", ( book_checkout,))
#             print("book found")
#             mydata.commit()
#             success= True
#         elif books[0] == book_checkout and books[4] == 0:
#             print("Not Available")
#         else:
#             print("wrong book")
    
#     return success
 
# def checkin_books():
#     success_in = False
#     book_checkin = int(input())
#     # my_cursor.execute("Select (book_id) from library_books")
#     my_cursor.execute("Select * from checkouts")
#     available_books = my_cursor.fetchall()

#     print(available_books)
#     for books in available_books:
#         # print(books[0])
#         # print(books[4])
#         if books[1] == book_checkin:
#             # my_cursor.execute("INSERT INTO checkouts (book_id, c_date) VALUES (%s, CURDATE())", (book_checkin,  ))
#             my_cursor.execute("DELETE FROM checkouts WHERE book_id = %s", (book_checkin,))
#             my_cursor.execute("UPDATE library_books SET is_available = True WHERE book_id = %s", ( book_checkin,))
#             print("book found")
#             mydata.commit()
#             success_in = True
#         else:
#             print("wrong book")
    
#     return success_in
 

# def start():
#     # Library.addBooks()
#     print("Welcome, please select an option:\n 1. View all books \n 2. Insert book \n 3. checkout_book \n 4. checkin_book")
#     input_tes = input()

#     if input_tes == '1' :
#         view_all_book()
#     elif  input_tes == '2':
#         add_book() 
#         print("Books added successfully.")
#     elif input_tes == '3':
#         checkout = checkout_books()
#         if checkout == True:
#             print("Checkout was successful!")
#         else:
#             print("Checkout Failed!")
#     elif input_tes == '4':
#         checkin = checkin_books()
#         if checkin == True:
#             print("Checkin was successful!")
#         else:
#             print("Checkin Failed!")
    
#     else :
#         print("not working")

# start()


