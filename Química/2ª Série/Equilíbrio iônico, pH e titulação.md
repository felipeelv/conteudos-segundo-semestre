# BL2_Capítulo 1 — Equilíbrio iônico, pH e titulação

> Como as concentrações de H₃O⁺ e OH⁻ determinam o pH e permitem medir a concentração desconhecida de uma solução?

---

## 1. Equilíbrio iônico da água

Mesmo a água pura contém pequenas concentrações de íons hidrônio e hidróxido.

### 1.1 Autoionização e Kw

**Autoionização é a transferência de próton entre duas moléculas de água.**

$$2\mathrm{H_2O(l)} \rightleftharpoons \mathrm{H_3O^{+}(aq)} + \mathrm{OH^{-}(aq)}$$

A expressão completa de Kc inclui a água, mas sua concentração praticamente constante é incorporada ao **produto iônico da água**:

$$K_{\mathrm{w}}=[\mathrm{H_3O^{+}}][\mathrm{OH^{-}}]$$

A 25 °C:

$$K_{\mathrm{w}}=1{,}0\times10^{-14}$$

Na água pura, as concentrações dos dois íons são iguais:

$$[\mathrm{H_3O^{+}}]=[\mathrm{OH^{-}}]=1{,}0\times10^{-7}\,\mathrm{mol/L}$$

### 1.2 Acidez, basicidade e temperatura

A classificação compara as concentrações:

| Meio | Relação |
|---|---|
| ácido | [H₃O⁺] > [OH⁻] |
| neutro | [H₃O⁺] = [OH⁻] |
| básico | [H₃O⁺] < [OH⁻] |

Adicionar ácido aumenta [H₃O⁺]; o equilíbrio reduz [OH⁻] para conservar Kw. Uma base produz o efeito inverso.

Kw varia com a temperatura. Portanto:

- **neutralidade** sempre significa [H₃O⁺] = [OH⁻];
- **pH 7** representa neutralidade apenas quando Kw = 10⁻¹⁴, aproximadamente a 25 °C;
- aquecer água pura pode alterar seu pH sem torná-la ácida.

---

## 2. pH, pOH e escala logarítmica

Uma escala logarítmica transforma grandes variações de concentração em números compactos.

### 2.1 Definições

**pH é o logaritmo negativo da atividade de H₃O⁺, aproximada pela concentração em soluções diluídas.**

No tratamento escolar:

$$\mathrm{pH}=-\log[\mathrm{H_3O^{+}}]$$

$$\mathrm{pOH}=-\log[\mathrm{OH^{-}}]$$

Como $K_{\mathrm{w}}=10^{-14}$ a 25 °C:

$$\mathrm{pH}+\mathrm{pOH}=14$$

Uma unidade de pH representa fator 10. Uma solução de pH 3 tem [H₃O⁺] dez vezes maior que outra de pH 4 e cem vezes maior que outra de pH 5.

