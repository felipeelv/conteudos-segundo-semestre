# Física — 1ª Série · Bloco 1

> **3º Bimestre — Dinâmica: leis de Newton e aplicações** · Bloco 1 (05/08–25/08)

**Capítulos deste bloco**

1. **Leis de Newton** (3 aulas)
2. **Forças mecânicas** (3 aulas)

---

# BL1_Capítulo 1 — Leis de Newton

> Você empurra o carrinho de supermercado vazio e ele dispara; cheio, mal sai do lugar — a mesma força, resultados diferentes. E o cinto de segurança: por que ele salva vidas se o carro é quem freia, não você?

---

## 1. A 1ª Lei de Newton

Em 1684 Halley perguntou a Newton qual seria a órbita de um planeta sob força que decai com o quadrado da distância. "Elipse — eu já calculei."

### 1.1 O enunciado vetorial

**1ª Lei (princípio da inércia)** — resultante nula equivale a velocidade constante:

$$\vec{F}_R = 0 \Leftrightarrow \vec{v} = \text{const.}$$

- $$\vec{F}_R$$ — força resultante (N);
- $$\vec{v}$$ — velocidade (m/s).

A seta não é decoração: velocidade constante significa **módulo, direção e sentido** constantes. Carro em curva com velocímetro fixo tem resultante não nula.

### 1.2 Os dois equilíbrios

| | Estático | Dinâmico |
|---|---|---|
| O corpo está | em repouso | em MRU (reta, velocidade constante) |
| Exemplo | livro sobre a mesa | avião em voo de cruzeiro |
| Resultante | nula | nula |

