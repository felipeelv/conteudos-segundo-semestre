# Operações — 1ª Série · Bloco 1

> **3º Bimestre — Função quadrática e inequações** · Bloco 1 (05/08–25/08)

**Capítulos deste bloco**

1. **Elementos e gráfico da função quadrática** (6 aulas)
2. **Estudo do sinal, forma canônica e gráficos** (3 aulas)
3. **Otimização e modelagem** (3 aulas)

---

# BL1_Capítulo 1 — Elementos e gráfico da função quadrática

> Como os coeficientes controlam o gráfico de uma função quadrática?

---

## 1. Definição e elementos

### 1.1 Forma geral

**Função quadrática** é a função definida por

$$f(x)=ax^2+bx+c$$

onde $$a$$, $$b$$ e $$c$$ são reais e $$a\neq 0$$. Seu domínio é ℝ.

Os coeficientes cumprem papéis distintos:

- $$a$$ garante o grau 2 e determina concavidade e abertura;
- $$b$$ participa da posição do eixo e do vértice;
- $$c$$ é o valor de $$f(0)$$ e marca a interseção com o eixo vertical.

Uma **equação do 2º grau** pede os valores que tornam uma igualdade verdadeira; a função associa cada entrada $$x$$ a uma imagem $$f(x)$$.

### 1.2 Cálculo do valor numérico

**Valor da função em uma entrada**

Calcule $$f(2)$$ para $$f(x)=x^2-4x+3$$.

**Resolução:**

- **Passo 1:** Substituir $$x$$ por 2.

$$f(2)=2^2-4\times 2+3$$

- **Passo 2:** Efetuar a potência.

$$f(2)=4-4\times 2+3$$

- **Passo 3:** Efetuar a multiplicação.

$$f(2)=4-8+3$$

- **Passo 4:** Somar os termos.

$$f(2)=-1$$

**Resposta:** A imagem de 2 é $$-1$$.

**Augustin-Louis Cauchy** (1789–1857) consolidou a definição rigorosa de função no *Cours d'analyse* (1821), tratando-a como objeto matemático preciso.

> ⚠️ **Atenção:**  
> Se $$a=0$$, a expressão deixa de definir uma função quadrática.

---

## 2. Parábola e concavidade

### 2.1 Forma do gráfico

O gráfico é uma **parábola**, e o sinal de $$a$$ determina sua concavidade:

- $$a>0$$: concavidade para cima;
- $$a<0$$: concavidade para baixo.

O valor absoluto de $$a$$ também influencia a abertura: quanto maior $$|a|$$, mais fechada é a curva.

### 2.2 Interseção com o eixo vertical

No eixo $$y$$, a abscissa vale zero. Portanto,

$$f(0)=c$$

e a parábola passa pelo ponto $$(0,c)$$.

**Leitura dos coeficientes de uma trajetória**

Considere $$h(t)=-5t^2+8t+2$$.

**Resolução:**

- **Passo 1:** Identificar o coeficiente quadrático.

$$a=-5<0$$

- **Passo 2:** Determinar a concavidade.

A parábola tem concavidade para baixo.

- **Passo 3:** Calcular a altura inicial.

$$h(0)=2$$

**Resposta:** A trajetória é parabólica, abre para baixo e começa no ponto $$(0,2)$$; os demais coeficientes participam da posição do vértice e das raízes.

> 🔢 **Padrão:**  
> O ponto $$(0,c)$$ pertence ao gráfico de toda função $$f(x)=ax^2+bx+c$$.

---

## 3. Raízes da função

### 3.1 Zeros e discriminante

**Raízes** ou **zeros** são os valores de $$x$$ para os quais $$f(x)=0$$. Para calculá-los, usa-se

$$\Delta=b^2-4ac$$

$$x=\frac{-b\pm\sqrt{\Delta}}{2a}$$

onde $$a$$, $$b$$ e $$c$$ são os coeficientes e $$a\neq 0$$.

O discriminante determina o número de raízes reais:

