# Operações — 1ª Série · Bloco 2

> **3º Bimestre — Função quadrática e inequações** · Bloco 2 (27/08–18/09)

**Capítulos deste bloco**

4. **Inequações do 1º grau e com módulo** (4 aulas)
5. **Inequações do 2º grau** (3 aulas)
6. **Sistemas de inequações, produto e quociente** (3 aulas)
7. **Modelagem com inequações** (2 aulas)

---

# BL2_Capítulo 1 — Inequações do 1º grau e com módulo

> Como representar e resolver faixas de valores com inequações?

---

## 1. Inequações do 1º grau

### 1.1 Símbolos e solução

Uma **inequação** compara duas expressões por um destes símbolos:

| Símbolo | Leitura | Tipo |
|---|---|---|
| $$>$$ | maior que | estrita |
| $$<$$ | menor que | estrita |
| $$\geq$$ | maior ou igual a | não estrita |
| $$\leq$$ | menor ou igual a | não estrita |

Resolver significa isolar a incógnita e obter todos os valores que tornam a comparação verdadeira. Por isso, a solução geralmente é um intervalo infinito.

### 1.2 Resolução algébrica

**Faixa determinada por uma inequação**

Resolva $$3x-5\leq7$$.

**Resolução:**

- **Passo 1:** Somar 5 aos dois membros: $$3x\leq12$$.

- **Passo 2:** Dividir os dois membros por 3: $$x\leq4$$.

**Resposta:** Todos os reais menores ou iguais a 4 satisfazem a inequação.

**Joseph Fourier** (1768–1830), no *Théorie analytique de la chaleur* (1822), sistematizou o uso de desigualdades em problemas matemáticos e físicos.

> ⚠️ **Atenção:**  
> Uma inequação descreve um conjunto de soluções, enquanto uma equação pode ter uma solução isolada.

---

## 2. Conjunto solução e reta

### 2.1 Extremos abertos e fechados

O símbolo da desigualdade decide se o extremo pertence ao conjunto:

