import json
import os


banco_dados = "banco_tarefas.json"

class Tarefa:
    def __init__(self, name, iscomplete = False):
        self.name = name
        self.iscomplete = iscomplete

    def __str__(self):
        return (f'{self.name} [{"X" if self.iscomplete else " "}]')

    def change_iscomplete(self):
        self.iscomplete = not self.iscomplete





menu_opcoes = {
    1: "Adicionar tarefa",
    2: "Listar tarefas",
    3: "Marcar como concluída",
    4: "Remover tarefa",
    0: "Sair"
}

def limpar_ecra():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
def separador():
    print("-" * 30)

def notificacao(message = "Ação finalizada"):
    print()
    input(f'{message}. Aperte enter para voltar ao menu.')

def tarefas_esta_vazio():
    return not tarefas

def pergunta_indice():
    opcao_selecionada = input("Escolha uma opção: ")
    try:
        opcao_selecionada = int(opcao_selecionada)
    except ValueError:
        return None
    opcao_selecionada -= 1
    if opcao_selecionada < 0 or opcao_selecionada >= len(tarefas):
        return None

    return opcao_selecionada


def adicionar_tarefa():
    nome_tarefa = input('Informe o nome da tarefa: ')
    nome_tarefa = nome_tarefa.strip()
    if nome_tarefa == '':
        notificacao('O nome precisa conter letras')
        return
    tarefas.append(Tarefa(nome_tarefa))
    notificacao('Tarefa inserida')

def mostra_menu():
    for item in menu_opcoes:
        print(item, menu_opcoes[item])

def listar_tarefas():
    for t,tarefa in enumerate(tarefas):
        print(f'{t+1} - {tarefa}')





def concluir_tarefa():
    if tarefas_esta_vazio():
        notificacao('Não existem tarefas')
        return
    listar_tarefas()
    opcao = pergunta_indice()
    if opcao is None:
        notificacao('Opção inválida')
        return

    tarefas[opcao].change_iscomplete()
    if tarefas[opcao].iscomplete:
        notificacao('Tarefa marcada como concluída')
    else:
        notificacao('Tarefa alterada para pendente')

def remover_tarefa():
    if tarefas_esta_vazio():
        notificacao('Não existem tarefas')
        return
    listar_tarefas()
    opcao = pergunta_indice()
    if opcao is None:
        notificacao('Opção inválida')
        return
    del tarefas[opcao]
    notificacao('Item removido.')


if os.path.exists(banco_dados):
    with open(banco_dados, 'r', encoding='utf8') as arquivo:
        try:
            tarefas = [Tarefa(tarefa['name'], tarefa['iscomplete']) for tarefa in json.load(arquivo)]
        except json.JSONDecodeError:
            tarefas = []
            notificacao('Caiu na excecao')

else:
    tarefas = []


while True:
    limpar_ecra()
    separador()
    print("="*6, "GESTOR DE TAREFAS","="*6)
    mostra_menu()
    separador()

    opcao = input('Escolha a opção desejada:')

    try:
        opcao = int(opcao)
    except ValueError:
        notificacao('Escolha um número inteiro')
        continue
    if opcao not in menu_opcoes:
        notificacao('Opção inválida')
        continue

    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        if tarefas_esta_vazio():
            notificacao('Não existem tarefas')
            continue
        listar_tarefas()
        notificacao()
    elif opcao == 3:
        concluir_tarefa()
    elif opcao == 4:
        remover_tarefa()
    elif opcao == 0:
        with open(banco_dados,'w', encoding="utf8") as arquivo:
            txt = json.dumps([tarefa.__dict__ for tarefa in tarefas],ensure_ascii=False)
            arquivo.write(txt)
        break