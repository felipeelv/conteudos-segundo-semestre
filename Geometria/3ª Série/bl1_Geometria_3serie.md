# Geometria — 3ª Série · Bloco 1

> **3º Bimestre — Cônicas: hipérbole e parábola** · Bloco 1 (05/08–25/08)

**Capítulos deste bloco**

1. **Hipérbole** (4 aulas)
2. **Parábola: definição e equações reduzidas** (2 aulas)

---

# BL1_Capítulo 1 — Hipérbole

> Antes do GPS, navios cruzaram o Atlântico por 70 anos usando o sistema LORAN — puramente hipérboles. Como uma curva de “duas folhas separadas” substituía 24 satélites?

---

## 1. Definição e elementos

Duas torres transmissoras podem definir uma curva pelos pontos cuja diferença de distâncias até elas permanece constante.

### 1.1 Lugar geométrico

A **hipérbole** é o lugar geométrico dos pontos $$P$$ para os quais a diferença em módulo das distâncias a dois focos é constante:

$$|PF_1-PF_2|=2a$$

Os focos são $$F_1$$ e $$F_2$$, separados por $$2c$$, com $$2a<2c$$. Diferentemente da elipse, que usa soma, a hipérbole tem duas folhas abertas e usa diferença.

<!-- tikz:inicio fig-01-definicao-por-diferenca-de-distancias -->
![Hipérbole de duas folhas com focos F1 e F2 e pontos P e Q cuja diferença das distâncias aos focos é constante](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/hiperbole/fig-01-definicao-por-diferenca-de-distancias.png)
<!-- tikz:fim fig-01-definicao-por-diferenca-de-distancias -->

### 1.2 Eixos e relação fundamental

Seus elementos são:

- centro — ponto médio dos focos;
- eixo real ou transverso — mede $$2a$$ e contém os dois vértices;
- eixo imaginário ou conjugado — mede $$2b$$;
- distância focal — mede $$2c$$.

<!-- tikz:inicio fig-02-elementos-da-hiperbole -->
![Hipérbole com centro O, vértices, focos, eixos real e imaginário e parâmetros a, b e c identificados](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/hiperbole/fig-02-elementos-da-hiperbole.png)
<!-- tikz:fim fig-02-elementos-da-hiperbole -->

A relação fundamental é:

$$c^{2}=a^{2}+b^{2}$$

**Elementos de uma hipérbole**

Uma hipérbole tem $$a=3$$ e $$c=5$$. Determine $$b$$ e as medidas dos eixos.

**Resolução:**

- **Passo 1:** Substituir na relação fundamental.

$$5^{2}=3^{2}+b^{2}$$

- **Passo 2:** Isolar $$b^{2}$$.

$$b^{2}=16$$

$$b=4$$

- **Passo 3:** Dobrar os parâmetros.

$$2a=6$$

$$2b=8$$

$$2c=10$$

**Resposta:** $$b=4$$; os eixos real e imaginário medem 6 e 8 unidades, e a distância focal mede 10 unidades.

**Ibrahim ibn Sinan (909–946)** desenvolveu construções de tangentes a cônicas em tratados escritos por volta de 940, combinando rigor geométrico e clareza demonstrativa.

> ⚠️ **Atenção:**
>
> Na hipérbole, $$c^{2}=a^{2}+b^{2}$$; na elipse, a posição desses parâmetros na relação é diferente.

---

## 2. Equações reduzidas e assíntotas

O termo positivo da equação indica a direção em que as duas folhas da hipérbole se abrem.

### 2.1 Orientação do eixo real

Com centro na origem, as formas reduzidas são:

| Eixo real | Equação | Assíntotas |
|---|---|---|
| horizontal | $$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$$ | $$y=\pm\frac{b}{a}x$$ |
| vertical | $$\frac{y^{2}}{a^{2}}-\frac{x^{2}}{b^{2}}=1$$ | $$y=\pm\frac{a}{b}x$$ |

