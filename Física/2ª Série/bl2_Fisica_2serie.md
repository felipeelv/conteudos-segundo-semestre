# Física — 2ª Série · Bloco 2

> **3º Bimestre — Óptica geométrica** · Bloco 2 (27/08–18/09)

**Capítulos deste bloco**

2. **Refração e lentes** (6 aulas)

---

# BL2_Capítulo 1 — Refração e lentes

> Por que um lápis parece quebrado na água, uma fibra de vidro conduz luz e uma lente corrige a visão?

---

## 1. Refração luminosa: leis

Um lápis imerso parece deslocado porque a luz muda de direção ao passar da água para o ar.

### 1.1 Mudança de meio

**Refração** — mudança da velocidade da luz ao atravessar a fronteira entre meios, geralmente acompanhada de desvio.

Os ângulos são medidos em relação à normal. A Lei de Snell-Descartes estabelece:

$$n_1\sin\theta_1=n_2\sin\theta_2$$

Os índices de refração $$n_1$$ e $$n_2$$ não possuem unidade; $$\theta_1$$ e $$\theta_2$$ identificam os ângulos nos dois meios.

O desvio segue duas tendências:

- para o meio mais refringente, o raio aproxima-se da normal;
- para o meio menos refringente, afasta-se da normal;
- com incidência normal, a velocidade muda, mas a direção não.

<!-- tikz:inicio fig-01-desvio-na-refracao -->
![Raios aproximando-se e afastando-se da normal ao mudar entre meios de índices diferentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/refracao-e-lentes/fig-01-desvio-na-refracao.png)
<!-- tikz:fim fig-01-desvio-na-refracao -->

A profundidade aparente de uma piscina resulta dos prolongamentos dos raios refratados.

<!-- tikz:inicio fig-02-profundidade-aparente -->
![Objeto submerso com raios refratados e prolongamentos formando imagem aparente mais rasa](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/refracao-e-lentes/fig-02-profundidade-aparente.png)
<!-- tikz:fim fig-02-profundidade-aparente -->

### 1.2 A lei dos senos

Por volta de 984, **Ibn Sahl** já descrevera uma relação equivalente. **Willebrord Snell** chegou à forma senoidal em 1621, mas não a publicou; **René Descartes** apresentou-a quantitativamente em *La Dioptrique*, de 1637.

📝 **Exemplo:**  
Da água, $$n_1=1{,}33$$, para o ar, $$n_2=1{,}00$$, um raio incide a $$30^\circ$$.

$$1{,}33\sin30^\circ=1{,}00\sin\theta_2$$

$$\sin\theta_2=0{,}665$$

$$\theta_2\approx41{,}7^\circ$$

O raio afasta-se da normal.

> ⏸️ **Pare e Pense:**  
> Por que o lápis parece deslocado exatamente na fronteira entre água e ar?

---

## 2. Índice de refração e reflexão total

Diamantes e fibras ópticas controlam a luz por meio de índices de refração diferentes.

### 2.1 Índice e velocidade

O **índice de refração** compara a velocidade da luz no vácuo com a velocidade no meio:

$$n=\frac{c}{v}$$

Como $$v\leq c$$, vale $$n\geq1$$.

Alguns valores aproximados permitem comparar materiais:

| Meio | Índice $$n$$ |
|---|---:|
| Água | 1,33 |
| Vidro comum | 1,50 |
| Diamante | 2,42 |

### 2.2 Reflexão total interna

A reflexão total exige duas condições:

- passagem do meio mais refringente para o menos refringente;
- ângulo de incidência maior que o ângulo limite.

Para $$n_1>n_2$$:

$$\sin\theta_L=\frac{n_2}{n_1}$$

📝 **Exemplo:**  
Na passagem do diamante, com $$n_1=2{,}42$$, para o ar, com $$n_2=1{,}00$$:

$$\sin\theta_L=\frac{1{,}00}{2{,}42}$$

$$\theta_L\approx24{,}4^\circ$$

O pequeno ângulo favorece múltiplas reflexões e o brilho. Fibras ópticas mantêm a luz no núcleo por reflexão total; miragens envolvem refração contínua em camadas de ar.

