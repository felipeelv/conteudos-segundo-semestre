# Geometria — 3ª Série · Bloco 2

> **3º Bimestre — Cônicas: hipérbole e parábola** · Bloco 2 (27/08–18/09)

**Capítulos deste bloco**

3. **Parábola e reconhecimento de cônicas** (6 aulas)

---

# BL2_Capítulo 1 — Parábola e reconhecimento de cônicas

> Por que uma antena é parabólica e como reconhecer a cônica escondida em uma equação sem calcular focos ou vértices?

---

## 1. Aplicações da parábola

Uma antena parabólica concentra em um receptor pequeno sinais captados por toda a sua superfície.

### 1.1 Propriedade reflexiva

Todo raio que chega paralelo ao eixo de uma parábola é refletido em direção ao foco. Por isso, antenas posicionam o receptor no foco. O caminho inverso também vale: uma fonte luminosa colocada no foco de um farol produz raios refletidos paralelos ao eixo.

<!-- tikz:inicio fig-01-reflexao-em-antena-e-farol -->
![Antena concentrando raios paralelos no foco e farol emitindo raios paralelos a partir de uma fonte no foco](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/parabola-e-reconhecimento-de-conicas/fig-01-reflexao-em-antena-e-farol.png)
<!-- tikz:fim fig-01-reflexao-em-antena-e-farol -->

No lançamento oblíquo ideal, sem resistência do ar e com gravidade uniforme, a trajetória é uma parábola. Em situações reais, o formato é aproximado porque o ar modifica o movimento.

<!-- tikz:inicio fig-02-trajetoria-ideal-e-com-resistencia -->
![Comparação entre trajetória parabólica ideal e trajetória mais curta alterada pela resistência do ar](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/parabola-e-reconhecimento-de-conicas/fig-02-trajetoria-ideal-e-com-resistencia.png)
<!-- tikz:fim fig-02-trajetoria-ideal-e-com-resistencia -->

Para uma antena de diâmetro $$D$$ e profundidade $$h$$, a distância focal é

$$p=\frac{D^2}{16h}$$

<!-- tikz:inicio fig-03-medidas-de-uma-antena-parabolica -->
![Secção de antena parabólica com diâmetro D, profundidade h, vértice e foco a distância p](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/parabola-e-reconhecimento-de-conicas/fig-03-medidas-de-uma-antena-parabolica.png)
<!-- tikz:fim fig-03-medidas-de-uma-antena-parabolica -->

### 1.2 Posição do receptor

**Antena residencial**

Uma antena possui diâmetro de $$1{,}2\,\mathrm{m}$$ e profundidade de $$0{,}15\,\mathrm{m}$$.

**Resolução:**

- **Passo 1:** Elevar o diâmetro ao quadrado.

$$D^2=1{,}44\,\mathrm{m^2}$$

- **Passo 2:** Calcular o denominador.

$$16h=2{,}4\,\mathrm{m}$$

- **Passo 3:** Dividir.

$$p=\frac{1{,}44}{2{,}4}$$

$$p=0{,}6\,\mathrm{m}$$

**Resposta:** o receptor deve ficar a $$0{,}6\,\mathrm{m}$$ do vértice, sobre o eixo.

> 🔢 **Padrão:**  
> A reflexão transforma muitos raios paralelos em trajetórias que passam pelo mesmo foco.

---

## 2. Equação geral de uma cônica

Termos quadráticos, lineares e mistos funcionam como pistas algébricas sobre a posição de uma cônica.

### 2.1 Estrutura dos coeficientes

A equação geral de segundo grau em duas variáveis é

$$Ax^2+Bxy+Cy^2+Dx+Ey+F=0$$

Os coeficientes $$A$$, $$B$$ e $$C$$ formam a parte quadrática, que determina o tipo e uma possível rotação. Os termos $$Dx$$ e $$Ey$$ deslocam a curva em relação à origem, e $$F$$ altera o nível constante.

Quando $$B=0$$, não há termo misto e os eixos da cônica estão alinhados aos eixos coordenados. Quando $$B\neq0$$, o termo $$Bxy$$ indica que a cônica pode estar rotacionada. O cálculo do ângulo de rotação não é necessário para o reconhecimento inicial.

<!-- tikz:inicio fig-04-conica-alinhada-e-rotacionada -->
![Mesma elipse com eixos alinhados e rotacionados em relação ao sistema cartesiano](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/parabola-e-reconhecimento-de-conicas/fig-04-conica-alinhada-e-rotacionada.png)
<!-- tikz:fim fig-04-conica-alinhada-e-rotacionada -->

