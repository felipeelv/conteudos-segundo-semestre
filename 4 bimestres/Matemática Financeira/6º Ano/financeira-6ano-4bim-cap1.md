# Capítulo 1 — Medidas de tendência central

> Numa rua vivem 10 famílias com renda de R$ 3.000 e 1 família com renda de R$ 100.000. A média é R$ 11.818 — um valor que ninguém ganha. Qual número descreve melhor a “renda típica” da rua?

---

## 1. Média aritmética, moda e mediana

As notas hipotéticas 5, 7, 7, 9 e 12 produzem três resumos diferentes do mesmo conjunto.

### 1.1 Média e moda

A **média aritmética** reparte igualmente a soma dos valores:

$$\bar{x}=\frac{5+7+7+9+12}{5}$$

$$\bar{x}=\frac{40}{5}$$

$$\bar{x}=8$$

A **moda** é o valor mais frequente. Nesse conjunto, $$\mathrm{Mo}=7$$.

Os conjuntos podem ser classificados pela quantidade de modas:

| Frequência máxima | Classificação | Exemplo |
|---|---|---|
| um valor | unimodal | 2, 3, 3, 5 |
| dois valores | bimodal | 2, 2, 4, 4 |
| nenhum valor repetido | amodal | 2, 3, 4, 5 |

Moda também resume dados qualitativos. Se azul foi escolhida cinco vezes, verde três e amarela duas, azul é a moda; não existe “cor média”.

Uma tabela de frequência evita repetir cada valor. Suponha cinco notas 8 e três notas 5:

$$\bar{x}=\frac{5\cdot8+3\cdot5}{8}$$

$$\bar{x}=\frac{55}{8}=6{,}875$$

**Resposta:** a média da turma hipotética é 6,875; cada nota entrou na soma tantas vezes quanto sua frequência.

### 1.2 Mediana

A **mediana** divide os dados ordenados em duas metades. Ordenar é indispensável.

Com quantidade ímpar, usa-se o valor central:

$$3,\ 5,\ \mathbf{7},\ 8,\ 20$$

$$\mathrm{Md}=7$$

Com quantidade par, calcula-se a média dos dois centrais:

$$3,\ \mathbf{5},\ \mathbf{7},\ 20$$

$$\mathrm{Md}=\frac{5+7}{2}=6$$

Trocar 20 por 200 não altera essa mediana. O valor extremo muda muito a média, mas permanece na mesma ponta do rol.

> 🔢 **Padrão:**  
> A mediana só pode ser localizada depois que todos os valores estão em ordem.

---

## 2. Comparação das medidas de tendência central

Escolher um resumo significa decidir qual característica do conjunto precisa ser preservada.

### 2.1 Qual medida usar

As três medidas respondem a perguntas diferentes:

| Situação | Medida mais informativa | Motivo |
|---|---|---|
| categoria mais escolhida | moda | identifica a maior frequência |
| valores equilibrados, sem extremos | média | usa todos os valores |
| valores com extremos | mediana | resiste ao valor muito alto ou baixo |

Nenhuma medida conta a história inteira:

- a média pode ser puxada por um extremo;
- a moda não informa a distribuição da minoria;
- a mediana não mostra a intensidade dos extremos.

Em conjuntos aproximadamente simétricos, média, moda e mediana tendem a ficar próximas. Quando se afastam, essa diferença revela desigualdade ou concentração.

### 2.2 A rua com onze famílias

Na situação da abertura, dez rendas valem R$ 3.000,00 e uma vale R$ 100.000,00.

**Renda média e mediana**

**Resolução:**

- **Passo 1:** Calcular a renda média.

$$\bar{x}=\frac{10\cdot3000+100000}{11}$$

$$\bar{x}=\frac{130000}{11}$$

$$\bar{x}\approx\mathrm{R\$}\,11\,818{,}18$$

- **Passo 2:** Ordenar os onze valores. A sexta posição é central.

$$3000,\ 3000,\ 3000,\ 3000,\ 3000,\ \mathbf{3000},\ 3000,\ 3000,\ 3000,\ 3000,\ 100000$$

$$\mathrm{Md}=\mathrm{R\$}\,3\,000{,}00$$

**Resposta:** a mediana descreve melhor a renda típica da rua; a média de R$ 11.818,18 é correta, mas foi elevada por uma única renda extrema.

Pesquisas de renda publicam média e mediana justamente porque a comparação revela o efeito das rendas mais altas. O estatístico inglês **Francis Galton** propôs, em 1882, o uso moderno do termo *mediana*. Ele também promoveu a eugenia, ideologia discriminatória hoje rejeitada; sua contribuição técnica não legitima essa posição.

> ⚠️ **Atenção:**  
> Um resumo estatístico deve ser escolhido pela pergunta e conferido junto da distribuição dos dados.