<!-- tikz:inicio fig-03-reflexao-total-na-fibra -->
![Raio luminoso refletindo sucessivamente no núcleo de uma fibra óptica](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/refracao-e-lentes/fig-03-reflexao-total-na-fibra.png)
<!-- tikz:fim fig-03-reflexao-total-na-fibra -->

> ⚡ **Física no Dia a Dia:**  
> Na fibra óptica, o revestimento possui índice menor que o núcleo para favorecer a reflexão total.

---

## 3. Lentes esféricas

Óculos e lupas desviam raios luminosos por refração em superfícies curvas.

### 3.1 Convergente × divergente

**Lente** — meio transparente limitado por superfícies, pelo menos uma delas curva, que refrata a luz.

No modelo de lente fina no ar:

| Lente | Forma típica | Raios paralelos | Foco |
|---|---|---|---|
| Convergente | mais espessa no centro | aproximam-se | real |
| Divergente | mais espessa nas bordas | afastam-se | virtual |

<!-- tikz:inicio fig-04-lente-convergente-e-divergente -->
![Raios paralelos convergindo após uma lente e divergindo após a outra](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/refracao-e-lentes/fig-04-lente-convergente-e-divergente.png)
<!-- tikz:fim fig-04-lente-convergente-e-divergente -->

O comportamento depende também do índice do meio ao redor; a tabela descreve o caso usual de vidro ou plástico no ar.

### 3.2 Elementos geométricos

Três elementos organizam a construção de imagens:

- **centro óptico $$O$$** — ponto central atravessado sem desvio no modelo fino;
- **focos $$F$$ e $$F'$$** — pontos associados aos raios paralelos;
- **distância focal $$f$$** — distância entre o centro óptico e o foco, medida em metro (m).

<!-- tikz:inicio fig-05-elementos-da-lente-fina -->
![Eixo de lente fina com centro óptico, focos e distâncias focais identificados](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/refracao-e-lentes/fig-05-elementos-da-lente-fina.png)
<!-- tikz:fim fig-05-elementos-da-lente-fina -->

A convenção de sinais distingue os tipos:

$$f>0$$ para lente convergente e $$f<0$$ para lente divergente.

Esse sinal descreve a ação óptica, não apenas o formato observado. Lentes finas idealizam espessura desprezível e raios próximos do eixo principal.

> 💡 **Você sabia?**  
> Uma lente convergente imersa em outro meio pode perder parte de sua capacidade de convergir a luz.

---

## 4. Formação de imagens em lentes

O encontro de raios refratados, ou de seus prolongamentos, determina posição e natureza da imagem.

### 4.1 Raios notáveis

Três raios permitem construir a imagem:

- paralelo ao eixo principal — emerge passando pelo foco imagem;
- dirigido ao foco objeto — emerge paralelo ao eixo;
- pelo centro óptico — segue sem desvio no modelo de lente fina.

<!-- tikz:inicio fig-06-raios-notaveis-na-convergente -->
![Três raios notáveis formando imagem real em uma lente convergente](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/refracao-e-lentes/fig-06-raios-notaveis-na-convergente.png)
<!-- tikz:fim fig-06-raios-notaveis-na-convergente -->

Raios que se encontram formam imagem real; prolongamentos que se encontram formam imagem virtual.

### 4.2 Casos da lente convergente

A posição do objeto determina o resultado:

| Objeto | Imagem |
|---|---|
| Além de $$2F$$ | real, invertida e reduzida |
| Em $$2F$$ | real, invertida e igual |
| Entre $$2F$$ e $$F$$ | real, invertida e ampliada |
| Em $$F$$ | imprópria, no infinito |
| Entre $$F$$ e $$O$$ | virtual, direita e ampliada |

<!-- tikz:inicio fig-07-casos-principais-da-convergente -->
![Quatro posições do objeto na lente convergente com orientação e tamanho das imagens](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/refracao-e-lentes/fig-07-casos-principais-da-convergente.png)
<!-- tikz:fim fig-07-casos-principais-da-convergente -->

