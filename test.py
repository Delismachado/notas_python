# variáveis 
idade = 10
print(id(idade))

nome = "oi"
salario = 1500.00
verdadeiro = False


idade = "teste"
print(id(idade))

# listas compostas
#- list
name_l =  ['nome1', 'nome2', 'nome3', 0, ['one', 'two']]
print (name_l)

# tuplas são imutáveis
#- tuple 
name_t = ('nome1', 'nome2', 'nome3', 0)
print (name_t)

# formato json
#- dict
register = {
  'name': 'name1',
  'idade': 10,
  'email': 'teste.com'
}
print(register['email'])
