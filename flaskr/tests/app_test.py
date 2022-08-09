from project.app import app


def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")
    
    
def test_database():
    assert Path("flaskr.db").is_file()
