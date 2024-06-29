# Projeto: integration_python_with_sqlite

Este projeto demonstra a integração de Python com SQLite usando SQLAlchemy para gerenciar clientes e contas bancárias fictícias.

## Pré-requisitos

Certifique-se de ter Python 3 instalado juntamente com as seguintes bibliotecas Python:

- sqlalchemy

Você pode instalar as dependências executando o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

## Configuração do Ambiente

Este projeto utiliza SQLite como banco de dados. Certifique-se de que o arquivo `bank.db` seja criado automaticamente ao executar o código.

### Funcionalidades Implementadas

1. **Classes de Modelo**:

   - `Cliente`: Representa um cliente com atributos como nome, CPF, endereço e suas contas.
   - `Conta`: Representa uma conta bancária com tipo, agência, número, saldo e seu titular.

2. **População Inicial de Dados**:

   - O código inicializa o banco de dados SQLite com clientes e contas fictícias geradas aleatoriamente.

3. **Funções de Consulta**:
   - `get_clientes()`: Retorna todos os clientes armazenados no banco de dados.
   - `get_contas()`: Retorna todas as contas bancárias armazenadas no banco de dados.
