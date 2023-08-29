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
    sortudos = list(range(100))
    # faz umas contas aqui para achar os sortudos
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
    texto_em_morse = "●●●－－－●●●"
    return texto_em_morse


fox = "－ ●●●● ● / －－●－ ●●－ ●● －●－● －●－ / －●●● ●－● －－－ ●－－ －● / ●●－● －－－ －●●－"
assert converta_em_morse("the quick brown fox") == fox
ovr = "●－－－ ●●－ －－ ●－－● ●●● / －－－ ●●●－ ● ●－●"
assert converta_em_morse("jumps over") == ovr
dog = "－ ●●●● ● / ●－●● ●－ －－●● －●－－ / －●● －－－ －－●"
assert converta_em_morse("the lazy dog") == dog
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
    bloqueio = 0
    return bloqueio


assert bloqueie_velha(0, 1) == 2
assert bloqueie_velha(0, 3) == 6
assert bloqueie_velha(6, 4) == 2
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
    maior, menor = numero, numero
    return maior - menor


assert reorganize_o_numero(213) == 198

_SET4_ = {
    "script_name": "dojo_medio_4",
    "script_div_id": "dojo_medio_4",
    "height": 400, "index": "2.5", "title": "Conte o número de Xs e o número de Os"
}  # _SEC_


def conte_xs_eos(texto):
    """Conte o número de Xs e o número de Os.
    """
    eh_igual = True
    return eh_igual


assert conte_xs_eos("O show da Xuxa foi cancelado") == False

_SET5_ = {
    "script_name": "dojo_medio_5",
    "script_div_id": "dojo_medio_5",
    "height": 400, "index": "2.6", "title": "Crie uma função de calculadora"
}  # _SEC_


def calculadora(operando1, operador, operando2):
    """Crie uma função de calculadora.
    """
    resultado = 0
    return resultado


assert calculadora(6, ".", 4) == 24

_SET6_ = {
    "script_name": "dojo_medio_6",
    "script_div_id": "dojo_medio_6",
    "height": 400, "index": "2.7", "title": "Dê-me o desconto"
}  # _SEC_


def de_me_o_desconto(valor, desconto):
    """A função deve retornar o preço do item após a aplicação do desconto.
.
    """
    resultado = 0
    return resultado


assert de_me_o_desconto(100, 20) == 80

_SET7_ = {
    "script_name": "dojo_medio_7",
    "script_div_id": "dojo_medio_7",
    "height": 400, "index": "2.8", "title": "Apenas os números"
}  # _SEC_


def apenas_os_numeros(lista):
    """A função deve retornar apenas os números.
.
    """
    resultado = 0
    return resultado


assert apenas_os_numeros([3, "oi", 'ola', 9, 2]) == [3, 9, 2]

_SET8_ = {
    "script_name": "dojo_medio_8",
    "script_div_id": "dojo_medio_8",
    "height": 400, "index": "2.9", "title": "Repita os caracteres"
}  # _SEC_


def repita_os_caracteres(texto):
    """A função deve retornar uma string, com cada caractere na string original duplicado.
    """
    resultado = 0
    return resultado


assert repita_os_caracteres("agora") == "aaggoorraa"
