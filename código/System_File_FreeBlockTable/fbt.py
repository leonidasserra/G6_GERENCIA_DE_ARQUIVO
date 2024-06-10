# Importa o módulo tkinter como tk para criação de interfaces gráficas
import tkinter as tk
# Importa messagebox e simpledialog do tkinter para exibição de mensagens e diálogos simples
from tkinter import messagebox, simpledialog

# Define a classe FileSystem para gerenciar o sistema de arquivos
class FileSystem:
    # Método inicializador da classe FileSystem
    def __init__(self, total_blocks):
        # Define o número total de blocos no sistema de arquivos
        self.total_blocks = total_blocks
        # Inicializa o conjunto de blocos livres
        self.free_blocks = set(range(total_blocks))
        # Inicializa o dicionário de blocos alocados
        self.allocated_blocks = {}
        # Inicializa o dicionário de arquivos
        self.files = {}
        # Inicializa o dicionário de diretórios com o diretório raiz
        self.directories = {'/': set()}
        # Define o diretório atual como raiz
        self.current_directory = '/'

    # Método para alocar um bloco livre
    def allocate_block(self):
        # Verifica se há blocos livres
        if len(self.free_blocks) == 0:
            raise Exception("Nenhum bloco livre disponível")
        # Remove e retorna um bloco livre
        block = self.free_blocks.pop()
        # Adiciona o bloco aos blocos alocados
        self.allocated_blocks[block] = None
        return block

    # Método para liberar um bloco alocado
    def free_block(self, block):
        # Verifica se o bloco está alocado
        if block not in self.allocated_blocks:
            raise Exception("Bloco não está alocado")
        # Remove o bloco dos blocos alocados
        del self.allocated_blocks[block]
        # Adiciona o bloco aos blocos livres
        self.free_blocks.add(block)

    # Método para escrever dados em um bloco alocado
    def write_block(self, block, data):
        # Verifica se o bloco está alocado
        if block not in self.allocated_blocks:
            raise Exception("Bloco não está alocado")
        # Escreve os dados no bloco alocado
        self.allocated_blocks[block] = data

    # Método para ler dados de um bloco alocado
    def read_block(self, block):
        # Verifica se o bloco está alocado
        if block not in self.allocated_blocks:
            raise Exception("Bloco não está alocado")
        # Retorna os dados do bloco alocado
        return self.allocated_blocks[block]

    # Método para criar um arquivo
    def create_file(self, filename, content='', directory=None):
        # Define o diretório como o diretório atual, se não especificado
        if directory is None:
            directory = self.current_directory
        # Verifica se o diretório existe
        if directory not in self.directories:
            raise Exception("Diretório não existe")
        # Verifica se o arquivo já existe
        if filename in self.files:
            raise Exception("Arquivo já existe")
        # Aloca um bloco para o arquivo
        block = self.allocate_block()
        # Armazena o arquivo no dicionário de arquivos
        self.files[filename] = (block, directory)
        # Adiciona o arquivo ao diretório
        self.directories[directory].add(filename)
        # Escreve o conteúdo no bloco, se fornecido
        if content:
            self.write_block(block, content)
    
    # Método para visualizar o conteúdo de um arquivo
    def view_file(self, filename):
        # Verifica se o arquivo existe
        if filename not in self.files:
            raise Exception("Arquivo não existe")
        # Obtém o bloco do arquivo
        block, _ = self.files[filename]
        # Retorna o conteúdo do bloco
        return self.read_block(block)

    # Método para editar o conteúdo de um arquivo
    def edit_file(self, filename, data):
        # Verifica se o arquivo existe
        if filename not in self.files:
            raise Exception("Arquivo não existe")
        # Obtém o bloco do arquivo
        block, _ = self.files[filename]
        # Escreve os novos dados no bloco
        self.write_block(block, data)

    # Método para remover um arquivo
    def remove_file(self, filename):
        # Verifica se o arquivo existe
        if filename not in self.files:
            raise Exception("Arquivo não existe")
        # Obtém o bloco do arquivo
        block, _ = self.files[filename]
        # Libera o bloco alocado
        self.free_block(block)
        # Remove o arquivo do dicionário de arquivos
        del self.files[filename]
        # Remove o arquivo do diretório atual
        self.directories[self.current_directory].remove(filename)

    # Método para remover um diretório
    def remove_directory(self, directory):
        # Verifica se o diretório existe
        if directory not in self.directories:
            raise Exception("Diretório não existe")
        # Verifica se o diretório é o diretório raiz
        if directory == '/':
            raise Exception("Não é possível remover o diretório raiz")
        # Verifica se o diretório está vazio
        if self.list_directory(directory):
            raise Exception("Diretório não está vazio")
        # Remove o diretório do dicionário de diretórios
        del self.directories[directory]
        # Remove o diretório do diretório atual
        self.directories[self.current_directory].remove(directory)

    # Método para criar um diretório
    def create_directory(self, directory):
        # Verifica se o diretório já existe
        if directory in self.directories:
            raise Exception("Diretório já existe")
        # Verifica se o diretório atual existe
        if self.current_directory not in self.directories:
            raise Exception("Diretório atual não existe")
        # Adiciona o novo diretório ao dicionário de diretórios
        self.directories[directory] = set()
        # Adiciona o novo diretório ao diretório atual
        self.directories[self.current_directory].add(directory)

    # Método para listar os arquivos e diretórios em um diretório
    def list_directory(self, directory=None):
        # Define o diretório como o diretório atual, se não especificado
        if directory is None:
            directory = self.current_directory
        # Verifica se o diretório existe
        if directory not in self.directories:
            raise Exception("Diretório não existe")
        # Retorna a lista de arquivos e diretórios no diretório
        return list(self.directories[directory])

    # Método para navegar para um diretório
    def navigate(self, directory):
        # Verifica se o diretório existe
        if directory not in self.directories:
            raise Exception("Diretório não existe")
        # Verifica se é possível navegar de volta para o diretório raiz
        if directory == '/' and self.current_directory != '/':
            raise Exception("Não é possível navegar de volta para o diretório raiz")
        # Define o diretório atual como o diretório especificado
        self.current_directory = directory

    # Método para voltar ao diretório pai
    def navigate_back(self):
        # Verifica se o diretório atual é o diretório raiz
        if self.current_directory == '/':
            return
        # Obtém o diretório pai
        parent_directory = '/'.join(self.current_directory.split('/')[:-1])
        # Define o diretório pai como raiz, se necessário
        if parent_directory == '':
            parent_directory = '/'
        # Define o diretório atual como o diretório pai
        self.current_directory = parent_directory

