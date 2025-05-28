import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

def list_authors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()
    print("\nAll Authors:")
    for author in authors:
        print(f"- {author['name']}")
    conn.close()

def list_magazines():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM magazines")
    magazines = cursor.fetchall()
    print("\nAll Magazines:")
    for mag in magazines:
        print(f"- {mag['name']} ({mag['category']})")
    conn.close()

def articles_by_magazine():
    name = input("Enter magazine name: ")
    mag = Magazine.find_by_name(name)
    if not mag:
        print("Magazine not found.")
        return
    print(f"\nArticles in {mag.name}:")
    for article in mag.articles():
        print(f"- {article['title']}")

def top_author():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT authors.name, COUNT(articles.id) as article_count
        FROM authors
        JOIN articles ON authors.id = articles.author_id
        GROUP BY authors.id
        ORDER BY article_count DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    if row:
        print(f"\nTop Author: {row['name']} ({row['article_count']} articles)")
    else:
        print("\nNo articles found.")
    conn.close()

def magazines_with_multiple_authors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.name, COUNT(DISTINCT a.author_id) as author_count
        FROM magazines m
        JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
        HAVING author_count >= 2
    """)
    mags = cursor.fetchall()
    print("\nMagazines with articles by at least 2 different authors:")
    for mag in mags:
        print(f"- {mag['name']} ({mag['author_count']} authors)")
    conn.close()

def author_menu():
    name = input("Enter author name: ")
    author = Author.find_by_name(name)
    if not author:
        print("Author not found.")
        return
    print(f"\nArticles by {author.name}:")
    for article in author.articles():
        print(f"- {article['title']}")
    print("\nMagazines contributed to:")
    for mag in author.magazines():
        print(f"- {mag['name']} ({mag['category']})")
    print("\nTopic areas:")
    for cat in author.topic_areas():
        print(f"- {cat}")

def magazine_menu():
    name = input("Enter magazine name: ")
    mag = Magazine.find_by_name(name)
    if not mag:
        print("Magazine not found.")
        return
    print(f"\nArticles in {mag.name}:")
    for article in mag.articles():
        print(f"- {article['title']}")
    print("\nContributors:")
    for contributor in mag.contributors():
        print(f"- {contributor['name']}")
    print("\nArticle titles:")
    for title in mag.article_titles():
        print(f"- {title}")

def main_menu():
    while True:
        print("\n--- Article Management CLI ---")
        print("1. Query by Author")
        print("2. Query by Magazine")
        print("3. List all Authors")
        print("4. List all Magazines")
        print("5. List Articles by Magazine")
        print("6. Show Top Author")
        print("7. Magazines with Multiple Authors")
        print("8. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            author_menu()
        elif choice == "2":
            magazine_menu()
        elif choice == "3":
            list_authors()
        elif choice == "4":
            list_magazines()
        elif choice == "5":
            articles_by_magazine()
        elif choice == "6":
            top_author()
        elif choice == "7":
            magazines_with_multiple_authors()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()