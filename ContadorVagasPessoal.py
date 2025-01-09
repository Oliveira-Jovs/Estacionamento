arquivo = open("C:/Users/oliveira/AreaDesenvolvimento/Estacionamento/Coordenadas_Vagas/Coordenadas_Vagas2.txt", "r")
conteudo = arquivo.readlines()
arquivo.close()


def pegar_coordenadas():
    vagas = []

    for vaga in conteudo:
        # Divide a linha em partes e extrai os números após "="
        partes = vaga.split()
        coordenadas = []
        for parte in partes:
            if "=" in parte:
                _, valor = parte.split("=")
                valor = valor.strip(',')  # Remove a vírgula se houver
                coordenadas.append(int(valor))  # Converte os valores para inteiros
        vagas.append(coordenadas)
    return vagas

vagas = pegar_coordenadas()

