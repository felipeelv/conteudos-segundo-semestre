# Física — 1ª Série · Bloco 2

> **3º Bimestre — Dinâmica: leis de Newton e aplicações** · Bloco 2 (27/08–18/09)

**Capítulos deste bloco**

3. **Aplicações da dinâmica** (6 aulas)

---

# BL2_Capítulo 1 — Aplicações da dinâmica

> Um sofá resiste ao primeiro empurrão, mas desliza com mais facilidade depois. Em um looping, por que o carrinho não cai no topo?

---

## 1. Força de atrito: estático e cinético

Ao empurrar um sofá, o atrito muda de intensidade antes de o movimento começar.

### 1.1 Dois regimes

O atrito atua paralelamente ao contato e se opõe ao deslizamento ou à sua tendência.

| Regime | Intensidade | Situação |
|---|---|---|
| Estático | $$F_{at,e} \leq \mu_e N$$ | varia até o limite de escorregamento |
| Cinético | $$F_{at,c} = \mu_c N$$ | atua durante o deslizamento |

Os coeficientes $$\mu_e$$ e $$\mu_c$$ não possuem unidade. Em geral, $$\mu_e>\mu_c$$, por isso iniciar o movimento exige maior força.

<!-- tikz:inicio fig-01-transicao-do-atrito-estatico-ao-cinetico -->
![Gráfico qualitativo em que o atrito estático cresce com a força aplicada até um máximo e então diminui para o patamar do atrito cinético](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/aplicacoes-da-dinamica/fig-01-transicao-do-atrito-estatico-ao-cinetico.png)
<!-- tikz:fim fig-01-transicao-do-atrito-estatico-ao-cinetico -->

### 1.2 Modelo de Amontons–Coulomb

Em 1699, **Guillaume Amontons** publicou regularidades observadas em máquinas. No modelo de atrito seco:

- a força de atrito é proporcional à normal;
- independe da área aparente de contato;
- no regime cinético ideal, independe da velocidade.

Os coeficientes dependem do par de materiais: borracha e asfalto seco têm $$\mu_c \approx 0{,}7$$; aço e gelo, cerca de $$0{,}03$$.

> ⚡ **Física no Dia a Dia:**  
> Frear sobre gelo é difícil porque o baixo coeficiente limita a força de atrito disponível.

---

## 2. Aplicações no plano horizontal

Uma caixa puxada no piso acelera somente quando a força aplicada supera o atrito.

### 2.1 Diagrama de corpo livre

Em piso horizontal, sem aceleração vertical, quatro forças podem atuar:

- peso $$\vec{P}$$, para baixo;
- normal $$\vec{N}$$, para cima;
- força aplicada $$\vec{F}$$, na direção do movimento;
- atrito $$\vec{F}_{at}$$, em sentido oposto.

<!-- tikz:inicio fig-02-diagrama-de-corpo-livre-horizontal -->
![Caixa isolada com peso para baixo, normal para cima, força aplicada para a direita e atrito para a esquerda](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/aplicacoes-da-dinamica/fig-02-diagrama-de-corpo-livre-horizontal.png)
<!-- tikz:fim fig-02-diagrama-de-corpo-livre-horizontal -->

O equilíbrio vertical fornece:

$$N=P=m g$$

Antes do movimento, o atrito iguala a força aplicada até $$F_{at,e}^{max}=\mu_eN$$. Após o deslizamento, vale $$F_{at,c}=\mu_cN$$.

### 2.2 Resultante e aceleração

No eixo horizontal, a 2ª Lei fica:

$$F_R = F - F_{at,c} = m a$$

📝 **Exemplo:**  
Uma caixa de $$10\,\mathrm{kg}$$ recebe $$50\,\mathrm{N}$$. Adote $$\mu_c=0{,}20$$ e $$g=10\,\mathrm{m/s^2}$$.

$$N = m g$$

$$N = 10 \cdot 10$$

$$N = 100\,\mathrm{N}$$

$$F_{at,c} = \mu_c N$$

$$F_{at,c} = 0{,}20 \cdot 100$$

$$F_{at,c} = 20\,\mathrm{N}$$

$$F_R = F-F_{at,c}$$

$$F_R = 50-20$$

$$F_R = 30\,\mathrm{N}$$

$$a = \frac{F_R}{m}$$

$$a = \frac{30}{10}$$

$$a = 3\,\mathrm{m/s^2}$$

> ⏸️ **Pare e Pense:**  
> Se a força aplicada ainda não atingiu o limite estático, por que não se deve usar automaticamente $$F_{at,e}=\mu_eN$$?