| Desigualdade | Intervalo | Ponto na reta |
|---|---|---|
| $$x<a$$ | $$]-\infty,a[$$ | aberto em $$a$$ |
| $$x\leq a$$ | $$]-\infty,a]$$ | fechado em $$a$$ |
| $$a<x<b$$ | $$]a,b[$$ | abertos |
| $$a\leq x<b$$ | $$[a,b[$$ | fechado em $$a$$, aberto em $$b$$ |

### 2.2 Tradução para intervalo e reta

**Velocidade permitida**

Uma via admite velocidades de pelo menos $$60\,\mathrm{km/h}$$ e menores que $$100\,\mathrm{km/h}$$.

**Resolução:**

- **Passo 1:** Traduzir as duas condições: $$v\geq60$$; $$v<100$$.

- **Passo 2:** Reunir as condições: $$60\leq v<100$$.

- **Passo 3:** Escrever o intervalo: $$v\in[60,100[$$.

```text
60 ●════════════○ 100
```

**Resposta:** As velocidades permitidas pertencem a $$[60,100[$$.

> 🔢 **Padrão:**  
> Desigualdade estrita gera extremo aberto; desigualdade não estrita gera extremo fechado.

---

## 3. Propriedades das desigualdades

### 3.1 Operações nos dois membros

Somar ou subtrair o mesmo número preserva o sentido. Multiplicar ou dividir por número positivo também preserva; por número negativo, **inverte** o símbolo.

A inversão mantém a comparação verdadeira. Por exemplo,

$$-2<1$$

Ao multiplicar por $$-3$$:

$$6>-3$$

### 3.2 Aplicação da regra de inversão

**Coeficiente negativo**

Resolva $$5-2x>3$$.

**Resolução:**

- **Passo 1:** Subtrair 5 dos dois membros: $$-2x>-2$$.

- **Passo 2:** Dividir por $$-2$$ e inverter o símbolo: $$x<1$$.

- **Passo 3:** Registrar o conjunto solução.

$$S=]-\infty,1[$$

**Resposta:** A inequação é verdadeira para $$x<1$$.

> ⚠️ **Atenção:**  
> Dividir ou multiplicar uma desigualdade por número negativo exige inverter seu símbolo.

---

## 4. Inequações com módulo

### 4.1 Faixa central e faixas externas

O **módulo** $$|x|$$ é a distância de $$x$$ até zero e, portanto, nunca é negativo. Para $$a>0$$:

$$|x|<a\Longleftrightarrow -a<x<a$$

$$|x|>a\Longleftrightarrow x<-a\ \text{ou}\ x>a$$

A primeira relação seleciona a faixa central; a segunda, as duas faixas externas.

### 4.2 Interpretação como distância

**Distância menor que quatro**

Resolva $$|x|<4$$.

**Resolução:**

- **Passo 1:** Interpretar o módulo como distância à origem.

A distância de $$x$$ até zero deve ser menor que 4.

- **Passo 2:** Escrever a desigualdade dupla: $$-4<x<4$$.

- **Passo 3:** Registrar o intervalo.

$$S=]-4,4[$$

**Resposta:** A solução é o intervalo aberto entre $$-4$$ e 4.

> 🔢 **Padrão:**  
> Com $$a>0$$, $$|x|<a$$ indica região interna e $$|x|>a$$ indica regiões externas.

---

# BL2_Capítulo 2 — Inequações do 2º grau

> Como encontrar a faixa em que uma expressão quadrática é positiva?

---

## 1. Conceito de inequação quadrática

### 1.1 Significado gráfico

Uma **inequação do 2º grau** apresenta uma das formas

$$ax^2+bx+c>0$$

$$ax^2+bx+c<0$$

ou as versões não estritas, com $$a\neq0$$. Resolver é localizar no domínio os pontos do gráfico que estão acima, abaixo ou sobre o eixo $$x$$.

As raízes são as fronteiras possíveis dos intervalos, pois nelas a função vale zero.

### 1.2 Leitura pelos zeros

**Leitura de uma condição quadrática**

Considere $$f(x)=x^2-5x+6$$ e a condição $$f(x)>0$$.

**Resolução:**

- **Passo 1:** Fatorar para obter as raízes.

$$f(x)=(x-2)(x-3)$$

$$x_1=2$$

$$x_2=3$$

- **Passo 2:** Identificar a concavidade.

$$a=1>0$$

- **Passo 3:** Ler onde o gráfico está acima do eixo: $$x<2\ \text{ou}\ x>3$$.

**Resposta:** A condição vale em $$]-\infty,2[\cup]3,+\infty[$$.

> 🔢 **Padrão:**  
> As raízes dividem a reta nos intervalos em que o sinal da função quadrática é constante.

---

## 2. Resolução de inequações quadráticas

### 2.1 Roteiro por discriminante

O método tem quatro etapas:

- calcular as raízes reais;
- identificar o sinal de $$a$$;
- distribuir os sinais nos intervalos;
- selecionar as regiões pedidas e incluir extremos apenas com $$\geq$$ ou $$\leq$$.

Se $$\Delta=0$$, há uma única fronteira; se $$\Delta<0$$, o sinal é o de $$a$$ em todo ℝ.

### 2.2 Aplicação do roteiro

**Faixa entre duas raízes**

Resolva $$-x^2+5x-6\geq0$$.

**Resolução:**

- **Passo 1:** Encontrar as raízes da igualdade associada.

$$-x^2+5x-6=0$$

$$x^2-5x+6=0$$

$$(x-2)(x-3)=0$$

$$x_1=2$$

$$x_2=3$$

- **Passo 2:** Identificar o sinal entre as raízes.

$$a=-1<0$$

A função é positiva entre 2 e 3.

- **Passo 3:** Incluir as raízes por causa de $$\geq$$.

$$S=[2,3]$$

**Resposta:** A solução é $$[2,3]$$.

> ⚠️ **Atenção:**  
> O símbolo não estrito inclui raízes, mas o símbolo estrito as exclui.

---

## 3. Quadro de sinais aplicado

### 3.1 Lucro positivo

**David Hilbert** (1862–1943) defendeu o tratamento formal das relações matemáticas por regras explícitas. Em inequações, esse rigor aparece na separação de casos e na escrita precisa do conjunto solução.

### 3.2 Interpretação da faixa de lucro

**Faixa de preços lucrativa**

Resolva $$L(x)=-2x^2+40x-150>0$$.

**Resolução:**

- **Passo 1:** Resolver a igualdade associada.

$$-2x^2+40x-150=0$$

$$x^2-20x+75=0$$

$$\Delta=(-20)^2-4\times1\times75$$

$$\Delta=100$$

$$x=\frac{20\pm10}{2}$$

$$x_1=5$$

$$x_2=15$$

- **Passo 2:** Montar o quadro pelo sinal de $$a$$.

| Intervalo | $$]-\infty,5[$$ | $$5$$ | $$]5,15[$$ | $$15$$ | $$]15,+\infty[$$ |
|---|---:|---:|---:|---:|---:|
| Sinal de $$L(x)$$ | − | 0 | + | 0 | − |

- **Passo 3:** Selecionar o sinal positivo.

$$S=]5,15[$$

**Resposta:** O lucro é positivo para preços entre R$ 5,00 e R$ 15,00, sem incluir os extremos.

> 🔢 **Padrão:**  
> Em um quadro de sinais, cada coluna representa um intervalo sem mudança de sinal.

---

# BL2_Capítulo 3 — Sistemas de inequações, produto e quociente

> Como combinar desigualdades e analisar produtos e quocientes?

---

## 1. Sistemas de inequações

### 1.1 Interseção das soluções

Um **sistema de inequações** é resolvido em duas etapas:

- resolver cada inequação separadamente;
- calcular a interseção dos conjuntos obtidos.

Sobrepor os intervalos na reta mostra a região comum. Ela pode ser limitada, ilimitada ou vazia.

### 1.2 Sistema misto

**Sistema misto**

Resolva

$$\begin{cases}x>-1\\x^2-4\leq0\end{cases}$$

**Resolução:**

- **Passo 1:** Resolver a condição linear.

$$S_1=]-1,+\infty[$$

- **Passo 2:** Fatorar a condição quadrática: $$x^2-4\leq0$$; $$(x-2)(x+2)\leq0$$.

$$S_2=[-2,2]$$

- **Passo 3:** Interseccionar os intervalos.

$$S=S_1\cap S_2$$

$$S=]-1,2]$$

**Resposta:** O sistema é satisfeito no intervalo $$]-1,2]$$.

> ⚠️ **Atenção:**  
> Em um sistema, unir respostas aceita valores que podem descumprir uma das condições.

---

## 2. Inequações produto

### 2.1 Quadro do produto

Para fatores reais $$f(x)$$ e $$g(x)$$:

- o produto é positivo quando os sinais são iguais;
- o produto é negativo quando os sinais são opostos;
- o produto é zero quando ao menos um fator é zero.

**Thomas Harriot** (1560–1621) introduziu os símbolos $$>$$ e $$<$$ em *Artis Analyticae Praxis* (1631), tornando a comparação algébrica mais direta.

### 2.2 Montagem do quadro

**Produto não negativo**

Resolva $$(x-1)(x+3)\geq0$$.

**Resolução:**

- **Passo 1:** Identificar os zeros dos fatores.

$$x=-3$$

$$x=1$$

- **Passo 2:** Montar o quadro de sinais.

| Intervalo | $$]-\infty,-3[$$ | $$]-3,1[$$ | $$]1,+\infty[$$ |
|---|---:|---:|---:|
| $$x+3$$ | − | + | + |
| $$x-1$$ | − | − | + |
| Produto | + | − | + |

- **Passo 3:** Selecionar o sinal positivo e os zeros.

$$S=]-\infty,-3]\cup[1,+\infty[$$

**Resposta:** A solução é $$]-\infty,-3]\cup[1,+\infty[$$.

> 🔢 **Padrão:**  
> Produto de fatores com sinais iguais é positivo; com sinais opostos, é negativo.

---

## 3. Inequações quociente

### 3.1 Zeros e restrições

Em uma inequação quociente:

- o zero do numerador pode entrar com símbolo não estrito;
- o zero do denominador nunca pertence ao domínio;
- os pontos críticos dividem a reta para o quadro de sinais.

### 3.2 Restrição do denominador

**Quociente não positivo**

Resolva

$$\frac{x-2}{x+1}\leq0$$

**Resolução:**

- **Passo 1:** Identificar os pontos críticos.

$$x=-1$$

$$x=2$$

- **Passo 2:** Registrar a restrição: $$x\neq-1$$.

- **Passo 3:** Determinar os sinais.

| Intervalo | $$]-\infty,-1[$$ | $$]-1,2[$$ | $$]2,+\infty[$$ |
|---|---:|---:|---:|
| Quociente | + | − | + |

- **Passo 4:** Selecionar o negativo e incluir o zero do numerador.

$$S=]-1,2]$$

**Resposta:** A solução é $$]-1,2]$$; o valor $$-1$$ permanece excluído.

