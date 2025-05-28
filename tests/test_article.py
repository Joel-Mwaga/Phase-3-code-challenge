from lib.models.article import Article

def test_find_by_title():
    article = Article.find_by_title("AI Revolution")
    assert article is not None
    assert article.title == "AI Revolution"