# Define a classe FileSystemGUI para gerenciar a interface gráfica do sistema de arquivos
class FileSystemGUI:
    # Método inicializador da classe FileSystemGUI
    def __init__(self, master):
        # Define a janela principal da interface gráfica
        self.master = master
        self.master.title("Sistema de Arquivos GUI")

        # Inicializa o sistema de arquivos com 100 blocos
        self.file_system = FileSystem(100)

        # Define o diretório atual como raiz
        self.current_directory = '/'
        # Cria um rótulo para exibir o diretório atual
        self.current_path_label = tk.Label(master, text="Diretório Atual: " + self.current_directory)
        self.current_path_label.pack()

        # Cria uma listbox para exibir os diretórios
        self.directory_listbox = tk.Listbox(master, height=10, width=50)
        self.directory_listbox.pack()

        # Cria uma listbox para exibir os arquivos
        self.file_listbox = tk.Listbox(master, height=10, width=50)
        self.file_listbox.pack()

        # Cria botões para diversas funcionalidades
        self.navigate_button = tk.Button(master, text="Abrir Diretório", command=self.open_directory)
        self.navigate_button.pack()

        self.navigate_back_button = tk.Button(master, text="Voltar", command=self.go_back)
        self.navigate_back_button.pack()

        self.create_directory_button = tk.Button(master, text="Criar Diretório", command=self.create_directory)
        self.create_directory_button.pack()

        self.create_file_button = tk.Button(master, text="Criar Arquivo", command=self.create_file)
        self.create_file_button.pack()

        self.view_file_button = tk.Button(master, text="Visualizar Arquivo", command=self.view_file)
        self.view_file_button.pack()

        self.edit_file_button = tk.Button(master, text="Editar Arquivo", command=self.edit_file)
        self.edit_file_button.pack()

        self.remove_file_button = tk.Button(master, text="Remover Arquivo", command=self.remove_file)
        self.remove_file_button.pack()

        self.remove_directory_button = tk.Button(master, text="Remover Diretório", command=self.remove_directory)
        self.remove_directory_button.pack()

        # Atualiza as listas de diretórios e arquivos
        self.update_lists()

    # Método para atualizar as listas de diretórios e arquivos
    def update_lists(self):
        # Limpa as listboxes de diretórios e arquivos
        self.directory_listbox.delete(0, tk.END)
        self.file_listbox.delete(0, tk.END)

        # Obtém a lista de diretórios no diretório atual
        directories = self.file_system.list_directory()
        # Adiciona os diretórios à listbox de diretórios
        for directory in directories:
            self.directory_listbox.insert(tk.END, "  " + directory + "/")

        # Obtém a lista de arquivos no diretório atual
        files = self.file_system.list_directory()
        # Adiciona os arquivos à listbox de arquivos
        for file in files:
            self.file_listbox.insert(tk.END, "  " + file)

        # Atualiza o rótulo do diretório atual
        self.current_path_label.config(text="Diretório Atual: " + self.current_directory)

    # Método para abrir um diretório
    def open_directory(self):
        # Obtém a seleção na listbox de diretórios
        selection = self.directory_listbox.curselection()
        if selection:
            directory = self.directory_listbox.get(selection[0])
            directory = directory.strip().rstrip('/')
        try:
            # Navega para o diretório selecionado
            self.file_system.navigate(directory)
            self.current_directory = directory
            self.update_lists()
        except Exception as e:
            tk.messagebox.showerror("Erro", str(e))

    # Método para voltar ao diretório pai
    def go_back(self):
        try:
            # Navega para o diretório pai
            self.file_system.navigate_back()
            self.update_lists()
        except Exception as e:
            tk.messagebox.showerror("Erro", str(e))

    # Método para criar um novo diretório
    def create_directory(self):
        # Solicita o nome do novo diretório ao usuário
        directory = tk.simpledialog.askstring("Criar Diretório", "Digite o nome do diretório:")
        if directory:
            try:
                # Cria o novo diretório
                self.file_system.create_directory(directory.strip())
                self.update_lists()
            except Exception as e:
                tk.messagebox.showerror("Erro", str(e))

    # Método para criar um novo arquivo
    def create_file(self):
        # Solicita o nome do novo arquivo ao usuário
        filename = tk.simpledialog.askstring("Criar Arquivo", "Digite o nome do arquivo:")
        if filename:
            try:
                # Cria o novo arquivo
                self.file_system.create_file(filename.strip())
                self.update_lists()
            except Exception as e:
                tk.messagebox.showerror("Erro", str(e))

    # Método para visualizar o conteúdo de um arquivo
    def view_file(self):
        # Obtém a seleção na listbox de arquivos
        selection = self.file_listbox.curselection()
        if selection:
            filename = self.file_listbox.get(selection[0])
            filename = filename.strip()
            try:
                # Obtém o conteúdo do arquivo
                file_content = self.file_system.view_file(filename)
                tk.messagebox.showinfo("Conteúdo do Arquivo", file_content)
            except Exception as e:
                tk.messagebox.showerror("Erro", str(e))

    # Método para editar o conteúdo de um arquivo
    def edit_file(self):
        # Obtém a seleção na listbox de arquivos
        selection = self.file_listbox.curselection()
        if selection:
            filename = self.file_listbox.get(selection[0])
            # Solicita o novo conteúdo do arquivo ao usuário
            file_content = tk.simpledialog.askstring("Editar Arquivo", "Digite o novo conteúdo:")
            if file_content:
                try:
                    # Edita o arquivo com o novo conteúdo
                    self.file_system.edit_file(filename.strip(), file_content)
                    self.update_lists()
                except Exception as e:
                    tk.messagebox.showerror("Erro", str(e))

    # Método para remover um arquivo
    def remove_file(self):
        # Obtém a seleção na listbox de arquivos
        selection = self.file_listbox.curselection()
        if selection:
            filename = self.file_listbox.get(selection[0])
            try:
                # Remove o arquivo selecionado
                self.file_system.remove_file(filename.strip())
                self.update_lists()
            except Exception as e:
                tk.messagebox.showerror("Erro", str(e))
    
    # Método para remover um diretório
    def remove_directory(self):
        # Obtém a seleção na listbox de diretórios
        selection = self.directory_listbox.curselection()
        if selection:
            directory = self.directory_listbox.get(selection[0])
            directory = directory.strip().rstrip('/')
            try:
                # Remove o diretório selecionado
                self.file_system.remove_directory(directory)
                self.update_lists()
            except Exception as e:
                tk.messagebox.showerror("Erro", str(e))

# Cria a janela principal da interface gráfica
root = tk.Tk()
# Inicializa a aplicação do sistema de arquivos
app = FileSystemGUI(root)
# Inicia o loop principal da interface gráfica
root.mainloop()
