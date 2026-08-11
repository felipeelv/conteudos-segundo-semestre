# Operações — 3ª Série · Bloco 2

> **3º Bimestre — Funções e álgebra (aprofundamento)** · Bloco 2 (27/08–18/09)

**Capítulos deste bloco**

4. **Matrizes, determinantes e sistemas lineares** (6 aulas)
5. **Polinômios** (2 aulas)
6. **Progressões aritméticas e geométricas** (4 aulas)

---

# BL2_Capítulo 1 — Matrizes, determinantes e sistemas lineares

> Como matrizes, determinantes e sistemas se conectam?

---

## 1. Matrizes: tipos

### 1.1 Ordem e elementos

**Matriz** é uma organização retangular de elementos. Em uma matriz de ordem $$m\times n$$, o elemento $$a_{ij}$$ ocupa a linha $$i$$ e a coluna $$j$$.

Os tipos principais são:

- linha: uma linha;
- coluna: uma coluna;
- quadrada: mesmo número de linhas e colunas;
- nula: todos os elementos iguais a zero;
- identidade: diagonal principal igual a 1 e demais elementos iguais a zero;
- transposta: linhas e colunas trocam de posição;
- simétrica: matriz quadrada igual à própria transposta.

### 1.2 Igualdade e sistemas

Duas matrizes são iguais quando têm a mesma ordem e elementos correspondentes iguais. A matriz dos coeficientes registra um sistema mantendo cada incógnita em uma coluna fixa.

**Leitura de uma matriz**

Considere:

$$A=\begin{pmatrix}2&-1&0\\4&3&5\end{pmatrix}$$

Determine a ordem, $$a_{23}$$ e a transposta.

**Resolução:**

- **Passo 1:** Contar linhas e colunas: $$A\text{ tem ordem }2\times3$$.

- **Passo 2:** Ler linha 2, coluna 3.

$$a_{23}=5$$

- **Passo 3:** Trocar linhas por colunas.

$$A^T=\begin{pmatrix}2&4\\-1&3\\0&5\end{pmatrix}$$

**Resposta:** a ordem é 2×3, $$a_{23}=5$$ e a transposta é a matriz apresentada.

> ⚠️ **Atenção:**  
> A posição $$a_{ij}$$ é lida como linha $$i$$ e coluna $$j$$, nessa ordem.

---

## 2. Matrizes: operações

### 2.1 Operações básicas

Adição e subtração exigem matrizes de mesma ordem e operam elementos correspondentes. Multiplicar por um escalar multiplica cada elemento.

No produto $$AB$$, o número de colunas de $$A$$ deve igualar o número de linhas de $$B$$. Cada elemento resulta do produto de uma linha por uma coluna. Em geral:

$$AB\neq BA$$

### 2.2 Produto e inversa

**Produto linha por coluna**

Considere:

$$A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$$

$$B=\begin{pmatrix}2&0\\1&5\end{pmatrix}$$

Calcule $$AB$$.

**Resolução:**

- **Passo 1:** Calcular o elemento da linha 1, coluna 1.

$$c_{11}=1\times2+2\times1$$

$$c_{11}=4$$

- **Passo 2:** Calcular o elemento da linha 1, coluna 2.

$$c_{12}=1\times0+2\times5$$

$$c_{12}=10$$

- **Passo 3:** Calcular os elementos da segunda linha.

$$c_{21}=3\times2+4\times1$$

$$c_{21}=10$$

$$c_{22}=3\times0+4\times5$$

$$c_{22}=20$$

- **Passo 4:** Montar o produto.

$$AB=\begin{pmatrix}4&10\\10&20\end{pmatrix}$$

**Resposta:** o produto é a matriz apresentada.

A inversa de uma matriz quadrada $$A$$ satisfaz $$AA^{-1}=I$$. Ela existe somente quando $$\det A\neq0$$ e permite escrever a solução de $$AX=B$$ como $$X=A^{-1}B$$.

> 🔢 **Padrão:**  
> A ordem do produto é linhas da primeira matriz por colunas da segunda.

---

## 3. Determinantes: cálculo

### 3.1 Segunda e terceira ordens

Para uma matriz 2×2:

$$A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$$

$$\det A=ad-bc$$

Na ordem 3, a regra de Sarrus soma os três produtos das diagonais descendentes e subtrai os três produtos das diagonais ascendentes.

### 3.2 Cofatores e Laplace

O menor complementar $$M_{ij}$$ é o determinante obtido ao retirar a linha $$i$$ e a coluna $$j$$. O cofator é:

$$C_{ij}=(-1)^{i+j}M_{ij}$$

