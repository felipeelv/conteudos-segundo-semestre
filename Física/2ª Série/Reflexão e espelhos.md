# BL1_Capítulo 1 — Reflexão e espelhos

> Por que o "1234" do carro de polícia parece "4321" no retrovisor? Por que o farol projeta luz a 100 m à frente, o espelho de maquiagem amplia o rosto e o retrovisor convexo reduz tudo — e o Hubble usa espelhos curvos gigantes em vez de lentes?

---

## 1. Fundamentos da óptica geométrica

Por volta de 1015, no Cairo, um estudioso contrariou mil anos de tradição grega: os olhos não emitem nada — a luz vem dos objetos até nós.

### 1.1 Alhazen e o método

**Ibn al-Haytham** (965–1040), o Alhazen, escreveu o *Kitāb al-Manāẓir*, refutando a emissão visual e estudando a reflexão com geometria rigorosa. O que o consagrou foi o procedimento — hipótese, teste, verificação —, e por isso é chamado de pai da óptica.

### 1.2 O modelo de raios e seus três princípios

A óptica geométrica trata a luz como **raios**: retas orientadas na direção de propagação. O modelo ignora a natureza ondulatória e vale enquanto o comprimento de onda for muito menor que os objetos.

| Princípio | O que diz | Consequência |
|---|---|---|
| **Propagação retilínea** | em meio homogêneo a luz vai em reta | sombras de contorno definido |
| **Independência** | feixes que se cruzam não se perturbam | projetores cruzados seguem nítidos |
| **Reversibilidade** | o caminho de A a B serve de B a A | quem você vê pelo retrovisor vê você |

### 1.3 Reflexão e imagem

| | Regular | Difusa |
|---|---|---|
| Superfície | polida | irregular |
| Raios paralelos | saem paralelos | espalham |
| Imagem | sim | não |

<!-- tikz:inicio fig-01-reflexao-regular-e-difusa -->
![Feixes paralelos refletidos paralelamente em superfície lisa e espalhados em superfície irregular](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-01-reflexao-regular-e-difusa.png)
<!-- tikz:fim fig-01-reflexao-regular-e-difusa -->

| | Real | Virtual |
|---|---|---|
| O que se cruza | os raios refletidos | só os **prolongamentos** |
| Projeta em anteparo? | sim | não |

---

## 2. Reflexão e espelhos planos

"POLÍCIA" vem escrito ao contrário no capô e aparece legível no retrovisor de quem está à frente.

### 2.1 A lei da reflexão

Duas condições:

- raio incidente, normal e raio refletido no **mesmo plano**;
- ângulos iguais: $$\hat{i} = \hat{r}$$, onde $$\hat{i}$$ é a incidência e $$\hat{r}$$ a reflexão.

<!-- tikz:inicio fig-02-lei-da-reflexao -->
![Raio incidente e refletido com ângulos iguais medidos a partir da normal](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-02-lei-da-reflexao.png)
<!-- tikz:fim fig-02-lei-da-reflexao -->

O erro mais comum da óptica: os ângulos se medem **em relação à normal** (perpendicular à superfície), nunca à superfície. Medir do espelho dá o complemento e erra tudo em seguida.

### 2.2 A imagem no espelho plano

Quatro características, todas decorrentes da lei da reflexão:

- **virtual** — forma-se atrás do espelho, no encontro dos prolongamentos;
- **direita** — não invertida de cabeça para baixo;
- **do mesmo tamanho** do objeto;
- **simétrica** — imagem e objeto à mesma distância do espelho.

<!-- tikz:inicio fig-03-imagem-no-espelho-plano -->
![Objeto e imagem virtual simétricos a distâncias iguais do espelho plano](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-03-imagem-no-espelho-plano.png)
<!-- tikz:fim fig-03-imagem-no-espelho-plano -->

A "inversão" do espelho não é esquerda-direita nem cima-baixo: é **troca de frente e fundo**, ao longo do eixo perpendicular. Sua mão direita continua à direita — inverteu-se a profundidade.

