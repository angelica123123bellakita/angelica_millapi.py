import csv
def registrar_propiedad(): 
   correlativo = input("Ingrese correlativo: ") 
   tipo_propiedad = input("Ingrese tipo de propiedad (1 = Casa, 2 = Departamento): ") 
   nro_dormitorios = input("Ingrese número de dormitorios: ")
   nro_baños = input("Ingrese número de baños: ") 
   precio = input("Ingrese precio: ") 
   tipo_propiedad_str = "Casa" if tipo_propiedad == '1' else "Departamento"

   with open('REGISTRO_PROPIEDADES_USADAS.csv', 'a', newline='') as file: writer = csv.writer(file) writer.writerow([correlativo, tipo_propiedad_str, nro_dormitorios, nro_baños, precio])  
 
def listar_propiedades():
    print("\nListado de propiedades:")
    with open('REGISTRO_PROPIEDADES_USADAS.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        
        print("{:<12} {:<20} {:<22} {:<15} {}".format("CORRELATIVO", "TIPO-DE-PROPIEDAD", "NUMERO-DE-DORMITORIOS", "NUMERO-DE-BAÑOS", "PRECIO"))
        for row in reader:
            print("{:<12} {:<20} {:<22} {:<15} {}".format(row[0], row[1], row[2], row[3], row[4]))
  
def imprimir_oferta_por_tipo(tipo):
     tipo_propiedad_str = "Casa" if tipo == '2' else "Departamento"
     output_file = f'PROPIEDADES_{tipo_propiedad_str}.csv'

     with open('REGISTRO_PROPIEDADES_USADAS.csv', 'r', newline='') as file:
        reader = csv.reader(file)

        with open(output_file, 'w', newline='') as outfile: 
              writer = csv.writer(outfile)
             # Escribir encabezado 
              writer.writerow(["Correlativo", "Tipo-Propiedad", "Numero de dormitorios", "Numero de baños", "Precio"]) 
              for row in reader:
                 if row[1] == tipo_propiedad_str:
                     writer.writerow(row)

print(f"Se ha generado el archivo {output_file} con las propiedades tipo {tipo_propiedad_str}.")  


def menu(): 
  while True:  
      print("\n--- Menú ---") 
      print("1. Registrar propiedad") 
      print("2. Listar propiedades") 
      print("3. Imprimir oferta por tipo de propiedad") 
      print("4. Salir del programa") 

opcion = input("Seleccione una opción: ") 
if opcion == '1':
     registrar_propiedad() 
elif opcion == '2':
     listar_propiedades() 
elif opcion == '3':
     tipo = input("Ingrese el tipo de propiedad (1 = Casa, 2 = Departamento): ")
     if tipo in ['1', '2']: 
         imprimir_oferta_por_tipo(tipo) 
     else: 
         print("Opción no válida.") 
elif opcion == '4': 
     print("Saliendo del programa...") 
     break
else: 
    print("Opción no válida. Intente de nuevo.") 

if __name__ == "__main__": menu()  

