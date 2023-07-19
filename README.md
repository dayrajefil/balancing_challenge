# O Desafio - CustomerSuccess Balancing

Este desafio consiste em criar um sistema de balanceamento entre clientes e Customer Success (CSs). Os CSs são Gerentes de Sucesso que são responsáveis pelo acompanhamento estratégico dos clientes.

O objetivo do sistema é associar cada cliente a um CS com capacidade de atendimento adequada, levando em consideração o tamanho do cliente/empresa. Quanto maior o cliente, mais capacitado deve ser o CS atribuído.

## Premissas

- Não há limite de clientes por CS
- Clientes podem ficar sem serem atendidos
- Os CSs podem não estar disponíveis
- Clientes são atendidos por CSs onde: nivel do customer success >= nível do customer

## Como testar

### Teste em Ruby

No terminal, execute os comandos:

```
cd ruby
ruby test_customer_success.rb
```

### Teste em Python

No terminal, execute os comandos:

```
cd python
python3 test_customer_success.py
```

## Considerações finais

O método 'execute' foi desenvolvido atendendo às premissas do desafio, criando um sistema de balanceamento e passando nos testes pré-existentes. Os testes em Python foram implementados do zero, com base no código em Ruby.
