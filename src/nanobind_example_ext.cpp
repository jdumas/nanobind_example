#include <nanobind/nanobind.h>
#include <nanobind/stl/bind_vector.h>
#include <nanobind/stl/vector.h>
#include <nanobind_json/nanobind_json.hpp>

#include <string>

namespace nb = nanobind;
namespace nl = nlohmann;

using namespace nb::literals;

struct Foo {
    nl::json data;
};

// Prefer binding over type caster for std::vector<Foo>
NB_MAKE_OPAQUE(std::vector<Foo>);

NB_MODULE(nanobind_example_ext, m) {
    m.doc() = "This is a \"hello world\" example with nanobind";

    nb::class_<Foo>(m, "Foo")
        .def(nb::init<>())
        .def_rw("data", &Foo::data);
}
