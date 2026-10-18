# TaskTracker

Aplicação de linha de comando desenvolvida para a Fase 2 do Bootcamp II. Permite cadastrar tarefas, validar os dados informados e visualizar todas as tarefas registradas durante a execução.

## Funcionalidades

- Cadastro de tarefas com título, descrição, prioridade e data limite.
- Validação de título obrigatório.
- Validação das prioridades Alta, Média e Baixa.
- Status inicial automático como Pendente.
- Listagem organizada e legível das tarefas.
- Menu contínuo até o usuário escolher sair.

## Tecnologias

- Python 3
- Git
- GitHub

## Estrutura

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Como executar

1. Instale Python 3.
2. Clone este repositório.
3. Entre na pasta do projeto.
4. Execute:

```bash
python src/main.py
```

## Uso

O menu oferece três opções:

1. Cadastrar nova tarefa.
2. Visualizar tarefas cadastradas.
3. Sair da aplicação.

As tarefas permanecem disponíveis enquanto o programa estiver em execução. Persistência em arquivo e containerização serão tratadas nas próximas etapas.

## Vídeo de apresentação

[Assista à demonstração técnica do TaskTracker no YouTube](https://youtu.be/-L0KpZp6HNU).

## Autor

Nícolas Henrique Tito Lettieri  
Ciência de Dados e Machine Learning  
Unidade Asa Norte, 2º semestre, matutino
