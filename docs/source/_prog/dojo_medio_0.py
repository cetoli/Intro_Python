_SET0_ = {
    "script_name": "dojo_medio_0",
    "script_div_id": "dojo_medio_0",
    "height": 400, "index": "2.1", "title": "revele se é sortudo"
}  # _SEC_


def diga_se_e_sortudo(n):
    """Descubra se um número é sortudo.
        :param n: O número a ser investigado
        :return: True se é sortudo, senão False
    """
    sortudos = list(range(n+10))
    # faz umas contas aqui para achar os sortudos
    _ = sortudos   # não faz nada, finge ser a solução
    um_sortudo = False
    return um_sortudo


assert diga_se_e_sortudo(25) is False
assert diga_se_e_sortudo(49) is True
assert diga_se_e_sortudo(83) is False
assert diga_se_e_sortudo(91) is True
print("Acertou os sortudos!")


_SET1_ = {
    "script_name": "dojo_medio_1",
    "script_div_id": "dojo_medio_1",
    "height": 400, "index": "2.2", "title": "Converta em código Morse"
}  # _SEC_


def converta_em_morse(texto):
    """Converta em código Morse.
        :param texto: O texto a ser codificado
        :return: O texto em código morse
    """
    # faz a conversão aqui
    _ = texto  # não faz nada, finge ser a solução
    texto_em_morse = "●●●－－－●●●"
    return texto_em_morse


fox = "－ ●●●● ● / －－●－ ●●－ ●● －●－● －●－ / －●●● ●－● －－－ ●－－ －● / ●●－● －－－ －●●－"
assert converta_em_morse("the quick brown fox") == fox, f"deveria ser {fox}"
ovr = "●－－－ ●●－ －－ ●－－● ●●● / －－－ ●●●－ ● ●－●"
assert converta_em_morse("jumps over") == ovr, f"deveria ser {ovr}"
dog = "－ ●●●● ● / ●－●● ●－ －－●● －●－－ / －●● －－－ －－●"
assert converta_em_morse("the lazy dog") == dog, f"deveria ser {dog}"
print("Acertou o conversor de morse!")


_SET2_ = {
    "script_name": "dojo_medio_2",
    "script_div_id": "dojo_medio_2",
    "height": 400, "index": "2.3", "title": "Bloqueador de jogo da velha"
}  # _SEC_


def bloqueie_velha(uma_marca, outra_marca):
    """Bloqueador de jogo da velha.
        :param uma_marca: O texto a ser codificado
        :param outra_marca: O texto a ser codificado
        :return: O índice da marca que bloqueia as duas outras
    """
    _ = uma_marca, outra_marca  # não faz nada, finge ser a solução
    bloqueio = 0
    _ = uma_marca, outra_marca  # não faz nada, finge ser a solução
    return bloqueio


assert bloqueie_velha(0, 1) == 2, f"deveria ser 2"
assert bloqueie_velha(0, 3) == 6, f"deveria ser 6"
assert bloqueie_velha(6, 4) == 2, f"deveria ser 2"
print("Bloqueou todas as jogadas!")


_SET3_ = {
    "script_name": "dojo_medio_3",
    "script_div_id": "dojo_medio_3",
    "height": 400, "index": "2.4", "title": "Reorganize o número"
}  # _SEC_


def reorganize_o_numero(numero):
    """Converta em código Morse.
        :param numero: O número a ser reorganizado
        :return: A diferença entre o maior e o menor
    """
    maior, menor = numero, numero  # não faz nada, finge ser a solução
    return maior - menor


assert reorganize_o_numero(213) == 198, f"deveria ser 198"
print("Resultado correto!")

_SET4_ = {
    "script_name": "dojo_medio_4",
    "script_div_id": "dojo_medio_4",
    "height": 400, "index": "2.5", "title": "A moeda falsificada"
}  # _SEC_


