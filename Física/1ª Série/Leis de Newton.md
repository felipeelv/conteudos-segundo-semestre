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
![Comparação entre corpo em repouso e corpo em movimento retilíneo uniforme, ambos com resultante nula](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/leis-de-newton/fig-01-equilibrio-estatico-e-dinamico.png)
<!-- tikz:fim fig-01-equilibrio-estatico-e-dinamico -->

São o mesmo fenômeno — a distinção depende do referencial. A lei vale em qualquer **referencial inercial**, o que não está acelerado.

### 1.3 O cinto de segurança

Num carro a 60 km/h o passageiro se move a:

$$v = \frac{60}{3{,}6} \approx 16{,}7\,\mathrm{m/s}$$

Na colisão a estrutura recebe a força e para. Sobre o passageiro **não age força alguma** — pela 1ª Lei ele continua a 16,7 m/s. O cinto aplica a força que falta; sem ele, quem freia é o painel.

<!-- tikz:inicio fig-02-inercia-do-passageiro -->
![Carro freando enquanto o passageiro tende a manter sua velocidade para a frente](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/leis-de-newton/fig-02-inercia-do-passageiro.png)
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

📝 **Bloco de 10 kg com duas forças perpendiculares**

$$m = 10\,\mathrm{kg} \qquad F_x = 30\,\mathrm{N} \qquad F_y = 40\,\mathrm{N}$$

$$F_R = \sqrt{30^2 + 40^2} = 50\,\mathrm{N}$$

$$a = \frac{50}{10} = 5\,\mathrm{m/s^2}$$

<!-- tikz:inicio fig-03-resultante-de-forcas-perpendiculares -->
![Forças perpendiculares de 30 N e 40 N compondo uma resultante de 50 N](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/leis-de-newton/fig-03-resultante-de-forcas-perpendiculares.png)
<!-- tikz:fim fig-03-resultante-de-forcas-perpendiculares -->

A aceleração aponta na direção e sentido da resultante.

<!-- tikz:inicio fig-04-velocidade-e-aceleracao-opostas -->
![Corpo movendo-se para a direita com aceleração e resultante para a esquerda](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/leis-de-newton/fig-04-velocidade-e-aceleracao-opostas.png)
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
![Pessoa empurrando carrinho com forças opostas aplicadas em corpos diferentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/leis-de-newton/fig-05-acao-e-reacao-em-corpos-diferentes.png)
<!-- tikz:fim fig-05-acao-e-reacao-em-corpos-diferentes -->

A reação do peso do livro é a atração que ele exerce sobre a Terra.

### 3.3 Pares no cotidiano

| Situação | Ação | Reação |
|---|---|---|
| Caminhar | pé empurra o chão para trás | chão empurra o pé para frente |
| Nadar | mão empurra a água para trás | água empurra a mão para frente |
| Foguete | motor expulsa gases para baixo | gases empurram o foguete para cima |

O foguete não precisa de ar: a reação vem dos próprios gases expelidos, e a propulsão funciona no vácuo.