### 2.3 Associação de espelhos planos

Dois espelhos a um ângulo $$\theta$$ produzem múltiplas imagens:

$$N = \frac{360^{\circ}}{\theta} - 1$$

📝 **Dois espelhos a 60°**

$$N = \frac{360}{60} - 1 = 5$$

É o princípio do caleidoscópio.

---

## 3. Espelhos esféricos

No lado côncavo da colher sua imagem aparece invertida; no convexo, direita e menor.

### 3.1 Côncavo × convexo

**Espelho esférico** — calota esférica com uma das faces refletora.

| | Côncavo | Convexo |
|---|---|---|
| Face refletora | interna | externa |
| Raios paralelos ao eixo | **convergem** | **divergem** |
| Foco | **real**, à frente | **virtual**, atrás |

<!-- tikz:inicio fig-04-espelho-concavo-e-convexo -->
![Raios paralelos convergindo no foco do côncavo e divergindo como se viessem do foco do convexo](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-04-espelho-concavo-e-convexo.png)
<!-- tikz:fim fig-04-espelho-concavo-e-convexo -->

### 3.2 Elementos geométricos

Cinco elementos descrevem qualquer espelho esférico:

| Elemento | Símbolo | O que é |
|---|---|---|
| Vértice | V | centro da calota, sobre a superfície |
| Centro de curvatura | C | centro da esfera de onde a calota veio |
| Foco | F | ponto onde os raios paralelos convergem |
| Raio de curvatura | R | distância de V até C |
| Eixo principal | — | reta que passa por V e C |

Foco e centro guardam relação fixa — o foco fica no meio do caminho entre V e C:

$$f = \frac{R}{2}$$

<!-- tikz:inicio fig-05-elementos-do-espelho-esferico -->
![Eixo principal do espelho côncavo com vértice, foco, centro e raio de curvatura](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-05-elementos-do-espelho-esferico.png)
<!-- tikz:fim fig-05-elementos-do-espelho-esferico -->

### 3.3 O limite do modelo

A relação vale sob **aproximação paraxial** — só raios próximos ao eixo e pouco inclinados.

Raios afastados não convergem no foco e a imagem perde nitidez nas bordas: é a **aberração esférica**, razão de faróis e telescópios de qualidade usarem superfícies parabólicas.

> ⏸️ **Pare e Pense:**  
> Se o foco de um espelho côncavo é real e o de um convexo é virtual, qual dos dois poderia concentrar luz solar num ponto?

---

## 4. Formação de imagens

Não é preciso desenhar todos os raios: bastam dois, e três têm comportamento conhecido.

### 4.1 Os três raios notáveis

| Raio que chega | Reflete |
|---|---|
| paralelo ao eixo principal | passando pelo **foco** |
| passando pelo **foco** | paralelo ao eixo |
| no **vértice** | simetricamente ao eixo |

Traçados dois a partir do topo do objeto, a imagem se forma onde eles — ou seus prolongamentos — se cruzam.

<!-- tikz:inicio fig-06-raios-notaveis-no-concavo -->
![Três raios notáveis partindo do topo do objeto e formando uma imagem no espelho côncavo](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-06-raios-notaveis-no-concavo.png)
<!-- tikz:fim fig-06-raios-notaveis-no-concavo -->

### 4.2 Os cinco casos do côncavo

O tipo de imagem muda conforme a posição do objeto:

| Posição do objeto | Imagem |
|---|---|
| Além de C | real, invertida, reduzida |
| Em C | real, invertida, mesmo tamanho |
| Entre C e F | real, invertida, ampliada |
| Em F | não se forma (raios saem paralelos) |
| Entre F e V | virtual, direita, ampliada |

<!-- tikz:inicio fig-07-casos-principais-do-concavo -->
![Quatro posições do objeto no espelho côncavo com orientação e tamanho das imagens](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-07-casos-principais-do-concavo.png)
<!-- tikz:fim fig-07-casos-principais-do-concavo -->

Duas linhas explicam o cotidiano: a última é o espelho de maquiagem; a terceira, o projetor.

