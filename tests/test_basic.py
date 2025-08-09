import nanobind_example as m

def test_fail():
    f = m.Foo()
    f.x = 42
    assert f.x == 42
    b = m.Bar()
    assert len(b.foos) == 0

    # Does not work
    b.foos.append(f)
    assert len(b.foos) == 1

def test_pass():
    f = m.Foo()
    f.x = 42
    assert f.x == 42
    b = m.Bar()
    assert len(b.foos) == 0

    # This works
    foos = b.foos
    assert len(foos) == 0
    foos.append(f)
    assert len(foos) == 1
    b.foos = foos
    assert len(b.foos) == 1
