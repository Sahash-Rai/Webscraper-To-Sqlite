from scraper import scrape_books
from db_handler import store_books_in_db, create_db

def main():
    create_db()  
    print("Starting Book Scraper...")
    
    books = scrape_books()
    
    if books:
        print(f"Scraped {len(books)} books!")
        store_books_in_db(books)
        print("Data stored in SQLite database.")
    else:
        print("No books found!")

if __name__ == "__main__":
    main()
