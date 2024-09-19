import tkinter as tk
from tkinter import messagebox

# Cardápio_Restaurante
menu = {
    '1': {'nome': 'Parmegiana', 'preco': 25.00},
    '2': {'nome': 'Picadinho', 'preco': 15.00},
    '3': {'nome': 'Panquecas', 'preco': 12.00},
    '4': {'nome': 'Refrigerante', 'preco': 5.00},
    '5': {'nome': 'Sobremesa', 'preco': 10.00},
    '6': {'nome': 'Feijoada Pequena', 'preco': 39.00},
    '7': {'nome': 'Feijoada Grande', 'preco': 49.00},
}

# Função para adicionar itens ao pedido
def adicionar_pedido(item_id, quantidade_var, pedido_var, total_var):
    quantidade = int(quantidade_var.get())
    if quantidade <= 0:
        messagebox.showwarning("Quantidade inválida", "Por favor, insira uma quantidade válida.")
        return
    
    item = menu[item_id]
    preco_total = item['preco'] * quantidade
    pedido_var.append({'nome': item['nome'], 'quantidade': quantidade, 'preco_total': preco_total})
    
    total_atual = sum(item['preco_total'] for item in pedido_var)
    total_var.set(f"Total: R$ {total_atual:.2f}")
    
    messagebox.showinfo("Pedido adicionado", f"{quantidade}x {item['nome']} adicionado(s) ao pedido.")
    quantidade_var.set(0)

# Função para exibir o resumo do pedido
def exibir_resumo(pedido_var, total_var):
    if not pedido_var:
        messagebox.showwarning("Pedido vazio", "Você ainda não fez nenhum pedido.")
        return
    
    resumo = "\n".join([f"{item['quantidade']}x {item['nome']} - R$ {item['preco_total']:.2f}" for item in pedido_var])
    resumo += f"\n\n{total_var.get()}"
    
    messagebox.showinfo("Resumo do Pedido", resumo)

# Função para limpar o pedido
def limpar_pedido(pedido_var, total_var):
    pedido_var.clear()
    total_var.set("Total: R$ 0.00")
    messagebox.showinfo("Pedido limpo", "O pedido foi limpo com sucesso.")

# Função do chatbot manual baseado em regras
def responder_chatbot(mensagem):
    mensagem = mensagem.lower()
    
    respostas = {
        "oi": "Olá! Como posso ajudar?",
        "qual o horário de funcionamento?": "Funcionamos das 8h às 22h, todos os dias.",
        "quais são os itens do cardápio?": "Temos Parmegiana, Picadinho, Panquecas, Refrigerante, Sobremesa e Feijoada (pequena e grande).",
        "quais são os preços?": "Os preços variam de R$5,00 a R$49,00.",
        "como faço um pedido?": "Você pode adicionar itens ao seu pedido usando a interface principal do sistema.",
        "obrigado": "De nada! Estou aqui para ajudar.",
        "tchau": "Até logo! Volte sempre."
    }
    
    return respostas.get(mensagem, "Desculpe, não entendi. Pode repetir?")

# Função para iniciar o chatbot
def iniciar_chat():
    def enviar_mensagem():
        mensagem = entrada_usuario.get()
        if mensagem:
            chatbox.insert(tk.END, f"Você: {mensagem}\n")
            resposta = responder_chatbot(mensagem)
            chatbox.insert(tk.END, f"Bot: {resposta}\n")
            entrada_usuario.delete(0, tk.END)

    chat_window = tk.Toplevel()
    chat_window.title("ChatBot - Restaurante")

    chatbox = tk.Text(chat_window, height=20, width=50)
    chatbox.pack(pady=10)

    entrada_usuario = tk.Entry(chat_window, width=40)
    entrada_usuario.pack(side=tk.LEFT, padx=10)

    enviar_btn = tk.Button(chat_window, text="Enviar", command=enviar_mensagem)
    enviar_btn.pack(side=tk.LEFT)

# Função principal para configurar a interface gráfica
def sistema_pedidos_gui():
    # Janela principal
    root = tk.Tk()
    root.title("Sistema de Pedidos - Adribeck")

    # Variáveis
    pedido_var = []
    total_var = tk.StringVar(value="Total: R$ 0.00")

    # Título
    tk.Label(root, text="Bem-vindo ao Adribeck Restaurante", font=('Arial', 16)).pack(pady=10)

    # Cardápio
    tk.Label(root, text="Escolha os itens do cardápio:", font=('Arial', 14)).pack(pady=10)

    # Frame para os itens do cardápio
    frame_cardapio = tk.Frame(root)
    frame_cardapio.pack(pady=10)

    # Adiciona os itens do cardápio à interface
    for item_id, item in menu.items():
        tk.Label(frame_cardapio, text=f"{item['nome']} - R$ {item['preco']:.2f}").grid(row=int(item_id)-1, column=0, padx=10, pady=5)
        
        quantidade_var = tk.IntVar(value=0)
        tk.Entry(frame_cardapio, textvariable=quantidade_var, width=5).grid(row=int(item_id)-1, column=1, padx=10, pady=5)
        
        tk.Button(frame_cardapio, text="Adicionar", 
                  command=lambda item_id=item_id, quantidade_var=quantidade_var: 
                  adicionar_pedido(item_id, quantidade_var, pedido_var, total_var)).grid(row=int(item_id)-1, column=2, padx=10, pady=5)

    # Exibir o total do pedido
    total_label = tk.Label(root, textvariable=total_var, font=('Arial', 14))
    total_label.pack(pady=10)

    # Botões de ações
    frame_acoes = tk.Frame(root)
    frame_acoes.pack(pady=10)
    
    tk.Button(frame_acoes, text="Resumo do Pedido", command=lambda: exibir_resumo(pedido_var, total_var), width=20).grid(row=0, column=0, padx=10, pady=5)
    tk.Button(frame_acoes, text="Limpar Pedido", command=lambda: limpar_pedido(pedido_var, total_var), width=20).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(frame_acoes, text="Iniciar Chatbot", command=iniciar_chat, width=20).grid(row=0, column=2, padx=10, pady=5)
    tk.Button(frame_acoes, text="Sair", command=root.quit, width=20).grid(row=0, column=3, padx=10, pady=5)

    # Inicia o loop principal
    root.mainloop()

# Executa o sistema de pedidos com interface gráfica
if __name__ == "__main__":
    sistema_pedidos_gui()