---

## 3. Aplicações no plano inclinado

Em uma rampa, parte do peso puxa o bloco ladeira abaixo e parte o comprime contra a superfície.

### 3.1 Decomposição do peso

Para uma rampa de ângulo $$\theta$$, o peso $$P=mg$$ possui duas componentes:

$$P_x = P\sin\theta$$

$$P_y = P\cos\theta$$

<!-- tikz:inicio fig-03-decomposicao-do-peso-na-rampa -->
![Bloco em rampa com peso vertical decomposto em uma componente paralela e outra perpendicular ao plano inclinado](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/aplicacoes-da-dinamica/fig-03-decomposicao-do-peso-na-rampa.png)
<!-- tikz:fim fig-03-decomposicao-do-peso-na-rampa -->

$$N=P\cos\theta$$

Portanto, usar $$N=P$$ em plano inclinado é incorreto.

### 3.2 Atrito e movimento

Se o corpo desliza para baixo, o atrito aponta para cima:

$$F_{at,c}=\mu_cP\cos\theta$$

$$F_R=P\sin\theta-F_{at,c}=ma$$

Na iminência de escorregar, a componente paralela do peso iguala o atrito estático máximo:

$$P\sin\theta_{im}=\mu_eP\cos\theta_{im}$$

$$\tan\theta_{im}=\mu_e$$

📝 **Exemplo:**  
Um bloco de $$10\,\mathrm{kg}$$ desce uma rampa de $$30^\circ$$. Adote $$\mu_c=0{,}20$$, $$g=10\,\mathrm{m/s^2}$$, $$\sin30^\circ=0{,}50$$ e $$\cos30^\circ\approx0{,}87$$.

$$P=mg$$

$$P=10\cdot10$$

$$P=100\,\mathrm{N}$$

$$P_x=P\sin\theta$$

$$P_x=100\cdot0{,}50$$

$$P_x=50\,\mathrm{N}$$

$$N=P\cos\theta$$

$$N=100\cdot0{,}87$$

$$N=87\,\mathrm{N}$$

$$F_{at,c}=\mu_cN$$

$$F_{at,c}=0{,}20\cdot87$$

$$F_{at,c}=17{,}4\,\mathrm{N}$$

$$F_R=P_x-F_{at,c}$$

$$F_R=50-17{,}4$$

$$F_R=32{,}6\,\mathrm{N}$$

$$a=\frac{F_R}{m}$$

$$a=\frac{32{,}6}{10}$$

$$a=3{,}26\,\mathrm{m/s^2}$$

O sentido do atrito deve ser definido pela tendência de deslizamento, não pela inclinação isoladamente.

> 💡 **Você sabia?**  
> Uma rampa mais inclinada reduz a normal e, com ela, o maior atrito estático possível.

---

## 4. Dinâmica curvilínea: força centrípeta

Em uma curva, a velocidade muda de direção mesmo quando seu módulo permanece constante.

### 4.1 A resultante para o centro

A **aceleração centrípeta** aponta para o centro da trajetória circular:

$$a_c=\frac{v^2}{R}=\omega^2R$$

Pela 2ª Lei de Newton:

$$F_c=ma_c=m\frac{v^2}{R}=m\omega^2R$$

<!-- tikz:inicio fig-04-velocidade-e-resultante-centripeta -->
![Corpo em trajetória circular com velocidade tangente à curva e força resultante dirigida para o centro](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/aplicacoes-da-dinamica/fig-04-velocidade-e-resultante-centripeta.png)
<!-- tikz:fim fig-04-velocidade-e-resultante-centripeta -->

Aqui, $$\omega$$ é a velocidade angular, em rad/s.

### 4.2 Um papel, não uma força nova

“Centrípeta” identifica o papel da resultante radial. Esse papel pode ser exercido por forças reais:

| Situação | Força que aponta para o centro |
|---|---|
| Carro em curva plana | atrito |
| Pedra presa a um fio | tração |
| Satélite | gravidade |
| Carrinho em looping | combinação de normal e peso |

Em 1673, **Christiaan Huygens** apresentou a primeira expressão explícita para $$a_c=v^2/R$$.

> ⏸️ **Pare e Pense:**  
> Se a “força centrípeta” fosse uma força adicional, qual interação física seria responsável por ela?

---

## 5. Movimento circular: aplicações

Curvas, lombadas e loopings mudam a direção da resultante e a força de contato.

### 5.1 Curva plana e pista vertical

Numa curva plana, o atrito fornece a resultante centrípeta. No limite:

