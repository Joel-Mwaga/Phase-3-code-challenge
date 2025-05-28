import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

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

if __name__ == "__main__":
    while True:
        print("\n--- Article Management CLI ---")
        print("1. Query by Author")
        print("2. Query by Magazine")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            author_menu()
        elif choice == "2":
            magazine_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")