# BL1_Capítulo 1 — Trabalho e máquinas simples

> Você empurra a parede com toda a força — suor escorre, braços tremem, você fica exausto. Em Física, o trabalho realizado é zero. Como pode? E como uma rampa deixa você erguer uma geladeira com metade da força — você ganhou energia de graça?

---

## 1. O trabalho de uma força

Empurre a parede por cinco minutos: suor, braços tremendo, cansaço real. A parede não saiu do lugar.

### 1.1 Sem deslocamento, sem trabalho

**Trabalho (W)** — mede o efeito de uma força ao longo de um deslocamento:

$$W = F \cdot d \cdot \cos\theta$$

- $$W$$ — trabalho, em **joule (J)**, onde $$1\,\mathrm{J} = 1\,\mathrm{N} \cdot 1\,\mathrm{m}$$;
- $$F$$ — intensidade da força (N);
- $$d$$ — deslocamento (m);
- $$\theta$$ — ângulo entre a força e o deslocamento.

Aí está o enigma da parede: se $$d = 0$$, o produto é zero, por maior que seja a força. O cansaço é **biológico** — músculo contraído consome energia. Trabalho físico exige deslocamento.

O trabalho é **escalar**: tem valor e sinal, não tem direção nem sentido.

### 1.2 Os três sinais do trabalho

O sinal depende do ângulo entre a força e o deslocamento:

| Tipo | Ângulo | A força | Exemplo |
|---|---|---|---|
| **Motor** ($$W > 0$$) | $$\theta < 90^{\circ}$$ | favorece o movimento | empurrar o carrinho |
| **Resistente** ($$W < 0$$) | $$\theta > 90^{\circ}$$ | opõe-se ao movimento | atrito, sempre |
| **Nulo** ($$W = 0$$) | $$\theta = 90^{\circ}$$ ou $$d = 0$$ | não desloca | mochila no plano |

<!-- tikz:inicio fig-01-sinais-do-trabalho -->
![Três casos com força paralela, perpendicular e oposta ao deslocamento e sinais do trabalho](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/9ano/trabalho-e-maquinas-simples/fig-01-sinais-do-trabalho.png)
<!-- tikz:fim fig-01-sinais-do-trabalho -->

📝 **Caixa empurrada com 50 N por 3 m, na direção do movimento**

$$W = 50 \cdot 3 \cdot \cos 0^{\circ} = 150\,\mathrm{J}$$

### 1.3 Coriolis e a palavra "trabalho"

Em 1829 o engenheiro francês **Gaspard-Gustave de Coriolis** (1792–1843) publicou *Du calcul de l'effet des machines*, medindo o que as máquinas industriais de fato produziam.

Foi ele quem usou *travail* — trabalho — no sentido moderno: força vezes distância.

---

## 2. Calculando o trabalho

Três valores de $$\theta$$ cobrem quase todas as situações do dia a dia.

### 2.1 O ângulo decide o sinal

| Ângulo | $$\cos\theta$$ | Expressão | Situação |
|---|---|---|---|
| $$0^{\circ}$$ | 1 | $$W = F \cdot d$$ | trabalho **máximo** |
| $$90^{\circ}$$ | 0 | $$W = 0$$ | mochila carregada no plano; força normal |
| $$180^{\circ}$$ | −1 | $$W = -F \cdot d$$ | atrito, **sempre negativo** |

Na mochila você sustenta para cima e o deslocamento é horizontal: força alguma realiza trabalho sobre ela. O atrito retira energia útil do sistema, virando calor.

### 2.2 Trabalho da força peso

$$W_{peso} = m \cdot g \cdot h$$

- $$m$$ — massa (kg) · $$g$$ — gravidade ($$10\,\mathrm{m/s^2}$$) · $$h$$ — desnível (m).

Duas propriedades:

- **positivo na descida**, negativo na subida;
- **não depende da trajetória** — escada reta ou rampa sinuosa dão o mesmo, se o desnível for igual.

<!-- tikz:inicio fig-02-trabalho-do-peso-independe-do-caminho -->
![Dois caminhos entre as mesmas alturas com o mesmo vetor peso e o mesmo desnível](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/9ano/trabalho-e-maquinas-simples/fig-02-trabalho-do-peso-independe-do-caminho.png)
<!-- tikz:fim fig-02-trabalho-do-peso-independe-do-caminho -->

