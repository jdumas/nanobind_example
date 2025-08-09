import nanobind_example as m

def test_fail():
    b = m.Bar()
    assert len(b.foos) == 0

    # Does not work
    b.foos.append(42)
    assert len(b.foos) == 1
    assert b.foos[0] == 42

def test_pass():
    b = m.Bar()
    assert len(b.foos) == 0

    # This works
    foos = b.foos
    assert len(foos) == 0
    foos.append(42)
    assert len(foos) == 1
    assert foos[0] == 42
    b.foos = foos
    assert len(b.foos) == 1
    assert b.foos[0] == 42
