#include <nanobind/nanobind.h>
#include <nanobind/stl/vector.h>

#include <string>

namespace nb = nanobind;

using namespace nb::literals;

struct Bar {
    std::vector<int> foos;
};

NB_MODULE(nanobind_example_ext, m) {
    m.doc() = "This is a \"hello world\" example with nanobind";

    nb::class_<Bar>(m, "Bar")
        .def(nb::init<>())
        .def_rw("foos", &Bar::foos);
}
