# Operações — 3ª Série · Bloco 1

> **3º Bimestre — Funções e álgebra (aprofundamento)** · Bloco 1 (05/08–25/08)

**Capítulos deste bloco**

1. **Funções afim e quadrática** (4 aulas)
2. **Função modular, composta e inversa** (4 aulas)
3. **Funções exponencial e logarítmica** (4 aulas)

---

# BL1_Capítulo 1 — Funções afim e quadrática

> Como os coeficientes determinam retas e parábolas?

---

## 1. Função afim: definição e gráfico

### 1.1 Coeficientes e interseções

**Função afim** é a função definida por:

$$f(x)=ax+b$$

Os coeficientes controlam elementos distintos:

- $$a$$ é a taxa de variação e determina a inclinação;
- $$b$$ é o valor inicial e determina o ponto $$(0,b)$$;
- se $$a>0$$, a função é crescente; se $$a<0$$, é decrescente;
- para $$a\neq0$$, a raiz é o ponto em que a reta cruza o eixo horizontal.

$$x=-\frac{b}{a}$$

### 1.2 Taxa de variação constante

Entre dois pontos com $$x_1\neq x_2$$, a taxa é:

$$a=\frac{f(x_2)-f(x_1)}{x_2-x_1}$$

Diferenças iguais em $$x$$ produzem sempre a mesma diferença em $$f(x)$$. Essa constância caracteriza o comportamento afim.

**Tarifa de transporte**

Uma corrida custa R$ 6,00 de bandeirada e R$ 3,00 por quilômetro. Determine a função e o custo de 8 km.

**Resolução:**

- **Passo 1:** Identificar valor inicial e taxa.

$$b=6$$

$$a=3$$

- **Passo 2:** Escrever a função.

$$C(x)=3x+6$$

- **Passo 3:** Substituir 8 km.

$$C(8)=3\times8+6$$

$$C(8)=30$$

**Resposta:** a função é $$C(x)=3x+6$$ e a corrida custa R$ 30,00.

> 🔢 **Padrão:**  
> Diferenças constantes entre imagens consecutivas indicam um modelo afim.

---

## 2. Função afim: aplicações

### 2.1 Modelos lineares

Um custo total combina parcela fixa e parcela por unidade:

$$C(x)=C_f+cx$$

Nos juros simples, o montante também varia de forma afim com o tempo:

$$M(t)=C(1+it)$$

Para reconhecer esse modelo no enunciado, procure taxa constante, acréscimo fixo ou pontos alinhados em uma reta.

### 2.2 Ajuste por dois pontos

Dois pontos distintos determinam uma única reta. Primeiro se calcula $$a$$; depois, substitui-se um ponto em $$f(x)=ax+b$$ para obter $$b$$.

**Produção mensal**

Uma fábrica registrou os pontos $$(1,5)$$ e $$(3,11)$$, em centenas de unidades. Determine a função afim.

**Resolução:**

- **Passo 1:** Calcular a taxa de variação.

$$a=\frac{11-5}{3-1}$$

$$a=3$$

- **Passo 2:** Usar o primeiro ponto para encontrar $$b$$.

$$5=3\times1+b$$

$$b=2$$

- **Passo 3:** Escrever a função.

$$f(x)=3x+2$$

- **Passo 4:** Conferir com o segundo ponto.

$$f(3)=3\times3+2$$

$$f(3)=11$$

**Resposta:** a função ajustada é $$f(x)=3x+2$$.

**Felix Klein** apresentou o Programa de Erlangen em 1872. Sua visão unificadora classificava objetos por estruturas e transformações, ideia útil para comparar famílias de funções sem confundi-las.

> ⚠️ **Atenção:**  
> Crescimento constante indica função afim; razão constante entre valores indica outro tipo de modelo.

---

## 3. Função quadrática: estudo completo

### 3.1 Elementos da parábola

**Função quadrática** tem a forma:

$$f(x)=ax^2+bx+c$$

com $$a\neq0$$. Seus elementos principais são:

- concavidade para cima se $$a>0$$ e para baixo se $$a<0$$;
- raízes dadas pela fórmula resolutiva, quando reais;
- vértice no eixo de simetria;
- interseção com o eixo vertical em $$(0,c)$$.

$$\Delta=b^2-4ac$$

$$x_v=-\frac{b}{2a}$$

$$y_v=-\frac{\Delta}{4a}$$

### 3.2 Sinal, imagem e forma canônica

Com duas raízes, o sinal é igual ao de $$a$$ fora delas e oposto entre elas. A forma canônica exibe o vértice:

$$f(x)=a(x-x_v)^2+y_v$$

**Estudo de uma parábola**

Estude $$f(x)=-x^2+6x-5$$.

