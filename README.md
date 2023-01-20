### Módulo 1: Algoritmos

- [x] `Ordenador:` Escreva um algoritmo ordene as cartas de um naipe do baralho;

- [x] `Soma:` Somar três números;

- [x] `Média:` Calcular a média de um aluno numa disciplina;

- [x] `Peso:` Calcular o peso ideal de uma pessoa;

- [x] `Moeda 5:` Escreva um algoritmo para descobrir a moeda falsa (mais leve) de um total de 5 moedas usando uma balança analítica;

Dica: é possível resolver com somente duas pesagens.

- [x] `Moeda 27:` Idem ao anterior, mas com um total de 27 moedas;

Dica: é possível resolver com somente três pesagens.

### Módulo 2: Introdução ao Python

- [x] `Parágrafo:` Faça um programa que leia o nome, a idade, a altura, o peso e a nacionalidade do usuário e escreva essas informações na forma de um parágrafo de
apresentação;

- [x] `Perímetro:` Faça um programa que exiba o perímetro de uma circunferência a partir do seu raio;

- [x] `IMC:` Faça um programa que calcule o IMC de uma pessoa (IMC = massa em kg / altura em metros elevado ao quadrado) e informe a sua classificação;

### Módulo 3: Vetores e Matrizes

- [ ] `:` Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal da matriz por um número k. Imprima a matriz na tela antes e depois da multiplicação;

- [ ] `:` Faça um programa que leia duas matrizes A e B 2x2 e imprima a matriz C que é a soma das matrizes A e B;

- [ ] `:` Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas matrizes. Se as matrizes forem de tamanhos compatíveis para multiplicação, multiplique as matrizes. Imprima as matrizes A, B e a matriz resultante da multiplicação;

- [ ] `:` Faça um programa que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma. Imprima na tela a matriz, a linha de maior soma e a soma;

- [ ] `:` Faça um programa que leia a ordem de uma matriz quadrada A (até 100), posteriormente leia seus valores e escreva sua transposta AT, onde AT[i][j] = A[j][i];

- [ ] `:` Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Faça um programa que leia os nomes e os tempos (em segundos) de cada volta de cada corredor e guarde as informações em uma matriz. Ao final, o programa deve informar:
De quem foi a melhor volta da prova, e em que volta
Classificação final em ordem (1o. o campeão)
Qual foi a volta com a média mais rápida

- [ ] `:` Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre: (a) o maior elemento da matriz e sua respectiva posição (linha e coluna); (b) o menor elemento da matriz e sua respectiva posição;

- [ ] `:` Faça um programa que leia duas matrizes A e B e verifica se ambas são inversas (ou seja, se a multiplicação de A por B é a matriz identidade);

- [ ] `:` Faça um programa que leia uma matriz 3x3 que representa um tabuleiro de jogo da velha e indique qual posição deveria ser jogada para ganhar o jogo (se possível) ou ao menos evitar uma derrota;

- [ ] `:` Faça um programa que lê duas notas para cada aluno de duas turmas. Cada turma tem 3 alunos. Armazene os dados em uma matriz M. Cada aluno deve ter três notas (as duas digitadas e a média dessas duas). Calcule a média de cada turma e armazene em um vetor TURMA. Informe qual turma tem maior média, e quais alunos tiveram média maior que a média de sua turma;

- [ ] `:` Faça um programa que percorre uma lista com o seguinte formato: [["Brasil", "Italia", [10, 9]]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9. O programa deve imprimir na tela:
(a) o total de faltas do campeonato
(b) o time que fez mais faltas
(c) o time que fez menos faltas

- [ ] `:` Faça um programa que simule um lançamento de dados. Lance o dado 10 vezes e armazene os resultados em um vetor. Depois, monte um outro vetor contendo quantas vezes cada valor foi obtido. Imprima os dois vetores. Use uma função para gerar números aleatórios, simulando os lançamentos dos dados.

Exemplo de uma possível saída:
[3, 1, 5, 3, 5, 4, 5, 5, 3, 6]
[1, 0, 3, 1, 4, 1]

- [ ] `:` Faça um programa que percorre um vetor e imprime na tela o valor mais próximo da média dos valores do vetor. 

Exemplo:
vetor = [2.5, 7.5, 10.0, 4.0] (média = 6.0)
Valor mais próximo da média = 7.5

- [ ] `:` Faça um programa que percorre duas listas e intercala os elementos de ambas, formando uma terceira lista. A terceira lista deve começar pelo primeiro elemento da lista menor.

Exemplo:
lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40, 50, 60]
lista_intercalada = [1, 10, 2, 20, 3, 30, 4, 40, 50, 60]

