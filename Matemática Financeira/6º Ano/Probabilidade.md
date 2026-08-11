# BL2_Capítulo 1 — Probabilidade

> Na rifa da turma, 50 números foram vendidos e você comprou 5. Qual sua chance de ganhar — em fração, decimal e porcentagem? E qual a chance de sair o número 51?

---

## 1. Conceito e problemas

Um dado, duas moedas ou uma urna exigem primeiro a lista dos resultados possíveis.

### 1.1 Listar e contar

Para resultados com a mesma chance, usamos:

$$P(E) = \frac{n(E)}{n(\Omega)}$$

Nessa fórmula:

- $$n(E)$$ é a quantidade de resultados favoráveis;
- $$n(\Omega)$$ é a quantidade de resultados do espaço amostral.

Em 1654, **Pierre de Fermat** usou a enumeração de resultados em sua correspondência com Pascal sobre jogos de dados. O mesmo método organiza os exemplos a seguir.

**Um dado de seis faces**

Calcule as probabilidades de sair número par e múltiplo de 3.

**Resolução:**

- **Passo 1:** Listar o espaço amostral.

$$\Omega = \{1, 2, 3, 4, 5, 6\}$$

- **Passo 2:** Contar os resultados favoráveis.

$$P(\text{par}) = \frac{3}{6} = \frac{1}{2} = 0{,}5 = 50\%$$

$$P(\text{multiplo de 3}) = \frac{2}{6} = \frac{1}{3} \approx 0{,}3333 = 33{,}33\%$$

**Resposta:** um número par é mais provável, pois ocupa metade dos resultados; múltiplos de 3 ocupam um terço.

### 1.2 Mais de um objeto

Dois dados geram $$6 \cdot 6 = 36$$ pares ordenados.

**Soma igual a 7**

Os seis pares favoráveis são $$(1,6)$$, $$(2,5)$$, $$(3,4)$$, $$(4,3)$$, $$(5,2)$$ e $$(6,1)$$.

**Resolução:**

- **Passo 1:** Dividir os seis casos favoráveis pelos 36 possíveis.

$$P(E) = \frac{6}{36} = \frac{1}{6}$$

- **Passo 2:** Converter, com duas casas decimais na porcentagem.

$$\frac{1}{6} \approx 0{,}1667 = 16{,}67\%$$

**Resposta:** aproximadamente 16,67% dos pares possíveis produzem soma 7.

Para moedas, cada lançamento dobra o espaço amostral:

| Moedas | Resultados possíveis | Chance de todas serem cara |
|---:|---:|---:|
| 1 | 2 | $$\frac{1}{2} = 0{,}5 = 50\%$$ |
| 2 | 4 | $$\frac{1}{4} = 0{,}25 = 25\%$$ |
| 3 | 8 | $$\frac{1}{8} = 0{,}125 = 12{,}5\%$$ |

> 🔢 **Padrão:**
>
> Com $$n$$ moedas, o espaço amostral possui $$2^n$$ resultados quando cada moeda pode dar cara ou coroa.

---

## 2. Eventos certos e impossíveis

Num dado comum, sair um número de 1 a 6 é garantido; sair 7 não pode ocorrer.

### 2.1 Os extremos da escala

Um **evento certo** contém todo o espaço amostral:

$$P(E) = \frac{n(\Omega)}{n(\Omega)} = 1 = 100\%$$

Um **evento impossível** não possui resultado favorável:

$$P(E) = \frac{0}{n(\Omega)} = 0 = 0\%$$

Toda probabilidade fica na faixa:

$$0 \leq P(E) \leq 1$$

Os valores 0 e 1 são categorias exatas, não apenas eventos “pouco” ou “muito” prováveis.

### 2.2 Comparar probabilidades

**Quatro eventos no dado**

Compare sair 7, sair 6, sair número par e sair número de 1 a 6.

**Resolução:**

- **Passo 1:** Calcular cada probabilidade.

| Evento | Fração | Decimal | Porcentagem |
|---|---:|---:|---:|
| Sair 7 | $$\frac{0}{6}$$ | 0 | 0% |
| Sair 6 | $$\frac{1}{6}$$ | 0,1667 | 16,67% |
| Sair par | $$\frac{3}{6}$$ | 0,5000 | 50,00% |
| Sair de 1 a 6 | $$\frac{6}{6}$$ | 1 | 100% |

- **Passo 2:** Ordenar do menos ao mais provável.

$$0 < \frac{1}{6} < \frac{1}{2} < 1$$

- **Passo 3:** Comparar os eventos possíveis não certos.

$$\frac{\frac{1}{2}}{\frac{1}{6}} = 3$$

**Resposta:** sair número par é três vezes mais provável que sair 6; sair 7 é impossível e sair de 1 a 6 é certo.

> ⚠️ **Atenção:**
>
> Dizer “duas vezes mais provável” exige comparar as probabilidades, não apenas contar categorias.

---

## 3. Situações do cotidiano

Rifas, urnas e sorteios mudam de contexto, mas conservam o método de contar resultados.

### 3.1 Rifas e urnas

**Rifa da turma**

Numa rifa com 50 números, uma pessoa comprou 5.

**Resolução:**

- **Passo 1:** Calcular a chance de um dos cinco números ser sorteado.

$$P(E) = \frac{5}{50} = \frac{1}{10} = 0{,}1 = 10\%$$

- **Passo 2:** Verificar o número 51, que não pertence ao espaço amostral.

$$P(51) = \frac{0}{50} = 0 = 0\%$$

**Resposta:** a chance de ganhar é 10%; a chance de sair 51 é zero. Numa rifa de 100 números, cada número comprado corresponderia a 1%.

Uma urna com 5 bolas vermelhas, 3 azuis e 2 verdes possui dez resultados possíveis:

| Cor | Probabilidade | Leitura |
|---|---:|---|
| Vermelha | $$\frac{5}{10} = 0{,}5 = 50\%$$ | metade das bolas |
| Azul | $$\frac{3}{10} = 0{,}3 = 30\%$$ | três em cada dez |
| Verde | $$\frac{2}{10} = 0{,}2 = 20\%$$ | duas em cada dez |

### 3.2 Modelos e grandes números

Outras situações usam espaços amostrais simples:

- escolher um naipe entre quatro: $$\frac{1}{4} = 0{,}25 = 25\%$$;
- sortear uma pessoa entre 30: $$\frac{1}{30} \approx 0{,}0333 = 3{,}33\%$$;
- em um modelo que trata os meses como igualmente prováveis, nascer em um mês específico: $$\frac{1}{12} \approx 0{,}0833 = 8{,}33\%$$.

Na Mega-Sena, uma aposta simples corresponde a uma entre 50.063.860 combinações possíveis:

$$P(E) = \frac{1}{50\,063\,860} \approx 0{,}00000002$$

$$P(E) \approx 0{,}000002\%$$

Propagandas destacam ganhadores; o cálculo mostra que a chance individual permanece extremamente pequena.

> ⚠️ **Atenção:**
>
> Um resultado possível não é necessariamente um resultado provável.
