#include <nanobind/nanobind.h>
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

NB_MODULE(nanobind_example_ext, m) {
    m.doc() = "This is a \"hello world\" example with nanobind";

    nb::class_<Foo>(m, "Foo")
        .def(nb::init<>())
        .def_rw("x", &Foo::x)
        .def("__repr__", [](const Foo &f) { return "Foo(" + std::to_string(f.x) + ")"; });

    nb::class_<Bar>(m, "Bar")
        .def(nb::init<>())
        .def_rw("foos", &Bar::foos);

    m.def("add", [](int a, int b) { return a + b; }, "a"_a, "b"_a);
}
