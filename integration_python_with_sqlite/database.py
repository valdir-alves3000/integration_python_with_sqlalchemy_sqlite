import random

from sqlalchemy import (Column, Float, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    endereco = Column(String(255), nullable=False)
    contas = relationship("Conta", back_populates="cliente")

    def __repr__(self):
        return f"<Cliente(id={self.id}, nome='{self.nome}', cpf='{self.cpf}', endereco='{self.endereco}')>"
class Conta(Base):
    __tablename__ = 'conta'

    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    agencia = Column(String, nullable=False)
    num = Column(Integer, nullable=False, unique=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    saldo = Column(Float, nullable=False)
    cliente = relationship("Cliente", back_populates="contas")

engine = create_engine('sqlite:///bank.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def generete_number(min,max):
    if not isinstance(min, int) or not isinstance(max, int):
        raise ValueError("Os parâmetros min e max devem ser inteiros.")
    if min >= max:
        raise ValueError("O valor de min deve ser menor que o valor de max.")
    number_account = random.randint(min, max)
    return number_account

users = [
    {
        "nome": "João Silva",
        "endereco": "Rua A, 123"
    },
    {
        "nome": "Maria Oliveira",
        "endereco": "Avenida B, 456"
    },
    {
        "nome": "Carlos Pereira",
        "endereco": "Travessa C, 789"
    },
    {
        "nome": "Ana Costa",
        "endereco": "Praça D, 101"
    },
    {
        "nome": "Paulo Souza",
        "endereco": "Estrada E, 202"
    }
]

for user in users:
    cpf = generete_number(00000000000,99999999999)
    cliente = session.query(Cliente).filter_by(cpf=cpf).first()
    if not cliente:
        cliente = Cliente(nome=user["nome"], cpf=cpf, endereco=user["endereco"])
        session.add(cliente)
        session.commit()


    number_account = generete_number(00000,99999)
    saldo = generete_number(10,1000)
    agencia = generete_number(0000,9999)
    conta = session.query(Conta).filter_by(num=number_account).first()
    if not conta:
        tipo = "Corrente" if saldo % 2 == 0 else "Poupança"
        conta = Conta(tipo=tipo, agencia=agencia, num=number_account, saldo=saldo, cliente=cliente)
        session.add(conta)
        session.commit()

def get_clientes():
    return session.query(Cliente).all()

def get_contas():
    return session.query(Conta).all()

clientes = get_clientes()
for cliente in clientes:
    print(cliente.nome, cliente.cpf, cliente.endereco)
    for conta in cliente.contas:
        print(f"Conta {conta.tipo} com saldo de {conta.saldo}")

contas = get_contas()
for conta in contas:
    print(f"Conta: {conta.tipo}, Agencia: {conta.agencia}, Conta: {conta.num}, Saldo: {conta.saldo} Titular: {conta.cliente.nome}")
