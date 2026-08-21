# Capítulo 1 — Eletroquímica: pilhas

> O que conecta a ferrugem de um prego, a queima do metano e o funcionamento de uma pilha — e como dois pedaços de metal mergulhados em solução conseguem acender uma lâmpada?

---

## 1. Oxirredução: oxidação, redução e NOX

Ferrugem, combustão e pilhas envolvem transferência de elétrons entre espécies químicas.

### 1.1 Duas transformações simultâneas

**Oxidação é a perda de elétrons, acompanhada pelo aumento do número de oxidação (NOX); redução é o ganho de elétrons e a diminuição do NOX.** Como os elétrons perdidos por uma espécie são recebidos por outra, os dois processos sempre ocorrem juntos.

Na transformação do zinco em íon zinco, o NOX aumenta de 0 para +2:

$$\mathrm{Zn(s)} \rightarrow \mathrm{Zn^{2+}(aq)} + 2e^-$$

Já o cobre sofre redução quando seu íon ganha elétrons:

$$\mathrm{Cu^{2+}(aq)} + 2e^- \rightarrow \mathrm{Cu(s)}$$

### 1.2 Regras para determinar o NOX

O elemento em uma substância simples tem NOX zero. O flúor vale −1; o hidrogênio geralmente vale +1, mas vale −1 em hidretos metálicos; o oxigênio geralmente vale −2, mas vale −1 em peróxidos. A soma dos NOX é zero em uma substância neutra e igual à carga em um íon.

No permanganato, $\mathrm{MnO_4^-}$:

$$x+4(-2)=-1 \quad\Rightarrow\quad x=+7$$

No dicromato, $\mathrm{Cr_2O_7^{2-}}$:

$$2x+7(-2)=-2 \quad\Rightarrow\quad x=+6$$

Esses valores permitem reconhecer qual átomo foi oxidado ou reduzido ao comparar reagentes e produtos.

---

## 2. Balanceamento redox e agentes

Uma equação de oxirredução deve conservar simultaneamente átomos, carga elétrica e elétrons transferidos.

### 2.1 Agente oxidante e agente redutor

**Agente oxidante é a espécie que recebe elétrons e sofre redução; agente redutor é a espécie que doa elétrons e sofre oxidação.** Assim, o agente oxidante provoca a oxidação da outra espécie, enquanto o agente redutor provoca sua redução.

Na reação entre zinco e cobre(II), o Zn é o agente redutor e $\mathrm{Cu^{2+}}$ é o agente oxidante:

$$\mathrm{Zn(s)}+\mathrm{Cu^{2+}(aq)}\rightarrow\mathrm{Zn^{2+}(aq)}+\mathrm{Cu(s)}$$

### 2.2 Método das semirreações

O balanceamento separa oxidação e redução, equilibra os átomos e a carga de cada parte, iguala a quantidade de elétrons e soma as semirreações. Em meio ácido, permanganato oxida ferro(II):

$$\mathrm{Fe^{2+}}\rightarrow\mathrm{Fe^{3+}}+e^-$$

$$\mathrm{MnO_4^-}+8\mathrm{H^+}+5e^-\rightarrow\mathrm{Mn^{2+}}+4\mathrm{H_2O}$$

Multiplicando a primeira por 5 e somando:

$$\mathrm{MnO_4^-}+5\mathrm{Fe^{2+}}+8\mathrm{H^+}\rightarrow\mathrm{Mn^{2+}}+5\mathrm{Fe^{3+}}+4\mathrm{H_2O}$$

O número de elétrons não aparece na equação global porque os elétrons cedidos pelo Fe²⁺ são totalmente recebidos pelo permanganato. O $\mathrm{MnO_4^-}$ é o agente oxidante; o $\mathrm{Fe^{2+}}$, o agente redutor.

---

## 3. Pilhas e células galvânicas

Uma pilha galvânica converte a energia de uma reação redox espontânea em corrente elétrica.

### 3.1 Da pilha voltaica à célula de Daniell

Em 1800, **Alessandro Volta** construiu a primeira fonte contínua de corrente ao empilhar discos de zinco e cobre separados por material úmido. Em 1836, John Daniell desenvolveu uma célula mais estável, com duas semicélulas.

Na pilha de Daniell, o zinco oxida no **ânodo**, polo negativo:

$$\mathrm{Zn(s)}\rightarrow\mathrm{Zn^{2+}(aq)}+2e^-$$

Os elétrons percorrem o circuito externo até o **cátodo**, polo positivo, onde ocorre redução:

$$\mathrm{Cu^{2+}(aq)}+2e^-\rightarrow\mathrm{Cu(s)}$$

### 3.2 Circuito completo e notação

A reação global é:

$$\mathrm{Zn(s)}+\mathrm{Cu^{2+}(aq)}\rightarrow\mathrm{Zn^{2+}(aq)}+\mathrm{Cu(s)}$$

Enquanto elétrons circulam no fio, uma **ponte salina** permite o deslocamento de íons e evita o acúmulo de cargas nas soluções: ânions migram em direção ao ânodo e cátions, ao cátodo. Sem essa ligação interna, a corrente logo cessaria.

A notação convencional registra as fases e a ponte salina:

$$\mathrm{Zn(s)|Zn^{2+}(aq)||Cu^{2+}(aq)|Cu(s)}$$

A barra simples indica separação de fases; a barra dupla representa a ponte salina. Ânodo fica à esquerda e cátodo à direita.

---

## 4. Potencial de eletrodo, fem e espontaneidade

A voltagem de uma pilha depende da tendência relativa de suas semicélulas a sofrer redução.

### 4.1 Potenciais padrão e força eletromotriz

**Potencial padrão de redução, E°, mede a tendência de uma espécie receber elétrons em condições padrão.** Os valores são comparados ao eletrodo padrão de hidrogênio, definido como 0,00 V. Quanto maior E°, maior a tendência de redução.

Para a pilha de Daniell:

| Semirreação de redução | E° |
|---|---:|
| $\mathrm{Cu^{2+}+2e^-\rightarrow Cu}$ | +0,34 V |
| $\mathrm{Zn^{2+}+2e^-\rightarrow Zn}$ | −0,76 V |

$$E^\circ_{\mathrm{pilha}}=E^\circ_{\mathrm{cátodo}}-E^\circ_{\mathrm{ânodo}}$$

$$E^\circ_{\mathrm{pilha}}=0{,}34-(-0{,}76)=1{,}10\ \mathrm{V}$$

O resultado positivo indica reação espontânea no sentido escrito.

### 4.2 Concentração e pilhas comerciais

Fora das condições padrão, a concentração dos íons modifica a tensão. A equação de Nernst, introduzida por Walther Nernst em 1889, relaciona o potencial ao quociente da reação: consumir reagentes ou acumular produtos tende a reduzir a tensão durante a descarga.

O mesmo princípio redox aparece em pilhas secas e alcalinas, baterias chumbo-ácido e baterias de íons de lítio. Materiais e reações variam, mas todas separam oxidação e redução para dirigir elétrons pelo circuito externo. Pilhas recarregáveis recebem energia elétrica para reverter parcialmente as transformações ocorridas na descarga.

