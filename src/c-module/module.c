#include <stdlib.h>
#include <stdio.h>

int PrintFromCModule(int value) {
    fprintf(stdout, "I am inside a C module [value = %d]!\n", value);
    return 0;
}
