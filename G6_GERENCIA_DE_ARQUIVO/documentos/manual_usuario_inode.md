# Manual do Usuário para Sistema de Arquivos GUI

## Introdução

Este manual descreve como utilizar a interface gráfica de um sistema de arquivos implementado em Python usando a biblioteca `tkinter`. O sistema permite a criação, visualização, edição e remoção de arquivos e diretórios, além de outras funcionalidades como navegação e gerenciamento de atributos.

## Recomendações
- Evite clicar em outros botões enquanto você estiver no meio da execução de uma determinada funcionalidade, especialmente se ela envolver entrada de dados.
- Se uma funcionalidade que envolva entrada de dados não exibir a tela para o usuário colocar os dados dê um clique em qualquer local "em branco" da interface, ou seja, um clique que não ative uma nova funcionaliade 

## Requisitos

- Python instalado (versão 3.11.0 recomendada).
- Biblioteca `tkinter` instalada (versão 8.6 recomendada).

## Instalação

Caso a biblioteca Tkinter não esteja instalada, digite o seguinte comando no prompt da sua IDE:

```sh
pip install tk
```


## Execução

Para executar o programa, salve o código fornecido em um arquivo Python (`sistema_de_arquivos_gui.py`) e execute-o com o comando:

```sh
python sistema_de_arquivos_gui.py
```

## Funcionalidades

### Login e Registro

Ao iniciar a aplicação, a janela de login será exibida.

- **Login:** Digite seu nome de usuário e senha e clique em "Login".
- **Registro:** Para registrar um novo usuário, digite um novo nome de usuário e senha e clique em "Registrar".

### Interface Principal

Após o login bem-sucedido, a interface principal do sistema de arquivos será exibida.

#### Caminho Atual

Um rótulo exibe o caminho atual do diretório.

#### Menu

O menu "Arquivo" oferece as seguintes opções:

- **Abrir Diretório:** Permite a navegação para outro diretório.
- **Diretório Anterior:** Retorna ao diretório anterior.
- **Sair:** Fecha a aplicação.

### Gerenciamento de Arquivos e Diretórios

#### Botões de Ação

- **Criar Arquivo:** Abre uma janela para criar um novo arquivo no diretório atual.
- **Visualizar Arquivo:** Abre uma janela para visualizar o conteúdo de um arquivo no diretório atual.
- **Editar Arquivo:** Abre uma janela para editar o conteúdo de um arquivo no diretório atual.
- **Remover Arquivo:** Remove um arquivo no diretório atual.
- **Criar Diretório:** Abre uma janela para criar um novo diretório no diretório atual.
- **Remover Diretório:** Remove um diretório no diretório atual.
- **Listar Diretório:** Lista o conteúdo do diretório atual.
- **Definir Atributo:** Define um atributo para um arquivo ou diretório.
- **Obter Atributo:** Obtém o valor de um atributo de um arquivo ou diretório.

### Mensagens de Erro

- **Erro ao abrir diretório:** Diretório não encontrado.
- **Erro ao criar diretório:** Erro ao criar o diretório.
- **Erro ao criar arquivo:** Erro ao criar o arquivo.
- **Erro ao visualizar arquivo:** Arquivo não encontrado.
- **Erro ao editar arquivo:** Erro ao editar o arquivo.
- **Erro ao remover arquivo:** Arquivo não encontrado.
- **Erro ao remover diretório:** Diretório não encontrado.
- **Erro ao listar diretório:** Erro ao listar o diretório.
- **Erro ao definir atributo:** Todos os campos são obrigatórios.
- **Erro ao obter atributo:** Todos os campos são obrigatórios.

## Descrição das Funcionalidades

### Abrir Diretório

Permite a navegação para um diretório específico. O usuário insere o caminho do diretório e, se encontrado, o caminho atual é atualizado.

### Voltar ao Diretório Anterior

Retorna ao diretório visitado anteriormente. O diretório atual é atualizado para o diretório anterior na lista de navegação.

### Criar Arquivo

Permite a criação de um novo arquivo. O usuário insere o nome do arquivo e o conteúdo. O arquivo é criado no diretório atual. Após o arquivo criado, é recomendável dar um clique em algum espaço em branco na interface caso a tela de entrada de conteúdo ainda não tenha aparecido. Durante esse processo, evite clicar em outras funcionaliades.

### Visualizar Arquivo

Permite visualizar o conteúdo de um arquivo. O usuário insere o nome do arquivo e o conteúdo é exibido em uma janela de mensagem.

### Editar Arquivo

Permite editar o conteúdo de um arquivo existente. O usuário insere o nome do arquivo e o novo conteúdo. O conteúdo do arquivo é atualizado.

### Remover Arquivo

Remove um arquivo existente. O usuário insere o nome do arquivo a ser removido.

### Criar Diretório

Permite a criação de um novo diretório. O usuário insere o nome do diretório. O diretório é criado no diretório atual.

### Remover Diretório

Remove um diretório existente. O usuário insere o nome do diretório a ser removido.

### Listar Diretório

Lista o conteúdo do diretório atual. Uma janela de mensagem exibe a lista de arquivos e diretórios.

### Definir Atributo

Define um atributo para um arquivo ou diretório. O usuário insere o caminho do nó, o nome do atributo e o valor do atributo.

### Obter Atributo

Obtém o valor de um atributo de um arquivo ou diretório. O usuário insere o caminho do nó e o nome do atributo. O valor do atributo é exibido em uma janela de mensagem.

## Conclusão

Este manual cobre as funcionalidades básicas da interface gráfica do sistema de arquivos em i-node. Em caso de dúvidas, verifique o código fonte para entender melhor o funcionamento interno.