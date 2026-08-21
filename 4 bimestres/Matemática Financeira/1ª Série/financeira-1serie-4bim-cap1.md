# Capítulo 1 — Análise combinatória

> As placas Mercosul têm quatro letras e três algarismos. Como contar quase meio bilhão de possibilidades sem listar nenhuma delas?

---

## 1. Princípio fundamental da contagem

### 1.1 Multiplicar etapas e somar alternativas

O **princípio fundamental da contagem** multiplica as quantidades de escolhas de etapas sucessivas. Se uma refeição tem 3 opções de prato e 2 de bebida, cada prato se ramifica em 2 bebidas: $3\cdot2=6$ refeições. Uma árvore de possibilidades torna visíveis essas ramificações.

Em geral, para etapas independentes,

$$
N=n_1\cdot n_2\cdot\ldots\cdot n_k.
$$

O conectivo “e” costuma indicar multiplicação. Já alternativas mutuamente exclusivas ligadas por “ou” são somadas. Se um código pode ser uma letra **ou** um algarismo, há $26+10=36$ escolhas.

Bhaskara II tratou de problemas de permutação em *Lilavati*, no século XII, séculos antes da sistematização europeia da combinatória.

### 1.2 Placas e restrições

Cada uma das quatro posições de letras de uma placa possui 26 possibilidades, e cada posição numérica possui 10. Admitindo repetições:

**Resolução:**

- **Passo 1:** Contar as sequências de letras.

$$
26^4=456\,976
$$

- **Passo 2:** Contar as sequências de algarismos.

$$
10^3=1\,000
$$

- **Passo 3:** Multiplicar as etapas.

$$
456\,976\cdot1\,000=456\,976\,000
$$

**Resposta:** o padrão permite 456.976.000 placas, considerando apenas as posições e a repetição permitida.

Uma restrição altera as escolhas seguintes. Para formar quatro letras distintas, há 26 opções na primeira posição, 25 na segunda, 24 na terceira e 23 na quarta:

$$
26\cdot25\cdot24\cdot23=358\,800.
$$

O mesmo raciocínio vale para senhas sem repetição. A árvore continua possível, mas a multiplicação resume um número enorme de ramos.

> 🔢 **Em resumo:** antes de multiplicar, identifique as etapas e verifique se cada escolha muda as opções seguintes.

---

## 2. Arranjos e permutações simples

### 2.1 Fatorial e arranjo

O **fatorial** de um natural $n$ é o produto decrescente até 1:

$$
n!=n\cdot(n-1)\cdot\ldots\cdot2\cdot1.
$$

Por convenção, $0!=1$ e $1!=1$. Por exemplo, $5!=5\cdot4\cdot3\cdot2\cdot1=120$. Para escolher $p$ elementos distintos entre $n$ e considerar a ordem, usa-se o **arranjo simples**:

$$
A(n,p)=\frac{n!}{(n-p)!}.
$$

Em uma final com oito competidores, quantos pódios diferentes podem ocupar primeiro, segundo e terceiro lugares?

**Resolução:**

- **Passo 1:** Há 8 escolhas para o primeiro lugar, 7 para o segundo e 6 para o terceiro.

$$
8\cdot7\cdot6=336
$$

- **Passo 2:** Conferir pela fórmula.

$$
A(8,3)=\frac{8!}{5!}=8\cdot7\cdot6=336
$$

**Resposta:** existem 336 pódios, pois trocar as posições produz outro resultado.

### 2.2 Permutar todos

Quando todos os $n$ elementos distintos são ordenados, ocorre uma **permutação simples**:

$$
P(n)=n!=A(n,n).
$$

As letras distintas de ROMA podem ser ordenadas de $4!=24$ maneiras. A primeira posição oferece 4 escolhas; depois restam 3, 2 e 1.

Arranjo e permutação consideram a ordem. A diferença é que o arranjo usa apenas parte dos elementos, enquanto a permutação usa todos. Se apenas o grupo importasse, e não sua ordem, teríamos uma **combinação**. Escolher Ana e Beto representa o mesmo grupo que escolher Beto e Ana; já primeiro Ana e segundo Beto é uma ordenação diferente.

| Situação | Usa todos? | Ordem importa? |
|---|---:|---:|
| pódio com 3 de 8 | não | sim |
| fila com 8 pessoas | sim | sim |
| comissão com 3 de 8 | não | não |

Aqui, a combinação é apenas distinguida conceitualmente; sua fórmula pertence a um estudo posterior.

> ⚠️ **Atenção:** contar um mesmo grupo em ordens diferentes quando a ordem não importa produz repetição indevida.