A expansão de Laplace calcula o determinante pela soma dos elementos de uma linha ou coluna multiplicados por seus cofatores.

**Determinante de ordem 3**

Calcule:

$$A=\begin{pmatrix}1&2&0\\3&1&2\\0&4&1\end{pmatrix}$$

**Resolução:**

- **Passo 1:** Aplicar Sarrus.

$$\det A=1\times1\times1+2\times2\times0+0\times3\times4-0\times1\times0-2\times3\times1-1\times2\times4$$

- **Passo 2:** Calcular os produtos.

$$\det A=1-6-8$$

$$\det A=-13$$

**Resposta:** $$\det A=-13$$.

> ⚠️ **Atenção:**  
> Determinante é definido para matrizes quadradas; matriz retangular não possui determinante.

---

## 4. Determinantes: propriedades

### 4.1 Efeito das operações nas linhas

Três transformações são essenciais:

- linha nula implica determinante zero;
- trocar duas linhas muda o sinal do determinante;
- multiplicar uma linha por $$k$$ multiplica o determinante por $$k$$;
- somar a uma linha um múltiplo de outra preserva o determinante;
- linhas proporcionais implicam determinante zero.

Além disso:

$$\det(AB)=\det A\times\det B$$

Uma matriz quadrada é inversível exatamente quando seu determinante é diferente de zero.

### 4.2 Simplificar antes de calcular

**Determinante por transformação**

Considere:

$$A=\begin{pmatrix}1&2\\3&7\end{pmatrix}$$

Subtraia três vezes a primeira linha da segunda.

**Resolução:**

- **Passo 1:** Efetuar a operação que preserva o determinante: $$L_2\leftarrow L_2-3L_1$$.

- **Passo 2:** Obter a matriz triangular.

$$A'=\begin{pmatrix}1&2\\0&1\end{pmatrix}$$

- **Passo 3:** Multiplicar os elementos da diagonal.

$$\det A=1\times1$$

$$\det A=1$$

**Resposta:** $$\det A=1$$, portanto $$A$$ é inversível.

**Sofya Kovalevskaya** tornou-se, em 1874, a primeira mulher a obter um doutorado em Matemática e depois ocupou uma cátedra em Estocolmo. Sua obra conectou álgebra, equações diferenciais e mecânica.

> 🔢 **Padrão:**  
> Operações que criam zeros sem alterar o determinante tornam o cálculo mais curto.

---

## 5. Sistemas lineares: métodos

### 5.1 Escolha do método

Quatro métodos formam uma caixa integrada:

- substituição: variável isolada ou coeficiente 1;
- adição: coeficientes facilmente opostos;
- escalonamento: sistemas maiores;
- Cramer: sistema quadrado pequeno com determinante não nulo.

### 5.2 Resolução e verificação

**Sistema de duas condições**

Resolva:

$$\begin{cases}2x+3y=8\\x-y=-1\end{cases}$$

**Resolução:**

- **Passo 1:** Isolar $$x$$ na segunda equação.

$$x=y-1$$

- **Passo 2:** Substituir na primeira.

$$2(y-1)+3y=8$$

$$5y=10$$

$$y=2$$

- **Passo 3:** Calcular $$x$$.

$$x=2-1$$

$$x=1$$

- **Passo 4:** Verificar nas equações originais.

$$2\times1+3\times2=8$$

$$1-2=-1$$

**Resposta:** a solução é $$(1,2)$$.

No formato matricial, o mesmo problema é $$AX=B$$. Substituição e adição são práticas para sistemas 2×2; escalonamento evita a explosão de determinantes em ordens maiores.

> ⚠️ **Atenção:**  
> A solução deve ser conferida nas equações originais, não apenas nas transformadas.

---

## 6. Sistemas lineares: classificação e discussão

### 6.1 Determinante e posto

Para sistema quadrado, $$\det A\neq0$$ garante uma solução única. Quando $$\det A=0$$, determinantes auxiliares não bastam em toda ordem; a classificação geral usa os postos:

- se $$\mathrm{posto}(A)\neq\mathrm{posto}([A|B])$$, o sistema é impossível;
- se os postos são iguais ao número de incógnitas, é possível e determinado;
- se os postos são iguais e menores que o número de incógnitas, é possível e indeterminado.

### 6.2 Discussão com parâmetro

**Parâmetro no sistema**

Classifique conforme $$m$$:

$$\begin{cases}mx+y=3\\x+y=2\end{cases}$$

**Resolução:**

- **Passo 1:** Calcular o determinante dos coeficientes.

$$\det A=m-1$$

- **Passo 2:** Analisar o caso não nulo: $$m\neq1$$.

Nesse caso, o sistema tem solução única.

