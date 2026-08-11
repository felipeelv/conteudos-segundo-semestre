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