A lente divergente produz, para objeto real, imagem sempre virtual, direita e reduzida, entre o foco e o centro óptico.

A construção deve respeitar simultaneamente os raios notáveis e as propriedades da tabela. Se houver discordância, o traçado ou a posição do objeto precisa ser revisto.

> ⏸️ **Pare e Pense:**  
> Por que uma lupa só amplia de forma direita quando o objeto fica entre o foco e a lente?

---

## 5. Equação das lentes e vergência

O traçado indica o tipo da imagem; as equações determinam posição, aumento e potência óptica.

### 5.1 Gauss e aumento

Para lentes finas, a equação de Gauss é:

$$\frac{1}{f}=\frac{1}{p}+\frac{1}{p'}$$

O aumento linear é:

$$A=-\frac{p'}{p}$$

Os sinais distinguem posição e natureza da imagem:

- $$f$$ — distância focal, positiva na convergente e negativa na divergente;
- $$p$$ — posição do objeto;
- $$p'$$ — posição da imagem, positiva se real e negativa se virtual;
- $$A$$ — aumento, sem unidade.

📝 **Exemplo:**  
Para $$f=0{,}20\,\mathrm{m}$$ e $$p=0{,}60\,\mathrm{m}$$:

$$\frac{1}{p'}=\frac{1}{0{,}20}-\frac{1}{0{,}60}$$

$$\frac{1}{p'}=3{,}33\,\mathrm{m^{-1}}$$

$$p'=0{,}30\,\mathrm{m}$$

$$A=-\frac{p'}{p}$$

$$A=-\frac{0{,}30}{0{,}60}$$

$$A=-0{,}50$$

A imagem é real, invertida e reduzida.

### 5.2 Vergência

A **vergência** é medida em dioptria (D):

$$V=\frac{1}{f}$$

Com $$f$$ em metro, a lente do exemplo possui $$V=5\,\mathrm{D}$$. Lentes em contato somam vergências:

$$V_{total}=V_1+V_2$$

Sem dedução, a equação dos fabricantes no ar é:

$$\frac{1}{f}=(n-1)\left(\frac{1}{R_1}-\frac{1}{R_2}\right)$$

Nessa expressão, $$R_1$$ e $$R_2$$ são os raios de curvatura, com sinais definidos pela orientação das superfícies.

> 💡 **Você sabia?**  
> “Grau dos óculos” é o nome cotidiano da vergência, expressa em dioptrias.

---

## 6. Óptica da visão

O olho ajusta sua lente interna para formar imagens nítidas sobre a retina.

### 6.1 Córnea, cristalino e retina

A córnea inicia a convergência da luz; o cristalino completa o ajuste; a retina recebe a imagem real e invertida.

Na **acomodação**, músculos alteram a curvatura do cristalino:

- objetos próximos exigem maior convergência;
- objetos distantes exigem menor convergência;
- a imagem nítida deve permanecer sobre a retina.

### 6.2 Defeitos e correções

Os principais casos se distinguem pela posição do foco:

| Condição | Formação da imagem | Correção |
|---|---|---|
| Miopia | antes da retina | lente divergente |
| Hipermetropia | depois da retina | lente convergente |
| Presbiopia | acomodação reduzida com a idade | lentes para visão próxima |
| Astigmatismo | curvaturas desiguais produzem focos diferentes | lente com correção direcional |

<!-- tikz:inicio fig-08-miopia-e-hipermetropia -->
![Olhos míope e hipermetrope com focos antes e depois da retina e lentes corretivas](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/2serie/refracao-e-lentes/fig-08-miopia-e-hipermetropia.png)
<!-- tikz:fim fig-08-miopia-e-hipermetropia -->

No século XVII, **Antonie van Leeuwenhoek** poliu lentes esféricas de cerca de 1 mm para microscópios simples com ampliações de até 270 vezes. Em 1676, descreveu bactérias observadas nesses instrumentos.

As lentes corretivas reposicionam o foco; não modificam diretamente a estrutura do olho.

> ⚡ **Física no Dia a Dia:**  
> A receita dos óculos indica vergência e outras correções necessárias para cada olho.
