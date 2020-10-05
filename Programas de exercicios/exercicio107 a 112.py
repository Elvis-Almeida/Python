from utilidadesCeV.moeda import moeda
from utilidadesCeV.dados import leitordados

p = leitordados.leiadinheiro('digite um valor monetário')
moeda.resumo(p, 10, 40)