| Condição | Raízes reais | Encontro com o eixo $$x$$ |
|---|---:|---|
| $$\Delta>0$$ | duas distintas | corta em dois pontos |
| $$\Delta=0$$ | uma dupla | toca em um ponto |
| $$\Delta<0$$ | nenhuma | não encontra |

### 3.2 Cálculo e leitura geométrica

**Zeros de uma parábola**

Determine as raízes de $$f(x)=x^2-4x+3$$.

**Resolução:**

- **Passo 1:** Calcular o discriminante.

$$\Delta=(-4)^2-4\times 1\times 3$$

$$\Delta=4$$

- **Passo 2:** Aplicar a fórmula.

$$x=\frac{4\pm\sqrt{4}}{2}$$

$$x=\frac{4\pm 2}{2}$$

- **Passo 3:** Separar os resultados.

$$x_1=1$$

$$x_2=3$$

**Resposta:** As raízes são 1 e 3, abscissas onde a parábola corta o eixo $$x$$.

> ⚠️ **Atenção:**  
> Se $$\Delta<0$$, a função não tem raízes reais.

---

## 4. Vértice da parábola

### 4.1 Coordenadas

O **vértice** é o ponto de retorno da parábola. Suas coordenadas são

$$x_v=-\frac{b}{2a}$$

$$y_v=-\frac{\Delta}{4a}$$

onde $$a$$ e $$b$$ são coeficientes da função e $$\Delta=b^2-4ac$$. Também é possível obter $$y_v$$ calculando $$f(x_v)$$.

### 4.2 Relação com as raízes

Quando as raízes reais $$x_1$$ e $$x_2$$ existem, a simetria fornece

$$x_v=\frac{x_1+x_2}{2}$$

**Vértice calculado por duas coordenadas**

Determine o vértice de $$f(x)=x^2-4x+3$$.

**Resolução:**

- **Passo 1:** Calcular a abscissa.

$$x_v=-\frac{-4}{2\times 1}$$

$$x_v=2$$

- **Passo 2:** Usar $$\Delta=4$$ para calcular a ordenada.

$$y_v=-\frac{4}{4\times 1}$$

$$y_v=-1$$

- **Passo 3:** Conferir pela média das raízes 1 e 3.

$$x_v=\frac{1+3}{2}$$

$$x_v=2$$

**Resposta:** O vértice é $$(2,-1)$$.

> ⚠️ **Atenção:**  
> O sinal negativo faz parte da fórmula de $$x_v$$ e deve ser aplicado ao valor de $$b$$.

---

## 5. Eixo de simetria

### 5.1 Reta de simetria

O **eixo de simetria** é a reta vertical que passa pelo vértice:

$$x=x_v$$

Para qualquer distância real $$d$$, os pontos simétricos satisfazem

$$f(x_v-d)=f(x_v+d)$$

Calcule um lado da curva e reflita os pontos.

### 5.2 Esboço por reflexão

Um procedimento econômico usa quatro dados:

- calcular o vértice;
- traçar o eixo de simetria;
- obter pontos de um lado;
- refletir cada ponto à mesma distância no outro lado.

**Pares simétricos**

Em $$f(x)=x^2-4x+3$$, o eixo é $$x=2$$. Verifique os pontos com abscissas 0 e 4.

**Resolução:**

- **Passo 1:** Calcular a primeira imagem.

$$f(0)=3$$

- **Passo 2:** Calcular a segunda imagem.

$$f(4)=4^2-4\times 4+3$$

$$f(4)=16-16+3$$

$$f(4)=3$$

- **Passo 3:** Comparar as distâncias ao eixo.

$$2-0=2$$

$$4-2=2$$

**Resposta:** Os pontos $$(0,3)$$ e $$(4,3)$$ são simétricos em relação a $$x=2$$.

> 🔢 **Padrão:**  
> A média das abscissas de dois pontos simétricos é $$x_v$$.

---

## 6. Máximo, mínimo e imagem

### 6.1 Valor extremo

A concavidade determina o tipo de extremo:

| Condição | Extremo | Imagem |
|---|---|---|
| $$a>0$$ | mínimo $$y_v$$ | $$[y_v,+\infty[$$ |
| $$a<0$$ | máximo $$y_v$$ | $$]-\infty,y_v]$$ |

