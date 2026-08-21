# Capítulo 2 — Geometria analítica

> Todo o plano da geometria analítica — ponto, reta, circunferência e cônicas — nasce de uma única ideia: traduzir geometria em álgebra. Como um só sistema de coordenadas une doze anos de geometria em uma linguagem?

---

## 1. Ponto: distância, ponto médio e alinhamento

Três marcos topográficos registrados por coordenadas permitem medir lados, centro de massa e área sem uma régua sobre o terreno.

### 1.1 Fórmulas do ponto

Para $$A(x_A,y_A)$$ e $$B(x_B,y_B)$$, Pitágoras produz:

$$d(A,B)=\sqrt{(x_B-x_A)^2+(y_B-y_A)^2}$$

O ponto médio e o baricentro são médias coordenada a coordenada:

$$M=\left(\frac{x_A+x_B}{2},\frac{y_A+y_B}{2}\right)$$

$$G=\left(\frac{x_A+x_B+x_C}{3},\frac{y_A+y_B+y_C}{3}\right)$$

A área orientada de um triângulo é metade do módulo do determinante:

$$S=\frac{1}{2}\left|x_A(y_B-y_C)+x_B(y_C-y_A)+x_C(y_A-y_B)\right|$$

Se o determinante é zero, os três pontos estão alinhados.

O ponto médio divide um segmento na razão 1:1. O baricentro é o encontro das medianas e representa a média das três posições; em uma lâmina triangular homogênea, coincide com o centro de massa. Essas interpretações dão significado geométrico às médias.

### 1.2 Triângulo por coordenadas

**Marcos de um terreno**

Considere $$A=(0,0)$$, $$B=(6,0)$$ e $$C=(2,4)$$.

**Resolução:**

- **Passo 1:** Calcular $$AB$$ e seu ponto médio.

$$AB=\sqrt{(6-0)^2+(0-0)^2}$$

$$AB=6\,\mathrm{m}$$

$$M=(3,0)$$

- **Passo 2:** Calcular o baricentro.

$$G=\left(\frac{0+6+2}{3},\frac{0+0+4}{3}\right)$$

$$G=\left(\frac{8}{3},\frac{4}{3}\right)$$

- **Passo 3:** Calcular a área.

$$S=\frac{1}{2}|0+6\cdot4+0|$$

$$S=12\,\mathrm{m^2}$$

**Resposta:** $$AB=6\,\mathrm{m}$$, $$M=(3,0)$$, $$G=(8/3,4/3)$$ e a área é $$12\,\mathrm{m^2}$$; como a área não é nula, os pontos não estão alinhados.

> ⚠️ **Atenção:**  
> O módulo no determinante transforma a área orientada em área geométrica não negativa.

---

## 2. Reta: equações e posições relativas

Uma rua retilínea pode ser descrita por inclinação, interseções com os eixos ou uma equação geral.

### 2.1 Formas da equação

| Forma | Equação | Informação direta |
|---|---|---|
| geral | $$ax+by+c=0$$ | vetor normal $$(a,b)$$ |
| reduzida | $$y=mx+n$$ | inclinação $$m$$ e intercepto $$n$$ |
| segmentária | $$\frac{x}{p}+\frac{y}{q}=1$$ | interceptos $$p$$ e $$q$$ |

Para dois pontos distintos, $$m=(y_2-y_1)/(x_2-x_1)$$ quando a reta não é vertical. Retas paralelas têm coeficientes angulares iguais; perpendiculares satisfazem $$m_1m_2=-1$$.

Retas com inclinações diferentes são concorrentes e possuem um único ponto comum. Retas verticais têm equação $$x=k$$ e não admitem coeficiente angular finito; suas perpendiculares são horizontais, da forma $$y=q$$.

O menor ângulo entre retas não perpendiculares obedece:

$$\mathrm{tg}\,\theta=\left|\frac{m_2-m_1}{1+m_1m_2}\right|$$

### 2.2 Uma rua em três formas

**Traçado entre dois pontos**

Uma rua passa por $$A=(0,1)$$ e $$B=(2,5)$$.

**Resolução:**

- **Passo 1:** Calcular a inclinação.

