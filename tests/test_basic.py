import nanobind_example as m


def test_foo():
    foo = m.Document()
    foo.data = dict()

    x = foo.data
    x.update({"extension0": {"key": [0, 1, 2]}})
    print(x)
    assert len(x) == 1

    foo.data.update({"extension0": {"key": [0, 1, 2]}})
    print(foo.data)
    assert len(foo.data) == 1
    assert foo.data["extension0"] == {"key": [0, 1, 2]}
    foo.data.update({"extension1": {"key": "foo"}})
    assert foo.size == 2
    assert foo.data["extension1"] == {"key": "foo"}
    foo.data["extension0"]["key"][0] = 10
    assert foo.data["extension0"] == {"key": [10, 1, 2]}
    foo.data["extension0"]["key"] = [3, 4, 5]
    assert foo.data["extension0"] == {"key": [3, 4, 5]}