📝 **Pessoa de 60 kg sobe 3 m de escada**

$$W_{peso} = 60 \cdot 10 \cdot 3 = 1800\,\mathrm{J}$$

Como ela sobe, o trabalho do peso é **negativo**: $$-1800\,\mathrm{J}$$.

---

## 3. Alavancas

Uma criança de 30 kg equilibra um adulto de 90 kg na gangorra, sentando-se três vezes mais longe do apoio.

### 3.1 O que é uma máquina simples

**Máquina simples** — facilita um trabalho **sem criar energia**: troca força por distância. No caso ideal:

$$F_1 \cdot d_1 = F_2 \cdot d_2$$

Metade da força, dobro da distância — o produto, que é o trabalho, não muda.

### 3.2 A alavanca

**Alavanca** — barra rígida que gira em torno de um **fulcro**. O equilíbrio iguala os produtos força × **braço** (distância até o fulcro): braço maior, força menor.

📝 **Pedra de 600 N a 0,5 m do fulcro; força aplicada a 1,5 m**

$$600 \cdot 0{,}5 = F_2 \cdot 1{,}5 \quad \Rightarrow \quad F_2 = 200\,\mathrm{N}$$

<!-- tikz:inicio fig-03-equilibrio-da-alavanca -->
![Alavanca com força de 600 N a meio metro e força de 200 N a um metro e meio do fulcro](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/9ano/trabalho-e-maquinas-simples/fig-03-equilibrio-da-alavanca.png)
<!-- tikz:fim fig-03-equilibrio-da-alavanca -->

### 3.3 Os três tipos

As alavancas se classificam pela posição do fulcro em relação à força aplicada e à resistência:

| Tipo | O que fica no meio | Exemplos |
|---|---|---|
| **Interfixa** | o fulcro | tesoura, alicate, gangorra |
| **Inter-resistente** | a resistência | carrinho de mão, quebra-nozes |
| **Interpotente** | a força aplicada | pinça, vassoura, braço humano |

> ⏸️ **Pare e Pense:**  
> Na alavanca interpotente a força aplicada é maior que a resistência. Que vantagem se ganha em troca?

### 3.4 Heron de Alexandria

No século I, **Heron de Alexandria** (c. 10–70 d.C.) reuniu em *Mechanica* as cinco máquinas simples: alavanca, polia composta, plano inclinado, parafuso e cunha.

---

## 4. Roldanas e plano inclinado

O guindaste levanta toneladas com cabo fino; a rampa sobe a geladeira.

### 4.1 Roldana fixa e roldana móvel

| | Roldana fixa | Roldana móvel |
|---|---|---|
| O que faz | muda a **direção** | **divide a força por 2** |
| Força necessária | igual ao peso | metade |
| Corda a puxar | igual à altura | **o dobro** |
| Por quê | presa ao suporte | dois trechos sustentam |

<!-- tikz:inicio fig-04-roldana-fixa-e-movel -->
![Comparação de roldana fixa e móvel com forças e deslocamentos da corda](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/9ano/trabalho-e-maquinas-simples/fig-04-roldana-fixa-e-movel.png)
<!-- tikz:fim fig-04-roldana-fixa-e-movel -->

Com $$n$$ roldanas móveis associadas, a força é dividida por $$2^n$$.

> 💡 **Você sabia?**  
> Um guindaste de torre com quatro trechos de cabo sustentando a carga exige do motor apenas um quarto da força correspondente ao peso levantado.

### 4.2 O plano inclinado

**Plano inclinado** — rampa que reduz a força para erguer um corpo. Desprezando o atrito:

$$F = P \cdot \sin\theta$$

- $$F$$ — força na rampa (N) · $$P$$ — peso (N) · $$\theta$$ — inclinação.

O seno cresce com o ângulo: **quanto menor a inclinação, menor a força** e maior o caminho. Daí as rampas de acessibilidade serem longas.

📝 **Geladeira de 1.000 N por rampa de 30°**

$$F = 1000 \cdot \sin 30^{\circ} = 500\,\mathrm{N}$$

Metade do peso — nada de graça: pela rampa a geladeira percorre mais do que a altura que sobe.