**Resolução:**

- **Passo 1:** Identificar a concavidade.

$$a=-1<0$$

- **Passo 2:** Calcular o discriminante.

$$\Delta=6^2-4\times(-1)\times(-5)$$

$$\Delta=16$$

- **Passo 3:** Calcular as raízes.

$$x=\frac{-6\pm4}{-2}$$

$$x_1=1$$

$$x_2=5$$

- **Passo 4:** Calcular o vértice.

$$x_v=3$$

$$y_v=4$$

**Resposta:** a parábola abre para baixo, tem raízes 1 e 5, vértice $$(3,4)$$ e imagem $$]-\infty,4]$$.

> 🔢 **Padrão:**  
> A forma canônica mostra diretamente o vértice e preserva a mesma função da forma geral.

---

## 4. Função quadrática: otimização e aplicações

### 4.1 Máximo ou mínimo

O sinal de $$a$$ define a natureza do extremo:

- se $$a>0$$, $$y_v$$ é mínimo;
- se $$a<0$$, $$y_v$$ é máximo.

O valor $$x_v$$ indica onde o extremo ocorre; $$y_v$$ indica quanto ele vale. A interpretação deve respeitar unidades, domínio e limites físicos.

### 4.2 Modelagem pelo vértice

**Receita de uma loja**

A demanda é $$q=100-2p$$, em que $$p$$ é o preço. Determine o preço que maximiza a receita.

**Resolução:**

- **Passo 1:** Escrever a receita como preço vezes quantidade.

$$R(p)=p(100-2p)$$

$$R(p)=-2p^2+100p$$

- **Passo 2:** Calcular a abscissa do vértice.

$$p_v=-\frac{100}{2\times(-2)}$$

$$p_v=25$$

- **Passo 3:** Calcular a receita máxima.

$$R(25)=-2\times25^2+100\times25$$

$$R(25)=1250$$

- **Passo 4:** Conferir a natureza do extremo.

$$a=-2<0$$

**Resposta:** o preço de R$ 25,00 maximiza a receita em R$ 1.250,00.

Áreas com perímetro fixo e trajetórias parabólicas seguem o mesmo roteiro: montar a função, localizar o vértice e validar o resultado no contexto. Medidas negativas ou valores fora do domínio devem ser descartados.

> ⚠️ **Atenção:**  
> Calcular o vértice sem interpretar $$x_v$$ e $$y_v$$ pode produzir uma resposta numericamente certa e contextualmente errada.

---

# BL1_Capítulo 2 — Função modular, composta e inversa

> Como interpretar módulo, composição e função inversa?

---

## 1. Função modular: definição e gráfico

### 1.1 Módulo e definição por partes

**Módulo** é a distância de um número real até zero:

$$|x|=\sqrt{x^2}$$

$$|x|=\begin{cases}x, & x\geq0\\-x, & x<0\end{cases}$$