<!-- tikz:inicio fig-03-hiperbole-horizontal-e-assintotas -->
![Hipérbole de eixo real horizontal com retângulo fundamental e assíntotas passando pelo centro](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/hiperbole/fig-03-hiperbole-horizontal-e-assintotas.png)
<!-- tikz:fim fig-03-hiperbole-horizontal-e-assintotas -->

<!-- tikz:inicio fig-04-hiperbole-vertical-e-assintotas -->
![Hipérbole de eixo real vertical com retângulo fundamental e assíntotas passando pelo centro](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/hiperbole/fig-04-hiperbole-vertical-e-assintotas.png)
<!-- tikz:fim fig-04-hiperbole-vertical-e-assintotas -->

O denominador do termo positivo contém $$a^{2}$$ e determina os vértices. O outro contém $$b^{2}$$.

### 2.2 Retângulo fundamental

As retas que passam pelo centro e pelas diagonais do retângulo de lados $$2a$$ e $$2b$$ são assíntotas: as folhas se aproximam delas sem tocá-las.

**Leitura de uma equação**

Considere:

$$\frac{x^{2}}{9}-\frac{y^{2}}{4}=1$$

**Resolução:**

- **Passo 1:** Identificar os parâmetros.

$$a=3$$

$$b=2$$

- **Passo 2:** Calcular a distância focal.

$$c=\sqrt{3^{2}+2^{2}}$$

$$c=\sqrt{13}$$

- **Passo 3:** Escrever as assíntotas.

$$y=\pm\frac{2}{3}x$$

**Resposta:** a hipérbole abre horizontalmente, tem vértices $$(\pm3,0)$$, focos $$(\pm\sqrt{13},0)$$ e assíntotas $$y=\pm2x/3$$.

> 🔢 **Padrão:**
>
> Na equação reduzida, a variável do termo positivo está alinhada ao eixo real.

---

## 3. Excentricidade e hipérbole equilátera

A excentricidade informa quanto as folhas se afastam da forma-limite determinada por suas assíntotas.

### 3.1 Excentricidade

Na hipérbole:

$$e=\frac{c}{a}>1$$

Quanto mais próximo $$e$$ está de 1, mais estreita é a abertura; valores maiores indicam folhas mais abertas. Na elipse, em contraste, $$0<e<1$$.

<!-- tikz:inicio fig-05-comparacao-de-excentricidades -->
![Duas hipérboles na mesma escala com excentricidades um vírgula dois e dois, mostrando aberturas diferentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/hiperbole/fig-05-comparacao-de-excentricidades.png)
<!-- tikz:fim fig-05-comparacao-de-excentricidades -->

### 3.2 Caso equilátero

A **hipérbole equilátera** satisfaz $$a=b$$. Com centro na origem e eixo real horizontal, suas propriedades são:

- assíntotas perpendiculares;
- equações das assíntotas $$y=\pm x$$ no caso horizontal;
- excentricidade $$e=\sqrt{2}$$.

<!-- tikz:inicio fig-06-hiperbole-equilatera -->
![Hipérbole equilátera com parâmetros a e b iguais, retângulo fundamental quadrado e assíntotas perpendiculares](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/hiperbole/fig-06-hiperbole-equilatera.png)
<!-- tikz:fim fig-06-hiperbole-equilatera -->

**Hipérbole com parâmetros iguais**

Considere $$a=b=4$$. Determine $$c$$ e $$e$$.

**Resolução:**

- **Passo 1:** Aplicar a relação fundamental.

$$c^{2}=4^{2}+4^{2}$$

$$c^{2}=32$$

$$c=4\sqrt{2}$$

- **Passo 2:** Calcular a excentricidade.

$$e=\frac{4\sqrt{2}}{4}$$

$$e=\sqrt{2}$$

**Resposta:** a distância do centro a cada foco é $$4\sqrt{2}$$ unidades e a excentricidade é $$\sqrt{2}$$; trata-se de hipérbole equilátera.

| Elipse | Hipérbole |
|---|---|
| soma de distâncias | diferença em módulo |
| curva fechada | duas folhas abertas |
| quatro vértices | dois vértices |
| $$0<e<1$$ | $$e>1$$ |

