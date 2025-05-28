from lib.models.author import Author

def test_find_by_name():
    author = Author.find_by_name("Alice")
    assert author is not None
    assert author.name == "Alice"

def test_articles():
    author = Author.find_by_name("Alice")
    articles = author.articles()
    assert len(articles) > 0