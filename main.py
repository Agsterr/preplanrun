#!/home/tiago/.pyenv/shims/python

def distribuir_corrida(D_total, V_inicial, C, razao):
    distancias = []
    velocidades = []
    
    # Calcular a soma total da progressão geométrica para normalizar as distâncias
    soma_geometrica = sum(razao ** (C - i) for i in range(1, C + 1))
    
    # Para cada ciclo, calcular a distância e a velocidade
    for n in range(1, C + 1):
        # Distância proporcional
        distancia = D_total * (razao ** (C - n)) / soma_geometrica
        distancias.append(distancia)
        
        # Velocidade proporcional (aumenta a cada ciclo)
        velocidade = V_inicial / (razao ** (n - 1))
        velocidades.append(velocidade)
    
    return distancias, velocidades



def exec(D_total, V_inicial, C, razao):
    distancias, velocidades = distribuir_corrida(D_total, V_inicial, C, razao)

# Exibindo os resultados
    etapa=0
    for i, (dist, vel) in enumerate(zip(distancias, velocidades), start=1):
        etapa+=dist
        print(f"Ciclo {i}: Distância = {dist:.2f} m, Velocidade = {(vel*1000)/60:.6f} s/m - etapa {etapa}")



def main():
    print('configuere sua corrida')

    distanciaTotalInformada = input('Distância total ')
    distanciaTotal = int(distanciaTotalInformada)
     

    # Solicita a quantidade de ciclos ou valor padrão
    quantidadeCiclosInformada = input('Informe a quantidade de ciclos ou digite 0 para o valor padrão: ')
    

   # Se a entrada for vazia, assume o valor padrão 10
    if quantidadeCiclosInformada.strip() == '' or quantidadeCiclosInformada == '0':
        quantidadeCiclos = 10
    else:
        quantidadeCiclos = int(quantidadeCiclosInformada)
    
      
    V_inicial = 360 / 1000  # Tempo por metro no primeiro ciclo (300s/1000m)
    razao = 1.04  # Razão da progressão geométrica para aumentar a velocidade
    exec(distanciaTotal, V_inicial, quantidadeCiclos, razao)

if __name__ == "__main__":
    main()
     