$$m=\frac{5-1}{2-0}$$

$$m=2$$

- **Passo 2:** Escrever as formas reduzida e geral.

$$y=2x+1$$

$$2x-y+1=0$$

- **Passo 3:** Obter o intercepto horizontal.

$$0=2x+1$$

$$x=-\frac{1}{2}$$

- **Passo 4:** Escrever a forma segmentária.

$$\frac{x}{-1/2}+\frac{y}{1}=1$$

**Resposta:** a rua tem inclinação 2 e as três equações acima; qualquer reta de inclinação $$-1/2$$ é perpendicular a ela.

> 🔢 **Padrão:**  
> Formas diferentes representam o mesmo conjunto de pontos e destacam informações distintas.

---

## 3. Reta: distâncias

Uma faixa de segurança pode ser definida por todos os pontos que permanecem a determinada distância de uma linha.

### 3.1 Ponto a reta e retas paralelas

Para a reta $$ax+by+c=0$$ e o ponto $$P(x_0,y_0)$$:

$$d(P,r)=\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$$

O numerador mede a substituição algébrica do ponto; o denominador normaliza os coeficientes para transformar esse valor em distância geométrica.

Entre retas paralelas escritas com os mesmos coeficientes $$a$$ e $$b$$:

$$d(r,s)=\frac{|c_2-c_1|}{\sqrt{a^2+b^2}}$$

Essas fórmulas descrevem margens de rodovia, corredores técnicos e alturas de triângulos em coordenadas.

### 3.2 Altura por coordenadas

**Terreno triangular**

A base do terreno está sobre $$3x+4y-12=0$$, com extremos separados por $$10\,\mathrm{m}$$. O terceiro vértice é $$P=(4,5)$$.

**Resolução:**

- **Passo 1:** Calcular a altura como distância à reta.

$$h=\frac{|3\cdot4+4\cdot5-12|}{\sqrt{3^2+4^2}}$$

$$h=\frac{20}{5}$$

$$h=4\,\mathrm{m}$$

- **Passo 2:** Calcular a área.

$$S=\frac{10\cdot4}{2}$$

$$S=20\,\mathrm{m^2}$$

**Resposta:** a altura relativa à base mede $$4\,\mathrm{m}$$ e a área do terreno é $$20\,\mathrm{m^2}$$.

Uma reta paralela com termo constante 13 unidades maior ficaria a $$13/5\,\mathrm{m}$$, ou $$2{,}6\,\mathrm{m}$$, da primeira.

> ⚠️ **Atenção:**  
> Na distância entre paralelas, as equações precisam ter os coeficientes de $$x$$ e $$y$$ normalizados da mesma maneira.

---

## 4. Circunferência: equações e posições relativas

Uma praça circular pode ser reconhecida por seu centro e raio mesmo quando a equação aparece expandida.

### 4.1 Forma reduzida e forma geral

A circunferência de centro $$(a,b)$$ e raio $$r$$ satisfaz:

$$(x-a)^2+(y-b)^2=r^2$$

Ao expandir, obtém-se a forma geral. O caminho inverso usa completar quadrados para recuperar centro e raio.

As posições dependem de comparar distâncias:

| Configuração | Comparação |
|---|---|
| ponto e circunferência | $$d(P,O)$$ com $$r$$ |
| reta e circunferência | $$d(O,s)$$ com $$r$$ |
| duas circunferências | $$O_1O_2$$ com $$r_1+r_2$$ e $$|r_1-r_2|$$ |

Uma reta é tangente quando sua distância ao centro é $$r$$; o raio até o ponto de contato é perpendicular à reta.

### 4.2 Centro oculto na equação

**Praça e via tangente**

Considere a circunferência:

$$x^2+y^2-6x+4y-12=0$$

**Resolução:**

- **Passo 1:** Agrupar e completar quadrados.

$$(x^2-6x)+(y^2+4y)=12$$

$$(x-3)^2+(y+2)^2=25$$

- **Passo 2:** Identificar centro e raio.

$$O=(3,-2)$$

$$r=5\,\mathrm{m}$$

- **Passo 3:** Comparar a reta $$y=3$$ com o centro.

