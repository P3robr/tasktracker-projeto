"""TaskTracker - aplicação CLI da Fase 2 do Bootcamp II."""


def ler_titulo() -> str:
    """Solicita um título não vazio."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título não pode ficar vazio.")


def ler_prioridade() -> str:
    """Solicita e normaliza uma prioridade válida."""
    prioridades = {
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa",
    }
    while True:
        entrada = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if entrada in prioridades:
            return prioridades[entrada]
        print("Erro: informe somente Alta, Média ou Baixa.")


def cadastrar_tarefa(tarefas: list[dict[str, str]]) -> None:
    """Valida os dados e adiciona uma tarefa pendente."""
    print("\n--- Nova tarefa ---")
    tarefa = {
        "titulo": ler_titulo(),
        "descricao": input("Descrição: ").strip(),
        "prioridade": ler_prioridade(),
        "data_limite": input("Data limite: ").strip(),
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso.")


def visualizar_tarefas(tarefas: list[dict[str, str]]) -> None:
    """Exibe todas as tarefas ou uma mensagem de lista vazia."""
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao'] or 'Não informada'}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite'] or 'Não informada'}")
        print(f"Status: {tarefa['status']}")


def exibir_menu() -> None:
    """Apresenta as opções disponíveis."""
    print("\n=== TaskTracker ===")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main() -> None:
    """Mantém o menu ativo até a opção de saída."""
    tarefas: list[dict[str, str]] = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("TaskTracker encerrado.")
            break
        else:
            print("Erro: escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