- [ ] `:` Em uma universidade são distribuídas 300 senhas para a fila do bandejão, da seguinte forma:

As filas começam a se formar pela manhã. Até às 11h, horário de abertura do restaurante, alunos podem guardar lugar para no máximo 3 outros colegas, depois disso a fila é congelada. Se a quantidade de pessoas na fila + lugares guardados ultrapassar 300, os extras ficarão sem senha.

Escreva um programa que percorre uma lista com as matrículas dos alunos que estão aguardando na fila. Para cada aluno, começando do último, descubra quantos alunos de fato comerão no bandejão (em dias de comida ruim, pode ser que sobrem senhas!). Para tanto, pergunte para quantas pessoas ele está guardando lugar na fila e se ele irá continuar na fila (para esta pergunta ele deverá responder ‘S’ ou ‘N’). Com essa informação, atualize a fila, inserindo a matrícula daqueles que ainda irão chegar e removendo aqueles que vão sair da fila. Imprima a fila final, de acordo com ordem de chegada (se a fila for maior que 300, remover os excedentes antes de imprimir a fila);

- [ ] `:` Faça um programa que manipula uma lista que contém modelos de carro e seu consumo (km/l), da seguinte forma: [[‘Vectra’, 9], [‘Gol’, 10], [‘Corsa’, 11], [‘Fit’, 12.5]]. O programa deve mostrar na tela o nome do modelo mais econômico. Além disso, deve mostrar na tela quanto cada um desses modelos gastaria para percorrer 1000 Km, assumindo que o valor do litro da gasolina é R$ 3,50;

- [ ] `:` Faça um programa que funciona como uma agenda telefônica. A agenda deve ser guardada em uma lista com o seguinte formato: [[‘Ana’, ‘99999-1234’], [‘Bia’, ‘99999-5678’]]. O programa deve ter um menu que tenha as seguintes opções:

(a) Adicionar telefones na agenda -- isso deve ser feito de forma que ela se mantenha sempre ordenada -- cada nome novo já deve ser inserido na posição correta dentro da agenda;
(b) Procurar um telefone -- o usuário informa um nome e o programa mostra o número do telefone, ou diz que não está na agenda A busca deve ser inteligente: deve parar assim que encontrar um nome maior do que o nome que está sendo buscado, ao invés de percorrer a lista sempre até o final para concluir que um nome não está na agenda;

- [ ] `:`

### Módulo 4: Funções e Ordenação

- [ ] `Bogo Sort`;

- [ ] `Insertion Sort`;

- [ ] `Selection Sort`;

- [ ] `Bubble Sort`; 

- [ ] `Combinações:` O professor deseja dividir uma turma com N alunos em dois grupos: um com M alunos e outro com (N-M) alunos. Faça o programa que lê o valor de N e M e informa o número de combinações possíveis;

Obs: Número de combinações é igual a N!/(M! * (N-M)!)

- [ ] `Status:` Faça uma função que informe o status do aluno a partir da sua média de acordo com a tabela a seguir:

Nota acima de 6 → “Aprovado”
Nota entre 4 e 6 → “Verificação Suplementar”
Nota abaixo de 4 → “Reprovado”

- [ ] `Calculadora:` Faça uma calculadora que forneça as seguintes opções para o usuário, usando funções sempre que necessário. Cada opção deve usar como operando um número lido do teclado e o valor atual da memória. Por exemplo, se o estado atual da memória é 5, e o usuário escolhe somar, ele deve informar um novo número (por exemplo, 3). Após a conclusão da soma, o novo estado da memória passa a ser 8;

- [ ] `Calculadora:` Refaça o programa anterior para adicionar uma opção para escrever um número por extenso, agora aceitando números de até 9 dígitos e usando funções para as traduções;

- [ ] `Área:` Faça um programa que, dado uma figura geométrica que pode ser uma circunferência, triângulo ou retângulo, calcule a área e o perímetro da figura.
Obs: O programa deve primeiro perguntar qual o tipo da figura:
(1) circunferência
(2) triângulo
(3) retângulo
Obs: Dependendo do tipo de figura, ler o (1) tamanho do raio da circunferência; (2) tamanho de cada um dos lados do triângulo; (3) tamanho dos dois lados retângulo
Obs: Usar funções sempre que possível