$$d=|3-(-2)|$$

$$d=5\,\mathrm{m}$$

**Resposta:** a praça tem centro $$(3,-2)$$ e raio $$5\,\mathrm{m}$$; a reta $$y=3$$ é tangente no ponto $$(3,3)$$.

> 🔢 **Padrão:**  
> Completar quadrados transforma coeficientes algébricos em centro e raio geométricos.

---

## 5. Cônicas: elipse, hipérbole e parábola

Órbitas, sistemas de localização e refletores usam curvas diferentes reunidas pela posição de foco e diretriz.

### 5.1 Três equações reduzidas

| Cônica | Equação canônica | Relação focal | Excentricidade |
|---|---|---|---|
| elipse | $$\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$$ | $$c^2=a^2-b^2$$ | $$0<e<1$$ |
| hipérbole | $$\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$$ | $$c^2=a^2+b^2$$ | $$e>1$$ |
| parábola | $$y^2=4px$$ | foco $$(p,0)$$ | $$e=1$$ |

Na elipse, a soma das distâncias aos focos é constante. Na hipérbole, é constante a diferença em módulo. Na parábola, cada ponto é equidistante do foco e da diretriz.

As assíntotas da hipérbole horizontal são $$y=\pm(b/a)x$$. A excentricidade $$e=c/a$$ organiza as três famílias em torno do valor 1.

### 5.2 Refletor parabólico

**Foco de uma antena**

A secção de uma antena é descrita por:

$$y^2=12x$$

**Resolução:**

- **Passo 1:** Comparar com $$y^2=4px$$.

$$4p=12$$

- **Passo 2:** Determinar o parâmetro.

$$p=3\,\mathrm{m}$$

- **Passo 3:** Escrever foco e diretriz.

$$F=(3,0)$$

$$x=-3$$

**Resposta:** o receptor deve ficar no foco $$(3,0)$$, a $$3\,\mathrm{m}$$ do vértice; a diretriz é $$x=-3$$.

A propriedade refletora direciona para o foco os raios paralelos ao eixo da parábola.

> ⚠️ **Atenção:**  
> Na hipérbole, o termo positivo indica a direção de abertura; na elipse, os dois termos quadráticos são positivos.

---

## 6. Reconhecimento e translação de cônicas

Uma equação expandida pode esconder a família da curva, seu centro e a posição de seus eixos.

### 6.1 Discriminante e translação

Na equação geral de segundo grau:

$$Ax^2+Bxy+Cy^2+Dx+Ey+F=0$$

o discriminante classifica cônicas não degeneradas:

| Discriminante | Família |
|---|---|
| $$B^2-4AC<0$$ | elipse; circunferência é caso particular |
| $$B^2-4AC=0$$ | parábola |
| $$B^2-4AC>0$$ | hipérbole |

Quando não há termo $$xy$$, completar quadrados equivale a transladar a origem para o centro ou vértice $$(h,k)$$, sem girar os eixos.

### 6.2 Curva, ponto e reta

**Galeria elíptica**

Considere:

$$x^2+4y^2-6x+16y+9=0$$

**Resolução:**

- **Passo 1:** Classificar pelo discriminante.

$$B^2-4AC=0^2-4\cdot1\cdot4$$

$$B^2-4AC=-16$$

- **Passo 2:** Completar quadrados.

$$(x-3)^2+4(y+2)^2=16$$

- **Passo 3:** Reduzir a equação.

$$\frac{(x-3)^2}{16}+\frac{(y+2)^2}{4}=1$$

- **Passo 4:** Testar a reta vertical $$x=7$$.

$$\frac{(7-3)^2}{16}+\frac{(y+2)^2}{4}=1$$

$$y=-2$$

**Resposta:** é uma elipse de centro $$(3,-2)$$ e semieixos 4 e 2; a reta $$x=7$$ toca a curva apenas em $$(7,-2)$$.

**Élie Cartan (1869–1951)** ampliou a integração entre geometria e transformações por meio de grupos de Lie e formas diferenciais, desenvolvidas a partir de 1899.

> 🔢 **Padrão:**  
> Classificar, transladar e interpretar são etapas distintas da leitura de uma cônica geral.
