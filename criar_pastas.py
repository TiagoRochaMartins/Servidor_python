import os

def criar_pastas_com_padrao(numero_pastas, caminhos):
    for caminho in caminhos:
        for i in range(numero_pastas):
            nome_pasta = f"{i:07d}"
            caminho_completo = os.path.join(caminho, nome_pasta)

            try:
                os.mkdir(caminho_completo)
                print(f"Pasta '{nome_pasta}' criada em '{caminho_completo}'.")
            except OSError as e:
                print(f"Falha ao criar a pasta '{nome_pasta}' em '{caminho_completo}': {e}")

if __name__ == "__main__":
    caminhos_destino = ["F:\\pastas", "F:\\pastas2"]
    numero_pastas = 100
    criar_pastas_com_padrao(numero_pastas, caminhos_destino)

