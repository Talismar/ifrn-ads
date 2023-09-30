#include <iostream>
#include <cstdlib>
#include <ctime>
#include <chrono>

using namespace std;

template <typename TF, typename... TArgs>
double measure_time(TF function, TArgs... args);
void swap(int & x, int& y);
int partition(int* arr, int index_start, int index_end);
void quicksort(int *array, int index_start, int index_end);
void bubble_sort(int *array, int array_size);
void random_sequence(int *array, int array_size);
void linear_search(int *array, int array_size, int data, bool *found);
void binary_search(int *array, int index_end, int data, bool *found);

int main() {

    int array_size = 10000;
    int* S = new int[array_size];

    // ############# QUICK SORT ##############
    random_sequence(S, array_size);

    cout << "RELATÓRIO\n";

    double duration_in_seconds = measure_time(quicksort, S, 0, array_size - 1);
    cout << "Quick Sort >> " << duration_in_seconds << " ns" << endl;
    cout << "\n##########################################################\n\n";

    // ############# BUBBLE SORT ##############
    random_sequence(S, array_size);
    duration_in_seconds = measure_time(bubble_sort, S, array_size);
    cout << "Bubble Sort >> " << duration_in_seconds << " ns" << endl;
    cout << "\n##########################################################\n\n";

    // ############# LINEAR SEARCH - MELHOR CASO ##############
    bool found = false;
    int data = S[0];
    duration_in_seconds = measure_time(linear_search, S, array_size, data, &found);
    cout << "Busca linear - MELHOR CASO >> " << duration_in_seconds << " ns" << endl;

    if (found) {
        cout << "Item encontrado por busca linear >> " << data << endl ;
    }

    // ############# LINEAR SEARCH - PIOR CASO ##############
    found = false;
    data = S[array_size - 1];
    duration_in_seconds = measure_time(linear_search, S, array_size, data, &found);
    cout << "Busca linear - PIOR CASO >> " << duration_in_seconds << " ns" << endl;

    if (found) {
        cout << "Item encontrado por busca linear >> " << data << endl << endl ;
    }

    cout << "\n##########################################################\n\n";

    // ############# BINARY LINEAR - MELHOR CASO ##############
    found = false;
    int index_middle = (array_size - 1) / 2;
    data = S[index_middle];
    duration_in_seconds = measure_time(binary_search, S, array_size - 1, data, &found);
    cout << "Busca binária - MELHOR CASO >> " << duration_in_seconds << " ns" << endl;

    if (found) {
        cout << "Item encontrado por busca binária >> " << data << endl ;
    }

    // ############# BINARY LINEAR - PIOR CASO ##############
    found = false;
    data = S[0];
    duration_in_seconds = measure_time(binary_search, S, array_size - 1, data, &found);
    cout << "Busca binária - PIOR CASO >> " << duration_in_seconds << " ns" << endl;

    if (found) {
        cout << "Item encontrado por busca binária >> " << data;
    }

    delete [] S;

    return 1;
}

template <typename TF, typename... TArgs>
double measure_time(TF function, TArgs... args) {
    auto start = std::chrono::high_resolution_clock::now();

    function(args...);

    auto end = std::chrono::high_resolution_clock::now();

    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);

    return elapsed.count();
}

void swap(int & x, int& y)
{
    int temp = x;
    x = y;
    y = temp;
}

int partition(int* arr, int index_start, int index_end)
{
    // O valor do pivó atual
    int pivot = arr[index_end];

    for (int j = index_start; j <= index_end - 1; j++) {
        // Se nenhum elemento for maior que o pivó, então eles seram maior
        // Logo o index_start deve ser subtituido pelo index_end

        if (arr[j] < pivot) {
            swap(arr[index_start], arr[j]);
            index_start++;
        }
    }

    swap(arr[index_start], arr[index_end]);
    return index_start;
}

void quicksort(int *array, int index_start, int index_end){

    if (index_start < index_end) {
        int index_partition = partition(array, index_start, index_end);

        quicksort(array, index_start, index_partition - 1);
        quicksort(array, index_partition + 1, index_end);
    }
}

void bubble_sort(int *array, int array_size) {
    for (int i = 0; i < array_size; ++i) {
        for (int j = 0; j < array_size - 1; ++j) {
            if (array[j] > array[j+1]) {
                swap(array[j], array[j+1]);
            }
        }
    }
}

void random_sequence(int *array, int array_size) {
    srand(time(nullptr));

    for (int i = 0; i < array_size; ++i) {
        array[i] = rand() % 100000;
    }
}

void linear_search(int *array, int array_size, int data, bool *found) {
    *found = false;

    for (int i = 0; i < array_size; ++i) {
        if (array[i] == data) {
            *found = true;
            break;
        }
    }
}

void binary_search(int *array, int index_end, int data, bool *found) {
    int index_start = 0;
    *found = false;

    while (index_start <= index_end) {
        int middle = index_start + (index_end - index_start) / 2;

        // Se o elemento no meio for igual ao alvo, encontramos o elemento
        if (array[middle] == data) {
            *found = true;
            break;
        }


        if (array[middle] > data) {
            index_end = middle - 1;
        }

        else {
            index_start = middle + 1;
        }
    }
}