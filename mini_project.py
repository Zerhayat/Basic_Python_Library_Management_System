books = {}
members = {}

# ---------- Load Data from File ----------

def load_books():
    f = open("books.txt", "r")
    for line in f:
        isbn, title, author, status, borrower = line.strip().split("|")
        books[isbn] = {
            "title": title,
            "author": author,
            "status": status,
            "borrowed_by": borrower if borrower != "None" else None
        }
    f.close()

def load_members():
    f = open("members.txt", "r")
    for line in f:
        name, borrowed = line.strip().split("|")
        borrowed_list = borrowed.split(",") if borrowed else []
        members[name] = borrowed_list
    f.close()

# ---------- Save Data to File ----------

def save_books():
    f = open("books.txt", "w")
    for isbn, info in books.items():
        borrower = info['borrowed_by'] if info['borrowed_by'] else "None"
        f.write(f"{isbn}|{info['title']}|{info['author']}|{info['status']}|{borrower}\n")
    f.close()

def save_members():
    f = open("members.txt", "w")
    for name, borrowed_books in members.items():
        borrowed_str = ",".join(borrowed_books)
        f.write(f"{name}|{borrowed_str}\n")
    f.close()

# ---------- Functionalities ----------

def add_book():
    isbn = input("Enter ISBN: ").strip()
    if isbn in books:
        print("Book already exists.")
        return
    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    books[isbn] = {
        "title": title,
        "author": author,
        "status": "Available",
        "borrowed_by": None
    }
    print("Book added.")

def search_book():
    keyword = input("Enter title or author to search: ").strip().lower()
    found = False
    for isbn, info in books.items():
        if keyword in info['title'].lower() or keyword in info['author'].lower():
            print(f"\nISBN: {isbn}\nTitle: {info['title']}\nAuthor: {info['author']}\nStatus: {info['status']}")
            found = True
    if not found:
        print("No book found.")

def borrow_book():
    isbn = input("Enter ISBN to borrow: ").strip()
    if isbn not in books:
        print("Book not found.")
        return
    if books[isbn]["status"] == "Borrowed":
        print("Book is already borrowed.")
        return
    name = input("Enter your name: ").strip()
    books[isbn]["status"] = "Borrowed"
    books[isbn]["borrowed_by"] = name
    if name not in members:
        members[name] = []
    members[name].append(isbn)
    print("Book borrowed.")

def return_book():
    isbn = input("Enter ISBN to return: ").strip()
    if isbn not in books or books[isbn]["status"] == "Available":
        print("Book is not borrowed.")
        return
    name = books[isbn]["borrowed_by"]
    books[isbn]["status"] = "Available"
    books[isbn]["borrowed_by"] = None
    if name in members and isbn in members[name]:
        members[name].remove(isbn)
    print("Book returned.")

def show_books():
    if not books:
        print("No books in the library.")
    else:
        for isbn, info in books.items():
            print(f"\nISBN: {isbn}\nTitle: {info['title']}\nAuthor: {info['author']}\nStatus: {info['status']}")

def show_members():
    if not members:
        print("No members yet.")
    else:
        for name, borrowed in members.items():
            print(f"\nMember: {name}\nBorrowed Books: {borrowed}")

# ---------- Main Program ----------

load_books()
load_members()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show All Books")
    print("6. Show All Members")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        search_book()
    elif choice == '3':
        borrow_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        show_books()
    elif choice == '6':
        show_members()
    elif choice == '7':
        save_books()
        save_members()
        print("Library data saved. Goodbye!")
        break
    else:
        print("Invalid input. Try again.")