- **Passo 3:** Substituir $$m=1$$.

$$\begin{cases}x+y=3\\x+y=2\end{cases}$$

As equações se contradizem.

**Resposta:** o sistema é determinado para $$m\neq1$$ e impossível para $$m=1$$.

Sistemas modelam balanceamento químico e relações econômicas, como a matriz de Leontief. Em cada aplicação, as variáveis e unidades completam a interpretação algébrica.

> 🔢 **Padrão:**  
> Determinante não nulo decide a unicidade; determinante zero exige análise de compatibilidade.

---

# BL2_Capítulo 2 — Polinômios

> Como operar, dividir e decompor polinômios?

---

## 1. Polinômios: operações

### 1.1 Operações e grau

Adição e subtração agrupam termos de mesmo grau. A multiplicação aplica a distributividade e soma os expoentes das potências de mesma base.

Se os coeficientes líderes não se anularem:

- o grau do produto é a soma dos graus;
- o grau da soma não supera o maior grau das parcelas;
- na divisão, o grau do resto é menor que o grau do divisor.

A divisão euclidiana é expressa por:

$$P(x)=D(x)Q(x)+R(x)$$

### 1.2 Chave e Briot–Ruffini

A chave funciona para qualquer divisor polinomial. Briot–Ruffini abrevia a divisão quando o divisor tem a forma $$x-r$$.

**Divisão por um binômio**

Divida $$P(x)=x^3-6x^2+11x-6$$ por $$x-1$$ usando Ruffini.

**Resolução:**

- **Passo 1:** Registrar a raiz do divisor e os coeficientes: $$1,-6,11,-6$$.

$$r=1$$

- **Passo 2:** Baixar o primeiro coeficiente e efetuar as multiplicações e somas sucessivas: $$1$$.

$$-6+1=-5$$

$$11+(-5)=6$$

$$-6+6=0$$

- **Passo 3:** Ler quociente e resto.

$$Q(x)=x^2-5x+6$$

$$R(x)=0$$

**Resposta:** $$P(x)=(x-1)(x^2-5x+6)$$.

**Charles Hermite** provou, em 1873, que $$e$$ não é raiz de polinômio inteiro não nulo.

> ⚠️ **Atenção:**  
> Termos ausentes devem entrar na divisão com coeficiente zero para preservar as posições.

---

## 2. Polinômios: teoremas e raízes

### 2.1 Resto, D'Alembert e raízes racionais

O Teorema do Resto afirma que o resto da divisão de $$P(x)$$ por $$x-r$$ é $$P(r)$$. Portanto:

$$P(r)=0\iff (x-r)\mid P(x)$$

Esse é o Teorema de D'Alembert. Candidatos racionais usam divisores do termo independente sobre divisores do coeficiente líder.

### 2.2 Fatoração, Girard e multiplicidade

**Fatoração completa**

Fatore $$P(x)=x^3-6x^2+11x-6$$.

**Resolução:**

- **Passo 1:** Testar o candidato 1.

$$P(1)=1-6+11-6$$

$$P(1)=0$$

- **Passo 2:** Usar o quociente da divisão por $$x-1$$.

$$Q(x)=x^2-5x+6$$

- **Passo 3:** Fatorar o trinômio.

$$Q(x)=(x-2)(x-3)$$

- **Passo 4:** Escrever a decomposição.

$$P(x)=(x-1)(x-2)(x-3)$$

**Resposta:** as raízes são 1, 2 e 3, todas de multiplicidade 1.

Girard relaciona coeficientes a somas e produtos das raízes. Pelo Teorema Fundamental da Álgebra, grau $$n$$ implica $$n$$ raízes complexas, contadas com multiplicidade.

> 🔢 **Padrão:**  
> Uma raiz de multiplicidade $$k$$ produz o fator $$(x-r)^k$$.

---

# BL2_Capítulo 3 — Progressões aritméticas e geométricas

> Como calcular termos e somas de PA e PG?

---

## 1. Progressão aritmética: termo geral

### 1.1 Razão e identificação

**Progressão aritmética (PA)** é a sequência em que a diferença entre termos consecutivos é constante:

$$r=a_{n+1}-a_n$$

Se $$r>0$$, a PA é crescente; se $$r<0$$, decrescente; se $$r=0$$, constante.

### 1.2 Termo geral e função afim

O termo de posição $$n$$ é:

$$a_n=a_1+(n-1)r$$

Cada avanço de posição acrescenta $$r$$; é um modelo afim discreto.

**Arquibancada em fileiras**

Uma arquibancada tem 18 lugares na primeira fileira e ganha 4 lugares por fileira. Determine a 20ª fileira.