> ⚡ **Física no Dia a Dia:**  
> Ao afastar o rosto do espelho de maquiagem, a imagem passa de ampliada e direita a invertida — você cruzou o foco.

### 4.3 O espelho convexo

No convexo não há casos a distinguir: para qualquer objeto real a imagem é **sempre virtual, direita e reduzida** — e o campo visual fica muito maior que o de um plano de mesmo tamanho.

<!-- tikz:inicio fig-08-campo-visual-do-convexo -->
![Comparação do campo visual de espelho plano e convexo para o mesmo observador](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/reflexao-e-espelhos/fig-08-campo-visual-do-convexo.png)
<!-- tikz:fim fig-08-campo-visual-do-convexo -->

---

## 5. A equação de Gauss

A construção mostra o tipo de imagem. Para saber **onde** e **de que tamanho**, calcula-se.

### 5.1 As duas equações

**Carl Friedrich Gauss** (1777–1855) formalizou em 1841, nas *Dioptrische Untersuchungen*, o comportamento dos espelhos sob aproximação paraxial — e fixou a convenção de sinais usada até hoje.

$$\frac{1}{p} + \frac{1}{p'} = \frac{1}{f} \qquad A = \frac{i}{o} = -\frac{p'}{p}$$

- $$p$$ — distância do objeto ao vértice · $$p'$$ — da imagem · $$f$$ — focal;
- $$i$$ — altura da imagem · $$o$$ — do objeto.

### 5.2 A convenção de sinais

| Grandeza | Positiva | Negativa |
|---|---|---|
| $$p$$ | objeto real (caso usual) | — |
| $$p'$$ | imagem real, à frente | virtual, atrás |
| $$f$$ | espelho côncavo | convexo |
| $$A$$ | imagem direita | invertida |

Em módulo, $$|A| > 1$$ indica ampliação.

📝 **Objeto a 60 cm de um côncavo de focal 20 cm**

$$\frac{1}{60} + \frac{1}{p'} = \frac{1}{20}$$

$$\frac{1}{p'} = \frac{3}{60} - \frac{1}{60} = \frac{2}{60}$$

$$p' = 30\,\mathrm{cm}$$

$$A = -\frac{p'}{p} = -\frac{30}{60} = -0{,}5$$

A imagem é real ($$p' > 0$$), invertida ($$A < 0$$) e reduzida à metade.

Confere com a tabela da aula anterior: o objeto está além de C (a 40 cm), e o previsto era real, invertida e reduzida. Desenho e cálculo precisam concordar.

---

## 6. Aplicações dos espelhos esféricos

Todas as perguntas do capítulo têm a mesma raiz: a curvatura decide o que acontece com a luz.

### 6.1 Farol e telescópio

No **farol**, a lâmpada fica **no foco** de um refletor côncavo: pela reversibilidade, os raios saem paralelos ao eixo e o feixe segue longe sem se abrir. Refletores de qualidade usam superfície **parabólica**, sem aberração esférica — mesmo princípio das antenas parabólicas.

Telescópios grandes usam espelho côncavo, não lente: uma lente de vários metros só poderia ser apoiada pelas bordas e se deformaria com o próprio peso; o espelho é sustentado por trás em toda a superfície.

> 📏 **Medidas Impressionantes:**  
> O Observatório do Pico dos Dias, em Minas Gerais, opera um telescópio refletor com espelho principal de 1,6 m de diâmetro.

### 6.2 Maquiagem e retrovisor

| | Espelho de maquiagem | Retrovisor lateral |
|---|---|---|
| Tipo | côncavo | convexo |
| Posição do objeto | entre o foco e o vértice | qualquer |
| Imagem | virtual, direita, **ampliada** | virtual, direita, **reduzida** |
| Vantagem | amplia o rosto de perto | campo visual largo, menos ponto cego |
| Limite | afastar além do foco inverte a imagem | objeto menor parece mais longe |

Daí o aviso impresso no retrovisor: os objetos estão mais perto do que aparentam.