- [ ] `Campeonato:` Refaça o exercício 1 da aula de manipulação de listas, usando uma função para calcular o total de faltas do campeonato, outra para calcular o time que fez mais faltas, e uma terceira para calcular o time que fez menos faltas. Antes de chamar essas funções, o programa deve permitir que o usuário adicione mais jogos ao campeonato;

### Módulo 5: Arquivos e Strings

- [ ] `Substitui Palavra:` Escreva uma função que recebe uma frase e uma palavra antiga e uma palavra nova. A função deve retornar uma string contendo a frase original, mas com as ocorrências da palavra antiga substituídas pela palavra nova. A entrada e saída de dados deve ser feita no programa principal;

- [ ] `Conta Palavras:` Faça uma função que recebe uma frase e retorna o número de palavras que a frase contém. Considere que a palavra pode começar e/ou terminar por espaços. A entrada e saída de dados deve ser feita no programa principal;

- [ ] `Tira Espaço:` Faça uma função que recebe uma frase e substitui todas as ocorrências de espaço por “#”. A entrada e saída de dados deve ser feita no programa principal;

- [ ] `Inverte:` Faça um programa que decida se duas strings lidas do teclado são palíndromas mútuas, ou seja, se uma é igual à outra quando lida de traz para frente;

Exemplo: amor e roma.

- [ ] `Inverte 2:` Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra ou frase. Por exemplo, “Iracema” é um anagrama para “America”. Escreva um programa que decida se uma string é um anagrama de outra string, ignorando os espaços em branco. O programa deve considerar maiúsculas e minúsculas como sendo caracteres iguais, ou seja, “a” = “A”;

- [ ] `Inverte 3:` Faça um programa que leia o nome do usuário e mostre o nome de traz para frente, utilizando somente letras maiúsculas;

Exemplo: Nome = Vanessa
Resultado gerado pelo programa: ASSENAV

- [ ] `Escada:` Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas;

Exemplo: Nome = Vanessa
Resultado gerado pelo programa:
V
VA
VAN
VANE
VANES
VANESS
VANESSA

- [ ] `Aniversário:` Faça um programa que leia uma data de nascimento no formato dd/mm/aaaa e imprima a data com o mês escrito por extenso;

Exemplo: Data = 20/02/1995
Resultado gerado pelo programa: Você nasceu em 20 de fevereiro de 1995

- [ ] `Justifica:` Faça um programa para justificar um texto com um número de colunas informado pelo usuário. Por exemplo, para o texto “Este é um exemplo de texto que vamos justificar usando o nosso programa.” quando justificado em 18 colunas, teríamos:

Este é um exemplo
de texto que vamos
justificar usando
o nosso programa.

- [ ] `Cadastro:` Faça um programa que leia um número N e gere um arquivo com N nomes e idades aleatórios;

Obs: Faça uso de duas listas criadas na mão: uma que contenha 20 nomes e outra que contenha 20 sobrenomes. Cada linha do arquivo resultante deve conter um nome completo e a sua idade;

- [ ] `Cadastro:` Estenda o exemplo do cadastro para considerar também a altura da pessoa;

- [ ] `Cópia:` Escreva uma função que recebe dois nomes de arquivos e copia o conteúdo do primeiro arquivo para o segundo arquivo. Considere que o conteúdo do arquivo de origem é um texto. Sua função não deve copiar linhas comentadas (que começam com #);

- [ ] `Média:` Faça um programa contendo uma função que recebe como argumentos os nomes de dois arquivos. O primeiro arquivo contém nomes de alunos e o segundo arquivo contém as notas dos alunos. No primeiro arquivo, cada linha corresponde ao nome de um aluno e no segundo arquivo, cada linha corresponde às notas dos alunos (uma ou mais). Assuma que as notas foram armazenadas como strings, e estão separadas umas das outras por espaços em branco. Leia os dois arquivos e gere um terceiro arquivo que contém o nome do aluno seguido da média de suas notas;

- [ ] `Altera Nota:` Faça um programa para alterar uma das notas de um aluno (usando os arquivos do exercício anterior). O programa deve ter uma função que recebe o nome do aluno, a nota velha e a nova nota. A função deve fazer a alteração no arquivo;

- [ ] `Valida IP:` Faça uma função que leia um arquivo texto contendo uma lista de endereços IP e gere dois outros arquivos, um contendo os endereços IP válidos e outro contendo os endereços inválidos. O formato de um endereço IP é num1.num.num.num, onde num1 vai de 1 a 255 e num vai de 0 a 255;
