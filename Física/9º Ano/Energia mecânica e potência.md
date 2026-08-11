# BL2_Capítulo 1 — Energia mecânica e potência

> No balanço, a criança ganha velocidade ao descer e para por um instante no alto. A energia some ou muda de forma?

---

## 1. Energia cinética

Um carrinho mais rápido causa um impacto maior porque o movimento está associado à energia.

### 1.1 Massa e velocidade

**Energia cinética** — energia associada ao movimento de um corpo.

$$E_c = \frac{m \cdot v^2}{2}$$

Aqui, $$E_c$$ é a energia cinética, em joule (J).

A energia cresce com o quadrado da velocidade. Se a velocidade dobra, a energia cinética fica quatro vezes maior.

<!-- tikz:inicio fig-01-energia-cinetica-e-velocidade -->
![Gráfico qualitativo parabólico da energia cinética em função da velocidade com pontos v e 2v](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/9ano/energia-mecanica-e-potencia/fig-01-energia-cinetica-e-velocidade.png)
<!-- tikz:fim fig-01-energia-cinetica-e-velocidade -->

📝 **Exemplo:**  
Um corpo de $$2\,\mathrm{kg}$$ move-se a $$3\,\mathrm{m/s}$$.

Dados: $$m = 2\,\mathrm{kg}$$ e $$v = 3\,\mathrm{m/s}$$

$$E_c = \frac{m \cdot v^2}{2}$$

$$E_c = \frac{2 \cdot 3^2}{2}$$

$$E_c = 9\,\mathrm{J}$$

### 1.2 Trabalho e variação da energia

O trabalho da força resultante altera a energia cinética:

$$W_R = \Delta E_c$$

Em 1807, **Thomas Young** empregou “energia” no sentido moderno de capacidade para realizar trabalho.

> ⏸️ **Pare e Pense:**  
> Por que aumentar a velocidade interfere mais na energia cinética do que aumentar igualmente a massa?

---

## 2. Energia potencial gravitacional

Um livro colocado em uma prateleira pode cair e ganhar velocidade devido à sua posição.

### 2.1 Energia de posição

**Energia potencial gravitacional** — energia associada à altura de um corpo em um campo gravitacional.

Perto da superfície da Terra, ela é calculada por:

$$E_{pg} = m \cdot g \cdot h$$

📝 **Exemplo:**  
Uma mochila de $$2\,\mathrm{kg}$$ está em uma prateleira a $$5\,\mathrm{m}$$ do piso. Adote $$g=10\,\mathrm{m/s^2}$$.

$$E_{pg} = m \cdot g \cdot h$$

$$E_{pg} = 2 \cdot 10 \cdot 5$$

$$E_{pg} = 100\,\mathrm{J}$$

### 2.2 O nível zero

O valor de $$E_{pg}$$ depende do nível definido como $$h=0$$. Escolher o piso ou o térreo muda os valores, mas não a variação de energia entre duas alturas.

<!-- tikz:inicio fig-02-nivel-de-referencia-da-energia -->
![Mesmo corpo e duas escolhas de nível zero mostrando energias diferentes e variação igual](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/9ano/energia-mecanica-e-potencia/fig-02-nivel-de-referencia-da-energia.png)
<!-- tikz:fim fig-02-nivel-de-referencia-da-energia -->

Em 1853, **William Rankine** criou o termo “energia potencial” para descrever energia armazenada pela configuração de um sistema.

> ⚡ **Física no Dia a Dia:**  
> Em uma queda, diminuir a altura permite que a energia potencial gravitacional se transforme em movimento.

---

## 3. Energia potencial elástica

Uma mola comprimida pode lançar um objeto quando recupera seu comprimento.

### 3.1 Força elástica

No modelo de mola ideal, a **Lei de Hooke** relaciona força e deformação:

$$F_{el} = k \cdot x$$

Aqui, $$k$$ é a constante elástica, em newton por metro (N/m).

Maior valor de $$k$$ indica uma mola mais rígida. A relação vale enquanto a mola retorna à forma original.

### 3.2 Energia armazenada

A deformação armazena energia potencial elástica:

$$E_{pe} = \frac{k \cdot x^2}{2}$$

📝 **Exemplo:**  
Uma mola de $$k=200\,\mathrm{N/m}$$ é comprimida $$0{,}10\,\mathrm{m}$$.

$$E_{pe} = \frac{k \cdot x^2}{2}$$

$$E_{pe} = \frac{200 \cdot 0{,}10^2}{2}$$

$$E_{pe} = 1\,\mathrm{J}$$

Molas, elásticos e trampolins transformam essa energia em movimento ao recuperar sua forma.

<!-- tikz:inicio fig-03-mola-deformada-e-energia -->
![Mola comprimida com força restauradora e gráfico da energia potencial elástica pela deformação](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/9ano/energia-mecanica-e-potencia/fig-03-mola-deformada-e-energia.png)
<!-- tikz:fim fig-03-mola-deformada-e-energia -->

> ⏸️ **Pare e Pense:**  
> Por que dobrar a deformação torna a energia elástica quatro vezes maior?

