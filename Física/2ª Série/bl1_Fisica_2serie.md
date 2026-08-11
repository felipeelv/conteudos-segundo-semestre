# Física — 2ª Série · Bloco 1

> **3º Bimestre — Óptica geométrica** · Bloco 1 (05/08–25/08)

**Capítulos deste bloco**

1. **Reflexão e espelhos** (6 aulas)

---

# BL1_Capítulo 1 — Reflexão e espelhos

> **Pergunta-guia:** como o formato de um espelho modifica a imagem que vemos?

**Ao final deste capítulo, você deverá ser capaz de:**

- aplicar a lei da reflexão;
- diferenciar imagens reais e virtuais;
- prever imagens em espelhos planos, côncavos e convexos;
- usar a equação de Gauss em situações simples.

---

## 1. Luz e reflexão

### 1.1 Modelo de raios

Na óptica geométrica, representamos a luz por **raios luminosos**: linhas com setas que indicam a direção de propagação.

| Princípio | O que diz | Consequência |
|---|---|---|
| **Propagação retilínea** | em meio homogêneo, a luz segue em linha reta | formação de sombras |
| **Independência** | raios que se cruzam continuam seus caminhos | feixes não se alteram |
| **Reversibilidade** | o caminho da luz pode ser percorrido nos dois sentidos | quem você vê no espelho também pode ver você |

> 🔎 **Contexto:** Alhazen demonstrou que enxergamos porque a luz chega aos olhos, e não porque os olhos emitem raios.

### 1.2 Reflexão regular e difusa

| | Regular | Difusa |
|---|---|---|
| Superfície | lisa | irregular |
| Raios refletidos | permanecem organizados | espalham-se em várias direções |
| Resultado | imagem nítida | sem imagem nítida |

Nos dois casos, cada raio obedece à **lei da reflexão**.

<!-- tikz:inicio fig-01-reflexao-regular-e-difusa -->
![Feixes paralelos refletidos paralelamente em superfície lisa e espalhados em superfície irregular](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-01-reflexao-regular-e-difusa.png)
<!-- tikz:fim fig-01-reflexao-regular-e-difusa -->

### 1.3 Imagem real e virtual

- **Imagem real:** os raios se encontram; pode ser projetada em uma tela.
- **Imagem virtual:** apenas os prolongamentos dos raios se encontram; não pode ser projetada.

---

## 2. Reflexão e espelhos planos

### 2.1 A lei da reflexão

Quando um raio atinge uma superfície refletora:

- raio incidente, normal e raio refletido ficam no **mesmo plano**;
- o ângulo de incidência é igual ao de reflexão: $$\hat{i} = \hat{r}$$.

<!-- tikz:inicio fig-02-lei-da-reflexao -->
![Raio incidente e refletido com ângulos iguais medidos a partir da normal](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-02-lei-da-reflexao.png)
<!-- tikz:fim fig-02-lei-da-reflexao -->

> ⚠️ **Atenção:** os ângulos são medidos em relação à **normal**, nunca em relação ao espelho.

### 2.2 A imagem no espelho plano

No espelho plano, a imagem é sempre:

- **virtual**;
- **direita**;
- do **mesmo tamanho** do objeto;
- simétrica: objeto e imagem ficam à mesma distância do espelho.

<!-- tikz:inicio fig-03-imagem-no-espelho-plano -->
![Objeto e imagem virtual simétricos a distâncias iguais do espelho plano](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-03-imagem-no-espelho-plano.png)
<!-- tikz:fim fig-03-imagem-no-espelho-plano -->

> O espelho não troca esquerda e direita: ele inverte a direção **frente–fundo**.

### 2.3 Associação de espelhos planos

Quando $$360^{\circ}/\theta$$ é par, dois espelhos que formam um ângulo $$\theta$$ produzem:

$$N = \frac{360^{\circ}}{\theta} - 1$$

📝 **Exemplo: dois espelhos a 60°**

$$N = \frac{360}{60} - 1 = 5$$

Logo, são formadas **cinco imagens**. Esse é o princípio do caleidoscópio.

---

## 3. Espelhos esféricos

### 3.1 Côncavo × convexo

Um **espelho esférico** é uma parte de uma esfera com uma face refletora.

| | Côncavo | Convexo |
|---|---|---|
| Face refletora | interna | externa |
| Efeito sobre raios paralelos | aproxima os raios | afasta os raios |
| Comportamento | **convergente** | **divergente** |
| Foco | **real**, à frente | **virtual**, atrás |

<!-- tikz:inicio fig-04-espelho-concavo-e-convexo -->
![Raios paralelos convergindo no foco do côncavo e divergindo como se viessem do foco do convexo](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-04-espelho-concavo-e-convexo.png)
<!-- tikz:fim fig-04-espelho-concavo-e-convexo -->

### 3.2 Elementos geométricos

| Elemento | Símbolo | O que é |
|---|---|---|
| Vértice | V | ponto central da superfície do espelho |
| Centro de curvatura | C | centro da esfera de onde a calota veio |
| Foco | F | ponto onde os raios, ou seus prolongamentos, se encontram |
| Raio de curvatura | R | distância de V até C |
| Eixo principal | — | reta que passa por V e C |

O foco fica no ponto médio entre V e C:

$$f = \frac{R}{2}$$

