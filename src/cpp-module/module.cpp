#include <cstdio>
#include <boost/python.hpp>

using namespace boost::python;

class MyModule {
 public:
    int PrintFromCppModule(int value) {
        fprintf(stdout, "I am inside a C++ module [value = %d]!\n", value);
        return 0;
    }
};

BOOST_PYTHON_MODULE(module) {
    class_<MyModule>("MyModule")
        .def("PrintFromCppModule", &MyModule::PrintFromCppModule);
}
