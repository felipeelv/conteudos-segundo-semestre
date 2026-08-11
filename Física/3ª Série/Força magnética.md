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
