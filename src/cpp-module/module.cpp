#include <cstdio>
#include <boost/python.hpp>
#include <functional>
#include <thread>

using namespace boost::python;

struct PythonCallback {
public:
    PythonCallback(PyObject func) : cb_(func) {}
    void operator() (const int& value) {
        // Call the callback function in python
        boost::python::call<int>(&cb_, value);
    }
private:
    PyObject cb_;
};

class Dispatcher {
 public:
    Dispatcher() {
   // sleep(3);
        static std::thread thread = std::thread(std::bind(&Dispatcher::Run, this));
    }

    void Run() {
        while (true) {
            if (callback_) {
                Call();
                sleep(1);
            } else {
                fprintf(stderr, "No Callback\n");
                sleep(1);
            }
        }
    }

    void SetCallback(PyObject callback) {
        callback_ = new PythonCallback(callback);
    }

    void Call() {
        static int counter = 0;
        (*callback_)(counter);
        //callback_(counter);
        counter++;
    }

 private:
    PythonCallback* callback_;
};

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
    class_<Dispatcher>("Dispatcher", init<>())
//        .def("set_callback", +[](Dispatcher& self, boost::python::object object) {
//      self.SetCallback(object);
//    });

        .def("SetCallback", &Dispatcher::SetCallback);

    class_<MyPrinter>("MyPrinter", init<>())
        .def("Print", &MyPrinter::Print);

    class_<MyModule>("MyModule", init<>())
        .def("PrintFromCppModule", &MyModule::PrintFromCppModule)
        .def("PrintFromOtherObject", &MyModule::PrintFromOtherObject);
}
