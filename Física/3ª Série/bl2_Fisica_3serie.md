# Física — 3ª Série · Bloco 2

> **3º Bimestre — Magnetismo e eletromagnetismo** · Bloco 2 (27/08–18/09)

**Capítulos deste bloco**

2. **Força magnética** (3 aulas)
3. **Indução eletromagnética** (3 aulas)

---

# BL2_Capítulo 1 — Força magnética

> Como um campo magnético faz motores girarem e curva prótons em um cíclotron sem aumentar diretamente sua velocidade?

---

## 1. Força magnética sobre carga

Uma carga em movimento pode ser desviada ao atravessar um campo magnético.

### 1.1 Força de Lorentz magnética

A componente magnética da força de Lorentz é:

$$\vec{F}_m=q\left(\vec{v}\times\vec{B}\right)$$

Seu módulo vale:

$$F_m=|q|vB\sin\theta$$

Aqui, $$q$$ é a carga elétrica, em coulomb (C), e $$\theta$$ é o ângulo entre $$\vec{v}$$ e $$\vec{B}$$.

Em 1895, **Hendrik Lorentz** reuniu as interações elétrica e magnética em uma formulação única.

A força é perpendicular à velocidade e ao campo. Pela regra da mão direita, os dedos acompanham $$\vec{v}$$ e se curvam para $$\vec{B}$$; o polegar indica $$\vec{F}_m$$ para carga positiva. Para carga negativa, o sentido é oposto.

<!-- tikz:inicio fig-01-regra-vetor-velocidade-campo-forca -->
![Vetores velocidade, campo e força magnética mutuamente perpendiculares para carga positiva](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/forca-magnetica/fig-01-regra-vetor-velocidade-campo-forca.png)
<!-- tikz:fim fig-01-regra-vetor-velocidade-campo-forca -->

### 1.2 Casos e trabalho

Dois ângulos delimitam o efeito:

| Condição | Força | Trajetória inicial |
|---|---|---|
| $$\theta=0^\circ$$ ou $$180^\circ$$ | nula | retilínea |
| $$\theta=90^\circ$$ | máxima | curvada |

<!-- tikz:inicio fig-02-casos-angulares-da-forca-magnetica -->
![Carga com velocidade paralela e perpendicular ao campo mostrando força nula e máxima](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/forca-magnetica/fig-02-casos-angulares-da-forca-magnetica.png)
<!-- tikz:fim fig-02-casos-angulares-da-forca-magnetica -->

Como $$\vec{F}_m\perp\vec{v}$$, a força magnética não realiza trabalho: muda a direção da velocidade, não seu módulo.

📝 **Exemplo:**  
Para $$|q|=2{,}0\,\mu\mathrm{C}$$, $$v=3{,}0\times10^4\,\mathrm{m/s}$$, $$B=0{,}50\,\mathrm{T}$$ e $$\theta=90^\circ$$:

$$F_m=2{,}0\times10^{-6}\cdot3{,}0\times10^4\cdot0{,}50$$

$$F_m=3{,}0\times10^{-2}\,\mathrm{N}$$

> ⏸️ **Pare e Pense:**  
> Se a força magnética não realiza trabalho, o que ela pode alterar no vetor velocidade?

---

## 2. Força magnética sobre condutor

Em um motor, a corrente atravessa fios imersos em um campo e produz movimento.

### 2.1 Do movimento das cargas ao fio

A soma das forças sobre as cargas livres produz força no condutor:

$$\vec{F}=I\left(\vec{L}\times\vec{B}\right)$$

$$F=BIL\sin\theta$$

O vetor $$\vec{L}$$ tem o módulo do comprimento do trecho e o sentido da corrente; $$\theta$$ é o ângulo entre corrente e campo.

Na regra da mão direita, os dedos seguem a corrente e curvam-se para $$\vec{B}$$; o polegar aponta a força.

<!-- tikz:inicio fig-03-forca-sobre-condutor -->
![Fio com corrente imerso em campo uniforme e vetor força perpendicular](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/forca-magnetica/fig-03-forca-sobre-condutor.png)
<!-- tikz:fim fig-03-forca-sobre-condutor -->

📝 **Exemplo:**  
Um fio de $$0{,}20\,\mathrm{m}$$ conduz $$5{,}0\,\mathrm{A}$$ perpendicularmente a $$B=0{,}40\,\mathrm{T}$$.

$$F=0{,}40\cdot5{,}0\cdot0{,}20$$

$$F=0{,}40\,\mathrm{N}$$

### 2.2 Motores e alto-falantes

Numa espira, forças opostas em lados diferentes formam um **binário**, que produz rotação. Esse é o princípio do motor elétrico.

