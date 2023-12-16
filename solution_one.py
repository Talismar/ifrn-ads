import threading


class Filosofo:
    def __init__(self, nome, garfo_esquerdo, garfo_direito):
        self.nome = nome
        self.garfo_esquerdo = garfo_esquerdo
        self.garfo_direito = garfo_direito

    def comer(self):
        with self.garfo_esquerdo, self.garfo_direito:
            print(f"{self.nome} está comendo.")


def jantar_dos_filosofos_limitacao_acessos():
    garfos = [threading.Lock() for _ in range(5)]
    threads = []

    for i in range(5):
        nome = f"Filósofo {i}"
        garfo_esquerdo = garfos[i]
        garfo_direito = garfos[(i + 1) % 5]

        filosofo = Filosofo(nome, garfo_esquerdo, garfo_direito)

        thread = threading.Thread(target=filosofo.comer)
        threads.append(thread)

        thread.start()

    for thread in threads:
        thread.join()


jantar_dos_filosofos_limitacao_acessos()