> ⚠️ **Atenção:**  
> O zero do denominador é excluído mesmo quando a inequação usa $$\leq$$ ou $$\geq$$.

---

# BL2_Capítulo 4 — Modelagem com inequações

> Como traduzir limites reais em inequações e encontrar soluções viáveis?

---

## 1. Modelagem com inequações do 1º grau

### 1.1 Vocabulário e faixa viável

Algumas expressões indicam diretamente o símbolo matemático:

| Expressão | Símbolo |
|---|---|
| no máximo | $$\leq$$ |
| pelo menos | $$\geq$$ |
| menos que | $$<$$ |
| mais que | $$>$$ |

Cruze o intervalo obtido com as restrições do contexto.

### 1.2 Orçamento e restrições reais

**Serviço dentro do orçamento**

Um serviço cobra taxa fixa de R$ 80,00 e R$ 12,00 por hora. Com orçamento máximo de R$ 200,00, determine o tempo viável.

**Resolução:**

- **Passo 1:** Modelar o custo: $$80+12h\leq200$$.

- **Passo 2:** Isolar a parcela variável: $$12h\leq120$$.

- **Passo 3:** Dividir por 12: $$h\leq10$$.

- **Passo 4:** Incluir a condição física: $$h\geq0$$.

**Resposta:** O tempo viável pertence ao intervalo $$[0,10]$$ horas.

