.. Open Source Notification: This file is part of open source program **SuuCuriJuba**
   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
   `Labase <http://labase.selfip.org/>`_ - `NCE <http://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. include:: special.rst

.. _modulo_dojo_medio_medio:

Problemas para o Dojo Intermediário
===================================

1. Ordene uma lista
-------------------------

Os números da sorte são um subconjunto de números inteiros.
Em vez de entrar em muita teoria, vejamos o processo para chegar aos números da sorte:

     Pegue o conjunto de inteiros
     1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,……
     Primeiro, exclua cada segundo número, obtemos o seguinte conjunto reduzido.
     1,3,5,7,9,11,13,15,17,19,…………
     Agora, exclua cada terceiro número, obtemos
     1, 3, 7, 9, 13, 15, 19,….….
     Continue este processo indefinidamente......
     Qualquer número que NÃO seja excluído devido ao processo acima é chamado de “sortudo”.
     Portanto, o conjunto de números da sorte é 1, 3, 7, 13,………


Dado um número inteiro n, escreva uma função para dizer se esse número é sortudo ou não.

.. raw:: html

  <div id="dojo_medio_0"></div>
  <script type="text/python">
      from ScriptWidget import ScriptBuilder
      sw2 = ScriptBuilder("dojo_medio_0.py", height=400, index="1.1", title="dojo médio")
  </script>


2. Converta para código morse
--------------------------------------------------

Não usamos mais o código Morse para transferir informações, mas isso não significa
que você não possa usá-lo em um desafio de código. Escreva uma função em Python que
receba uma string que pode ter caracteres alfanuméricos em letras minúsculas ou maiúsculas.

A string também pode conter quaisquer caracteres especiais tratados em código Morse,
incluindo vírgulas, dois pontos, apóstrofos, pontos, pontos de exclamação e pontos de interrogação.
A função deve retornar o código Morse equivalente para a string.

.. image:: https://i.imgur.com/0OwDj2u.jpg

.. raw:: html

  <div id="dojo_medio_1"></div>

3. Bloqueador Tic Tac Toe
---------------------------------

Neste desafio Python, escreva uma função que aceite dois números.
Esses números representarão uma posição em um tabuleiro de jogo da velha.
Eles podem ser de 0 a 8, onde 0 é o ponto superior esquerdo e 8 é o ponto inferior direito.

Esses parâmetros são duas marcas no tabuleiro do jogo da velha.
A função deve retornar o número da vaga que pode impedir que essas duas vagas ganhem o jogo.

.. raw:: html

  <div id="dojo_medio_2"></div>


4. Reorganize o número
------------------------------------------------------------------

Para completar este desafio, escreva uma função que aceite um número como parâmetro.
A função deve retornar um número que é a diferença entre o maior e o menor número que os dígitos podem formar no número.

Por exemplo, se o parâmetro for “213”, a função deverá retornar “198”, que é o resultado de 123 subtraído de 321.

.. raw:: html

  <div id="dojo_medio_3"></div>

5. Os Xs são iguais aos Os?
---------------------------------

Crie uma função Python que aceite uma string. Esta função deve contar
o número de Xs e o número de Os na string. Ele deve retornar um valor booleano de True ou False.
Se a contagem de Xs e Os for igual, a função deve retornar True.
Se a contagem não for a mesma, deve retornar False.
Se não houver Xs ou Os na string, ela também deve retornar True porque 0 é igual a 0.
A string pode conter qualquer tipo e número de caracteres.

.. raw:: html

  <div id="dojo_medio_4"></div>

6. Crie uma função de calculadora
---------------------------------

Escreva uma função Python que aceite três parâmetros. O primeiro parâmetro é um número inteiro.
O segundo é um dos seguintes operadores matemáticos: +, -, / ou .
O terceiro parâmetro também será um número inteiro.
A função deve realizar um cálculo e retornar os resultados.
Por exemplo, se a função for passada 6 e 4, ela deve retornar 24.

.. raw:: html

  <div id="dojo_medio_5"></div>

7. Dê-me o desconto
---------------------------------

Crie uma função em Python que aceite dois parâmetros.
O primeiro deve ser o preço total de um item como um número inteiro.
O segundo deve ser a porcentagem de desconto como um número inteiro.

A função deve retornar o preço do item após a aplicação do desconto.
Por exemplo, se o preço for 100 e o desconto for 20, a função deve retornar 80.

.. raw:: html

  <div id="dojo_medio_6"></div>

8. Apenas os números
---------------------------------

Escreva uma função em Python que aceite uma lista de qualquer tamanho
que contenha uma mistura de inteiros não negativos e strings.
A função deve retornar uma lista apenas com os inteiros da lista original na mesma ordem.

.. raw:: html

  <div id="dojo_medio_7"></div>

9. Repita os caracteres
---------------------------------

Crie uma função Python que aceite uma string.
A função deve retornar uma string, com cada caractere na string original duplicado.
Se você enviar a função "agora" como parâmetro, ela deve retornar "aaggoorraa",
e se você enviar "123a!", ela deve retornar "112233aa!!".

.. raw:: html

  <div id="dojo_medio_8"></div>