<!-- tikz:inicio fig-04-binario-na-espira -->
![Espira retangular com forças opostas em lados distintos produzindo rotação](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/forca-magnetica/fig-04-binario-na-espira.png)
<!-- tikz:fim fig-04-binario-na-espira -->

No alto-falante, a corrente variável na bobina altera a força magnética e movimenta o cone, produzindo som.

> ⚡ **Física no Dia a Dia:**  
> Ventiladores e carros elétricos convertem interação magnética em rotação controlada.

---

## 3. Movimento de cargas em campo magnético

Quando velocidade e campo são perpendiculares, a força magnética atua como resultante centrípeta.

### 3.1 Movimento circular e helicoidal

No campo uniforme, com $$\vec{v}\perp\vec{B}$$:

$$|q|vB=\frac{mv^2}{R}$$

$$R=\frac{mv}{|q|B}$$

O período da órbita é:

$$T=\frac{2\pi m}{|q|B}$$

O período independe do módulo da velocidade no modelo não relativístico. Se $$\vec{v}$$ também possui componente paralela ao campo, essa parte permanece uniforme e a trajetória torna-se helicoidal.

<!-- tikz:inicio fig-05-trajetorias-circular-e-helicoidal -->
![Comparação entre trajetória circular e helicoidal de cargas em campo uniforme](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/forca-magnetica/fig-05-trajetorias-circular-e-helicoidal.png)
<!-- tikz:fim fig-05-trajetorias-circular-e-helicoidal -->

### 3.2 Seleção e aceleração de partículas

Dois equipamentos exploram o raio da trajetória:

| Equipamento | Função |
|---|---|
| Cíclotron | campo elétrico aumenta a rapidez; campo magnético curva a trajetória |
| Espectrômetro de massa | separa íons conforme massa, carga e velocidade |

No cíclotron médico, prótons em espiral podem produzir radioisótopos usados em exames PET. A energia vem do campo elétrico entre as regiões de aceleração; o campo magnético apenas reorienta as partículas.

No espectrômetro, medir $$R$$ permite comparar a razão $$m/|q|$$ dos íons.

> 💡 **Você sabia?**  
> Cíclotrons médicos operam tipicamente com campos da ordem de 1,5 a 2 T.

---

# BL2_Capítulo 2 — Indução eletromagnética

> Por que um ímã cai lentamente em um tubo de cobre e a transmissão elétrica usa tensões de centenas de quilovolts?

---

## 1. Fluxo magnético

Uma espira girando em um campo muda a quantidade de linhas que atravessam sua área.

### 1.1 Campo através da superfície

O **fluxo magnético** mede a passagem do campo por uma superfície:

$$\Phi_B=\vec{B}\cdot\vec{A}=BA\cos\theta$$

Aqui, $$\Phi_B$$ é o fluxo magnético, em weber (Wb), e $$\theta$$ é o ângulo entre o campo e o vetor perpendicular à área.

A unidade relaciona campo e área:

$$1\,\mathrm{Wb}=1\,\mathrm{T\cdot m^2}$$

O fluxo é máximo para $$\theta=0^\circ$$ e nulo para $$\theta=90^\circ$$.

<!-- tikz:inicio fig-01-fluxo-e-orientacao-da-area -->
![Três orientações da superfície em campo uniforme com fluxos máximo, intermediário e nulo](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/inducao-eletromagnetica/fig-01-fluxo-e-orientacao-da-area.png)
<!-- tikz:fim fig-01-fluxo-e-orientacao-da-area -->

### 1.2 Como variar o fluxo

Três mudanças podem produzir variação:

- alterar a intensidade $$B$$;
- alterar a área $$A$$ atravessada pelo campo;
- girar a superfície e alterar $$\theta$$.

<!-- tikz:inicio fig-02-tres-modos-de-variar-o-fluxo -->
![Comparação entre variar campo, área e ângulo de uma espira](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/inducao-eletromagnetica/fig-02-tres-modos-de-variar-o-fluxo.png)
<!-- tikz:fim fig-02-tres-modos-de-variar-o-fluxo -->

📝 **Exemplo:**  
Uma espira de $$0{,}50\,\mathrm{m^2}$$ está em $$B=0{,}20\,\mathrm{T}$$, com $$\theta=60^\circ$$.

$$\Phi_B=BA\cos\theta$$

$$\Phi_B=0{,}20\cdot0{,}50\cdot0{,}50$$

$$\Phi_B=5{,}0\times10^{-2}\,\mathrm{Wb}$$

Fluxo não é quantidade de linhas materiais; é uma medida escalar da orientação e da intensidade do campo através da área.

> ⏸️ **Pare e Pense:**  
> Uma espira pode ter fluxo nulo mesmo estando em um campo magnético intenso?

