#include <stdlib.h>
#include <string.h>

class DynamicArray {
private:
    int length;
    int capacity;
    int *values;
public:
    DynamicArray(int capacity) {
        this->length = 0;
        this->capacity = capacity;
        this->values = (int *) malloc(capacity * sizeof(int));
    }

    int get(int i) {
        return *(this->values + i);
    }

    void set(int i, int n) {
        *(this->values + i) = n;
    }

    void pushback(int n) {
        if (this->length == this->capacity) {
            this->resize();
        }
        *(this->values + this->length) = n;
        this->length++;
    }

    int popback() {
        this->length--;
        return *(this->values + this->length);
    }

    void resize() {
        this->capacity *= 2;
        void *new_values = malloc(this->capacity * sizeof(int));
        this->values = (int *) memcpy(new_values, values, this->length * sizeof(int));
    }

    int getSize() {
        return this->length;
    }

    int getCapacity() {
        return this->capacity;
    }
};
