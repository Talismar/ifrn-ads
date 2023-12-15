from faker import Faker
from httpx import Client

client = Client(base_url="http://localhost:8000/api")
fake = Faker()


def test_article_create():
    title = fake.paragraph(nb_sentences=1)
    content = fake.text()

    request_data = {"title": title, "content": content}

    response = client.post("/article", json=request_data)

    assert response.status_code == 201
    assert "title" in response.json()
    assert title in response.json()["title"]


def test_article_list():
    title = fake.paragraph(nb_sentences=1)
    content = fake.text()

    request_data = {"title": title, "content": content}
    response = client.post("/article", json=request_data)

    response = client.get("/article")

    assert response.status_code == 200
    assert len(response.json()) > 0


def test_article_delete():
    title = fake.paragraph(nb_sentences=1)
    content = fake.text()

    request_data = {"title": title, "content": content}
    response = client.post("/article", json=request_data)

    artiche_id = response.json()["id"]

    response = client.delete(f"/article/{artiche_id}")

    assert response.status_code == 204


def test_article_retrieve():
    title = fake.paragraph(nb_sentences=1)
    content = fake.text()

    request_data = {"title": title, "content": content}
    response = client.post("/article", json=request_data)

    artiche_id = response.json()["id"]

    response = client.get(f"/article/{artiche_id}")

    assert response.status_code == 200
    assert "title" in response.json()
    assert "content" in response.json()
    assert title == response.json()["title"]
    assert content == response.json()["content"]
