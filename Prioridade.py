class Processo:
    def __init__(self, nome_pr, tempo_pr, prioridade):
        self.nome_pr = nome_pr
        self.tempo_pr = tempo_pr
        self.prioridade = prioridade

class Agendamento_prioridade:
    def __init__(self, processos):
        self.processos = processos

    def calcular_tempo_espera(self):
      
        self.processos.sort(key=lambda x: x.prioridade)

        tempo_espera = []
        total_tempo_espera = 0

  
        for i in range(len(self.processos)):
            if i == 0:
                tempo_espera.append(0) 
            else:
                tempo_espera.append(tempo_espera[i-1] + self.processos[i-1].tempo_pr)  

            total_tempo_espera += tempo_espera[i]

 
        tempo_medio = total_tempo_espera / len(self.processos)
        return tempo_medio


def pegar_processo_usuarios():
    processos = []
    n = int(input("Quantos processos você deseja inserir? "))
    for i in range(n):
        nome_pr = str(input(f"Digite o nome do processo {i+1}: "))
        tempo_pr = int(input(f"Digite o tempo de execução do processo {i+1}: "))
        prioridade = int(input(f"Digite a prioridade do processo {i+1} (quanto menor, maior a prioridade): "))
        processos.append(Processo(nome_pr, tempo_pr, prioridade))
    return processos


processos = pegar_processo_usuarios()


prioridade_agendamento = Agendamento_prioridade(processos)
tempo_medio = prioridade_agendamento.calcular_tempo_espera()
print(f'Tempo médio de espera (Prioridade): {tempo_medio} minutos')