# =================================================================
# PROYECTO INTEGRADOR: SISTEMA DE ANÁLISIS Y CONTROL DE PRODUCCIÓN
# =================================================================

# UNIDAD 4: Estructuras de Datos - Tuplas (Datos inmutables)
LINEAS_PRODUCCION = ("Línea 1 - Nutrición Animal Aves", "Línea 2 - Nutrición Animal Cerdos")

# UNIDAD 4: Estructuras de Datos - Listas (Almacenamiento dinámico)
base_de_datos_produccion = []

# UNIDAD 4: Funciones con parámetros
def evaluar_calidad(peso, temperatura):
    # UNIDAD 3: Condicionales (if) y Operadores Lógicos (and)
    # UNIDAD 2: Operadores Relacionales (>=, <=)
    # Condiciones: Batch mínimo de 1000 kg y Temp. máxima de 35 °C
    if peso >= 1000.0 and temperatura <= 35.0:
        return True # UNIDAD 2: Tipos de datos (Booleanos)
    else:
        return False

def registrar_lote():
    print("\n--- REGISTRO DE NUEVO LOTE ---")
    
    # UNIDAD 3: Bucle for iterando sobre una Tupla
    print("Líneas disponibles:")
    for indice in range(len(LINEAS_PRODUCCION)):
        print(f"{indice + 1}. {LINEAS_PRODUCCION[indice]}")
        
    # UNIDAD 2: Variables y Tipos de datos (Enteros y Cadenas)
    opcion_linea = int(input("Seleccione la línea de producción (1 o 2): "))
    
    # UNIDAD 3: Condicionales (if/elif/else)
    if opcion_linea == 1:
        linea_seleccionada = LINEAS_PRODUCCION[0]
    elif opcion_linea == 2:
        linea_seleccionada = LINEAS_PRODUCCION[1]
    else:
        print("❌ Error: Línea no válida. Ingrese 1 o 2.")
        return # Sale de la función si hay error

    codigo_lote = input("Ingrese el código del lote (Ej. L-001): ")
    
    # Ingreso de datos numéricos
    peso_lote = float(input("Ingrese el peso total en kg (Ej. 1200.5): ")) 
    temp_lote = float(input("Ingrese la temperatura del pellet en °C (Ej. 32.5): "))
    
    # Llamada a la función matemática
    es_aprobado = evaluar_calidad(peso_lote, temp_lote)
    
    # UNIDAD 4: Estructuras de Datos - Diccionarios
    registro = {
        "codigo": codigo_lote,
        "linea": linea_seleccionada,
        "peso": peso_lote,
        "temperatura": temp_lote,
        "aprobado": es_aprobado
    }
    
    # Agregamos el diccionario a la base de datos
    base_de_datos_produccion.append(registro)
    
    # ANUNCIO INMEDIATO DE APROBACIÓN O RECHAZO
    print("\n" + "="*45)
    print("   RESULTADO DE LA EVALUACIÓN DEL LOTE")
    print("="*45)
    if es_aprobado:
        print(f"✅ ESTADO: APROBADO")
        print(f"El lote {codigo_lote} cumple con los estándares de peso (>=1000kg) y temperatura (<=35°C).")
    else:
        print(f"❌ ESTADO: RECHAZADO")
        print(f"El lote {codigo_lote} NO cumple con los estándares. Revise peso o temperatura.")
    print("="*45 + "\n")

def analizar_datos():
    print("\n--- ANÁLISIS DE PRODUCCIÓN DEL TURNO ---")
    # UNIDAD 3: Condicional simple
    if len(base_de_datos_produccion) == 0:
        print("No hay datos registrados en este turno para analizar.")
        return

    total_peso = 0
    lotes_aprobados = 0
    
    # UNIDAD 3: Bucle for con diccionario
    for lote in base_de_datos_produccion:
        # UNIDAD 2: Operadores aritméticos (+, +=)
        total_peso += lote["peso"] 
        if lote["aprobado"] == True:
            lotes_aprobados += 1
            
        estado = "APROBADO" if lote["aprobado"] else "RECHAZADO"
        print(f"Lote: {lote['codigo']} | {lote['linea']} | {lote['peso']}kg | {lote['temperatura']}°C | Estado: {estado}")

    # UNIDAD 2: Prioridad de operaciones y cálculos
    porcentaje_aprobacion = (lotes_aprobados / len(base_de_datos_produccion)) * 100
    
    print("\n--- MÉTRICAS GLOBALES ---")
    print(f"Total de lotes procesados: {len(base_de_datos_produccion)}")
    print(f"Peso total acumulado: {total_peso} kg")
    print(f"Porcentaje de aprobación: {porcentaje_aprobacion}%")

# UNIDAD 1 y 3: Bucles anidados (while dentro de while)
def iniciar_sistema():
    print("\n" + "="*45)
    print("   SISTEMA DE CONTROL - NUTRICIÓN ANIMAL v1.0")
    print("="*45)

    while True: # Bucle exterior
        print("\n=== ESTADO DEL SISTEMA: EN ESPERA ===")
        iniciar = input("¿Desea iniciar un nuevo turno de producción? (S para Sí / N para No / X para Apagar): ").upper()
        
        if iniciar == "X":
            print("\n" + "="*45)
            print("   SISTEMA APAGADO CORRECTAMENTE")
            print("="*45)
            print("Turno finalizado. Los datos han sido resguardados.")
            input("\n>> Presione ENTER para cerrar esta ventana y salir del programa...")
            break 
            
        elif iniciar == "N":
            print("Entendido. El sistema permanecerá en estado de reposo.")
            
        elif iniciar == "S":
            print("\n=== NUEVO TURNO INICIADO ===")
            base_de_datos_produccion.clear() 
            
            while True: # Bucle interior
                print("\n=== PANEL DE CONTROL DEL MONITORISTA ===")
                print("1. Ingresar datos de lote (Mezcladora/Peletizadora)")
                print("2. Generar análisis y métricas del turno")
                print("3. Finalizar turno actual")
                
                opcion = input("Seleccione una opción: ")
                
                if opcion == "1":
                    registrar_lote()
                elif opcion == "2":
                    analizar_datos()
                elif opcion == "3":
                    print("Guardando registros del turno... Turno finalizado.")
                    break 
                else:
                    print("❌ Opción inválida. Intente de nuevo.")
        else:
            print("❌ Comando no reconocido. Por favor escriba S, N o X.")

if __name__ == "__main__":
    iniciar_sistema()