> ⚠️ **Atenção:**
>
> “Equilátera” não significa lados iguais: significa parâmetros $$a$$ e $$b$$ iguais e assíntotas perpendiculares.

---

## 4. Aplicações da hipérbole

Sistemas de navegação hiperbólica localizam um receptor comparando o tempo de chegada de sinais enviados por estações conhecidas.

### 4.1 Diferença de tempo e distância

Se dois sinais viajam com velocidade $$v_s$$ e chegam separados por $$\Delta t$$, a diferença entre as distâncias percorridas é:

$$\Delta d=v_s\Delta t$$

<!-- tikz:inicio fig-07-uma-hiperbole-de-localizacao -->
![Duas estações S1 e S2 servem de focos para um ramo hiperbólico que contém as posições possíveis do receptor P](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/hiperbole/fig-07-uma-hiperbole-de-localizacao.png)
<!-- tikz:fim fig-07-uma-hiperbole-de-localizacao -->

Manter $$\Delta d$$ constante define uma hipérbole com as estações nos focos. Uma segunda dupla de estações produz outra hipérbole; a interseção indica a posição.

<!-- tikz:inicio fig-08-intersecao-de-duas-hiperboles -->
![Duas duplas de estações geram hipérboles distintas cuja interseção determina a posição P do receptor](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/hiperbole/fig-08-intersecao-de-duas-hiperboles.png)
<!-- tikz:fim fig-08-intersecao-de-duas-hiperboles -->

**Diferença registrada pelo receptor**

Considere $$v_s\approx3\cdot10^{8}\,\mathrm{m/s}$$ e $$\Delta t=20\,\mu\mathrm{s}$$.

**Resolução:**

- **Passo 1:** Converter o intervalo para segundos.

$$20\,\mu\mathrm{s}=20\cdot10^{-6}\,\mathrm{s}$$

- **Passo 2:** Calcular a diferença de distâncias.

$$\Delta d=3\cdot10^{8}\cdot20\cdot10^{-6}$$

$$\Delta d=6000\,\mathrm{m}$$

$$\Delta d=6\,\mathrm{km}$$

**Resposta:** o receptor está num ramo da hipérbole cujos pontos diferem em $$6\,\mathrm{km}$$ nas distâncias às duas estações.

### 4.2 Outros contextos

| Contexto | Papel da hipérbole |
|---|---|
| LORAN e DECCA | localizar por diferenças de tempo |
| cometa C/1980 E1, $$e\approx1{,}05$$ | órbita hiperbólica, não periódica |
| cometa Halley, $$e\approx0{,}967$$ | contraste: órbita elíptica e periódica |
| radar meteorológico | localizar fontes por diferenças de chegada |

> 🔢 **Padrão:**
>
> Uma diferença constante define uma hipérbole; duas hipérboles independentes determinam uma posição possível.

---

# BL1_Capítulo 2 — Parábola: definição e equações reduzidas

> O que uma bola lançada, o cabo de uma ponte e a curva de uma antena têm em comum do ponto de vista geométrico?

---

## 1. Definição e elementos da parábola

Um ponto luminoso e uma linha de referência podem determinar uma curva inteira.

### 1.1 Lugar geométrico

A **parábola** é o conjunto dos pontos $$P$$ equidistantes de um ponto fixo, o **foco** $$F$$, e de uma reta fixa, a **diretriz** $$d$$:

$$PF=d(P,d)$$

<!-- tikz:inicio fig-01-definicao-por-foco-e-diretriz -->
![Ponto P da parábola ligado ao foco F e à diretriz por segmentos perpendiculares de mesma medida](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/parabola-definicao-e-equacoes-reduzidas/fig-01-definicao-por-foco-e-diretriz.png)
<!-- tikz:fim fig-01-definicao-por-foco-e-diretriz -->

Sua excentricidade é $$e=1$$, valor intermediário entre a elipse, com $$e<1$$, e a hipérbole, com $$e>1$$. A parábola possui um foco e uma diretriz, enquanto as outras duas cônicas são descritas por dois focos.

