.. Open Source Notification: This file is part of open source program **SuuCuriJuba**
   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
   `Labase <http://labase.selfip.org/>`_ - `NCE <http://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. include:: special.rst

.. _modulo_dojo_medio_medio:

Problemas para o Dojo Intermediário
===================================

1. Números da Sorte
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

5. A moeda falsificada
---------------------------------

Você recebeu doze moedas, mas uma é falsificada e o peso dela é ligeiramente diferente das outras.
Usando uma balança de dois pratos, identifique qual moeda é a falsa e se seu peso é superior ou inferior ao normal.
Desenvolva um programa que descubra a moeda falsa em três pesagens.

.. raw:: html

  <div id="dojo_medio_4"></div>

6. Os três mercadores muçulmanos
---------------------------------

Disse o xeique, apontando para os três muçulmanos:

- Aqui estão, ó Calculista, os três amigos. São criadores de carneiros em Damasco.
   Enfrentam agora um dos problemas mais curiosos que tenho visto. E esse problema é o seguinte:
   - Como pagamento de pequeno lote de carneiros, receberam aqui, em Bagdá, uma partida de vinho,
   muito fino, composta de 21 vasos iguais, sendo: 7 cheios; 7 meio cheios; 7 vazios.
   Querem, agora, dividir os 21 vasos de modo que cada um deles
   receba o mesmo número de vasos e a mesma porção de vinho. Repartir os vasos é fácil.
   Cada um dos sócios deve ficar com sete vasos. A dificuldade, a meu ver, está em
   repartir o vinho sem abrir os vasos, isto é, conservando-os exatamente como estão.

Desenvolva um programa que retorne três listas de vasos, cada lista deve obedecer às regras dadas.

    Malba Tahan, `O homem que Calculava <https://malbatahan.com.br/portfolio/o-homem-que-calculava/>`_

.. raw:: html

  <div id="dojo_medio_5"></div>

7. O problema do joalheiro
---------------------------------

Um homem que veio da Síria vender jóias em Bagdá prometeu ao dono de uma
hospedagem que pagaria 20 dinares pela hospedagem se vendesse as jóias por 100 dinares,
pagando 35 se as vendesse por 200 dinares. Mas acabou vendendo tudo por 140 dinares.
Quanto deve pagar pela hospedagem então?

Desenvolva um programa que calcule o preço a ser pago

    Malba Tahan, `O homem que Calculava <https://malbatahan.com.br/portfolio/o-homem-que-calculava/>`_

.. raw:: html

  <div id="dojo_medio_6"></div>

8. As pilhas de moedas, uma falsa
---------------------------------

Suponha-se que temos 10 pilhas de moedas. Uma das pilhas é inteiramente formada de moedas falsas,
mas não sabemos qual é essa pilha. Sabemos apenas que as moedas falsas pesam uma grama a menos que as genuínas.
A balança é uma que tem um ponteiro e diz quanto é o peso no prato.

Desenvolva um programa que em uma única pesagem diga qual é a pilha de moedas falsas.

    Malba Tahan, `O homem que Calculava <https://malbatahan.com.br/portfolio/o-homem-que-calculava/>`_

.. raw:: html

  <div id="dojo_medio_7"></div>

9. O problema dos 8 pães
---------------------------------

João deseja pagar Pedro e Marcus que durante uma viagem repartiram com ele 8 pães,
sendo que Pedro tinha 5 pães e Marcus tinha 3. A divisão foi feita de modo uniforme e cada pão custa 1 moeda.
Quantas moedas Pedro e Marcus devem receber?

Desenvolva um programa que retorne o valor devido a Pedro e a Marcus.

    Malba Tahan, `O homem que Calculava <https://malbatahan.com.br/portfolio/o-homem-que-calculava/>`_


.. raw:: html

  <div id="dojo_medio_8"></div>