<!-- tikz:inicio fig-01-equilibrio-estatico-e-dinamico -->
![Comparação entre corpo em repouso e corpo em movimento retilíneo uniforme, ambos com resultante nula](https://raw.githubusercontent.com/felipeelv/imagens-tikz/1addc5b0379a44995a89003d50781f5d7d10d764/fisica/1serie/leis-de-newton/fig-01-equilibrio-estatico-e-dinamico.png)
<!-- tikz:fim fig-01-equilibrio-estatico-e-dinamico -->

São o mesmo fenômeno — a distinção depende do referencial. A lei vale em qualquer **referencial inercial**, o que não está acelerado.

### 1.3 O cinto de segurança

Num carro a 60 km/h o passageiro se move a:

$$v = \frac{60}{3{,}6} \approx 16{,}7\,\mathrm{m/s}$$

Na colisão a estrutura recebe a força e para. Sobre o passageiro **não age força alguma** — pela 1ª Lei ele continua a 16,7 m/s. O cinto aplica a força que falta; sem ele, quem freia é o painel.

<!-- tikz:inicio fig-02-inercia-do-passageiro -->
![Carro freando enquanto o passageiro tende a manter sua velocidade para a frente](https://raw.githubusercontent.com/felipeelv/imagens-tikz/1addc5b0379a44995a89003d50781f5d7d10d764/fisica/1serie/leis-de-newton/fig-02-inercia-do-passageiro.png)
<!-- tikz:fim fig-02-inercia-do-passageiro -->

> 📏 **Medidas Impressionantes:**  
> A 60 km/h, um corpo de 70 kg chega ao para-brisa com energia comparável à de uma queda do terceiro andar.

---

## 2. A 2ª Lei de Newton

O carrinho vazio dispara com um empurrão leve; cheio, resiste ao mesmo empurrão.

### 2.1 A lei fundamental da dinâmica

$$\vec{F}_R = m\vec{a}$$

- $$\vec{F}_R$$ — força resultante (N);
- $$m$$ — massa (kg);
- $$\vec{a}$$ — aceleração (m/s²).

Duas leituras:

- a aceleração tem **a direção e o sentido da resultante**, não da velocidade;
- para a mesma força, a aceleração é **inversamente proporcional à massa** — o caso do carrinho cheio.

A lei define o **newton**: 1 N imprime 1 m/s² a um corpo de 1 kg.

### 2.2 Diagrama de corpo livre

Procedimento padrão de qualquer problema de dinâmica:

- **Passo 1:** representar o corpo como um ponto;
- **Passo 2:** desenhar só as forças que agem **sobre ele**;
- **Passo 3:** adotar eixos e projetar cada força.

A equação vetorial vira duas escalares independentes:

$$F_{Rx} = m a_x \qquad F_{Ry} = m a_y$$

<!-- tikz:inicio fig-06-diagrama-de-corpo-livre -->
![Cena física de um bloco empurrado em ângulo e o diagrama de corpo livre correspondente, com a força inclinada projetada nos eixos](https://raw.githubusercontent.com/felipeelv/imagens-tikz/1addc5b0379a44995a89003d50781f5d7d10d764/fisica/1serie/leis-de-newton/fig-06-diagrama-de-corpo-livre.png)
<!-- tikz:fim fig-06-diagrama-de-corpo-livre -->

📝 **Bloco de 10 kg com duas forças perpendiculares**

$$m = 10\,\mathrm{kg} \qquad F_x = 30\,\mathrm{N} \qquad F_y = 40\,\mathrm{N}$$

$$F_R = \sqrt{30^2 + 40^2} = 50\,\mathrm{N}$$

$$a = \frac{50}{10} = 5\,\mathrm{m/s^2}$$

<!-- tikz:inicio fig-03-resultante-de-forcas-perpendiculares -->
![Forças perpendiculares de 30 N e 40 N compondo uma resultante de 50 N](https://raw.githubusercontent.com/felipeelv/imagens-tikz/1addc5b0379a44995a89003d50781f5d7d10d764/fisica/1serie/leis-de-newton/fig-03-resultante-de-forcas-perpendiculares.png)
<!-- tikz:fim fig-03-resultante-de-forcas-perpendiculares -->

A aceleração aponta na direção e sentido da resultante.

<!-- tikz:inicio fig-04-velocidade-e-aceleracao-opostas -->
![Corpo movendo-se para a direita com aceleração e resultante para a esquerda](https://raw.githubusercontent.com/felipeelv/imagens-tikz/1addc5b0379a44995a89003d50781f5d7d10d764/fisica/1serie/leis-de-newton/fig-04-velocidade-e-aceleracao-opostas.png)
<!-- tikz:fim fig-04-velocidade-e-aceleracao-opostas -->

> ⏸️ **Pare e Pense:**  
> Um corpo tem velocidade para a direita e força resultante para a esquerda. Ele vai para que lado — e o que acontece com sua rapidez?

---

## 3. A 3ª Lei de Newton

Para nadar você empurra a água para trás; o foguete empurra gases para baixo e sobe.

### 3.1 Pares de ação e reação

**3ª Lei** — se A exerce força sobre B, B exerce sobre A uma força oposta:

$$\vec{F}_{AB} = -\vec{F}_{BA}$$

Quatro características do par:

- mesma intensidade;
- mesma direção;
- sentidos opostos;
- **atuam em corpos diferentes** — o item decisivo.

### 3.2 Por que os pares nunca se anulam

Se toda força tem reação igual e oposta, por que algo se move? Porque **as duas agem em corpos diferentes** — no cálculo de um corpo entram só as forças aplicadas **sobre ele**.

| | Mesmo corpo | Corpos diferentes |
|---|---|---|
| Exemplo | peso e normal no livro | você empurra o carrinho |
| Se anulam? | **sim** | **não** |
| É par ação-reação? | **não** | **sim** |

<!-- tikz:inicio fig-05-acao-e-reacao-em-corpos-diferentes -->
![Pessoa empurrando carrinho com forças opostas aplicadas em corpos diferentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/1addc5b0379a44995a89003d50781f5d7d10d764/fisica/1serie/leis-de-newton/fig-05-acao-e-reacao-em-corpos-diferentes.png)
<!-- tikz:fim fig-05-acao-e-reacao-em-corpos-diferentes -->

A reação do peso do livro é a atração que ele exerce sobre a Terra.

<!-- tikz:inicio fig-07-par-livro-e-terra -->
![Livro e Terra atraindo-se com forças de mesmo módulo e sentidos opostos, cada uma aplicada em um corpo](https://raw.githubusercontent.com/felipeelv/imagens-tikz/1addc5b0379a44995a89003d50781f5d7d10d764/fisica/1serie/leis-de-newton/fig-07-par-livro-e-terra.png)
<!-- tikz:fim fig-07-par-livro-e-terra -->

### 3.3 Pares no cotidiano

| Situação | Ação | Reação |
|---|---|---|
| Caminhar | pé empurra o chão para trás | chão empurra o pé para frente |
| Nadar | mão empurra a água para trás | água empurra a mão para frente |
| Foguete | motor expulsa gases para baixo | gases empurram o foguete para cima |

O foguete não precisa de ar: a reação vem dos próprios gases expelidos, e a propulsão funciona no vácuo.

---

# BL1_Capítulo 2 — Forças mecânicas

> No elevador subindo, seu estômago "pesa" mais; em queda livre, a balança marcaria zero. Você não engordou e a gravidade não mudou — o que mudou? E por que a mola da suspensão do carro "sabe" exatamente quanto empurrar de volta?

---

## 1. Peso e normal

Numa balança dentro do elevador, o ponteiro sobe no instante em que ele arranca — e você não ganhou massa.

### 1.1 Peso e massa

**Peso** — força gravitacional com que um astro atrai um corpo:

$$\vec{P} = m\vec{g}$$

- $$m$$ — massa (kg);
- $$\vec{g}$$ — aceleração da gravidade (m/s²), vertical e para baixo; na Terra, $$g = 10\,\mathrm{m/s^2}$$.

| | Massa | Peso |
|---|---|---|
| O que é | propriedade do corpo | força |
| Unidade | kg | N |
| Muda de astro? | não | sim |

### 1.2 A força normal

**Normal** ($$\vec{N}$$) — força que a superfície exerce sobre o corpo apoiado, sempre **perpendicular** a ela.

Tratar $$N = P$$ como regra geral é armadilha: a igualdade só vale com superfície **horizontal** e sem aceleração vertical. Fora disso, calcule a normal pela 2ª Lei.

<!-- tikz:inicio fig-01-normal-em-superficies-diferentes -->
![Bloco no piso e na rampa com forças normais perpendiculares a cada superfície](https://raw.githubusercontent.com/felipeelv/imagens-tikz/f00a6edd55765ba1a600e93f290e2ba3953a4f98/fisica/1serie/forcas-mecanicas/fig-01-normal-em-superficies-diferentes.png)
<!-- tikz:fim fig-01-normal-em-superficies-diferentes -->

### 1.3 Peso aparente

A balança não mede seu peso: mede a **normal** com que ela empurra seus pés.

| Situação | Normal | A balança |
|---|---|---|
| Subindo acelerado | $$N = m(g + a)$$ | marca mais |
| Descendo acelerado | $$N = m(g - a)$$ | marca menos |
| Queda livre ($$a = g$$) | $$N = 0$$ | marca zero |

<!-- tikz:inicio fig-02-peso-aparente-no-elevador -->
![Três diagramas do elevador acelerando para cima, para baixo e em queda livre](https://raw.githubusercontent.com/felipeelv/imagens-tikz/f00a6edd55765ba1a600e93f290e2ba3953a4f98/fisica/1serie/forcas-mecanicas/fig-02-peso-aparente-no-elevador.png)
<!-- tikz:fim fig-02-peso-aparente-no-elevador -->

📝 **Pessoa de 70 kg em elevador subindo a 2 m/s²**

$$N = 70 \cdot (10 + 2) = 840\,\mathrm{N}$$

Parada, a balança indicaria 700 N. O peso não mudou: aumentou a força de contato necessária para acelerá-la.

Astronautas em órbita flutuam não por ausência de gravidade — ela é intensa lá em cima —, mas porque estação e tripulantes caem juntos.

---

## 2. Tração

O guindaste ergue a viga por um cabo. O cabo não empurra: só puxa, e puxa igual nas duas pontas.

### 2.1 O cabo ideal

**Tração** ($$\vec{T}$$) — força transmitida ao longo de um fio, cabo ou corda esticada.

O modelo do **cabo ideal** (sem massa, inextensível) tem uma consequência decisiva:

- a tração é **a mesma em todos os pontos do fio**;
- num cabo real, com massa, cada trecho suportaria também o peso do que está abaixo.

A **polia ideal** (massa desprezível, sem atrito) **muda a direção** da tração sem alterar seu módulo — daí puxar para baixo e erguer algo.

<!-- tikz:inicio fig-03-tracao-em-cabo-e-polia-ideais -->
![Corda sobre polia ideal com vetores de tração iguais nos dois trechos](https://raw.githubusercontent.com/felipeelv/imagens-tikz/f00a6edd55765ba1a600e93f290e2ba3953a4f98/fisica/1serie/forcas-mecanicas/fig-03-tracao-em-cabo-e-polia-ideais.png)
<!-- tikz:fim fig-03-tracao-em-cabo-e-polia-ideais -->

### 2.2 Sistemas de corpos ligados

Dois corpos unidos por fio inextensível têm a **mesma aceleração em módulo**. Esse é o vínculo que resolve o sistema.

Método: **uma equação por corpo**, pela 2ª Lei, com o sentido positivo no do movimento previsto.

📝 **Bloco A (3 kg) na mesa lisa, ligado por polia ao bloco B (2 kg) pendurado**

$$T = m_A \cdot a \qquad m_B \cdot g - T = m_B \cdot a$$

<!-- tikz:inicio fig-06-diagramas-dos-corpos-ligados -->
![Diagramas de corpo livre dos dois blocos ligados, com a tração em ambos e o peso maior no bloco pendurado](https://raw.githubusercontent.com/felipeelv/imagens-tikz/f00a6edd55765ba1a600e93f290e2ba3953a4f98/fisica/1serie/forcas-mecanicas/fig-06-diagramas-dos-corpos-ligados.png)
<!-- tikz:fim fig-06-diagramas-dos-corpos-ligados -->

Somando:

$$20 = 5a \quad \Rightarrow \quad a = 4\,\mathrm{m/s^2}$$

$$T = 3 \cdot 4 = 12\,\mathrm{N}$$

<!-- tikz:inicio fig-04-corpos-ligados-e-mesma-aceleracao -->
![Bloco na mesa e bloco pendente ligados por corda com acelerações de mesmo módulo](https://raw.githubusercontent.com/felipeelv/imagens-tikz/f00a6edd55765ba1a600e93f290e2ba3953a4f98/fisica/1serie/forcas-mecanicas/fig-04-corpos-ligados-e-mesma-aceleracao.png)
<!-- tikz:fim fig-04-corpos-ligados-e-mesma-aceleracao -->

> ⏸️ **Pare e Pense:**  
> A tração (12 N) é menor que o peso de B (20 N). Por que ela não poderia ser igual?

---

## 3. A força elástica

Em 1678, Hooke publicou a descoberta como anagrama — "ceiiinosssttuv" — para garantir a prioridade. Decifrado: *Ut tensio, sic vis*.

### 3.1 A lei de Hooke

$$F_{el} = -k \cdot x$$

- $$F_{el}$$ — força elástica (N);
- $$k$$ — constante elástica da mola (N/m);
- $$x$$ — deformação em relação ao comprimento natural (m).

O sinal negativo é o coração da expressão: a força tem **sentido oposto ao da deformação**. Comprima e a mola empurra de volta; estique e ela puxa de volta — por isso é **restauradora**. Em módulo, $$|F_{el}| = k|x|$$.

**Robert Hooke** (1635–1703), primeiro Curador de Experimentos da Royal Society, cunhou também o termo "célula", em 1665.

### 3.2 A constante elástica

**$$k$$** mede a dureza da mola, em N/m: valor alto, mola dura; valor baixo, mola macia.

Cada mola da suspensão de um carro de passeio tem $$k$$ da ordem de 30.000 N/m.

📝 **Mola de 200 N/m comprimida em 5 cm**

$$|F_{el}| = 200 \cdot 0{,}05 = 10\,\mathrm{N}$$

### 3.3 O limite elástico

A proporcionalidade descreve o **regime linear** da mola. Acima do **limite elástico** ela se deforma permanentemente e não volta ao comprimento original — é a mola de caneta esticada demais.

<!-- tikz:inicio fig-07-grafico-forca-e-deformacao -->
![Gráfico do módulo da força elástica em função da deformação, com reta no regime linear e desvio após o limite elástico](https://raw.githubusercontent.com/felipeelv/imagens-tikz/f00a6edd55765ba1a600e93f290e2ba3953a4f98/fisica/1serie/forcas-mecanicas/fig-07-grafico-forca-e-deformacao.png)
<!-- tikz:fim fig-07-grafico-forca-e-deformacao -->

Todo modelo físico tem domínio de validade, e conhecer esse limite faz parte de usá-lo.

<!-- tikz:inicio fig-05-forca-restauradora-e-limite-elastico -->
![Mola comprimida, alongada e deformada além do limite com respostas distintas](https://raw.githubusercontent.com/felipeelv/imagens-tikz/f00a6edd55765ba1a600e93f290e2ba3953a4f98/fisica/1serie/forcas-mecanicas/fig-05-forca-restauradora-e-limite-elastico.png)
<!-- tikz:fim fig-05-forca-restauradora-e-limite-elastico -->
