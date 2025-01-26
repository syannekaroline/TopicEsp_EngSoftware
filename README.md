# TopicEsp_EngSoftware

# Repositório de Exercícios - Tópicos Especiais em Engenharia de Software

Este repositório contém os códigos desenvolvidos na disciplina de **Tópicos Especiais em Engenharia de Software**.

## Exercícios



### 1. **Gerenciamento de Aulas**
**Descrição**: Um sistema para gerenciar o ciclo de vida de uma aula, incluindo estados como planejada, em realização, realizada e não realizada. Permite iniciar, encerrar ou excluir aulas, com validações baseadas no horário planejado e no horário atual.

**Padrão de Projeto Utilizado**: **State**
- O padrão State é implementado para modelar os diferentes estados de uma aula. Cada estado (Planejada, Em Realização, Realizada, Não Realizada) possui seu próprio comportamento e regras, facilitando a adição de novos estados ou modificações futuras.

---
### 2. **Sorveteria Interativa**
**Descrição**: Um sistema interativo que simula o funcionamento de uma sorveteria. O usuário pode montar pedidos personalizados escolhendo recipientes, sabores de sorvete e coberturas. O programa utiliza um menu para interação.

**Padrão de Projeto Utilizado**: **Decorator**
- O padrão Decorator é utilizado para adicionar dinamicamente funcionalidades ao sorvete (bolas e coberturas) sem modificar o código existente, garantindo flexibilidade e manutenção simples.

---

## Como Executar os Exercícios
Cada exercício foi implementado em Python e pode ser executado diretamente no terminal. Certifique-se de ter o Python instalado em sua máquina.

### Passos Gerais:
1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```
2. Navegue até o diretório do exercício desejado.
3. Execute o script correspondente:
   ```bash
   python nome_do_arquivo.py
   ```


