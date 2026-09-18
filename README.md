# Sistema de Controle de Qualidade de Peças Industriais

Projeto desenvolvido em Python para a disciplina de Algoritmos e Lógica de Programação.

O sistema simula o controle de qualidade de peças industriais, realizando o cadastro, a aprovação ou reprovação das peças, a organização das peças aprovadas em caixas e a geração de um relatório final.

## Autor

Ronaldo Gomes Reis

## Funcionalidades

O sistema permite:

- Cadastrar peças industriais;
- Impedir o cadastro de IDs repetidos;
- Validar peso, cor e comprimento;
- Listar peças aprovadas e reprovadas;
- Informar os motivos de reprovação;
- Remover uma peça cadastrada;
- Organizar peças aprovadas em caixas;
- Fechar automaticamente uma caixa com 10 peças;
- Listar caixas fechadas e a caixa atual;
- Gerar um relatório final consolidado.

## Critérios de qualidade

Uma peça será aprovada quando atender simultaneamente aos seguintes critérios:

| Característica | Critério de aprovação |
|---|---|
| Peso | Entre 95 g e 105 g |
| Cor | Azul ou verde |
| Comprimento | Entre 10 cm e 20 cm |

Se um ou mais critérios não forem atendidos, a peça será reprovada e o sistema apresentará os motivos.

## Organização das caixas

Somente peças aprovadas são adicionadas às caixas.

Cada caixa possui capacidade máxima de 10 peças. Quando a décima peça aprovada é cadastrada, a caixa é fechada automaticamente e uma nova caixa é iniciada.

## Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub

O projeto não utiliza bibliotecas externas.

## Como executar

1. Instale o Python 3.
2. Baixe ou clone este repositório.
3. Abra a pasta do projeto no Visual Studio Code.
4. Abra o terminal na pasta do projeto.
5. Execute o comando:

```bash
python sistema_qualidade.py
```

## Menu principal

```text
=== MENU PRINCIPAL ===
1. Cadastrar nova peça
2. Listar peças aprovadas e reprovadas
3. Remover uma peça
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
```

## Exemplo de entrada — peça aprovada

```text
Digite o ID da peça: 001
Digite o peso em gramas: 100
Digite a cor da peça: azul
Digite o comprimento em centímetros: 15
```

Saída esperada:

```text
Peça 001 APROVADA e adicionada à caixa atual.
```

## Exemplo de entrada — peça reprovada

```text
Digite o ID da peça: 002
Digite o peso em gramas: 120
Digite a cor da peça: vermelha
Digite o comprimento em centímetros: 25
```

Saída esperada:

```text
Peça 002 REPROVADA.
- Peso fora do padrão de 95g a 105g
- Cor inválida: deve ser azul ou verde
- Comprimento fora do padrão de 10cm a 20cm
```

## Exemplo de relatório

```text
--- RELATÓRIO FINAL ---
Total de peças cadastradas: 2
Total de peças aprovadas: 1
Total de peças reprovadas: 1
Caixas fechadas: 0
Peças na caixa atual: 1
Quantidade de caixas utilizadas: 1

--- MOTIVOS DE REPROVAÇÃO ---
ID 002: Peso fora do padrão de 95g a 105g, Cor inválida: deve ser azul ou verde, Comprimento fora do padrão de 10cm a 20cm
```

## Estruturas utilizadas

Os dados são armazenados em listas e dicionários durante a execução do programa:

- `pecas`: armazena todas as peças cadastradas;
- `caixa_atual`: armazena as peças aprovadas da caixa em preenchimento;
- `caixas_fechadas`: armazena as caixas que atingiram 10 peças.

Os dados permanecem na memória somente enquanto o programa estiver aberto. Ao encerrar e executar novamente, as listas começam vazias.

## Arquivo principal

```text
sistema_qualidade.py
```

## Status do projeto

Projeto concluído e testado.