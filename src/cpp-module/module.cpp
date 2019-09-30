#include <cstdio>
#include <boost/python.hpp>

using namespace boost::python;

class MyPrinter {
 public:
    MyPrinter() : value_(100) {}

    MyPrinter(const MyPrinter& other) : value_(other.value_) {}

    void Print() {
        fprintf(stdout, "I am inside a C++ module (dependency) [value = %d]!\n", value_);
        value_++;
    }
 private:
    int value_;
};

class MyModule {
 public:
    int PrintFromCppModule(int value) {
        fprintf(stdout, "I am inside a C++ module [value = %d]!\n", value);
        return 0;
    }

    void PrintFromOtherObject(MyPrinter* printer) {
        if (nullptr == printer) {
            fprintf(stderr, "Invalid pointer\n");
            return;
        }
        printer->Print();
    }
};

BOOST_PYTHON_MODULE(module) {
    class_<MyPrinter>("MyPrinter", init<>())
        .def("Print", &MyPrinter::Print);

    class_<MyModule>("MyModule", init<>())
        .def("PrintFromCppModule", &MyModule::PrintFromCppModule)
        .def("PrintFromOtherObject", &MyModule::PrintFromOtherObject);
}