$$\mu N = m\frac{v_{max}^2}{R}$$

Como $$N=mg$$:

$$v_{max}=\sqrt{\mu gR}$$

<!-- tikz:inicio fig-05-atrito-na-curva-plana -->
![Vista superior de carro em curva plana com velocidade tangente à pista e atrito apontando para o centro da trajetória](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/aplicacoes-da-dinamica/fig-05-atrito-na-curva-plana.png)
<!-- tikz:fim fig-05-atrito-na-curva-plana -->

Em trajetórias verticais, peso e normal mudam sua relação:

| Posição | Sentido do centro | Relação |
|---|---|---|
| Topo de lombada | para baixo | $$P-N=m\dfrac{v^2}{R}$$, então $$N<P$$ |
| Fundo de vale | para cima | $$N-P=m\dfrac{v^2}{R}$$, então $$N>P$$ |

<!-- tikz:inicio fig-06-forcas-na-lombada-e-no-vale -->
![Comparação entre topo de lombada, onde a normal é menor que o peso, e fundo de vale, onde a normal é maior que o peso](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/aplicacoes-da-dinamica/fig-06-forcas-na-lombada-e-no-vale.png)
<!-- tikz:fim fig-06-forcas-na-lombada-e-no-vale -->

### 5.2 Looping vertical

No topo de um looping, peso e normal apontam para o centro:

$$P+N=m\frac{v^2}{R}$$

A velocidade mínima ocorre no limite de contato, quando $$N=0$$:

$$v_{min}=\sqrt{gR}$$

<!-- tikz:inicio fig-07-forcas-no-topo-e-na-base-do-looping -->
![Looping vertical com peso dirigido ao centro e normal tendendo a zero no topo limite, além de normal maior que o peso na base](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/aplicacoes-da-dinamica/fig-07-forcas-no-topo-e-na-base-do-looping.png)
<!-- tikz:fim fig-07-forcas-no-topo-e-na-base-do-looping -->

Na base, a normal precisa superar o peso para produzir a resultante para cima. Por isso, a sensação de peso é maior na parte inferior e menor no topo.

> ⚡ **Física no Dia a Dia:**  
> Por isso a velocidade se reduz antes da curva: frear dentro dela consome parte do atrito disponível para mudar a direção.

---

## 6. Sistemas com blocos e cordas

Uma corda ideal faz blocos ligados compartilharem o mesmo módulo de aceleração.

### 6.1 Equações por corpo

No modelo ideal, o fio é inextensível e sem massa, e a polia não possui atrito nem inércia. Assim:

- os blocos têm acelerações de mesmo módulo;
- a tração $$T$$ é igual em toda a corda;
- cada corpo recebe sua própria equação da 2ª Lei.

Para um bloco $$A$$ sobre a mesa ligado a um bloco pendente $$B$$:

$$T-F_{at}=m_Aa$$

$$m_Bg-T=m_Ba$$

<!-- tikz:inicio fig-08-sistema-de-blocos-e-diagramas -->
![Blocos ligados por uma corda sobre polia acompanhados dos diagramas de forças separados para o bloco da mesa e o bloco pendente](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/aplicacoes-da-dinamica/fig-08-sistema-de-blocos-e-diagramas.png)
<!-- tikz:fim fig-08-sistema-de-blocos-e-diagramas -->

Somar as equações elimina a tração.

### 6.2 Sistema com atrito

📝 **Exemplo:**  
Considere $$m_A=4\,\mathrm{kg}$$, $$m_B=2\,\mathrm{kg}$$, $$\mu_c=0{,}25$$ e $$g=10\,\mathrm{m/s^2}$$.

$$F_{at}=\mu_cm_Ag$$

$$F_{at}=0{,}25\cdot4\cdot10$$

$$F_{at}=10\,\mathrm{N}$$

$$P_B=m_Bg$$

$$P_B=2\cdot10$$

$$P_B=20\,\mathrm{N}$$

$$P_B-F_{at}=(m_A+m_B)a$$

$$20-10=(4+2)a$$

$$10=6a$$

$$a=\frac{10}{6}$$

$$a\approx1{,}67\,\mathrm{m/s^2}$$

Pela equação do bloco $$A$$:

$$T=F_{at}+m_Aa$$

$$T=10+4\cdot1{,}67$$

$$T=16{,}68\,\mathrm{N}$$

$$T\approx16{,}7\,\mathrm{N}$$

> 💡 **Você sabia?**  
> Se a corda tiver massa ou a polia tiver inércia, a tração pode deixar de ser igual nos dois trechos.
