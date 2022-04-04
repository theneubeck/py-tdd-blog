def test_set_and_get(db):
    assert db.get("1") is None
    db.set("1", "hej")
    assert db.get("1") == "hej"


def test_delete(db):
    assert db.get("1") is None
    db.set("1", "hej")
    db.delete("1")
    assert db.get("1") is None


def test_items(db):
    assert list(db.items()) == []
    db.set("12", "hej")
    assert list(db.items()) == [
        ("12", "hej"),
    ]