### 2.2 Leitura de uma equação

**Mapa dos coeficientes**

Considere

$$3x^2+2xy+5y^2-6x+4y-7=0$$

**Resolução:**

- **Passo 1:** Comparar termo a termo com a forma geral.

$$A=3,\ B=2,\ C=5$$

$$D=-6,\ E=4,\ F=-7$$

- **Passo 2:** Examinar o termo misto.

$$B\neq0$$

**Resposta:** a equação possui todos os tipos de termo e indica uma cônica rotacionada.

> ⚠️ **Atenção:**  
> A ausência de um termo significa coeficiente zero; ela não altera a posição dos demais coeficientes.

---

## 3. Discriminante de uma cônica

Três coeficientes da equação geral bastam para uma primeira classificação.

### 3.1 Regra de classificação

O discriminante da parte quadrática é

$$\Delta=B^2-4AC$$

| Sinal | Cônica não degenerada |
|---|---|
| $$\Delta<0$$ | elipse |
| $$\Delta=0$$ | parábola |
| $$\Delta>0$$ | hipérbole |

Se $$A=C$$ e $$B=0$$, o caso elíptico pode ser uma circunferência. O matemático francês **Jean-Victor Poncelet** (1788–1867) desenvolveu a geometria projetiva e tratou as três cônicas como manifestações de uma mesma estrutura contínua. O discriminante traduz algebricamente essa mudança de tipo.

<!-- tikz:inicio fig-05-continuum-e-discriminante-das-conicas -->
![Elipse, parábola e hipérbole em sequência associadas aos sinais negativo, zero e positivo do discriminante](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/parabola-e-reconhecimento-de-conicas/fig-05-continuum-e-discriminante-das-conicas.png)
<!-- tikz:fim fig-05-continuum-e-discriminante-das-conicas -->

Multiplicar toda a equação por uma constante não nula multiplica $$\Delta$$ pelo quadrado dessa constante. Portanto, seu sinal e a classificação permanecem inalterados.

### 3.2 Classificação direta

**Equação sem termo misto**

Considere

$$4x^2+9y^2-8x+18y-23=0$$

**Resolução:**

- **Passo 1:** Identificar os coeficientes quadráticos.

$$A=4,\ B=0,\ C=9$$

- **Passo 2:** Calcular o discriminante.

$$\Delta=0^2-4\cdot4\cdot9$$

$$\Delta=-144$$

- **Passo 3:** Interpretar o sinal.

$$\Delta<0$$

**Resposta:** a equação representa uma elipse não rotacionada, desde que a curva real não seja degenerada.

> 🔢 **Padrão:**  
> O discriminante classifica o tipo antes de qualquer translação ou obtenção dos elementos da cônica.

---

## 4. Identificação de cônicas

Equações visualmente diferentes podem pertencer à mesma família de curvas.

### 4.1 Tipo e casos especiais

Com $$B=0$$, o sinal e a presença dos termos quadráticos permitem uma leitura rápida:

- coeficientes quadráticos de mesmo sinal indicam tipo elíptico;
- somente uma variável ao quadrado indica tipo parabólico;
- coeficientes quadráticos de sinais opostos indicam tipo hiperbólico.

No tipo elíptico, $$A=C$$ caracteriza uma possível circunferência.

<!-- tikz:inicio fig-06-circunferencia-e-elipse -->
![Circunferência com eixos iguais comparada a elipse com semieixos de medidas diferentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/parabola-e-reconhecimento-de-conicas/fig-06-circunferencia-e-elipse.png)
<!-- tikz:fim fig-06-circunferencia-e-elipse -->

O discriminante, porém, não garante sozinho uma curva não degenerada: certas equações representam um ponto, um par de retas, uma reta dupla ou não possuem pontos reais.

<!-- tikz:inicio fig-07-casos-degenerados-de-conicas -->
![Casos degenerados representados por um ponto, um par de retas concorrentes e uma reta dupla](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/parabola-e-reconhecimento-de-conicas/fig-07-casos-degenerados-de-conicas.png)
<!-- tikz:fim fig-07-casos-degenerados-de-conicas -->

Completar quadrados resolve essa verificação algébrica.

### 4.2 Reconhecimento em segundos

**Cônica deslocada**

Considere

$$x^2-y^2-4x+2y=0$$

**Resolução:**

- **Passo 1:** Identificar $$A$$, $$B$$ e $$C$$.

$$A=1,\ B=0,\ C=-1$$

