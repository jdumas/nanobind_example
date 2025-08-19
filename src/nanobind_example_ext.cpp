#include <nanobind/nanobind.h>
#include <nanobind/stl/bind_vector.h>
#include <nanobind/stl/vector.h>
#include <nanobind_json/nanobind_json.hpp>

#include <string>

namespace nb = nanobind;
namespace nl = nlohmann;

using namespace nb::literals;

struct Document {
    nl::json data;
};

NB_MODULE(nanobind_example_ext, m) {
    m.doc() = "This is a \"hello world\" example with nanobind";

    nb::class_<Document>(m, "Document")
        .def(nb::init<>())
        .def_rw("data", &Document::data, nb::rv_policy::reference_internal);
}