---

## 2. Lei de Faraday e lei de Lenz

Mover um ímã perto de uma bobina pode gerar tensão sem contato elétrico entre os dois.

### 2.1 Variação de fluxo

Em 29 de agosto de 1831, **Michael Faraday** observou corrente momentânea em uma bobina quando o campo produzido em outra bobina variava.

Para uma espira, a fem induzida é:

$$\varepsilon=-\frac{\Delta\Phi_B}{\Delta t}$$

Aqui, $$\varepsilon$$ é a fem induzida, em volt (V). Uma variação mais rápida produz maior módulo de fem.

<!-- tikz:inicio fig-03-ima-em-movimento-e-corrente-induzida -->
![Ímã aproximando-se de bobina ligada a medidor com corrente induzida](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/inducao-eletromagnetica/fig-03-ima-em-movimento-e-corrente-induzida.png)
<!-- tikz:fim fig-03-ima-em-movimento-e-corrente-induzida -->

📝 **Exemplo:**  
O fluxo diminui de $$0{,}12\,\mathrm{Wb}$$ para $$0{,}02\,\mathrm{Wb}$$ em $$0{,}05\,\mathrm{s}$$.

$$\Delta\Phi_B=0{,}02-0{,}12$$

$$\Delta\Phi_B=-0{,}10\,\mathrm{Wb}$$

$$|\Delta\Phi_B|=0{,}10\,\mathrm{Wb}$$

$$|\varepsilon|=\frac{|\Delta\Phi_B|}{\Delta t}$$

$$|\varepsilon|=\frac{0{,}10}{0{,}05}$$

$$|\varepsilon|=2{,}0\,\mathrm{V}$$

### 2.2 Oposição de Lenz

O sinal negativo expressa a **Lei de Lenz**: a corrente induzida cria um campo que se opõe à variação do fluxo que a originou.

<!-- tikz:inicio fig-04-oposicao-de-lenz -->
![Bobina criando polos que se opõem à aproximação e ao afastamento do ímã](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/inducao-eletromagnetica/fig-04-oposicao-de-lenz.png)
<!-- tikz:fim fig-04-oposicao-de-lenz -->

Em 1834, **Heinrich Lenz** formulou essa orientação como consequência da conservação de energia. Num tubo de cobre, correntes induzidas se opõem ao movimento do ímã e retardam sua queda.

Entre 1861 e 1873, **James Clerk Maxwell** sintetizou o eletromagnetismo em quatro equações.

> 💡 **Você sabia?**  
> Sem a oposição de Lenz, a indução poderia reforçar indefinidamente a própria causa e violar a conservação de energia.

---

## 3. Geradores e transformadores

Usinas e carregadores sem fio convertem variações de fluxo em transferências controladas de energia.

### 3.1 Gerar e controlar movimento

Um **gerador** gira espiras em um campo. A rotação varia o fluxo e induz fem; cada unidade de Itaipu tem potência nominal de 700 MW.

<!-- tikz:inicio fig-05-gerador-por-rotacao-da-espira -->
![Espira girando entre polos magnéticos e produzindo variação periódica de fluxo](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/inducao-eletromagnetica/fig-05-gerador-por-rotacao-da-espira.png)
<!-- tikz:fim fig-05-gerador-por-rotacao-da-espira -->

Freios eletromagnéticos usam **correntes parasitas** para desacelerar sem contato mecânico direto.

### 3.2 Transformar tensão

No transformador ideal, duas bobinas compartilham um fluxo variável:

$$\frac{V_1}{V_2}=\frac{N_1}{N_2}$$

$$V_1I_1=V_2I_2$$

<!-- tikz:inicio fig-06-transformador-e-razao-de-espiras -->
![Núcleo ferromagnético com bobinas primária e secundária de números de espiras diferentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/3serie/inducao-eletromagnetica/fig-06-transformador-e-razao-de-espiras.png)
<!-- tikz:fim fig-06-transformador-e-razao-de-espiras -->

Os índices 1 e 2 identificam as bobinas, e $$N$$ indica o número de espiras.

Elevar a tensão reduz a corrente para a mesma potência e diminui as perdas:

$$P_d=I^2R$$

Nessa expressão, $$R$$ é a resistência da linha.

Por isso, linhas de transmissão operam em alta tensão; transformadores próximos ao consumo reduzem valores como 13,8 kV para 220/127 V.

Recarga Qi transfere energia por indução entre bobinas próximas. NFC usa acoplamento indutivo em 13,56 MHz para comunicação a curta distância.

> ⚡ **Física no Dia a Dia:**  
> Um transformador elevador aumenta a tensão e reduz a corrente sem criar potência no modelo ideal.
