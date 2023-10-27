# Teste de Software

## Especificações da atividade

Nesta tarefa, você obterá alguma prática na criação de testes de unidade eficazes.

Temos que triângulos são figuras geométricas formadas por três segmentos de reta que se encontram nas extremidades. Assim, são polígonos com três lados, três ângulos e três vértices.

Definição e Propriedades dos Triângulos:
- All sides zero
- No side may have a length of zero
- Each side must be shorter than the sum of all sides divided by 2;
- One side equals the sum of the other

Mais detalhes são apresentados no anexo abaixo.

Font: [Anexo](https://mundoeducacao.uol.com.br/matematica/triangulos.htm#:~:text=Tri%C3%A2ngulos%20s%C3%A3o%20figuras%20geom%C3%A9tricas%20formadas,tr%C3%AAs%20%C3%A2ngulos%20e%20tr%C3%AAs%20v%C3%A9rtices.)


### Questões

1. Implemente uma classe que receba três lados e identifique se é um triângulo ou não. É necessário testar essa classe para todas as possibilidades de valores para cada tipo de triângulo (Enviar link para commit do github).

2. Planeje os casos de teste utilizando os critérios de teste visto em sala. Descreva passo a passo como você encontrou a lista de casos de teste para testar o programa (Anexar link para documento).

Vimos em sala dois critérios: identificar as Classes de Equivalência e valores limites

### Identificar as Classes de Equivalência

#### Triângulo Válido:

- Todos os lados são maiores que zero.
- Pelo menos um lado é igual a zero.
- Todos os lados são iguais a zero.

##### Triângulo Inválido:

- A soma de dois lados não é maior que o terceiro.
- Um lado é igual à soma dos outros dois lados

##### Valores Limites

#### Triângulo Válido

- Qualquer valor dos lados maior que zero .


##### Triângulo inválido

- Pelo menos um lado igual a zero
- Todos os lados igual a zero
- A soma de dois lados não é maior que o terceiro
- Um lado é igual à soma dos outros dois lados



| System:        | Programa Identifier                                   |                               |                       |                                      |               |
|----------------|-------------------------------------------------------|-------------------------------|-----------------------|--------------------------------------|---------------|
| Use Case:      | Programa Triangle Identifier                          | Version:                      | 1.0                   |                                      |               |
| Suite Type:    | Reduced (Greedy Heuristic - Transition Pair Coverage) |                               | Size: 1 test case(s)) | Creation Date:                       | 27/10/2023    |
|                |                                                       |                               |                       |                                      |               |
|                |                                                       |                               |                       |                                      |               |
| Test Case ID:  | TC1                                                   | Priority low,medium,high  |                       | Executed by:                         |               |
| Description:   | Identificador de triangulos                           |                               |                       | Execution Date:                      |               |
| Precondition:  | ...                                                   |                               |                       |                                      |               |
| #              | Steps                                                 | Test Data                     | Expected Results      | Execution Status (pass/fail/blocked) | Actual Result |
| 1              | Informar 3 lados de um triangulo (Equilateral)        | 3 - 3 - 3                     | Válido                | pass                                 | Válido        |
| 2              | Informar 3 lados de um triangulo (Isosceles)          | 4 - 4 - 5                     | Válido                | pass                                 | Válido        |
| 3              | Informar 3 lados de um triangulo (Scalene)            | 3 - 4 - 5                     | Válido                | pass                                 | Válido        |
| 4              | Informar 3 lados de um triangulo                      | 5 - 6 - 11                    | Inválido              | pass                                 | Inválido      |
| 5              | Informar 3 lados de um triangulo                      | 3 - 4 - 7                     | Inválido              | pass                                 | Inválido      |
| 6              | Informar 3 lados de um triangulo                      | 0 - 4 - 5                     | Inválido              | pass                                 | Inválido      |
| 7              | Informar 3 lados de um triangulo                      | 0 - 0 - 0                     | Inválido              | pass                                 | Inválido      |
| Postcondition: | ...                                                   |                               |                       |                                      |               |


3. Implemente os casos de testes planejados. O projeto deve apresentar a implementação dos testes e implementação do programa em teste em pastas separadas.

4. Execução dos casos de teste: Execute os casos de teste implementados. Algum teste falou? Quais? Por qual motivo?

5. Se algum caso de teste falhar, realize as alterações necessárias nos casos de teste ou no programa e descreva quais altereações foram feitas e por qual motivo.