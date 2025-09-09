def calculadora_avanzada():
    """
    =========================================================
    Calculadora avanzada con operaciones básicas y combinadas
    =========================================================
    """
    
    print("""
    =============================================
    CALCULADORA AVANZADA - PYTHON                
    ---------------------------------------------
    Operaciones disponibles:                     
      +  : Suma                                  
      -  : Resta                                 
      *  : Multiplicación                        
      /  : División                              
      () : Paréntesis para operaciones combinadas
      salir : Para terminar el programa          
    =============================================
    """)
    
    while True:
        try:
            expresion = input("\nIngrese una expresión matemática (o 'salir'): ").strip()
            
            if expresion.lower() == 'salir':
                print("¡Gracias por usar la calculadora!")
                break
            
            if not expresion:
                continue
            
            resultado = calcular_expresion(expresion)
            print(f"Resultado: {expresion} = {resultado}")
            
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
        except Exception as e:
            print(f"Error: {str(e)}")

def calcular_expresion(expresion):
    """
    =======================================================
    Función principal para calcular expresiones matemáticas
    =======================================================
    """
    expresion = expresion.replace(" ", "")
    
    if not es_expresion_valida(expresion):
        raise ValueError("Expresión no válida")
    
    # Procesar paréntesis primero
    expresion = procesar_parentesis(expresion)
    
    # Evaluar la expresión resultante
    return evaluar_operaciones(expresion)

def es_expresion_valida(expresion):
    """
    =============================================
    Valida que la expresión matemática sea válida
    =============================================
    """
    caracteres_validos = "0123456789+-*/()."
    if any(c not in caracteres_validos for c in expresion if c != ' '):
        return False
    
    # Verificar paréntesis balanceados
    balance = 0
    for c in expresion:
        if c == '(':
            balance += 1
        elif c == ')':
            balance -= 1
            if balance < 0:
                return False
    
    return balance == 0

def procesar_parentesis(expresion):
    """
    =========================================================
    Procesa y resuelve todas las expresiones entre paréntesis
    =========================================================
    """
    while '(' in expresion:
        inicio = expresion.rfind('(')
        fin = expresion.find(')', inicio)
        
        if fin == -1:
            raise ValueError("Paréntesis no balanceados")
        
        # Calcular la expresión dentro de los paréntesis
        contenido = expresion[inicio + 1:fin]
        resultado = str(evaluar_operaciones(contenido))
        
        # Reemplazar con el resultado
        expresion = expresion[:inicio] + resultado + expresion[fin + 1:]
    
    return expresion

def evaluar_operaciones(expresion):
    """
    =========================================================================
    Evalúa expresiones sin paréntesis respetando la precedencia de operadores
    =========================================================================
    """
    # Convertir a tokens
    tokens = tokenizar(expresion)
    
    # Primero multiplicaciones y divisiones
    tokens = procesar_operaciones(tokens, ['*', '/'])
    
    # Luego sumas y restas
    tokens = procesar_operaciones(tokens, ['+', '-'])
    
    if len(tokens) != 1:
        raise ValueError("Expresión no válida")
    
    return tokens[0]

def tokenizar(expresion):
    """
    ========================================================
    Convierte una expresión en tokens numéricos y operadores
    ========================================================
    """
    tokens = []
    numero_actual = ""
    
    for caracter in expresion:
        if caracter in '+-*/':
            if numero_actual:
                tokens.append(float(numero_actual))
                numero_actual = ""
            tokens.append(caracter)
        else:
            numero_actual += caracter
    
    if numero_actual:
        tokens.append(float(numero_actual))
    
    return tokens

def procesar_operaciones(tokens, operadores):
    """
    ======================================================
    Procesa operaciones específicas en una lista de tokens
    ======================================================
    """
    i = 0
    while i < len(tokens):
        if isinstance(tokens[i], str) and tokens[i] in operadores:
            # Realizar la operación
            izquierda = tokens[i-1]
            operador = tokens[i]
            derecha = tokens[i+1]
            
            resultado = operar(izquierda, operador, derecha)
            
            # Reemplazar los tres elementos por el resultado
            tokens[i-1:i+2] = [resultado]
        else:
            i += 1
    
    return tokens

def operar(a, operador, b):
    """
    ===================================================================
    Función central que ejecuta la operación matemática correspondiente
    ===================================================================
    """
    # Diccionario de operaciones para evitar múltiples if/elif
    operaciones = {
        '+': suma,
        '-': resta,
        '*': multiplicacion,
        '/': division
    }
    
    if operador not in operaciones:
        raise ValueError(f"Operador no válido: {operador}")
    
    return operaciones[operador](a, b)

# Funciones específicas para cada operación matemática
def suma(a, b):
    """Realiza la operación de suma"""
    return a + b

def resta(a, b):
    """Realiza la operación de resta"""
    return a - b

def multiplicacion(a, b):
    """Realiza la operación de multiplicación"""
    return a * b

def division(a, b):
    """Realiza la operación de división con validación"""
    if b == 0:
        raise ZeroDivisionError("División por cero")
    return a / b

# Función para mostrar ejemplos de uso
def mostrar_ejemplos():
    """Muestra ejemplos de uso de la calculadora"""
    ejemplos = [
        "5 + 3",
        "10 - 2 * 3",
        "(5 + 3) * 2",
        "15 / 3 + 2",
        "2 * 3 + 4 * 5",
        "10 - 5 + 3 * 2"
    ]
    
    print(""""\n
    ===========================================
    Ejemplos de uso de la calculadora avanzada:
    ===========================================   
    """)
    
    for ejemplo in ejemplos:
        try:
            resultado = calcular_expresion(ejemplo)
            print(f"{ejemplo} = {resultado}")
        except Exception as e:
            print(f"{ejemplo} → Error: {e}")

if __name__ == "__main__":
    # Mostrar ejemplos primero
    mostrar_ejemplos()
    
    # Ejecutar la calculadora
    calculadora_avanzada()