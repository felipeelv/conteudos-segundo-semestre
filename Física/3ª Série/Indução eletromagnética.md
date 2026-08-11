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
