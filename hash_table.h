#include <iostream>
#include "resource.h"
using namespace std;

class HashTable {
    private:
        // maximum number of crew
        int structure_size;
        int items_quantity = 0;
        Resource** structure;

        int hash(int code) {
            return code % structure_size;
        }
    
    public:
        int cruise_ship_number;
        
        HashTable(int structure_size, int cruise_ship_number) {
            this->structure_size = structure_size;
            this->cruise_ship_number = cruise_ship_number;
            structure = new Resource*[structure_size];
        }

        ~HashTable() {
            for (int i = 0; i < structure_size; ++i) {
                Resource* current = structure[i];

                while (current != nullptr) {
                    Resource* temp = current;
                    current = current->getNext();
                    delete temp;
                }
            }
            
            delete [] structure;
        }

        bool isFull() {
            return items_quantity == structure_size;
        }

        void insert(int code, int age, string name) {
            if (isFull())
            {
                throw runtime_error("Is full");
            }

            
            Resource* newResource = new Resource(code, age, name);
            bool itemAlreadyExists = searchByCode(*newResource);

            if (itemAlreadyExists)
            {
                throw runtime_error("Item already exists");
            }
            
            
            int index = hash(code);
            
            if (structure[index] == nullptr) {
                structure[index] = newResource;
            } else {
                // Colisão - inserindo no inicio
                newResource->setNext(structure[index]);
                structure[index] = newResource;
            }

            items_quantity++;
        }

        bool searchByCode(Resource& resource) {
            int index = hash(resource.getCode());
            Resource* current = structure[index];

            while (current != nullptr) {
                if (current->getCode() == resource.getCode()) {
                    resource.age = current->age;
                    resource.name = current->name;
                    return true;
                }
                current = current->getNext();
            }
            
            return false;
        }

        void print_out() {
            for (int i = 0; i < structure_size; i++)
            {
                if (structure[i] == nullptr) continue;
                
                Resource* current = structure[i];
                
                while (current != nullptr) {
                    cout << current->getCode() << " - " << current->age  << " - " << current->name << endl;
                    current = current->getNext();
                }
            }
        }
};