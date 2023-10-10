#include <iostream>

class Resource
{
    private: 
        int code;
        Resource* next;

    public:    
        int age;
        std::string name;
        
        Resource() {
            code = -1;
            age = 0;
            name = "";
            next = nullptr;
        }
        Resource(int code, int age, std::string name) {
            this->code = code;
            this->age = age;
            this->name = name;
            next = nullptr;
        }
        

        int getCode() { 
            return code; 
        }

        void setCode(int code) { 
            this->code = code; 
        }

        Resource* getNext() { 
            return next; 
        }

        void setNext(Resource* next) {
            this->next = next;
        }


};