<!-- tikz:inicio fig-05-elementos-do-espelho-esferico -->
![Eixo principal do espelho côncavo com vértice, foco, centro e raio de curvatura](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-05-elementos-do-espelho-esferico.png)
<!-- tikz:fim fig-05-elementos-do-espelho-esferico -->

### 3.3 O limite do modelo

> A relação $$f = R/2$$ usa a **aproximação paraxial**: raios próximos e pouco inclinados em relação ao eixo. Fora dessa condição, pode ocorrer perda de nitidez chamada **aberração esférica**.

> ⏸️ **Pare e Pense:**  
> Se o foco de um espelho côncavo é real e o de um convexo é virtual, qual dos dois poderia concentrar luz solar num ponto?

---

## 4. Formação de imagens

### 4.1 Os três raios notáveis

No espelho côncavo:

| Raio que chega | Reflete |
|---|---|
| paralelo ao eixo principal | passando pelo **foco** |
| passando pelo **foco** | paralelo ao eixo |
| no **vértice** | simetricamente ao eixo |

Para localizar a imagem:

1. escolha dois raios notáveis;
2. trace os raios refletidos;
3. encontre o cruzamento dos raios ou de seus prolongamentos.

<!-- tikz:inicio fig-06-raios-notaveis-no-concavo -->
![Três raios notáveis partindo do topo do objeto e formando uma imagem no espelho côncavo](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-06-raios-notaveis-no-concavo.png)
<!-- tikz:fim fig-06-raios-notaveis-no-concavo -->

### 4.2 Os cinco casos do côncavo

| Posição do objeto | Imagem |
|---|---|
| Além de C | real, invertida, reduzida |
| Em C | real, invertida, mesmo tamanho |
| Entre C e F | real, invertida, ampliada |
| Em F | imprópria, no infinito (raios paralelos) |
| Entre F e V | virtual, direita, ampliada |

<!-- tikz:inicio fig-07-casos-principais-do-concavo -->
![Quatro posições do objeto no espelho côncavo com orientação e tamanho das imagens](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-07-casos-principais-do-concavo.png)
<!-- tikz:fim fig-07-casos-principais-do-concavo -->

> ⚡ **Física no Dia a Dia:**  
> No espelho de maquiagem, o rosto deve ficar entre F e V para produzir uma imagem direita e ampliada.

### 4.3 O espelho convexo

Para qualquer objeto real, o espelho convexo produz imagem:

- **virtual**;
- **direita**;
- **reduzida**.

Sua principal vantagem é o **campo visual maior**.

<!-- tikz:inicio fig-08-campo-visual-do-convexo -->
![Comparação do campo visual de espelho plano e convexo para o mesmo observador](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-08-campo-visual-do-convexo.png)
<!-- tikz:fim fig-08-campo-visual-do-convexo -->

---

## 5. A equação de Gauss

O desenho permite prever a imagem. As equações permitem calcular sua **posição** e seu **tamanho**.

### 5.1 As duas equações

$$\frac{1}{p} + \frac{1}{p'} = \frac{1}{f} \qquad A = \frac{i}{o} = -\frac{p'}{p}$$

| Símbolo | Significado |
|---|---|
| $$p$$ | distância do objeto ao vértice |
| $$p'$$ | distância da imagem ao vértice |
| $$f$$ | distância focal |
| $$o$$ | altura do objeto |
| $$i$$ | altura da imagem |
| $$A$$ | aumento linear |

### 5.2 A convenção de sinais

| Resultado | Interpretação |
|---|---|
| $$p' > 0$$ | imagem real |
| $$p' < 0$$ | imagem virtual |
| $$f > 0$$ | espelho côncavo |
| $$f < 0$$ | espelho convexo |
| $$A > 0$$ | imagem direita |
| $$A < 0$$ | imagem invertida |

Para objetos reais, usamos $$p > 0$$. Em módulo, $$|A| > 1$$ indica ampliação e $$|A| < 1$$ indica redução.

### 5.3 Roteiro de resolução

1. identifique o tipo de espelho e os sinais;
2. aplique a equação de Gauss;
3. calcule o aumento e interprete os resultados.

📝 **Objeto a 60 cm de um côncavo de focal 20 cm**

$$\frac{1}{p'} = \frac{1}{20} - \frac{1}{60} = \frac{2}{60}$$

$$p' = 30\,\mathrm{cm} \qquad A = -\frac{30}{60} = -0{,}5$$

**Conclusão:** imagem real, invertida e com metade do tamanho do objeto.

---

## 6. Aplicações dos espelhos esféricos

| Aplicação | Espelho | Como funciona |
|---|---|---|
| **Farol** | côncavo | lâmpada no foco; os raios saem paralelos |
| **Telescópio refletor** | côncavo | concentra a luz recebida de objetos distantes |
| **Espelho de maquiagem** | côncavo | objeto entre F e V; imagem direita e ampliada |
| **Retrovisor lateral** | convexo | imagem reduzida e campo visual maior |

> Em equipamentos de maior precisão, refletores parabólicos reduzem a aberração esférica.

### 6.1 Síntese do capítulo

| Espelho | Comportamento da imagem |
|---|---|
| **Plano** | virtual, direita e do mesmo tamanho |
| **Convexo** | sempre virtual, direita e reduzida |
| **Côncavo** | depende da posição do objeto em relação a C, F e V |

Para resolver uma questão:

1. identifique o tipo de espelho;
2. localize o objeto em relação aos pontos principais;
3. preveja as características da imagem;
4. use as equações quando forem pedidas posição ou ampliação.