- **Passo 2:** Calcular o discriminante.

$$\Delta=0^2-4\cdot1\cdot(-1)$$

$$\Delta=4$$

- **Passo 3:** Interpretar.

$$\Delta>0$$

**Resposta:** a equação é do tipo hipérbole; completar quadrados permite verificar sua forma e seu centro.

> ⚠️ **Atenção:**  
> Classificar o tipo e verificar a existência real da curva são etapas relacionadas, mas não idênticas.

---

## 5. Conversão para a forma reduzida

Completar quadrados retira o disfarce dos termos lineares e revela centro, vértice e parâmetros.

### 5.1 Procedimento algébrico

Quando $$B=0$$, agrupam-se os termos de $$x$$ e de $$y$$. Em cada grupo, adiciona-se e subtrai-se o quadrado necessário, preservando a igualdade. Depois, a equação é normalizada para obter segundo membro igual a 1 ou a forma reduzida da parábola.

Os fatores dos termos quadráticos são colocados em evidência. Em seguida, metade de cada coeficiente linear interno é elevada ao quadrado.

Isso organiza os cálculos.

**Elipse na forma geral**

Considere

$$4x^2+9y^2-8x+18y-23=0$$

**Resolução:**

- **Passo 1:** Agrupar e completar quadrados.

$$4(x-1)^2+9(y+1)^2=36$$

- **Passo 2:** Dividir por 36.

$$\frac{(x-1)^2}{9}+\frac{(y+1)^2}{4}=1$$

- **Passo 3:** Ler os elementos.

$$C=(1,-1),\ a=3,\ b=2$$

**Resposta:** a cônica é uma elipse de centro $$(1,-1)$$ e semieixos 3 e 2.

### 5.2 As três famílias

O mesmo processo produz:

| Forma geral | Forma reduzida | Elemento principal |
|---|---|---|
| $$x^2-y^2-4x-2y-4=0$$ | $$\frac{(x-2)^2}{7}-\frac{(y+1)^2}{7}=1$$ | centro $$(2,-1)$$ |
| $$x^2-4x-8y+12=0$$ | $$(x-2)^2=8(y-1)$$ | vértice $$(2,1)$$, $$p=2$$ |

> 🔢 **Padrão:**  
> Complete quadrados separadamente em cada variável antes de dividir para normalizar a equação.

---

## 6. Translação de cônicas

Deslocar uma cônica no plano altera termos lineares, mas preserva seu tipo e suas dimensões.

### 6.1 Da origem para outro ponto

Substituir $$x$$ por $$x-h$$ e $$y$$ por $$y-k$$ move o centro ou vértice da origem para $$(h,k)$$. Assim, formas transladadas incluem

$$\frac{(x-h)^2}{a^2}+\frac{(y-k)^2}{b^2}=1$$

$$\frac{(x-h)^2}{a^2}-\frac{(y-k)^2}{b^2}=1$$

$$(x-h)^2=4p(y-k)$$

O sinal dentro do parêntese é oposto à coordenada lida: $$y+1=y-(-1)$$.

Todos os pontos notáveis acompanham o mesmo vetor de translação: centro ou vértice, focos, eixos e, quando existirem, assíntotas mantêm suas posições relativas.

Na forma expandida, esse deslocamento produz termos lineares. Completar quadrados recupera a forma transladada e permite ler diretamente as novas coordenadas de referência.

<!-- tikz:inicio fig-08-translacao-de-uma-hiperbole -->
![Hipérbole centrada na origem e cópia transladada para o centro h k com assíntotas paralelas preservadas](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/3serie/parabola-e-reconhecimento-de-conicas/fig-08-translacao-de-uma-hiperbole.png)
<!-- tikz:fim fig-08-translacao-de-uma-hiperbole -->

### 6.2 Centro de uma hipérbole

**Equação transladada**

Considere

$$9x^2-4y^2-54x-8y+41=0$$

**Resolução:**

- **Passo 1:** Agrupar e completar quadrados.

$$9(x-3)^2-4(y+1)^2=36$$

- **Passo 2:** Dividir por 36.

$$\frac{(x-3)^2}{4}-\frac{(y+1)^2}{9}=1$$

- **Passo 3:** Ler o centro e o tipo.

$$C=(3,-1)$$

**Resposta:** a cônica é uma hipérbole de centro $$(3,-1)$$, com eixo real horizontal.

> ⚠️ **Atenção:**  
> A translação muda a posição da cônica, mas não transforma elipse, parábola e hipérbole umas nas outras.