**George Dantzig** (1914–2005) criou o método simplex em 1947 e fundou a programação linear, área dedicada a decisões sob restrições. Aqui interessa apenas a ideia de região viável.

> ⚠️ **Atenção:**  
> A solução algébrica deve ser limitada pelas condições reais declaradas no problema.

---

## 2. Modelagem com inequações do 2º grau

### 2.1 Intervalo econômico

O procedimento aplicado conserva quatro etapas:

- definir a variável e sua unidade;
- escrever a função de lucro;
- resolver a condição de lucro ou prejuízo;
- interpretar raízes e intervalos no contexto.

### 2.2 Faixa de viabilidade econômica

**Faixa de preços com lucro**

Uma empresa modela o lucro, em reais, por $$L(x)=-2x^2+40x-150$$, onde $$x$$ é o preço do produto.

**Resolução:**

- **Passo 1:** Exigir lucro positivo: $$-2x^2+40x-150>0$$.

- **Passo 2:** Calcular os preços de equilíbrio.

$$-2x^2+40x-150=0$$

$$x^2-20x+75=0$$

$$(x-5)(x-15)=0$$

$$x_1=5$$

$$x_2=15$$

- **Passo 3:** Usar a concavidade para selecionar a faixa positiva: $$5<x<15$$.

$$a=-2<0$$

**Resposta:** Há lucro para preços entre R$ 5,00 e R$ 15,00; nos extremos, o lucro é zero.

> 🔢 **Padrão:**  
> As raízes de uma função de lucro são pontos de equilíbrio que delimitam faixas de lucro e prejuízo.
