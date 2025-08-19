import nanobind_example as m


def test_operator():
    foo = m.Document()
    foo.data = dict()

    foo.data |= {"extension0": {"key": [0, 1, 2]}}
    assert len(foo.data) == 1


def test_update():
    foo = m.Document()
    foo.data = dict()

    foo.data.update({"extension0": {"key": [0, 1, 2]}})
    assert len(foo.data) == 1
    assert foo.data["extension0"] == {"key": [0, 1, 2]}


def test_modify():
    foo = m.Document()
    foo.data = {"extension0": {"key": [0, 1, 2]}, "extension1": {"key": "foo"}}
    assert len(foo.data) == 1
    assert foo.data["extension0"] == {"key": [0, 1, 2]}
    assert foo.data["extension1"] == {"key": "foo"}

    foo.data["extension0"]["key"][0] = 10
    assert foo.data["extension0"] == {"key": [10, 1, 2]}

    foo.data["extension0"]["key"] = [3, 4, 5]
    assert foo.data["extension0"] == {"key": [3, 4, 5]}