def moeda_falsificada(moedas):
    """Descobre a moeda falsificada.
        :param moedas: Uma lista com pesos das moedas.
        :return: O índice da moeda e True se peso superior ou False 
    """
    # faz as três pesagens aqui
    _ = moedas  # não faz nada, finge ser a solução
    moeda_falsa, mais_pesada = 0, True
    return moeda_falsa, mais_pesada


assert moeda_falsificada([8, 8, 8, 8, 8, 8, 8, 8, 8, 9]) == (9, True), f"deveria ser {(9, True)}"
assert moeda_falsificada([8, 8, 8, 8, 8, 7, 8, 8, 8, 8]) == (5, False), f"deveria ser {(5, False)}"
print("Resultado correto!")


_SET5_ = {
    "script_name": "dojo_medio_5",
    "script_div_id": "dojo_medio_5",
    "height": 400, "index": "2.6", "title": "Os três mercadores muçulmanos"
}  # _SEC_


def reparte_os_vasos():
    """Retorne três listas de vasos repartidos igualitariamente.
        :return: Três listas de vasos repartidos segundo a regra.
    """
    # considere o valor do vaso meio cheio = 1 e o cheio = 2
    resultado = [[0]*3]*3  # não faz nada, finge ser a solução
    return resultado


m0, m1, m2 = reparte_os_vasos()
todos = m0+m1+m2
assert len(m0) == len(m1) == len(m2) == 7, f"os comprimentos {len(m0), len(m1), len(m2)} deveriam ser {7}"
assert sum(m0) == sum(m1) == sum(m2), f"número de vasos {len(m0), len(m1), len(m2)} deveriam ser iguais"
assert sum(todos), f"as somas {sum(todos)} deveriam ser {27}"
assert (s1 := sum([v for v in todos if v == 1])) == 7, f"as somas dos vasos meio cheios deveriam ser {7}, foi {s1}"
assert (s2 := sum([v for v in todos if v == 2])) == 14, f"as somas dos vasos todo cheios deveriam ser {14}, foi {s2}"
print("Resultado correto!")

_SET6_ = {
    "script_name": "dojo_medio_6",
    "script_div_id": "dojo_medio_6",
    "height": 400, "index": "2.7", "title": "O problema do joalheiro"
}  # _SEC_


def fatura_da_hospedaria():
    """Calcule o preço a ser pago.
        :return: O preço devido ao hospedeiro.
    """
    resultado = 0
    return resultado


assert fatura_da_hospedaria() == 26, f"deveria ser 26"

_SET7_ = {
    "script_name": "dojo_medio_7",
    "script_div_id": "dojo_medio_7",
    "height": 400, "index": "2.8", "title": "Encontre a pilha falsa"
}  # _SEC_


def acha_a_pilha_falsa(pilhas):
    """Encontra a pilha falsa.
        :param pilhas: Dez listas com pesos das moedas.
        :return: O índice da pilha com moedas falsas.
    """
    _ = pilhas  # não faz nada, finge ser a solução
    resultado = -1
    return resultado


boa, ruim = [9]*10, [8]*10
assert acha_a_pilha_falsa(boa*9 + ruim) == 9, f"deveria ser {9}"
assert acha_a_pilha_falsa(boa*4 + ruim + boa*5) == 4, f"deveria ser {4}"
print("Resultado correto!")

_SET8_ = {
    "script_name": "dojo_medio_8",
    "script_div_id": "dojo_medio_8",
    "height": 400, "index": "2.9", "title": "Reparta o dinheiro dos 8 pães"
}  # _SEC_


def reparta_o_dinheiro():
    """Reparte o dinheiro entre os donos dois oito pães.
        :return: O valor devido a Pedro, o do Marcus.
    """
    pedro, marcus = 0, 0
    return pedro, marcus


assert reparta_o_dinheiro() == (7, 1), f"deveria ser {(7, 1)}"
print("Resultado correto!")
