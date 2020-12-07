# notes for class
# Atividade: construir classe pessoa com todos os métodos, ver métodos privados
class Pessoa: 
  nome: str
  sobrenome: str
  idade: int

  def nome_completo(self):
    print(self.nome + ' ' + self.sobrenome)
  
  def get_idade(self):
    return self.idade
  
  def set_idade(self, idade: int):
    self.idade = idade
    

p = Pessoa()
#p.set.idade()
#p.nome_completo()
print(p.get_idade())