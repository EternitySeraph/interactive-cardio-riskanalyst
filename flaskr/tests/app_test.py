from project.app import app


def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")