O **vértice** é o ponto médio entre o foco e sua projeção perpendicular sobre a diretriz. O **eixo de simetria** passa pelo foco e pelo vértice. O parâmetro $$p$$ mede tanto a distância do vértice ao foco quanto a distância do vértice à diretriz.

<!-- tikz:inicio fig-02-elementos-da-parabola -->
![Parábola vertical com foco, vértice, diretriz, eixo de simetria e parâmetro p identificados](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/parabola-definicao-e-equacoes-reduzidas/fig-02-elementos-da-parabola.png)
<!-- tikz:fim fig-02-elementos-da-parabola -->

O matemático francês **Blaise Pascal** (1623–1662) investigou propriedades comuns às cônicas ainda na adolescência, evidenciando a unidade geométrica dessas curvas.

### 1.2 Elementos a partir do foco

**Parábola com eixo vertical**

O foco é $$F=(0,2)$$ e a diretriz é $$y=-2$$.

**Resolução:**

- **Passo 1:** Localizar o ponto médio entre foco e diretriz.

$$V=(0,0)$$

- **Passo 2:** Medir o parâmetro.

$$p=2$$

**Resposta:** o vértice é $$(0,0)$$, o eixo é o eixo $$y$$ e a concavidade aponta para cima.

> 🔢 **Padrão:**  
> Foco e diretriz ficam em lados opostos do vértice e à mesma distância dele.

---

## 2. Equações reduzidas da parábola

O termo elevado ao quadrado indica qual eixo é perpendicular à abertura da parábola.

### 2.1 Eixos e orientação

Com vértice na origem, as formas reduzidas são:

| Equação | Foco | Diretriz | Abertura |
|---|---|---|---|
| $$x^2=4py$$ | $$(0,p)$$ | $$y=-p$$ | vertical |
| $$y^2=4px$$ | $$(p,0)$$ | $$x=-p$$ | horizontal |

O sinal de $$p$$ define a orientação. Se $$p>0$$, a abertura ocorre para cima na primeira forma e para a direita na segunda. Se $$p<0$$, ocorre para baixo ou para a esquerda.

Nas equações com $$x^2$$, o eixo é vertical e a abertura pode apontar para cima ou para baixo.

<!-- tikz:inicio fig-03-parabolas-verticais -->
![Parábolas verticais com abertura para cima e para baixo mostrando focos e diretrizes correspondentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/parabola-definicao-e-equacoes-reduzidas/fig-03-parabolas-verticais.png)
<!-- tikz:fim fig-03-parabolas-verticais -->

Nas equações com $$y^2$$, o eixo é horizontal e a abertura pode apontar para a direita ou para a esquerda.

<!-- tikz:inicio fig-04-parabolas-horizontais -->
![Parábolas horizontais com abertura para a direita e para a esquerda mostrando focos e diretrizes correspondentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/parabola-definicao-e-equacoes-reduzidas/fig-04-parabolas-horizontais.png)
<!-- tikz:fim fig-04-parabolas-horizontais -->

A variável que não está ao quadrado acompanha o eixo de simetria. O coeficiente do segundo membro é $$4p$$, e não o próprio parâmetro.

### 2.2 Leitura dos coeficientes

**Equação vertical**

Considere a parábola

$$x^2=12y$$

**Resolução:**

- **Passo 1:** Comparar o coeficiente com $$4p$$.

$$4p=12$$

- **Passo 2:** Determinar o parâmetro.

$$p=3$$

- **Passo 3:** Localizar foco e diretriz.

$$F=(0,3)$$

$$y=-3$$

**Resposta:** a parábola tem vértice na origem, foco $$(0,3)$$, diretriz $$y=-3$$ e concavidade para cima.

Por exemplo, $$y^2=-8x$$ teria $$p=-2$$ e abertura para a esquerda.

> ⚠️ **Atenção:**  
> Divida o coeficiente por 4 antes de usar o parâmetro para localizar foco e diretriz.
