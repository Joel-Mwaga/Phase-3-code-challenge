from lib.models.magazine import Magazine

def test_find_by_name():
    mag = Magazine.find_by_name("Tech Today")
    assert mag is not None
    assert mag.name == "Tech Today"

def test_contributors():
    mag = Magazine.find_by_name("Tech Today")
    contributors = mag.contributors()
    assert len(contributors) > 0