O domínio de $$f(x)=|x|$$ é ℝ, e sua imagem é $$[0,+\infty[$$. O gráfico tem formato de V, com vértice na origem.

### 1.2 Módulo de outra função

Em $$y=|g(x)|$$, os pontos de $$g$$ que já estão acima do eixo horizontal permanecem. Os pontos abaixo dele são refletidos para cima.

**Imagem de uma parábola modular**

Descreva a transformação de $$g(x)=x^2-4$$ para $$f(x)=|x^2-4|$$.

**Resolução:**

- **Passo 1:** Encontrar onde a parábola corta o eixo horizontal.

$$x^2-4=0$$

$$x=-2$$

$$x=2$$

- **Passo 2:** Identificar o trecho negativo: $$-2<x<2$$.

- **Passo 3:** Refletir esse trecho.

$$f(x)=\begin{cases}x^2-4, & x\leq-2\\4-x^2, & -2<x<2\\x^2-4, & x\geq2\end{cases}$$

**Resposta:** o trecho entre −2 e 2 é refletido para cima; os demais permanecem.

**Karl Weierstrass** consolidou o rigor moderno na análise matemática. O cuidado com definições precisas sustenta o uso de módulo, composição e inversão sem ambiguidades.

> 🔢 **Padrão:**  
> Aplicar módulo à imagem preserva a parte não negativa e reflete a parte negativa.

---

## 2. Equações e inequações modulares

### 2.1 Equações com módulo

Para $$a>0$$, a equação se divide em dois casos:

$$|f(x)|=a$$

$$f(x)=a$$

$$f(x)=-a$$

Se $$a=0$$, resolve-se apenas $$f(x)=0$$. Se $$a<0$$, não existe solução real.

**Duas posições possíveis**

Resolva $$|2x-6|=4$$.

**Resolução:**

- **Passo 1:** Abrir o caso positivo.

$$2x-6=4$$

$$x=5$$

- **Passo 2:** Abrir o caso negativo.

$$2x-6=-4$$

$$x=1$$

**Resposta:** $$x=1$$ ou $$x=5$$.

### 2.2 Inequações e intervalos

Para $$a>0$$, valem as equivalências:

$$|x|<a\iff -a<x<a$$

$$|x|>a\iff x<-a\text{ ou }x>a$$

A primeira solução é uma interseção no intervalo central. A segunda é uma união de dois intervalos externos:

$$|x|>3\iff x\in]-\infty,-3[\cup]3,+\infty[$$

> ⚠️ **Atenção:**  
> As equivalências usuais de inequações modulares exigem $$a>0$$; sem essa condição, os casos mudam.

---

## 3. Função composta

### 3.1 Composição e ordem

**Função composta** aplica primeiro a função interna e depois a externa:

$$(f\circ g)(x)=f(g(x))$$

Em geral, a composição não é comutativa:

$$f\circ g\neq g\circ f$$

### 3.2 Cálculo e domínio

**Duas ordens de composição**

Dadas $$f(x)=2x+1$$ e $$g(x)=x^2$$, determine as duas composições.

**Resolução:**

- **Passo 1:** Aplicar $$g$$ dentro de $$f$$.

$$(f\circ g)(x)=f(x^2)$$

$$(f\circ g)(x)=2x^2+1$$

- **Passo 2:** Aplicar $$f$$ dentro de $$g$$.

$$(g\circ f)(x)=g(2x+1)$$

$$(g\circ f)(x)=(2x+1)^2$$

$$(g\circ f)(x)=4x^2+4x+1$$

**Resposta:** as composições são $$2x^2+1$$ e $$4x^2+4x+1$$, portanto são diferentes.

Para que $$f(g(x))$$ exista, $$x$$ deve pertencer ao domínio de $$g$$ e $$g(x)$$ deve pertencer ao domínio de $$f$$. Se $$f(x)=\sqrt{x}$$ e $$g(x)=x-4$$, então:

$$x-4\geq0$$

$$x\geq4$$

> 🔢 **Padrão:**  
> Na composição, a função mais próxima de $$x$$ é aplicada primeiro.

---

## 4. Função inversa

### 4.1 Existência e obtenção

**Função inversa** desfaz a função original. Ela existe quando a função é bijetora entre o domínio e o contradomínio considerados.

$$(f\circ f^{-1})(x)=x$$

$$(f^{-1}\circ f)(x)=x$$

O procedimento troca $$x$$ e $$y$$ e depois isola $$y$$.

**Inversa de uma função afim**

Determine a inversa de $$f(x)=2x+1$$.

**Resolução:**

- **Passo 1:** Escrever a função com $$y$$.

$$y=2x+1$$

- **Passo 2:** Trocar as variáveis.

$$x=2y+1$$

- **Passo 3:** Isolar $$y$$.

$$2y=x-1$$

$$y=\frac{x-1}{2}$$

**Resposta:** $$f^{-1}(x)=\dfrac{x-1}{2}$$.

### 4.2 Simetria dos gráficos

Se $$(a,b)$$ pertence ao gráfico de $$f$$, então $$(b,a)$$ pertence ao gráfico de $$f^{-1}$$. Os gráficos são reflexos em relação à reta $$y=x$$.

Domínio e imagem também trocam de papel. A função $$f(x)=x^2$$ em ℝ não é injetora, pois 3 e −3 têm a mesma imagem; ela só admite inversa após uma restrição adequada do domínio.

> ⚠️ **Atenção:**  
> O expoente −1 em $$f^{-1}$$ indica inversa, não o recíproco $$1/f(x)$$.

---

# BL1_Capítulo 3 — Funções exponencial e logarítmica

> Como exponencial e logaritmo se relacionam?

---

## 1. Função exponencial

### 1.1 Definição e gráfico

**Função exponencial** tem a variável no expoente:

$$f(x)=a^x$$

com $$a>0$$ e $$a\neq1$$. Suas propriedades centrais são:

- domínio ℝ e imagem $$]0,+\infty[$$;
- ponto comum $$(0,1)$$;
- crescimento para $$a>1$$;
- decrescimento para $$0<a<1$$;
- eixo horizontal como assíntota, sem ser tocado.

### 1.2 Crescimento e decaimento

Modelos exponenciais aparecem quando há um fator multiplicativo constante: crescimento populacional, meia-vida e juros compostos.

**Cultura de bactérias**

Uma cultura segue $$P(t)=1000\times2^t$$. Determine a população após 10 horas.

**Resolução:**

- **Passo 1:** Substituir o tempo.

$$P(10)=1000\times2^{10}$$

- **Passo 2:** Calcular a potência.

$$2^{10}=1024$$

- **Passo 3:** Multiplicar.

$$P(10)=1000\times1024$$

$$P(10)=1\,024\,000$$

**Resposta:** haverá 1.024.000 bactérias.

> 🔢 **Padrão:**  
> Razões constantes entre valores consecutivos indicam crescimento ou decaimento exponencial.

---

## 2. Função logarítmica

### 2.1 Definição e comportamento

**Função logarítmica** é definida por:

$$f(x)=\log_a x$$

com $$a>0$$, $$a\neq1$$ e $$x>0$$. Seu domínio é $$]0,+\infty[$$, sua imagem é ℝ e seu gráfico passa por $$(1,0)$$.

Ela é crescente se $$a>1$$ e decrescente se $$0<a<1$$. O eixo vertical é uma assíntota.

### 2.2 Propriedades operatórias

Para $$x>0$$ e $$y>0$$, as propriedades transformam produtos e potências:

$$\log_a(xy)=\log_a x+\log_a y$$

$$\log_a\left(\frac{x}{y}\right)=\log_a x-\log_a y$$

$$\log_a(x^n)=n\log_a x$$

**Logaritmo de um produto**

Calcule $$\log_2 32$$ usando uma decomposição.

**Resolução:**

- **Passo 1:** Escrever 32 como produto conveniente.

$$32=4\times8$$

- **Passo 2:** Aplicar a propriedade do produto.

$$\log_2 32=\log_2 4+\log_2 8$$

- **Passo 3:** Calcular os expoentes.

$$\log_2 32=2+3$$

$$\log_2 32=5$$

**Resposta:** $$\log_2 32=5$$.

**Henri Poincaré** estudou diferentes áreas da Matemática por suas relações e simetrias. Essa visão integrada ajuda a reconhecer exponencial e logarítmica como funções de comportamentos opostos, mas estruturalmente ligadas.

> ⚠️ **Atenção:**  
> Não existe propriedade que separe $$\log_a(x+y)$$ em uma soma de logaritmos.

---

## 3. Exponencial e logarítmica como inversas

### 3.1 Identidades e simetria

Para bases válidas e $$x>0$$:

$$a^{\log_a x}=x$$

Para todo $$x$$ real:

$$\log_a(a^x)=x$$

Os gráficos são simétricos em relação à reta $$y=x$$. O ponto $$(0,1)$$ da exponencial corresponde ao ponto $$(1,0)$$ da logarítmica.

### 3.2 Resolver o expoente

A equivalência fundamental é:

$$a^x=b\iff x=\log_a b$$

com $$b>0$$.

**Tempo de crescimento**

Uma cultura segue $$P(t)=1000\times2^t$$. Em quanto tempo atingirá 8.000 indivíduos?

**Resolução:**

- **Passo 1:** Igualar o modelo ao valor desejado.

$$1000\times2^t=8000$$

- **Passo 2:** Isolar a potência.

$$2^t=8$$

- **Passo 3:** Aplicar logaritmo de base 2.

$$t=\log_2 8$$

$$t=3$$

**Resposta:** a população atingirá 8.000 indivíduos em 3 horas.

> 🔢 **Padrão:**  
> A exponencial produz o valor; o logaritmo recupera o expoente.

---

## 4. Escolha do modelo

### 4.1 Critérios de decisão

Quatro padrões orientam a escolha:

| Comportamento | Modelo |
|---|---|
| acréscimo constante | afim |
| máximo, mínimo ou trajetória parabólica | quadrático |
| fator multiplicativo constante | exponencial |
| descobrir expoente ou trabalhar com escala de ordens de grandeza | logarítmico |

Escalas de pH, magnitude sísmica e decibéis são logarítmicas: aumentos iguais na escala representam multiplicações na grandeza original.

### 4.2 Problema integrado

**Duplicação de um investimento**

Um capital cresce 10% ao ano, segundo $$M(t)=C(1{,}1)^t$$. Determine o tempo de duplicação.

**Resolução:**

- **Passo 1:** Igualar o montante ao dobro do capital.

$$C(1{,}1)^t=2C$$

- **Passo 2:** Dividir por $$C$$, com $$C>0$$.

$$(1{,}1)^t=2$$

- **Passo 3:** Aplicar logaritmo.

$$t=\log_{1{,}1}2$$

- **Passo 4:** Usar mudança de base e aproximar: $$t\approx7{,}27$$.

$$t=\frac{\log 2}{\log 1{,}1}$$

**Resposta:** o capital dobra em aproximadamente 7,27 anos.

> ⚠️ **Atenção:**  
> A função deve ser escolhida pelo padrão de variação, não apenas pelas palavras do contexto.