**Resolução:**

- **Passo 1:** Identificar os dados.

$$a_1=18$$

$$r=4$$

$$n=20$$

- **Passo 2:** Aplicar o termo geral.

$$a_{20}=18+(20-1)\times4$$

$$a_{20}=18+76$$

$$a_{20}=94$$

**Resposta:** a 20ª fileira tem 94 lugares.

**Abu Bakr al-Karaji**, no *Al-Fakhri* por volta do ano 1000, sistematizou propriedades de progressões e usou raciocínios precursores da indução para fórmulas de somas.

> 🔢 **Padrão:**  
> PA apresenta diferenças constantes e corresponde a um modelo afim discreto.

---

## 2. Soma dos termos de uma PA

### 2.1 Fórmula da soma

Em uma PA finita, o primeiro e o último termo têm a mesma soma que o segundo e o penúltimo. Esse pareamento conduz a:

$$S_n=\frac{n(a_1+a_n)}{2}$$

Gauss usou esse pareamento para somar rapidamente os inteiros de 1 a 100.

### 2.2 Termos equidistantes

Termos equidistantes dos extremos têm soma constante. Em três termos consecutivos, o termo central é a média aritmética dos vizinhos.

**Soma das fileiras**

Calcule o total de lugares nas 20 fileiras da PA com $$a_1=18$$ e $$a_{20}=94$$.

**Resolução:**

- **Passo 1:** Aplicar a fórmula.

$$S_{20}=\frac{20(18+94)}{2}$$

- **Passo 2:** Somar os extremos.

$$S_{20}=\frac{20\times112}{2}$$

- **Passo 3:** Simplificar.

$$S_{20}=10\times112$$

$$S_{20}=1120$$

**Resposta:** as 20 fileiras totalizam 1.120 lugares.

Acúmulos com aumento linear, como depósitos que crescem por uma quantia fixa mensal, são modelados pela soma de uma PA.

> ⚠️ **Atenção:**  
> Na fórmula da soma, $$n$$ é a quantidade de termos, não o valor do último termo.

---

## 3. Progressão geométrica: termo geral

### 3.1 Razão e identificação

**Progressão geométrica (PG)** é a sequência em que o quociente entre termos consecutivos não nulos é constante:

$$q=\frac{a_{n+1}}{a_n}$$

O comportamento depende de $$q$$ e dos sinais dos termos. Com $$a_1>0$$ e $$q>1$$, a PG cresce; com $$0<q<1$$, decresce em direção a zero; com $$q<0$$, alterna sinais.

### 3.2 Termo geral e função exponencial

O termo de posição $$n$$ é:

$$a_n=a_1q^{n-1}$$

A PG é uma função exponencial restrita aos naturais.

**Crescimento de uma cultura**

Uma cultura começa com 500 células e dobra a cada período. Determine o 8º termo.

**Resolução:**

- **Passo 1:** Identificar os dados.

$$a_1=500$$

$$q=2$$

$$n=8$$

- **Passo 2:** Aplicar o termo geral.

$$a_8=500\times2^{8-1}$$

$$a_8=500\times128$$

$$a_8=64\,000$$

**Resposta:** o 8º termo é 64.000 células.

> 🔢 **Padrão:**  
> PG apresenta razões constantes e corresponde a um modelo exponencial discreto.

---

## 4. Soma dos termos de uma PG

### 4.1 Soma finita

Para $$q\neq1$$, a soma dos primeiros $$n$$ termos é:

$$S_n=a_1\frac{q^n-1}{q-1}$$

Se $$q=1$$, todos os termos são iguais e $$S_n=na_1$$.

### 4.2 Soma infinita

Quando $$|q|<1$$, os termos se aproximam de zero e a soma infinita converge para:

$$S_\infty=\frac{a_1}{1-q}$$

**Metades sucessivas**

Calcule:

$$1+\frac12+\frac14+\frac18+\ldots$$

**Resolução:**

- **Passo 1:** Identificar primeiro termo e razão.

$$a_1=1$$

$$q=\frac12$$

- **Passo 2:** Confirmar a condição de convergência: $$|q|<1$$.

- **Passo 3:** Aplicar a fórmula.

$$S_\infty=\frac{1}{1-\frac12}$$

$$S_\infty=2$$

**Resposta:** a soma infinita vale 2.

Juros compostos, decaimentos e prestações da Tabela Price usam estruturas geométricas. A soma infinita é uma ideia informal de limite: os totais parciais se aproximam de um valor fixo.

> ⚠️ **Atenção:**  
> A soma infinita só converge quando $$|q|<1$$; fora dessa condição, a fórmula não se aplica.
