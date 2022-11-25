#include "cpp/add_module/add.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(MyAddModule, m) {
  m.doc() = "pybind11 example add module";

  // Add bindings here
  m.def("add_from_cpp", plus, "Add two ints");
  m.def("minus_from_cpp", minus, "Add two ints");
}