---

## 4. Conservação da energia mecânica

No balanço ideal, altura e velocidade mudam, mas a energia mecânica permanece.

### 4.1 Soma das energias

**Energia mecânica** — soma das energias cinética e potencial de um sistema.

$$E_m = E_c + E_p$$

Em um **sistema conservativo**, sem atrito, a energia mecânica permanece constante:

$$E_{m,i} = E_{m,f}$$

Os índices $$i$$ e $$f$$ indicam os estados inicial e final.

No balanço ideal, a transformação ocorre assim:

| Posição | Energia cinética | Energia potencial |
|---|---|---|
| Ponto mais alto | mínima | máxima |
| Ponto mais baixo | máxima | mínima |

<!-- tikz:inicio fig-04-transformacao-no-balanco -->
![Balanço em três posições com energia potencial máxima no alto e cinética máxima embaixo](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/9ano/energia-mecanica-e-potencia/fig-04-transformacao-no-balanco.png)
<!-- tikz:fim fig-04-transformacao-no-balanco -->

### 4.2 Trabalho, calor e conservação

Em 1842, **Julius von Mayer** propôs a equivalência entre trabalho e calor. Em 1845, **James Prescott Joule** confirmou essa relação com pás que agitavam água e elevavam sua temperatura.

O resultado mostrou que a energia não desaparece: ela é transferida ou transformada. A equivalência medida foi aproximadamente:

$$1\,\mathrm{cal} = 4{,}18\,\mathrm{J}$$

A unidade joule homenageia esse trabalho.

> 💡 **Você sabia?**  
> O movimento das pás no experimento de Joule aumentava a temperatura da água sem criar energia.

---

## 5. Aplicações da conservação de energia

Uma montanha-russa ideal desce, ganha velocidade e usa esse movimento para subir novamente.

### 5.1 Estado inicial e final

Em sistemas ideais, pêndulos, quedas e montanhas-russas obedecem a:

$$E_{c,i} + E_{p,i} = E_{c,f} + E_{p,f}$$

📝 **Exemplo:**  
Um carrinho parte do repouso a $$5\,\mathrm{m}$$ de altura e chega ao nível $$h=0$$. Adote $$g=10\,\mathrm{m/s^2}$$ e despreze o atrito.

$$mgh = \frac{m \cdot v^2}{2}$$

$$10 \cdot 5 = \frac{v^2}{2}$$

$$50 = \frac{v^2}{2}$$

$$100 = v^2$$

$$v = 10\,\mathrm{m/s}$$

A massa aparece nos dois lados e não altera o resultado nesse modelo.

### 5.2 Forças dissipativas

Em uma montanha-russa real, atrito e resistência do ar transformam parte da energia mecânica em energia térmica e som.

Duas consequências distinguem o sistema real:

- a energia mecânica diminui;
- a energia total continua conservada quando todas as formas são consideradas.

Por isso, o carrinho não retorna sozinho à altura inicial. A energia não foi perdida; apenas mudou para formas menos úteis ao movimento.

<!-- tikz:inicio fig-05-montanha-russa-ideal-e-real -->
![Comparação entre trilha ideal que recupera a altura e trilha real com altura final menor](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/9ano/energia-mecanica-e-potencia/fig-05-montanha-russa-ideal-e-real.png)
<!-- tikz:fim fig-05-montanha-russa-ideal-e-real -->

> ⚡ **Física no Dia a Dia:**  
> Freios aquecem porque transformam energia cinética em energia térmica.

---

## 6. Potência

Duas máquinas podem realizar o mesmo trabalho, mas a mais rápida desenvolve maior potência.

### 6.1 Trabalho por tempo

**Potência** — taxa de realização de trabalho ou transferência de energia.

$$P = \frac{W}{\Delta t}$$

Aqui, $$P$$ é a potência, em watt (W).

Um watt equivale a um joule por segundo. Quando força e velocidade têm a mesma direção, também vale:

$$P = F \cdot v$$

<!-- tikz:inicio fig-06-mesmo-trabalho-potencias-diferentes -->
![Duas máquinas realizando o mesmo trabalho em tempos diferentes e produzindo potências diferentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/fisica/9ano/energia-mecanica-e-potencia/fig-06-mesmo-trabalho-potencias-diferentes.png)
<!-- tikz:fim fig-06-mesmo-trabalho-potencias-diferentes -->

### 6.2 Escalas e rendimento

Algumas potências mostram diferentes escalas:

| Sistema | Potência aproximada |
|---|---:|
| Chuveiro | 5.500 W |
| Carro popular | 70 kW |
| Usina de Itaipu | 14.000 MW |

O rendimento compara potência útil e total:

$$\eta = \frac{P_u}{P_t}$$

O rendimento $$\eta$$ não tem unidade; $$P_u$$ é a potência útil e $$P_t$$, a potência total. **James Watt** aperfeiçoou máquinas a vapor; a unidade de potência recebeu seu sobrenome.

> 📐 **Fazendo as Contas:**  
> Transferir 600 J em 3 s corresponde a uma potência de 200 W.
