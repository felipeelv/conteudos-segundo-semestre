# Capítulo 1 — Sequências e padrões

> Existe regularidade em sequências aparentemente caóticas? Como descobrir o termo 100 sem calcular os 99 primeiros?
---

## 1. Sequências numéricas: identificação de padrões

Sequência: lista ordenada de números; termo e posição (1º, 2º, …, n-ésimo).

### 1.1 Conceito e linguagem

A definição fica completa com estas relações:
- Estratégias de identificação de padrão: diferenças sucessivas, razões sucessivas, alternâncias.
- Exemplos variados de padrões (2, 5, 8, 11… · 3, 6, 12, 24… · 1, 4, 9, 16…) e a pergunta "qual é a regra?".

### 1.2 Procedimento e interpretação

**Diferenças observadas**

**Resolução:**

$$S=(4,7,10,13,\ldots)$$

$$d=3$$

$$a_5=16$$

**Resposta:** a regularidade +3 produz o termo seguinte 16.

Leonardo Fibonacci (c. 1170–c. 1240/50) é a referência histórica deste tema matemático.
---

## 2. Padrões de adição e de multiplicação; termos seguintes

Padrão aditivo (PA informal): diferença constante entre termos consecutivos (aₙ₊₁ = aₙ + r).

### 2.1 Conceito e linguagem

Na leitura da notação, dois pontos são decisivos:
- Padrão multiplicativo (PG informal): razão constante entre termos consecutivos (aₙ₊₁ = aₙ · q).
- Determinar termos seguintes aplicando o padrão; não confundir diferença (subtração) com razão (divisão).

### 2.2 Procedimento e interpretação

**Dois padrões**

**Resolução:**

$$A=(3,6,9,12,\ldots)$$

$$M=(3,6,12,24,\ldots)$$

$$M_5=48$$

**Resposta:** somar 3 e multiplicar por 2 produzem sequências diferentes.

---

## 3. Sequências não recursivas: regularidade por fórmula

Sequência não recursiva: o termo depende só da posição n, não dos termos anteriores.

### 3.1 Conceito e linguagem

O procedimento preserva estas condições:
- Fórmula explícita aₙ = f(n): exemplos aₙ = 2n + 1, aₙ = n², aₙ = 3n − 2.
- O poder da fórmula direta: a₁₀₀ sem calcular os 99 primeiros (aₙ = 2n + 1 ⟹ a₁₀₀ = 201).

### 3.2 Procedimento e interpretação

**Fórmula direta**

**Resolução:**

$$a_n=4n-1$$

$$a_7=27$$

**Resposta:** a posição 7 fornece o termo 27 sem calcular os anteriores.

---

## 4. Termo geral de sequências simples; fluxograma

Encontrar o termo geral a partir dos primeiros termos (do padrão observado à fórmula).

### 4.1 Conceito e linguagem

A definição fica completa com estas relações:
- Fluxograma como algoritmo: entrada n → calcular f(n) → saída aₙ (BNCC EF08MA10).
- Atenção à notação: a₁ é o primeiro termo (n = 1); verificar a fórmula em pelo menos 3 termos.

### 4.2 Procedimento e interpretação

**Fluxo posição-termo**

**Resolução:**

$$n=6$$

$$a_n=2n+3$$

$$a_6=15$$

**Resposta:** o fluxograma multiplica a posição por 2 e soma 3.

---

## 5. Sequências recursivas: termo a partir do anterior

Sequência recursiva: cada termo "lê" o anterior — aₙ = g(aₙ₋₁); exemplos: aₙ = aₙ₋₁ + 3; aₙ = 2aₙ₋₁.

### 5.1 Conceito e linguagem

Na leitura da notação, dois pontos são decisivos:
- Toda recursão precisa de caso base (primeiros termos definidos) + regra de avanço.
- Fluxograma com repetição (loop) até atingir a posição desejada (BNCC EF08MA11).

### 5.2 Procedimento e interpretação

**Regra recursiva**

**Resolução:**

$$a_1=2$$

$$a_{n+1}=2a_n+1$$

$$a_4=23$$

**Resposta:** cada termo é o dobro do anterior mais 1.

---

## 6. Sequência de Fibonacci (introdução)

A regra: Fₙ = Fₙ₋₁ + Fₙ₋₂, com F₁ = F₂ = 1 — recursão que olha dois termos para trás.

### 6.1 Conceito e linguagem

O procedimento preserva estas condições:
- O problema dos coelhos do Liber Abaci (1202) e a construção dos primeiros termos: 1, 1, 2, 3, 5, 8, 13, 21….
- Fibonacci na natureza: espirais de girassol, conchas, ramificação de árvores (apresentação, sem proporção áurea formalizada).

### 6.2 Procedimento e interpretação

**Soma dos anteriores**

**Resolução:**

$$F_1=1$$

$$F_2=1$$

$$F_7=13$$

**Resposta:** cada termo após os dois iniciais soma os dois anteriores.

---

## 7. Sequências figurais: padrões visuais e contagem

Sequência figural: o padrão está na figura e gera os números (palitos, bolinhas, quadrados).

### 7.1 Conceito e linguagem

A definição fica completa com estas relações:
- Contagem sistemática dos elementos das primeiras figuras; organizar em tabela posição × quantidade.
- Números triangulares (1, 3, 6, 10…) e quadrados (1, 4, 9, 16…) como sequências figurais clássicas.

### 7.2 Procedimento e interpretação

**Pontos triangulares**

**Resolução:**

$$T_n=\frac{n(n+1)}{2}$$

$$T_4=10$$

**Resposta:** a quarta figura triangular contém 10 pontos.

---

## 8. Generalização algébrica; relação posição–quantidade

Da tabela à fórmula: encontrar aₙ que liga a posição n à quantidade f(n).

### 8.1 Conceito e linguagem

Na leitura da notação, dois pontos são decisivos:
- Fórmulas das figurais clássicas: triangulares Tₙ = n(n+1)/2; quadrados Qₙ = n²; verificação em 3 termos antes de generalizar.
- Síntese do capítulo: padrão → regra (direta ou recursiva) → fórmula — a generalização algébrica prepara as funções do 9º Ano.

### 8.2 Procedimento e interpretação

**Palitos por posição**

**Resolução:**

$$q(n)=3n+1$$

$$q(8)=25$$

**Resposta:** a oitava figura exige 25 palitos.

