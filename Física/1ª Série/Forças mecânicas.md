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
![Bloco no piso e na rampa com forças normais perpendiculares a cada superfície](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/forcas-mecanicas/fig-01-normal-em-superficies-diferentes.png)
<!-- tikz:fim fig-01-normal-em-superficies-diferentes -->

### 1.3 Peso aparente

A balança não mede seu peso: mede a **normal** com que ela empurra seus pés.

| Situação | Normal | A balança |
|---|---|---|
| Subindo acelerado | $$N = m(g + a)$$ | marca mais |
| Descendo acelerado | $$N = m(g - a)$$ | marca menos |
| Queda livre ($$a = g$$) | $$N = 0$$ | marca zero |

<!-- tikz:inicio fig-02-peso-aparente-no-elevador -->
![Três diagramas do elevador acelerando para cima, para baixo e em queda livre](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/forcas-mecanicas/fig-02-peso-aparente-no-elevador.png)
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
![Corda sobre polia ideal com vetores de tração iguais nos dois trechos](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/forcas-mecanicas/fig-03-tracao-em-cabo-e-polia-ideais.png)
<!-- tikz:fim fig-03-tracao-em-cabo-e-polia-ideais -->

### 2.2 Sistemas de corpos ligados

Dois corpos unidos por fio inextensível têm a **mesma aceleração em módulo**. Esse é o vínculo que resolve o sistema.

Método: **uma equação por corpo**, pela 2ª Lei, com o sentido positivo no do movimento previsto.

📝 **Bloco A (3 kg) na mesa lisa, ligado por polia ao bloco B (2 kg) pendurado**

$$T = m_A \cdot a \qquad m_B \cdot g - T = m_B \cdot a$$

Somando:

$$20 = 5a \quad \Rightarrow \quad a = 4\,\mathrm{m/s^2}$$

$$T = 3 \cdot 4 = 12\,\mathrm{N}$$

<!-- tikz:inicio fig-04-corpos-ligados-e-mesma-aceleracao -->
![Bloco na mesa e bloco pendente ligados por corda com acelerações de mesmo módulo](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/forcas-mecanicas/fig-04-corpos-ligados-e-mesma-aceleracao.png)
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

Todo modelo físico tem domínio de validade, e conhecer esse limite faz parte de usá-lo.

<!-- tikz:inicio fig-05-forca-restauradora-e-limite-elastico -->
![Mola comprimida, alongada e deformada além do limite com respostas distintas](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/1serie/forcas-mecanicas/fig-05-forca-restauradora-e-limite-elastico.png)
<!-- tikz:fim fig-05-forca-restauradora-e-limite-elastico -->
