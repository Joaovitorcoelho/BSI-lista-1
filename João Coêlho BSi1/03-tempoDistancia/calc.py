def calculo (distancia,velocidade):
    resultado = (distancia / velocidade) * 60      
    horas,minutos = divmod(resultado,60)
    return horas,minutos
