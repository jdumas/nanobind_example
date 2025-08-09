#include <nanobind/nanobind.h>
#include <nanobind/stl/bind_vector.h>
#include <nanobind/stl/vector.h>

#include <string>

namespace nb = nanobind;

using namespace nb::literals;

struct Foo {
    int x;
};

struct Bar {
    std::vector<Foo> foos;
};

struct Baz {
    std::vector<int> ints;
};

// Prefer binding over type caster for std::vector<Foo>
NB_MAKE_OPAQUE(std::vector<Foo>);

NB_MODULE(nanobind_example_ext, m) {
    m.doc() = "This is a \"hello world\" example with nanobind";

    nb::bind_vector<std::vector<Foo>>(m, "FooVector");

    nb::class_<Foo>(m, "Foo")
        .def(nb::init<>())
        .def_rw("x", &Foo::x);

    nb::class_<Bar>(m, "Bar")
        .def(nb::init<>())
        .def_rw("foos", &Bar::foos);

    nb::class_<Baz>(m, "Baz")
        .def(nb::init<>())
        .def_rw("ints", &Baz::ints);
}
