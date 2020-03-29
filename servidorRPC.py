
def upload(file):
    a.append(file)
def download(file):
    if file in a:
        print ("Download efetuado:",file)
def delete(file):
    if file in a:
        a.remove(file)
        print("Removido")
def listar():
    for i in a:
        print (i)
