import csv

def load_library():
    try:
        with open('KachiCsv.csv', 'r') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []

def save_library(library):
    fieldnames = ['BookID', 'Title', 'Author', 'Status']
    with open('KachiCsv.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(library)

def add_book(title, author):
    library = load_library()
    book_id = len(library) + 1
    new_book = {'BookID': book_id, 'Title': title, 'Author': author, 'Status': 'Available'}
    library.append(new_book)
    save_library(library)
    print(f"Book '{title}' added successfully with ID {book_id}.")

def list_books():
    library = load_library()
    if len(library)==0:
        print("Library is currently empty; please add books to the library:")
    else:
        print("Library Books:")
    for book in library:
        print(f"{book['BookID']}. {book['Title']} by {book['Author']} [{book['Status']}]")

def borrow_book(book_id):
    library = load_library()
    for book in library:
        if int(book['BookID']) == book_id and book['Status'] == 'Available':
            book['Status'] = 'Unavailable'
            save_library(library)
            print(f"Book '{book['Title']}' borrowed successfully.")
            return
    print("Book not found or already borrowed.")

def return_book(book_id):
    library = load_library()
    for book in library:
        if int(book['BookID']) == book_id and book['Status'] == 'Unavailable':
            book['Status'] = 'Available'
            save_library(library)
            print(f"Book '{book['Title']}' returned successfully.")
            return
    print("Book not found or already available.")

if __name__ == "__main__":
    while True:
        print("\n1. Add Book\n2. List Books\n3. Borrow Book\n4. Return Book\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
        elif choice == '2':
            list_books()
        elif choice == '3':
            book_id = int(input("Enter Book ID to borrow: "))
            borrow_book(book_id)
        elif choice == '4':
            book_id = int(input("Enter Book ID to return: "))
            return_book(book_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
