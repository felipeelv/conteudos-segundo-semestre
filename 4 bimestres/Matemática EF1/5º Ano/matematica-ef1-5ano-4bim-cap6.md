# Capítulo 6 — Probabilidade

> Como medir uma chance quando o resultado ainda não pode ser previsto?

---

## 1. Situações aleatórias e previsíveis

Soltar uma pedra e lançar um dado são ações diferentes. A pedra cai; no dado, qualquer face pode ficar para cima.

```text
pedra solta → cai
dado lançado → 1, 2, 3, 4, 5 ou 6
```

### 1.1 Conhecer as opções sem prever a escolhida

Numa situação aleatória, sabemos os resultados que podem acontecer, mas não qual acontecerá.

- Sorteio de rifa é aleatório.
- Par ou ímpar é aleatório.
- Tirar uma carta embaralhada é aleatório.

Numa situação previsível, uma condição determina o resultado, como um objeto solto cair.

### 1.2 Classificar duas cenas

**Exemplo resolvido — Carta e calendário**

Retirar uma carta de um baralho embaralhado não permite prever a carta. Depois de segunda-feira, porém, vem terça-feira.

**Resposta:** a carta é aleatória; a sequência dos dias é previsível.

> ⚠️ **Atenção:**  
> Aleatório não significa que qualquer coisa possa acontecer.

---

## 2. Todos os resultados possíveis

Uma moeda oferece cara e coroa; um dado comum oferece as faces de 1 a 6. A lista precisa ficar completa.

```text
moeda: cara, coroa
dado:  1, 2, 3, 4, 5, 6
```

### 2.1 De um sorteio a dois dados

Num sorteio com 30 nomes, há 30 resultados possíveis, sem precisar copiá-los. Com dois dados, cada resultado é um par ordenado pelo dado azul e pelo dado branco.

```text
       branco: 1  2  3  4  5  6
azul 1:       (1,1) (1,2) (1,3) (1,4) (1,5) (1,6)
azul 2:       (2,1) (2,2) (2,3) (2,4) (2,5) (2,6)
azul 3:       (3,1) (3,2) (3,3) (3,4) (3,5) (3,6)
azul 4:       (4,1) (4,2) (4,3) (4,4) (4,5) (4,6)
azul 5:       (5,1) (5,2) (5,3) (5,4) (5,5) (5,6)
azul 6:       (6,1) (6,2) (6,3) (6,4) (6,5) (6,6)
```

### 2.2 Contar a tabela

**Exemplo resolvido — Dois dados**

Há 6 linhas e 6 pares em cada linha.

$$
\begin{aligned}
6\times6&=36
\end{aligned}
$$

**Resposta:** os dois dados formam 36 pares possíveis.

> 🔢 **Padrão:**  
> A organização evita omitir ou repetir resultados.

---

## 3. Resultados com chances iguais

Num dado honesto, nenhuma face é favorecida. Assim, 1, 2, 3, 4, 5 e 6 têm a mesma chance.

```text
dado honesto: 1 = 2 = 3 = 4 = 5 = 6 em chance
sacola: 8 azuis e 2 vermelhas → chances diferentes
```

### 3.1 Quando contar é suficiente

Resultados **equiprováveis** têm chances iguais.

- Cara e coroa são equiprováveis numa moeda honesta.
- As seis faces são equiprováveis num dado honesto.
- Cores com quantidades diferentes numa sacola não são equiprováveis.

Só quando os resultados têm chances iguais a contagem serve diretamente para calcular a probabilidade.

### 3.2 Comparar dois objetos

**Exemplo resolvido — Moeda e sacola**

Na moeda há uma face de cada tipo. Na sacola, há quatro vezes mais bolas azuis que vermelhas.

$$
\begin{aligned}
8\div2&=4
\end{aligned}
$$

**Resposta:** a moeda tem chances iguais; as cores da sacola não têm.

> ⚠️ **Atenção:**  
> Contar resultados não basta quando alguns são favorecidos.

---

## 4. Casos favoráveis e casos possíveis

Ao buscar um número par no dado, servem as faces 2, 4 e 6. Existem seis faces possíveis ao todo.

```text
favoráveis: 2, 4, 6 → 3
possíveis:  1, 2, 3, 4, 5, 6 → 6
```

### 4.1 Escrever a razão na ordem certa

A probabilidade compara casos favoráveis com casos possíveis, nessa ordem.

- O numerador conta os resultados que servem.
- O denominador conta todos os resultados.
- A fração pode ser simplificada.

Sair 7 é impossível e tem valor 0; sair um número de 1 a 6 é certo e tem valor 1.

### 4.2 Chance de sair par

**Exemplo resolvido — Dado comum**

$$
\begin{aligned}
\frac{3}{6}&=\frac{1}{2}
\end{aligned}
$$

**Resposta:** a chance de sair um número par é um meio.

> 🔢 **Padrão:**  
> Favoráveis ficam em cima; possíveis, embaixo.

---

## 5. Fração, decimal e porcentagem da chance

Numa moeda honesta, uma das duas faces favorece cara. A chance `1/2` também pode ser comunicada como 0,5 ou 50%.

```text
1/2  ↔  0,5  ↔  50%
```

### 5.1 Três escritas do mesmo valor

A fração mostra a contagem. O decimal e a porcentagem ajudam a comunicar a chance.

- Um meio corresponde a 0,5 e 50%.
- Um quarto corresponde a 0,25 e 25%.
- Um décimo corresponde a 0,1 e 10%.

### 5.2 Converter pelas divisões conhecidas

**Exemplo resolvido — Roleta com quatro partes iguais**

Uma das quatro partes é verde.

$$
\begin{aligned}
\frac{1}{4}&=1\div4\\
&=0{,}25\\
&=25\%
\end{aligned}
$$

**Resposta:** a chance de verde é `1/4`, 0,25 ou 25%.

> 🔢 **Padrão:**  
> Mudar a escrita não muda a chance representada.