A coordenada $$x_v$$ indica onde o extremo ocorre; $$y_v$$ indica seu valor.

### 6.2 Altura máxima

**Lançamento de uma bola**

Para $$h(t)=-5t^2+8t+2$$, determine o instante e a altura máxima.

**Resolução:**

- **Passo 1:** Calcular o instante do vértice.

$$t_v=-\frac{8}{2\times(-5)}$$

$$t_v=0{,}8$$

- **Passo 2:** Calcular a altura nesse instante.

$$h(0{,}8)=-5\times(0{,}8)^2+8\times0{,}8+2$$

$$h(0{,}8)=-5\times0{,}64+6{,}4+2$$

$$h(0{,}8)=-3{,}2+6{,}4+2$$

$$h(0{,}8)=5{,}2$$

**Resposta:** A bola atinge a altura máxima de $$5{,}2\,\mathrm{m}$$ em $$0{,}8\,\mathrm{s}$$.

> ⚠️ **Atenção:**  
> Não confunda a entrada do extremo, $$x_v$$, com o valor extremo, $$y_v$$.

---

# BL1_Capítulo 2 — Estudo do sinal, forma canônica e gráficos

> Como identificar onde uma função quadrática é positiva ou negativa?

---

## 1. Estudo do sinal

### 1.1 Regra pelos intervalos

**Estudar o sinal** é determinar onde $$f(x)$$ é positiva, negativa ou nula. Com duas raízes reais $$x_1<x_2$$:

- fora das raízes, $$f(x)$$ tem o sinal de $$a$$;
- entre as raízes, tem sinal contrário ao de $$a$$;
- nas raízes, vale zero.

Os seis casos completos são:

| Discriminante | $$a>0$$ | $$a<0$$ |
|---|---|---|
| $$\Delta>0$$ | positiva fora; negativa entre | negativa fora; positiva entre |
| $$\Delta=0$$ | positiva, exceto zero na raiz | negativa, exceto zero na raiz |
| $$\Delta<0$$ | positiva em ℝ | negativa em ℝ |

### 1.2 Aplicação da regra

**Sinal de uma função de duas raízes**

Estude $$f(x)=x^2-4x+3$$.

**Resolução:**

- **Passo 1:** Identificar as raízes e o coeficiente quadrático.

$$x_1=1$$

$$x_2=3$$

$$a=1>0$$

