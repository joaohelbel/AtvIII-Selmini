import requests
from concurrent.futures import ThreadPoolExecutor

url = 'http://127.0.0.1:5000/pedido'

def enviar_pedido():
    try:
        response = requests.post(url)
        if response.status_code == 202:
            print("Pedido enviado com sucesso!")
        else:
            print(f"Falha ao enviar pedido: {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar o pedido: {e}")

if __name__ == "__main__":
    print("🔁 Enviando 20 pedidos simultâneos...")
    with ThreadPoolExecutor(max_workers=20) as executor:
        for _ in range(20):
            executor.submit(enviar_pedido)