<!-- tikz:inicio fig-01-escala-logaritmica-ph -->
![Escala de pH de zero a quatorze mostrando que cada unidade corresponde a uma variação de dez vezes na concentração de hidrônio](https://raw.githubusercontent.com/felipeelv/imagens-tikz/7f6fa768495b0b5faa2a9b3de65baea9690dde62/quimica/2serie/3bim-cap2-ph-titulacao/fig-01-escala-logaritmica-ph.png)
<!-- tikz:fim fig-01-escala-logaritmica-ph -->

### 2.2 Leitura da escala

Valores aproximados ajudam a interpretar a ordem de grandeza:

| Material | pH aproximado |
|---|---:|
| suco de limão | 2 |
| café | 5 |
| água pura a 25 °C | 7 |
| solução de bicarbonato | 8 |
| água sanitária | 11–13 |

Composição, concentração e temperatura alteram os valores; a tabela não substitui uma medida.

Para inverter a relação:

$$[\mathrm{H_3O^{+}}]=10^{-\mathrm{pH}}$$

Assim, pH 5 corresponde a [H₃O⁺] = 1 × 10⁻⁵ mol/L.

---

## 3. Ácidos e bases fortes: cálculos

Eletrólitos fortes são tratados como totalmente dissociados nas concentrações escolares usuais.

### 3.1 Ácido forte

**Ácido forte apresenta ionização praticamente completa em água.**

Para HCl 0,010 mol/L:

$$\mathrm{HCl} + \mathrm{H_2O} \rightarrow \mathrm{H_3O^{+}} + \mathrm{Cl^{-}}$$

$$[\mathrm{H_3O^{+}}]=1{,}0\times10^{-2}\,\mathrm{mol/L}$$

$$\mathrm{pH}=-\log(10^{-2})=2{,}00$$

A concentração e a estequiometria da ionização precisam ser lidas antes do logaritmo. Em ácidos com mais de um hidrogênio ionizável, as etapas não são necessariamente equivalentes.

### 3.2 Base forte

**Base forte se dissocia praticamente por completo e fornece OH⁻ à solução.**

Para Ca(OH)₂ 0,0050 mol/L, cada unidade fornece dois OH⁻:

$$\mathrm{Ca(OH)_2} \rightarrow \mathrm{Ca^{2+}} + 2\mathrm{OH^{-}}$$

$$[\mathrm{OH^{-}}]=2(0{,}0050)=0{,}010\,\mathrm{mol/L}$$

$$\mathrm{pOH}=2{,}00$$

$$\mathrm{pH}=14-2{,}00=12{,}00$$

O resultado usa 25 °C. O mesmo roteiro vale para dados em notação científica:

1. determine [H₃O⁺] ou [OH⁻] pela equação;
2. calcule pH ou pOH;
3. use pH + pOH = 14 somente na temperatura indicada.

Em soluções extremamente diluídas, a autoionização da água deixa de ser desprezível.

---

## 4. Ácidos e bases fracos: Ka e Kb

Eletrólitos fracos estabelecem equilíbrio entre espécies ionizadas e não ionizadas.

### 4.1 Constantes de ionização

**Ka mede a extensão da ionização de um ácido fraco em determinada temperatura.**

$$\mathrm{HA(aq)} + \mathrm{H_2O(l)} \rightleftharpoons \mathrm{H_3O^{+}(aq)} + \mathrm{A^{-}(aq)}$$

$$K_{\mathrm{a}}=\frac{[\mathrm{H_3O^{+}}][\mathrm{A^{-}}]}{[\mathrm{HA}]}$$

Para uma base fraca:

$$\mathrm{B(aq)} + \mathrm{H_2O(l)} \rightleftharpoons \mathrm{BH^{+}(aq)} + \mathrm{OH^{-}(aq)}$$

$$K_{\mathrm{b}}=\frac{[\mathrm{BH^{+}}][\mathrm{OH^{-}}]}{[\mathrm{B}]}$$

Maior Ka indica maior ionização ácida nas mesmas condições; maior Kb indica maior ionização básica. Em 1923, Johannes Brønsted e Thomas Lowry definiram ácido como doador e base como receptor de prótons.

### 4.2 Ácido acético

Para CH₃COOH 0,10 mol/L, com Ka = 1,8 × 10⁻⁵:

$$K_{\mathrm{a}}\approx\frac{x^2}{0{,}10}$$

$$x\approx\sqrt{1{,}8\times10^{-6}}=1{,}34\times10^{-3}\,\mathrm{mol/L}$$

$$\mathrm{pH}=-\log(1{,}34\times10^{-3})\approx2{,}87$$

A aproximação considera $0{,}10-x\approx0{,}10$. A ionização calculada é:

$$\frac{1{,}34\times10^{-3}}{0{,}10}\times100\%=1{,}34\%$$

Como o valor é inferior a 5%, a aproximação é adequada.

---

## 5. Indicadores e titulação ácido-base

A mudança de cor de um indicador pode localizar uma região específica da curva de pH.

### 5.1 Viragem e equivalência

**Indicador ácido-base é uma substância cuja cor depende do pH do meio.**

| Indicador | Faixa de viragem aproximada | Mudança |
|---|---:|---|
| alaranjado de metila | 3,1–4,4 | vermelho → amarelo |
| fenolftaleína | 8,2–10,0 | incolor → rosa |

O **ponto de equivalência** é definido pela proporção estequiométrica da reação. O **ponto de viragem** é a mudança observável do indicador; ele deve ocorrer dentro da região íngreme da curva.

<!-- tikz:inicio fig-02-curva-titulacao-forte-forte -->
![Curva de titulação de ácido forte por base forte com região de salto, ponto de equivalência em pH sete e faixa de viragem indicada](https://raw.githubusercontent.com/felipeelv/imagens-tikz/7f6fa768495b0b5faa2a9b3de65baea9690dde62/quimica/2serie/3bim-cap2-ph-titulacao/fig-02-curva-titulacao-forte-forte.png)
<!-- tikz:fim fig-02-curva-titulacao-forte-forte -->

### 5.2 Concentração por titulação

Numa reação 1:1:

$$\mathrm{HCl} + \mathrm{NaOH} \rightarrow \mathrm{NaCl} + \mathrm{H_2O}$$

$$C_{\mathrm{a}}V_{\mathrm{a}}=C_{\mathrm{b}}V_{\mathrm{b}}$$

Uma amostra de 25,0 mL de HCl atinge equivalência com 20,0 mL de NaOH 0,100 mol/L:

$$C_{\mathrm{a}}=\frac{0{,}100\times20{,}0}{25{,}0}$$

$$C_{\mathrm{a}}=0{,}0800\,\mathrm{mol/L}$$

Para outras proporções, usa-se a equação balanceada. Na neutralização de H₂SO₄ por NaOH, por exemplo, 1 mol do ácido reage com 2 mol da base; igualar diretamente as quantidades de matéria seria incorreto.

---

## 6. Hidrólise salina

Íons provenientes de um sal podem transferir prótons para a água ou recebê-los dela.

### 6.1 Origem dos íons

**Hidrólise salina é a reação de um íon do sal com a água, capaz de alterar o pH.**

| Sal | Íon que reage | Efeito predominante |
|---|---|---|
| NaCl | nenhum de modo apreciável | neutro a 25 °C |
| NH₄Cl | NH₄⁺ | ácido |
| NaHCO₃ | HCO₃⁻ | básico nas condições usuais |

No NH₄Cl, o cátion doa próton:

$$\mathrm{NH_4^{+}(aq)} + \mathrm{H_2O(l)} \rightleftharpoons \mathrm{NH_3(aq)} + \mathrm{H_3O^{+}(aq)}$$

No bicarbonato de sódio, predomina a formação de OH⁻:

$$\mathrm{HCO_3^{-}(aq)} + \mathrm{H_2O(l)} \rightleftharpoons \mathrm{H_2CO_3(aq)} + \mathrm{OH^{-}(aq)}$$

O HCO₃⁻ é **anfiprótico**: pode doar ou receber próton. O efeito final depende das constantes dos dois processos.

### 6.2 Regra qualitativa

A força do ácido e da base de origem orienta a previsão:

- ácido forte + base forte → efeito de hidrólise desprezível;
- ácido forte + base fraca → cátion ácido;
- ácido fraco + base forte → ânion básico;
- ácido fraco + base fraca → é preciso comparar Ka e Kb.

Essas regras indicam o caráter da solução, mas não fornecem o pH numérico sem dados de equilíbrio.
