def empezar_eval():
    print("Empezando evaluación...\n")
    
    n1 = float(input("Ingrese la primera nota: "))
    n2 = float(input("Ingrese la segunda nota: "))
    n3 = float(input("Ingrese la tercera nota: "))
    
    asistencia = float(input("Ingrese el porcentaje de asistencia (0-100): "))
    
    promedio = round(evaluar_notas(n1, n2, n3), 2)
    print(f"El promedio de las notas es: {promedio}")
    
    resultado(promedio, asistencia)
        
def resultado(promedio: float, asistencia: float):
    if promedio >= 10.5:
        print("\n¡Aprobado! 🎉")
        dar_obsequio(promedio)
    else:
        print("\nDesaprobado. 😞")
        evaluar_asistencia(asistencia)
    
def evaluar_asistencia(asistencia: float):
    if asistencia > 60:
        print("Va a subsanación. 😐")
    else:
        print("Repite curso por baja asistencia. 😞")
        
def dar_obsequio(promedio: float):
    obsequios = [
        ("Beca completa", 20),
        ("Media beca", 18),
        ("Audífonos", 17),
        ("Mochila", 15),
        ("Lapicero", 12)
    ]
    
    for obsequio, nota_minima in obsequios:
        if promedio >= nota_minima:
            print(f"¡Felicidades! Has ganado un obsequio: {obsequio} 🎁")
            return
    
def evaluar_notas(n1: float, n2: float, n3: float) -> float:
    return (n1 + n2 + n3) / 3

if __name__ == "__main__":
    empezar_eval()
