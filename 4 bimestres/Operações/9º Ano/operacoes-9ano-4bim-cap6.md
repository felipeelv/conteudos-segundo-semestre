# Capítulo 6 — Sistemas 3×3 e escalonamento

> Três frutas somam 17 kg; a maçã pesa o dobro da banana; a pera pesa 5 kg a menos que a maçã. Três informações, três incógnitas — os métodos do 2×2 ainda dão conta?
---

## 1. Sistemas lineares 3×3: representação

Sistema 3×3: três equações, três incógnitas; solução como tripla ordenada (x, y, z).

### 1.1 Conceito e linguagem

A definição fica completa com estas relações:
- Forma geral com \begin{cases}; leitura geométrica leve: três planos no espaço buscando um ponto comum.
- Organização da escrita: cada incógnita na sua coluna — a disciplina que evita erros.

### 1.2 Procedimento e interpretação

**Três planos**

**Resolução:**

$$x+y+z=6$$

$$x-y+z=2$$

$$x+y-z=0$$

**Resposta:** três equações lineares representam três planos no espaço.

Gabriel Cramer (1704–1752) é a referência histórica deste tema matemático.
---

## 2. Escalonamento

Ideia: transformar o sistema em forma triangular — 1ª equação com 3 incógnitas, 2ª com 2, 3ª com 1.

### 2.1 Conceito e linguagem

Na leitura da notação, dois pontos são decisivos:
- Operações elementares (multiplicar equação por constante; somar equações) não alteram a solução — só simplificam.
- Passo a passo completo: eliminar x da 2ª e da 3ª usando a 1ª; eliminar y da 3ª usando a 2ª; resolver z; substituição reversa (z → y → x).

### 2.2 Procedimento e interpretação

**Forma escalonada**

**Resolução:**

$$x+y+z=6$$

$$y+z=3$$

$$z=1$$

**Resposta:** a forma triangular permite resolver de baixo para cima.

---

## 3. Aplicação dos métodos em sistemas 3×3

Resolução integral de sistemas 3×3 numéricos pelo escalonamento, com verificação da tripla nas três equações.

### 3.1 Conceito e linguagem

O procedimento preserva estas condições:
- Quando substituição/adição diretas ainda funcionam (sistemas pequenos com variável fácil de isolar) e por que o escalonamento é mais sistemático.
- Curiosidade histórica: Cramer (1750) e os determinantes; Gauss e a órbita de Ceres (1801) — o 3×3 como porta para a álgebra linear do EM.

### 3.2 Procedimento e interpretação

**Três produtos**

**Resolução:**

$$x+y+z=9$$

$$x-y=1$$

$$z=2$$

- **Passo 4:** Conferir no modelo original.

$$(x,y,z)=(4,3,2)$$

**Resposta:** o trio 4, 3 e 2 satisfaz as três condições.

