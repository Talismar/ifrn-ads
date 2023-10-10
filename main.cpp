#include <iostream>
#include "hash_table.h"
#include <limits>
using namespace std;

enum MenuOptionEnum {
    ADD_CREW_MEMBER,
    SEARCH_CREW_MEMBER_ON_SHIP,
    VIEW_CREW_ON_SHIP,
    CHANGE_TO_ANOTHER_SHIP,
    EXIT,
    VIEW_MENU_OPTION,
};

const int MAX_SIZE = 5;

void view_menu();
void handle_numeric_error(int & variable) {
    // Se o usuário digitar qualquer caracter que não seja númerico
    while (!cin.good())
    {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        
        cout << "Por favor entre com um número..." << endl;
        cin >> variable;
    }
}

int main()
{
    int option;
    int database_index = 0;
    HashTable database[MAX_SIZE] = {
        HashTable(50, 0), 
        HashTable(50, 1), 
        HashTable(50, 2), 
        HashTable(50, 3), 
        HashTable(50, 4)
    };
    
    Resource resourceToSearch(0, 0, "");
    bool has_error;
    int code;
    int age;
    string name;

    cout << "Bem vindo ao sistema da companhia de gestão de navios...\n";
    view_menu();

    while (true)
    {

        cin >> option;
        handle_numeric_error(option);

        switch (static_cast<MenuOptionEnum>(option))
        {
        case ADD_CREW_MEMBER:

            do
            {
                cout << "Informe o [código|idade|nome] do tripulante para adicionar a tabela atual" << endl;
                cin >> code;
                handle_numeric_error(code);
                cin >> age;
                handle_numeric_error(age);
                cin >> name;

                try
                {
                    database[database_index].insert(code, age, name);
                    has_error = false;
                    cout << "Novo item adicionado com sucesso na tabela - " << database_index << endl;
                }
                catch(const std::exception& e)
                {
                    has_error = true;
                    cerr << e.what() << '\n';
                }
            } while (has_error);
            
            break;
        case SEARCH_CREW_MEMBER_ON_SHIP:
            cout << "Digite um código para buscar na tabela atual: " << endl;
            
            cin >> code;
            handle_numeric_error(code);

            resourceToSearch.setCode(code);

            if (database[database_index].searchByCode(resourceToSearch))
            {
                cout << resourceToSearch.getCode() << " - " << resourceToSearch.age << " - " << resourceToSearch.name << endl;
            }
            else{
                cout << "Tripulante não existe na tabela atual" << endl;
            }            

            break;
        case VIEW_CREW_ON_SHIP:
            database[database_index].print_out();
            break;
        case CHANGE_TO_ANOTHER_SHIP:
            cout << "Digite o numero da tabela que deseja entrar: ";
            cin >> database_index;
            handle_numeric_error(database_index);

            if (database_index <= MAX_SIZE - 1)
            {   
                cout << "Você está na tabela " << database_index << endl;
            }else {
                cout << "Tabela não existe!" << endl;
            }
            
            break;
        case EXIT:
            return 0;
        case VIEW_MENU_OPTION:
            view_menu();
            break;
        default:
            cout << "Opição inválida! Pressione o 5 para visualizar novamente as opções do menu\n" << endl;
            break;
        }
    }

    return 0;
}

void view_menu() {
    string options_text[] = {
        "adicionar tribulante ao návio-cruzeiro",
        "procurar e visualizar os dados de tribulante em um návio-cruzeiro",
        "visualizar tribulantes em um návio-cruzeiro",
        "alterar a tabela atual de dados do navio",
        "sair do sistema"
    };

    cout << "################################# MENU #######################################" << endl;

    for (int i = 0; i < 5; i++)
    {
        cout << "Digite " << i << " para " << options_text[i] << endl;   
    }
}