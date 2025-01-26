#### Syanne Karoline Moreira Tavares - 202104940029
from abc import ABC, abstractmethod
from datetime import datetime

# Cores ANSI
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# Classe abstrata - State
class AulaState(ABC):
    @abstractmethod
    def aulaIniciada(self, aula):
        pass

    @abstractmethod
    def aulaEncerrada(self, aula):
        pass

    @abstractmethod
    def excluirAula(self, aula):
        pass

##### Subclasses -> PlanejadaState, EmRealizacaoState, RealizadaState, NaoRealizadaState
# Estado Planejada
class PlanejadaState(AulaState):
    def aulaIniciada(self, aula):

        if datetime.now().replace(second=0, microsecond=0) > aula.dtIniPlan:  # Verifica se a data/hora atual já passou da planejada
            print(RED,"A data planejada para aula já passou. Aula marcada como Não Realizada.",RESET) #Quando (Hoje> fata e hora prevista)
            aula.state = NaoRealizadaState()

        else:
            aula.dtIniReal = datetime.now().replace(second=0, microsecond=0)
            print(GREEN, "Aula iniciada com sucesso.",RESET)
            aula.state = EmRealizacaoState()

    def aulaEncerrada(self, aula):
        print(RED,"Aula não pode ser encerrada enquanto não estiver em realização.",RESET)

    def excluirAula(self, aula):
        print(GREEN,"Aula planejada excluída com sucesso.",RESET)
        aula.state = None
        
# Estado EmRealizacao
class EmRealizacaoState(AulaState):
    def aulaIniciada(self, aula):
        print(RED,"Aula já está em realização.",RESET)

    def aulaEncerrada(self, aula):
        aula.dtFimReal = datetime.now()  # Registrar a hora final real
        # Imprimir diretamente com a formatação brasileira
        
        print(GREEN + f"Aula encerrada com sucesso. Horários da aula:")
        print(f"Hora de início planejada: {aula.dtIniPlan.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Hora de fim planejada: {aula.dtFimPlan.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Hora de início real: {aula.dtIniReal.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Hora de fim real: {aula.dtFimReal.strftime('%d/%m/%Y %H:%M:%S')}")
        print(RESET)
        
        aula.state = RealizadaState()
        print(f"\n--- Estado atual: {aula.mostrarEstado()} ---")


    def excluirAula(self, aula):
        print(RED,"Aula excluída.",RESET)
        aula.state = None

# Estado Realizada
class RealizadaState(AulaState):
    def aulaIniciada(self, aula):
        pass

    def aulaEncerrada(self, aula):
        pass

    def excluirAula(self, aula):
        pass

# Estado NaoRealizada
class NaoRealizadaState(AulaState):
    def aulaIniciada(self, aula):
        pass

    def aulaEncerrada(self, aula):
        pass

    def excluirAula(self, aula):
        pass

# Classe Contexto
class Aula:
    def __init__(self, dtIniPlan, dtFimPlan):
        self.dtIniPlan = dtIniPlan
        self.dtFimPlan = dtFimPlan
        self.dtIniReal = None
        self.dtFimReal = None
        self.state = PlanejadaState()

    def aulaIniciada(self):
        self.state.aulaIniciada(self)

    def aulaEncerrada(self):
        self.state.aulaEncerrada(self)

    def excluirAula(self):
        self.state.excluirAula(self)

    def mostrarEstado(self):
        return self.state.__class__.__name__

# Função para pedir data e hora ao usuário
def obter_data_hora(mensagem):
    while True:
        try:
            data_hora_str = input(mensagem)
            data_hora = datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M")
            return data_hora
        except ValueError:
            print(RED,"Formato inválido. Por favor, use o formato dd/mm/aaaa hh:mm.",RESET)
# Função para validar o horário de início e fim
def verificar_horarios(dtIni, dtFim):
    # Verifica se o horário de fim é maior que o de início
    if dtFim <= dtIni:
        print(RED, "Erro: A hora de fim deve ser maior que a hora de início.", RESET)
        return False

    # Verifica se a data de início é no futuro
    if dtIni < datetime.now():
        print(RED, "Erro: planeje uma data no futuro! A data e hora planejada deve ser maior que a atual.", RESET)
        return False

    return True

# Função para interação com o usuário
def gerenciarAula(aula):
    while True:
        if isinstance(aula.state, NaoRealizadaState):
            print("Saindo do programa.")
            break

        print(f"\n--- Estado atual: {aula.mostrarEstado()} ---")
        print("Escolha uma ação:")
        print("1. Iniciar Aula")
        print("2. Encerrar Aula")
        print("3. Excluir Aula")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            aula.aulaIniciada()
        elif opcao == "2":
            aula.aulaEncerrada()
            print("Saindo do programa.")
            break
        elif opcao == "3" :
            aula.excluirAula()
            print("Saindo do programa.")
            break
        else:
            print(RED,"Opção inválida, tente novamente.",RESET)

# Main
if __name__ == "__main__":
    print("Bem-vindo ao sistema de gerenciamento de aulas!\n")
    
    # Obtendo as datas e horas do usuário
    dtIni = obter_data_hora("Digite a data e hora de início planejada da aula (dd/mm/aaaa hh:mm): ")
    dtFim = obter_data_hora("Digite a data e hora de fim planejada da aula (dd/mm/aaaa hh:mm): ")
    if not verificar_horarios(dtIni, dtFim):
        print(RED, "Não é possível continuar. A aula não será cadastrada.", RESET)
    else:
        aula = Aula(dtIni, dtFim)
        gerenciarAula(aula)
