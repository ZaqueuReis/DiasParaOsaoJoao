Contagem de Dias para o São João 

Este projeto em Python calcula quantos dias faltam para o dia 24 de junho (São João) a partir de uma data fornecida pelo usuário.
O programa também considera corretamente os anos bissextos, ajustando fevereiro para 29 dias quando necessário.
O que o programa faz

O usuário informa:

Dia
Mês
Ano

E o programa:

verifica se o ano é bissexto;
calcula quantos dias já passaram no ano;
calcula quantos dias faltam até o próximo São João;
imprime:
"Viva Sao Joao" caso seja 24 de junho;
ou a quantidade de dias restantes.

 Estrutura do código
anoBissexto(ano)

Função responsável por verificar se um ano é bissexto.

Retorna:

True e 366 caso seja bissexto;
False e 365 caso contrário.

Regras utilizadas:

divisível por 400 → bissexto;
divisível por 100 → não bissexto;
divisível por 4 → bissexto.
diasAteInicioDoMes(mes, ano)

Calcula quantos dias existem antes do mês informado.

Exemplo:

março → retorna os dias de janeiro + fevereiro;
julho → soma todos os meses anteriores.

A função também ajusta fevereiro dependendo do ano ser bissexto ou não.

calculoDias(dia, mes, ano)

Função principal do programa.

Ela:

calcula o dia atual dentro do ano;
calcula em qual dia do ano cai o São João;
verifica:
se o São João ainda vai acontecer no mesmo ano;
ou se já passou e será necessário calcular para o próximo ano.
▶️ Exemplo de execução

Entrada:

1
6
2026

Saída:

Faltam 23 dias para o Sao Joao chegar
🛠️ Tecnologias utilizadas
Linguagem: Python 3
📌 Observações

O código foi desenvolvido utilizando bastante lógica condicional (if/elif) para praticar:

funções;
manipulação de datas;
anos bissextos;
decomposição de problemas;
raciocínio lógico.

Apesar de existir maneiras mais curtas e elegantes de resolver o problema (como usando listas ou o módulo datetime), o foco deste projeto foi o aprendizado da lógica manualmente.

Como executar

Execute o arquivo Python:

Depois informe:

dia
mês
ano

cada valor em uma linha.
