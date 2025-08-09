import nanobind_example as m


def test_baz():
    b = m.Baz()
    assert len(b.ints) == 0

    # Using std::vector<int> type caster, appending to b.ints fails to mutate b.ints
    b.ints.append(42)
    assert len(b.ints) == 1


def test_bar():
    b = m.Bar()
    assert len(b.foos) == 0

    f = m.Foo()
    f.x = 42
    assert f.x == 42

    # Using std::vector<Foo> bindings, appendings to b.foos correctly mutates b.foos
    b.foos.append(f)
    assert len(b.foos) == 1
    assert b.foos[0].x == 42

    # However, mutating an element returned by a std::vector<Foo> fails as documented
    b.foos[0].x = 100
    assert b.foos[0].x == 100
