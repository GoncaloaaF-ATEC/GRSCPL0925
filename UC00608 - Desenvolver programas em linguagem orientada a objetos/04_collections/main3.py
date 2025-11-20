"""

lista       - []
tuplo       - ()
set         - {}
dicionario  - { : }


"""

aluno = {"nome": "Ricardo", "Turma": "GRSC", "Ano Inscricao": 2025, "Aprovado": False}

print(aluno["nome"])
print(aluno["Turma"])
# print(aluno["ano_inscricao"]) # se a key nao existir da erro

print(aluno.get("Ano Inscricao"))
print(aluno.get("ano_inscricao"))  # se a key nao existir -> None

print(aluno.get("Aprovado"))

aluno["Aprovado"] = True  # alterar um valor

print(aluno.get("Aprovado"))

"""
Criamos dict 
acedemos a valores 
mudamos valores 
add valor

"""

print(aluno)
aluno["Nota"] = 15  # add novo valor
print(aluno)

aluno.update({"Nota": 18})

print(aluno)

aluno.update({"idade": 18})  # edita se existir, add se nao existir

print(aluno)

aluno.update({"idade": 25, "Nota": 12})

print(aluno)

# remover
aluno.pop("Nota")
print(aluno)

aluno.popitem()  # remove sp o ultimo
print(aluno)

del aluno["Aprovado"]
print(aluno)

# infos

print(aluno.values())
print(aluno.keys())
print(aluno.items())

# iter
print("------for elm in aluno:-----")
for elm in aluno:
    print(elm)

print("-----for elm in aluno.keys():------")
for elm in aluno.keys():
    print(elm)

print("-----for elm in aluno.values():------")
for elm in aluno.values():
    print(elm)

print("-----for elm in aluno.values():------")
for elm in aluno.items():
    print(elm)

print("-----for elm in aluno.value" "" "" "s():------")
for chave, valor in aluno.items():
    print(f"chave: {chave} valor: {valor}")
