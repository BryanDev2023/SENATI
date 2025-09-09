# ===========
# PPT GAME :D
# ===========

from random import choice, choices
from time import sleep

# Options 
OPTIONS_GAME = ["Piedra", "Papel", "Tijera"]

def eleccion_jugador():
    while True:
      try:
        print("1 para PIEDRA, 2 para PAPEL y 3 para TIJERA")
        eleccion = int(input("Elige una opción: "))
        
        if eleccion in [1, 2, 3]:
            return OPTIONS_GAME[eleccion - 1]
        print("Elige un ataque por favor!")
      except ValueError:
        print("Entrada inválida, intenta de nuevo.")
        
        
def eleccion_ia(ultima_eleccion: str):
    if not ultima_eleccion:
        return choice(OPTIONS_GAME)
    
    probabilidades = {
        "Piedra": [("Papel", .6), ("Tijera", .2), ("Piedra", .2)],
        "Papel": [("Tijera", .6), ("Piedra", .2), ("Papel", .2)],
        "Tijera": [("Piedra", .6), ("Papel", .2), ("Tijera", .2)]
    }
    
    enemigos, pesos = zip(*probabilidades[ultima_eleccion])
    return choices(enemigos, pesos)[0]

def combate(jugador, enemigo):
    reglas = {
        ("Piedra", "Tijera"): "GanaJugador",
        ("Papel", "Piedra"): "GanaJugador",
        ("Tijera", "Papel"): "GanaJugador",
        ("Tijera", "Piedra"): "GanaEnemigo",
        ("Papel", "Tijera"): "GanaEnemigo",
        ("Piedra", "Papel"): "GanaEnemigo"
    }
    return "Empate" if jugador == enemigo else reglas.get((jugador, enemigo), "Empate")

def mostrar_resultado(resultado: str, vidas_jugador: int, vidas_enemigo: int):
    mensajes = {
        "Empate": "¡Empate!",
        "GanaJugador": "¡Ganaste! 😃",
        "GanaEnemigo": "Perdiste... 😢"
    }
    print(f"{mensajes[resultado]} / Tú: {vidas_jugador} | Enemigo: {vidas_enemigo}\n")
    
def verificar_final(vidas_jugador: int, vidas_enemigo: int, ganadas: int, perdidas: int):
    finales = {
        0: ("🏆 ¡Ganaste la partida campeón!", f"Marcador final: {ganadas} victorias y {perdidas} derrotas"),
        1: ("💀 Perdiste, suerte la próxima.", f"Marcador final: {ganadas} victorias y {perdidas} derrotas")
    }

    if vidas_jugador == 0 or vidas_enemigo == 0:
        mensaje, marcador = finales[0 if vidas_enemigo == 0 else 1]
        print(f"{mensaje}\n{marcador}")
        return True
    return False
    
def empezar_juego_ppt():
    vidas_jugador, vidas_enemigo = 3, 3
    ganadas, perdidas = 0, 0
    
    ultima_eleccion = None
    
    print("""
    =========================    
    PPT GAME - Bryan Quintana
    =========================
    """)
    
    while vidas_jugador > 0 and vidas_enemigo > 0:
        jugador = eleccion_jugador()
        print(f"Elegiste: {jugador}")
        
        sleep(1)
        
        enemigo = eleccion_ia(ultima_eleccion)
        print(f"El enemigo eligió: {enemigo}\n")
        
        ultima_eleccion = jugador
        
        sleep(2.5)
        
        resultado = combate(jugador, enemigo)
        
        if resultado == "GanaJugador":
            vidas_enemigo -= 1
            ganadas += 1
        elif resultado == "GanaEnemigo":
            vidas_jugador -= 1
            perdidas += 1
            
        mostrar_resultado(resultado, vidas_jugador, vidas_enemigo)
        
        sleep(1.25)
        
        if verificar_final(vidas_jugador, vidas_enemigo, ganadas, perdidas):
            print("""
            ========================
            FIN DEL JUEGO - PPT GAME
            ========================
               ¡Gracias por jugar!  
            ========================
            """)
            break
        
# =========================
# Empezar juego - EJECUCIÓN
# =========================

if __name__ == "__main__":
    empezar_juego_ppt()