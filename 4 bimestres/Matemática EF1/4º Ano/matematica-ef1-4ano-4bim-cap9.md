# Capítulo 9 — Contagem de possibilidades

> Como contar combinações sem repetir nem esquecer nenhuma?

---

## 1. Combinar duas coleções

Sobre a cama há três camisetas — azul, branca e verde — e duas bermudas — jeans e preta.

```text
camisetas: A, B, V
bermudas:  J, P
```

### 1.1 Um elemento de cada coleção

Cada roupa completa usa uma camiseta e uma bermuda. Uma lista organizada fixa a camiseta e troca as bermudas antes de passar à próxima.

- A com J; A com P.
- B com J; B com P.
- V com J; V com P.

Assim, nenhuma peça da mesma coleção ocupa os dois lugares.

### 1.2 Conferir a lista

**Exemplo resolvido — Roupas completas**

```text
AJ  AP
BJ  BP
VJ  VP
```

$$
\begin{aligned}
2+2+2&=6
\end{aligned}
$$

**Resposta:** existem 6 roupas diferentes, todas com uma camiseta e uma bermuda.

> 🔢 **Padrão:**  
> Fixar um item e variar o outro evita repetições e esquecimentos.

---

## 2. Diagrama de árvore e tabela

Uma lanchonete oferece pão francês ou integral e recheio de queijo, frango ou ovo.

```text
francês ─ queijo
         ├ frango
         └ ovo
integral ─ queijo
         ├ frango
         └ ovo
```

### 2.1 Dois registros da mesma combinação

Na árvore, cada pão abre três ramos. Na tabela, pães ficam nas linhas e recheios nas colunas.

|  | queijo | frango | ovo |
|---|---|---|---|
| francês | FQ | FF | FO |
| integral | IQ | IF | IO |

Cada célula guarda uma possibilidade.

### 2.2 Comparar os totais

**Exemplo resolvido — Sanduíches**

$$
\begin{aligned}
3+3&=6
\end{aligned}
$$

**Resposta:** árvore e tabela registram os mesmos 6 sanduíches possíveis.

> ⚠️ **Atenção:**  
> Cada caminho deve escolher exatamente um item de cada coleção.

---

## 3. Multiplicação como atalho

Há 4 sabores de suco e 3 tamanhos de copo. Para cada sabor, os três tamanhos aparecem novamente.

```text
laranja: P M G
uva:     P M G
limão:   P M G
manga:   P M G
```

### 3.1 Grupos iguais de possibilidades

Listar ajuda quando há poucas opções. Depois de perceber a repetição, a multiplicação encurta a contagem.

- Cada sabor forma 3 escolhas.
- Existem 4 grupos iguais de 3.
- O atalho vale porque combinamos duas coleções.

### 3.2 Contar sem escrever tudo

**Exemplo resolvido — Sabor e tamanho**

$$
\begin{aligned}
4\times3&=12
\end{aligned}
$$

Em outro balcão, 5 sanduíches podem acompanhar 2 sucos:

$$
\begin{aligned}
5\times2&=10
\end{aligned}
$$

**Resposta:** há 12 combinações de suco e copo; no segundo caso, 10 lanches.

> 🔢 **Padrão:**  
> Multiplique as quantidades das duas coleções depois de entender a lista.
