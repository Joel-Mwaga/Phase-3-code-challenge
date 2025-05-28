from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

 # This script is for debugging purposes to demonstrate the relationships
if __name__ == "__main__":
    alice = Author.find_by_name("Alice")
    print("Alice's articles:", alice.articles())
    print("Alice's magazines:", alice.magazines())
    tech_today = Magazine.find_by_name("Tech Today")
    print("Tech Today's contributors:", tech_today.contributors())