<!-- tikz:inicio fig-05-forca-no-plano-inclinado -->
![Carga de mil newtons em rampa de trinta graus com força paralela de quinhentos newtons](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/9ano/trabalho-e-maquinas-simples/fig-05-forca-no-plano-inclinado.png)
<!-- tikz:fim fig-05-forca-no-plano-inclinado -->

### 4.3 Parafuso e cunha

Dois planos inclinados disfarçados: o **parafuso**, rampa enrolada num cilindro; a **cunha** (machado, faca, prego), rampa dupla que converte o golpe em separação lateral.

---

## 5. Vantagem mecânica

Comparar alavanca com roldana composta exige um número comum: quanto cada uma multiplica a força.

### 5.1 A definição

**Vantagem mecânica (VM)** — razão entre a força resistente e a aplicada:

$$VM = \frac{F_R}{F_A}$$

- $$F_R$$ — carga a vencer (N) · $$F_A$$ — força aplicada (N);
- é razão entre forças, logo **não tem unidade**.

| VM | O que significa | Exemplo |
|---|---|---|
| **> 1** | multiplica a força | rampa, alavanca de braço longo |
| **< 1** | perde força, ganha velocidade ou precisão | pinça, braço humano |

📝 **Rampa da geladeira: carga 1.000 N, força aplicada 500 N**

$$VM = \frac{1000}{500} = 2$$

### 5.2 A vantagem de cada máquina

Cada máquina simples tem sua própria expressão para a vantagem mecânica:

| Máquina | Vantagem mecânica |
|---|---|
| Alavanca | razão entre os braços ($$d_2 / d_1$$) |
| Roldana fixa | 1 (só muda a direção) |
| Roldana móvel | 2 |
| Associação com $$n$$ roldanas móveis | $$2^n$$ |
| Plano inclinado | $$1/\sin\theta$$ |

Vale conferir a coerência: para a rampa de 30°, $$1/\sin 30^{\circ} = 1/0{,}5 = 2$$ — o mesmo valor obtido pela razão das forças.

### 5.3 Eficiência: o mundo real

As contas supõem máquinas **ideais**, sem atrito. Nas reais, parte do trabalho vira calor no eixo, no contato, nas dobradiças — o trabalho útil é sempre menor que o total, e a **eficiência** fica abaixo de 100%. Reduz-se o atrito com lubrificação e rolamentos; máquina perfeita não existe.

---

## 6. Máquinas simples no cotidiano

Poucas ferramentas são uma máquina simples pura; a maioria combina duas ou três.

### 6.1 Máquinas combinadas

| Ferramenta | O que combina | Efeito |
|---|---|---|
| Cortador de unhas | duas alavancas (interfixa + lâmina) | multiplica a força duas vezes |
| Guindaste de obra | polias compostas, 4 trechos de cabo | VM = 4 — motor faz ¼ do peso |
| Bicicleta | alavancas + coroa e catraca | troca força por velocidade conforme a marcha |

> ⚡ **Física no Dia a Dia:**  
> A marcha leve da bicicleta faz você pedalar mais vezes para andar a mesma distância — força menor, distância maior, exatamente a troca das máquinas simples.

### 6.2 A regra que não se quebra

**Nenhuma máquina cria energia.** O que se ganha em força, paga-se em distância:

$$F_1 \cdot d_1 = F_2 \cdot d_2$$

| Máquina | Ganho em força | Custo em distância |
|---|---|---|
| Roldana móvel | metade | dobro de corda |
| Rampa de 30° | metade | dobro de caminho |
| Alavanca 3× | um terço | mão desce 3× mais |

<!-- tikz:inicio fig-06-ganho-em-forca-custo-em-distancia -->
![Roldana, rampa e alavanca mostrando ganho de força e aumento correspondente da distância](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/9ano/trabalho-e-maquinas-simples/fig-06-ganho-em-forca-custo-em-distancia.png)
<!-- tikz:fim fig-06-ganho-em-forca-custo-em-distancia -->

Máquina alguma escapa dessa troca — por isso nunca existiu dispositivo que produza trabalho do nada.

### 6.3 O que Heron entendeu

As máquinas de Heron não tornaram ninguém mais forte: **redistribuíram o esforço**. Uma rampa permite que alguém em cadeira de rodas entre sozinho num prédio; uma polia deixa um trabalhador erguer o que dez carregariam.
