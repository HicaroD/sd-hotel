import requests

class Hotel:
    def __init__(self):
        self.quartos = {}

    def listar_quartos(self):
        quartos = requests.get("http://localhost:8900/rooms/")
        quartos = quartos.json()["rooms"]

        print("Quartos disponíveis:\n")
        for quarto in quartos:
            numero, ocupado, descricao = quarto
            print(f"Número do quarto: {numero}")
            print(f"Descrição: {descricao}")
            print("--")
    def check_in(self, numero_quarto):
        check_in = requests.patch(f"http://localhost:8900/rooms/{numero_quarto}/checkin/")
        if check_in.status_code==200:
            check_in=check_in.json()
            print(check_in["detail"])
        else: 
            print("Não foi possível efetuar o check-in.") 

    def check_out(self, numero_quarto):
        check_out = requests.patch(f"http://localhost:8900/rooms/{numero_quarto}/checkout/")
        if check_out.status_code==200:
            check_out=check_out.json()
            print(check_out["detail"]) 
        else: 
            print("Não foi possível efetuar o check-out.") 
def main():
    hotel = Hotel()

    while True:
        print("\n=========================")
        print("\nSeja bem-vindo ao Hotel! ")
        print("\n=========================\n")
        print("1 - Listar quartos")
        print("2 - Check-in no quarto")
        print("3 - Checkout no quarto")
        print("4 - Sair\n")

        escolha = input("Escolha uma opção (1/2/3/4): "+"\n")
        print("=============================")
        if escolha == "1":
            hotel.listar_quartos()
        elif escolha == "2":
            numero_quarto = input("Digite o número do quarto para check-in: \n")
            hotel.check_in(numero_quarto)
        elif escolha == "3":
            numero_quarto = input("Digite o número do quarto para check-out: \n")
            hotel.check_out(numero_quarto)
        elif escolha == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