- **Passo 2:** Aplicar a regra fora das raízes: $$f(x)>0\ \text{em}\ ]-\infty,1[\cup]3,+\infty[$$.

- **Passo 3:** Aplicar a regra entre as raízes: $$f(x)<0\ \text{em}\ ]1,3[$$.

**Resposta:** A função é positiva fora das raízes, negativa entre elas e nula em 1 e 3.

**Bernhard Riemann** (1826–1866) ampliou o estudo das funções no século XIX. Seu olhar estrutural ajuda a reconhecer que uma mesma regra organiza toda a família das parábolas.

> 🔢 **Padrão:**  
> Sem raízes reais, a função quadrática conserva o sinal de $$a$$ em todo o domínio.

---

## 2. Forma canônica

### 2.1 Completamento de quadrado

A **forma canônica** é

$$f(x)=a(x-x_v)^2+y_v$$

onde $$(x_v,y_v)$$ é o vértice e $$a\neq0$$. Ela é obtida da forma geral por completamento de quadrado.

**Dedução da forma canônica**

Parta de $$f(x)=ax^2+bx+c$$.

**Resolução:**

- **Passo 1:** Colocar $$a$$ em evidência nos termos com $$x$$.

$$f(x)=a\left(x^2+\frac{b}{a}x\right)+c$$

- **Passo 2:** Somar e subtrair o termo que completa o quadrado.

$$f(x)=a\left(x^2+\frac{b}{a}x+\frac{b^2}{4a^2}-\frac{b^2}{4a^2}\right)+c$$

- **Passo 3:** Fatorar o trinômio quadrado perfeito.

$$f(x)=a\left(x+\frac{b}{2a}\right)^2-\frac{b^2}{4a}+c$$

- **Passo 4:** Reunir os termos independentes.

$$f(x)=a\left(x+\frac{b}{2a}\right)^2-\frac{b^2-4ac}{4a}$$

**Resposta:** Como $$x_v=-\frac{b}{2a}$$ e $$y_v=-\frac{\Delta}{4a}$$, resulta $$f(x)=a(x-x_v)^2+y_v$$.

### 2.2 Equivalência das formas

Para $$f(x)=x^2-4x+3$$, a escrita canônica é

$$f(x)=(x-2)^2-1$$

Expandir essa expressão recupera a forma geral; portanto, as duas representam a mesma função.

> ⚠️ **Atenção:**  
> Na expressão $$(x+3)^2$$, a abscissa do vértice é $$-3$$.

---

## 3. Construção de gráficos

### 3.1 Roteiro completo

O gráfico pode ser construído nesta ordem:

- verificar o sinal de $$a$$;
- calcular raízes, quando reais;
- determinar o vértice;
- traçar o eixo $$x=x_v$$;
- marcar o ponto $$(0,c)$$.

Na forma canônica, vértice e concavidade são lidos diretamente.

**Esboço pelos elementos**

Analise $$f(x)=x^2-4x+3$$.

**Resolução:**

- **Passo 1:** Determinar a concavidade.

$$a=1>0$$

- **Passo 2:** Registrar raízes e vértice.

$$x_1=1$$

$$x_2=3$$

$$V=(2,-1)$$

- **Passo 3:** Registrar eixo e interseção vertical: $$(0,3)$$.

$$x=2$$

**Resposta:** A parábola abre para cima, corta o eixo $$x$$ em 1 e 3, tem vértice $$(2,-1)$$ e passa por $$(0,3)$$.

### 3.2 Esboço pela forma canônica

**Parábola com vértice explícito**

Analise $$g(x)=2(x-3)^2+1$$.

**Resolução:**

- **Passo 1:** Ler o vértice.

$$V=(3,1)$$

- **Passo 2:** Identificar concavidade e eixo.

$$a=2>0$$

$$x=3$$

- **Passo 3:** Ler a imagem a partir do mínimo.

$$\mathrm{Im}(g)=[1,+\infty[$$

**Resposta:** A parábola abre para cima, tem vértice $$(3,1)$$, eixo $$x=3$$ e não possui raízes reais.

### 3.3 Imagem e monotonicidade

Para $$a>0$$, a função decresce até $$x_v$$, cresce depois e tem imagem $$[y_v,+\infty[$$. Para $$a<0$$, cresce até $$x_v$$, decresce depois e tem imagem $$]-\infty,y_v]$$.

> 🔢 **Padrão:**  
> O vértice separa os dois intervalos de monotonicidade da função quadrática.

---

# BL1_Capítulo 3 — Otimização e modelagem

> Como usar o vértice para encontrar o maior ou o menor valor?

---

## 1. Problemas de otimização

### 1.1 Extremo pelo vértice

**Otimizar** é encontrar o máximo ou o mínimo de uma grandeza. Quando o modelo é quadrático, a concavidade classifica o extremo e o vértice fornece:

- $$x_v$$ — valor da variável que produz o extremo;
- $$y_v$$ — valor máximo ou mínimo obtido.

### 1.2 Área máxima

**Cercado de área máxima**

Com $$40\,\mathrm{m}$$ de cerca, determine as dimensões do retângulo de maior área.

**Resolução:**

- **Passo 1:** Escrever a restrição do perímetro.

$$2x+2y=40$$

$$y=20-x$$

- **Passo 2:** Modelar a área.

$$A(x)=x(20-x)$$

$$A(x)=-x^2+20x$$

- **Passo 3:** Calcular a abscissa do vértice.

$$x_v=-\frac{20}{2\times(-1)}$$

$$x_v=10$$

- **Passo 4:** Obter o outro lado e a área.

$$y=20-10$$

$$y=10$$

$$A(10)=10\times10$$

$$A(10)=100$$

**Resposta:** O quadrado de lado $$10\,\mathrm{m}$$ tem área máxima de $$100\,\mathrm{m^2}$$.

### 1.3 Receita máxima

**Preço e demanda**

Uma loja vende $$q=60-p$$ unidades ao preço de $$p$$ reais.

**Resolução:**

- **Passo 1:** Registrar o domínio econômico: $$0\leq p\leq60$$.

- **Passo 2:** Modelar a receita.

$$R(p)=p(60-p)$$

$$R(p)=-p^2+60p$$

- **Passo 3:** Calcular o preço do vértice.

$$p_v=-\frac{60}{2\times(-1)}$$

$$p_v=30$$

- **Passo 4:** Calcular a receita máxima.

$$R(30)=30\times30$$

$$R(30)=900$$

**Resposta:** O preço de R$ 30,00 produz receita máxima de R$ 900,00.

> 🔢 **Padrão:**  
> Entre retângulos de mesmo perímetro, o quadrado possui a maior área.

---

## 2. Modelagem com função quadrática

### 2.1 Da condição à função

Um modelo quadrático é construído por quatro decisões:

- escolher a variável independente;
- identificar a grandeza a otimizar;
- traduzir a restrição entre as grandezas;
- eliminar uma variável para obter uma função de uma entrada.

O intervalo admissível da variável deve ser registrado antes da interpretação.

### 2.2 Receita máxima

**Preço que maximiza a receita**

Uma loja vende $$q=100-2p$$ unidades quando cobra $$p$$ reais. Determine o preço e a receita máxima.

**Resolução:**

- **Passo 1:** Registrar o domínio econômico: $$0\leq p\leq50$$.

- **Passo 2:** Multiplicar preço pela quantidade.

$$R(p)=p(100-2p)$$

$$R(p)=-2p^2+100p$$

- **Passo 3:** Calcular o preço do vértice.

$$p_v=-\frac{100}{2\times(-2)}$$

$$p_v=25$$

- **Passo 4:** Calcular a quantidade e a receita.

$$q=100-2\times25$$

$$q=50$$

$$R(25)=25\times50$$

$$R(25)=1\,250$$

**Resposta:** O preço de R$ 25,00 gera receita máxima de R$ 1.250,00.

> ⚠️ **Atenção:**  
> Depois do cálculo, interprete $$x_v$$ e $$y_v$$ com as unidades exigidas pelo problema.

---

## 3. Função quadrática em contextos reais

### 3.1 Trajetória e significado físico

**Galileo Galilei** (1564–1642) demonstrou em *Duas Novas Ciências* (1638) que a trajetória ideal de um projétil é parabólica.

Em um modelo de altura

$$h(t)=at^2+bt+c$$

o coeficiente $$a<0$$ representa a concavidade para baixo, o vértice informa a altura máxima e as raízes indicam os instantes em que a altura é zero.

### 3.2 Altura e alcance temporal

**Altura de uma bola**

Considere $$h(t)=-5t^2+20t$$, com altura em metros e tempo em segundos.

**Resolução:**

- **Passo 1:** Calcular o instante de altura máxima.

$$t_v=-\frac{20}{2\times(-5)}$$

$$t_v=2$$

- **Passo 2:** Calcular a altura máxima.

$$h(2)=-5\times2^2+20\times2$$

$$h(2)=-20+40$$

$$h(2)=20$$

- **Passo 3:** Encontrar quando a bola está no solo.

$$-5t^2+20t=0$$

$$-5t(t-4)=0$$

$$t=0$$

$$t-4=0$$

$$t=4$$

**Resposta:** A bola atinge $$20\,\mathrm{m}$$ aos $$2\,\mathrm{s}$$ e retorna ao solo aos $$4\,\mathrm{s}$$.

Resultados negativos para tempo, comprimento ou preço são descartados quando o contexto não os admite; valores incompatíveis também exigem revisar o modelo.

> ⚠️ **Atenção:**  
> Uma solução algébrica só é válida no problema se respeitar as restrições físicas do contexto.
