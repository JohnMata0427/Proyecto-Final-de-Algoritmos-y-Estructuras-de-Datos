from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

if not os.path.isdir("Base de datos"): os.mkdir("Base de datos")

Raiz=Tk()
Raiz.geometry("1200x650")
Raiz.resizable(0,0)
Raiz.iconbitmap("Imagenes/Icono.ico")
Raiz.title("Gestion de calificaciones")

# -------------------------------- COLORES PARA LA GUI -------------------------------- #

Azul2="#006dff"
Gris="#c6c8c9"
Gris2="#414141"
Normal="#f0f0f0"

# -------------------------------- COLORES PARA VER EN CONSOLA -------------------------------- #

Azul="\33[34m"
Blanco="\33[0m"
Verde="\33[32m"
Rojo="\33[31m"
Negro="\33[30m"
Amarillo="\33[33m"

# -------------------------------- VARIABLES DE ENTRADA -------------------------------- #

global ArregloEstudiantes, IndiceEstudiantes

IndiceEstudiantes=0

Correo=StringVar()
Contrasena=StringVar()
CantidadEstudiantes=IntVar()
Semestre=StringVar()
Materia=StringVar()
Docente=StringVar()
NumeroDocente=StringVar()
Tipo_de_Ord=StringVar()
Ord=StringVar()
Segun=StringVar()
SegunB=StringVar()
Tipo_de_Bus=StringVar()
Buscar=StringVar()

TablaEntrada=[]
RegistroArchivo=[]
ArregloEstudiantes=[]

# -------------------------------- VENTANAS DEL PROGRAMA -------------------------------- #

Ventana1=Frame(Raiz, width=700, height=650, bg="grey", bd=3)
Ventana1.grid(row=0 ,column=0)

Ventana2=Frame(Raiz, width=500, height=650)
Ventana2.grid(row=0, column=1, padx=15)

VentanaMenu=Frame(Raiz, width=1200, height=650)
VentanaMenu.grid_forget()

# Ventana Registro de Estudiantes

VentanaRegistro=Frame(Raiz, width=1200, height=650)
VentanaRegistro.grid_forget()

VentanaApoyo1=Canvas(VentanaRegistro, width=1180, height=650)
VentanaApoyo1.grid_forget()

BarraDespla1=Scrollbar(VentanaRegistro, orient="vertical", command=VentanaApoyo1.yview)
BarraDespla1.grid_forget()

ContenidoRegistro=Frame(VentanaApoyo1)

VentanaR1=Frame(ContenidoRegistro)
VentanaR1.grid_forget()

VentanaR2=Frame(ContenidoRegistro)
VentanaR2.grid_forget()

VentanaR3=Frame(ContenidoRegistro)
VentanaR3.grid_forget()

# Ventana Ordenamiento de Estudiantes

VentanaOrdenamiento=Frame(Raiz, width=1200, height=650)
VentanaOrdenamiento.grid_forget()

VentanaApoyo2=Canvas(VentanaOrdenamiento, width=1180, height=650)
VentanaApoyo2.grid_forget()

BarraDespla2=Scrollbar(VentanaOrdenamiento, orient="vertical", command=VentanaApoyo2.yview)
BarraDespla2.grid_forget()

ContenidoOrdenamiento=Frame(VentanaApoyo2)

VentanaO1=Frame(ContenidoOrdenamiento)
VentanaO1.grid_forget()

VentanaO2=Frame(ContenidoOrdenamiento)
VentanaO2.grid_forget()

VentanaO3=Frame(ContenidoOrdenamiento)
VentanaO3.grid_forget()

# Ventana Busqueda de Estudiantes

VentanaBuscar=Frame(Raiz, width=1200, height=650)
VentanaBuscar.grid_forget()

VentanaApoyo3=Canvas(VentanaBuscar, width=1180, height=650)
VentanaApoyo3.grid_forget()

BarraDespla3=Scrollbar(VentanaBuscar, orient="vertical", command=VentanaApoyo3.yview)
BarraDespla3.grid_forget()

ContenidoBuscar=Frame(VentanaApoyo3)

VentanaB1=Frame(ContenidoBuscar)
VentanaB1.grid_forget()

VentanaB2=Frame(ContenidoBuscar)
VentanaB2.grid_forget()

VentanaB3=Frame(ContenidoBuscar)
VentanaB3.grid_forget()

# -------------------------------- FUNCIONES DE APOYO -------------------------------- #

def ValidarCredenciales():
    if Correo.get() != "docente@esfot.edu.ec" or Contrasena.get() != "Docente123*":
        messagebox.showerror("Credenciales Incorrectas", "¡Ingrese correctamente sus credenciales!")
    else:
        Ventana1.grid_forget()
        Ventana2.grid_forget()
        Raiz.config(bg="white")
        VentanaMenu.grid(row=0, column=0, pady=30)

def Salir():
    VentanaMenu.grid_forget()
    Contrasena.set("")
    Raiz.config(bg=Normal)
    Ventana1.grid(row=0, column=0)
    Ventana2.grid(row=0, column=1, padx=15)

def Anterior():
    VentanaRegistro.grid_forget()
    VentanaOrdenamiento.grid_forget()
    VentanaBuscar.grid_forget()
    VentanaMenu.grid(row=0, column=0, pady=30)
    BotonVolver.grid_forget()

def Enteros(Digito):
    Valor = Digito.widget.get()

    if not Valor.isdigit():
        Digito.widget.delete(0, END)
        Digito.widget.insert(0, ''.join(filter(str.isdigit, Valor)))

def Decimales(Digito):
    Valor = Digito.widget.get()

    if not all(c.isdigit() or c == '.' for c in Valor):
        Digito.widget.delete(0, END)
        Digito.widget.insert(0, ''.join(c for c in Valor if c.isdigit() or c == '.'))

def Palabras(Digito):
    Letra = Digito.widget.get()

    if not Letra.isalpha():
        Digito.widget.delete(0, 'end')
        Digito.widget.insert(0, ''.join(filter(str.isalpha, Letra)))

# -------------------------------- ALGORITMOS DE ORDENAMIENTO -------------------------------- #

def SelectiveSort(Arreglo, orden, por):
    # Complejidad temporal O(n^2) 
    if orden == "Ascendente":
        for i in range(len(Arreglo)):
            min=Arreglo[i]
            indice_min=i
            for j in range(i+1, len(Arreglo)):
                if Arreglo[j][f'{por}'] <= min[f'{por}']:
                    min=Arreglo[j]
                    indice_min=j
            Temporal=Arreglo[i]
            Arreglo[i]=min
            Arreglo[indice_min]=Temporal
    else:
        for i in range(len(Arreglo)):
            min=Arreglo[i]
            indice_min=i
            for j in range(i+1, len(Arreglo)):
                if Arreglo[j][f'{por}'] >= min[f'{por}']:
                    min=Arreglo[j]
                    indice_min=j
            Temporal=Arreglo[i]
            Arreglo[i]=min
            Arreglo[indice_min]=Temporal
    return Arreglo       

def BubbleSort(Arreglo, orden, por):
    # Complejidad temporal O(n^2)
    if orden == "Ascendente":
        for i in range(len(Arreglo)):
            for j in range (len(Arreglo)-1):
                if Arreglo[j][f'{por}']>=Arreglo[j+1][f'{por}']:
                    Temporal=Arreglo[j]
                    Arreglo[j]=Arreglo[j+1]
                    Arreglo[j+1]=Temporal
    else:
        for i in range(len(Arreglo)):
            for j in range (len(Arreglo)-1):
                if Arreglo[j][f'{por}']<=Arreglo[j+1][f'{por}']:
                    Temporal=Arreglo[j]
                    Arreglo[j]=Arreglo[j+1]
                    Arreglo[j+1]=Temporal
    return Arreglo

def InsertionSort(Arreglo, orden, por):
    # Complejidad temporal O(n^2)
    if orden == "Ascendente":
        for i in range(1, len(Arreglo)):
            comparativo=Arreglo[i]
            j=i-1
            while comparativo[f'{por}']<Arreglo[j][f'{por}'] and j>=0:
                Arreglo[j+1]=Arreglo[j]
                j-=1
            Arreglo[j+1]=comparativo
    else:
        for i in range(1, len(Arreglo)):
            comparativo=Arreglo[i]
            j=i-1
            while comparativo[f'{por}']>Arreglo[j][f'{por}'] and j>=0:
                Arreglo[j+1]=Arreglo[j]
                j-=1
            Arreglo[j+1]=comparativo
    return Arreglo  

def heapify(Arreglo, tamaño, i, orden, por): # Montificamiento para el Heap Sort
    if orden == "Ascendente":
        indi_max = i
        indi_izq = 2*i+1
        indi_der = 2*i+2

        if indi_izq < tamaño and Arreglo[i][f'{por}'] < Arreglo[indi_izq][f'{por}']:
            indi_max = indi_izq

        if indi_der < tamaño and Arreglo[indi_max][f'{por}'] < Arreglo[indi_der][f'{por}']:
            indi_max = indi_der
        
        if indi_max != i:
            Arreglo[i], Arreglo[indi_max] = Arreglo[indi_max], Arreglo[i]
            heapify(Arreglo, tamaño, indi_max, orden, por)
    else:
        indi_min = i
        indi_izq = 2*i+1
        indi_der = 2*i+2

        if indi_izq < tamaño and Arreglo[i][f'{por}'] > Arreglo[indi_izq][f'{por}']:
            indi_min = indi_izq

        if indi_der < tamaño and Arreglo[indi_min][f'{por}'] > Arreglo[indi_der][f'{por}']:
            indi_min = indi_der
        
        if indi_min != i:
            Arreglo[i], Arreglo[indi_min] = Arreglo[indi_min], Arreglo[i]
            heapify(Arreglo, tamaño, indi_min, orden, por)

def HeapSort(Arreglo, orden, por):
    tamaño=len(Arreglo)

    for i in range(tamaño//2-1, -1, -1):
        heapify(Arreglo, tamaño, i, orden, por)

    for i in range(tamaño-1, 0, -1):
        Arreglo[i], Arreglo[0] = Arreglo[0], Arreglo[i]
        heapify(Arreglo, i, 0, orden, por)

    return Arreglo

def merge(izquierda, derecha, orden, por): # Combinatoria para el Merge Sort
    resultado=[]
    indi_izq, indi_der=0,0
    if orden == "Ascendente":
        while indi_izq < len(izquierda) and indi_der < len(derecha):
            if izquierda[indi_izq][f'{por}'] < derecha[indi_der][f'{por}']:
                resultado.append(izquierda[indi_izq])
                indi_izq+=1
            else:
                resultado.append(derecha[indi_der])
                indi_der+=1
        if indi_der == len(derecha):
            resultado.extend(izquierda[indi_izq:])
        else:
            resultado.extend(derecha[indi_der:])
        return resultado
    else:
        while indi_izq < len(izquierda) and indi_der < len(derecha):
            if izquierda[indi_izq][f'{por}'] > derecha[indi_der][f'{por}']:
                resultado.append(izquierda[indi_izq])
                indi_izq+=1
            else:
                resultado.append(derecha[indi_der])
                indi_der+=1
        if indi_der == len(derecha):
            resultado.extend(izquierda[indi_izq:])
        else:
            resultado.extend(derecha[indi_der:])
        return resultado    
    
def MergeSort(Arreglo, orden, por):
    # Complejidad temporal O(n log n)
    if len(Arreglo) <= 1:
        return Arreglo
    else:
        indi_mitad = len(Arreglo)//2
        mitad_izq = Arreglo[:indi_mitad]
        mitad_der = Arreglo[indi_mitad:]

        mitad_izq=MergeSort(mitad_izq, orden, por)
        mitad_der=MergeSort(mitad_der, orden, por)

        return merge(mitad_izq, mitad_der, orden, por)

def QuickSort(Arreglo, orden, por):
    # Complejidad temporal O(n^2) en el peor caso
    # Complejidad temporal O(n log n) en promedio
    if len(Arreglo)<=1:
        return Arreglo
    else:
        if orden == "Ascendente":
            pivote_diccionario=Arreglo[-1]
            pivote=pivote_diccionario[f'{por}']

            menores=[]
            mayores=[]
            
            for elemento in Arreglo[:-1]:
                if elemento[f'{por}'] < pivote:
                    menores.append(elemento)
                else:
                    mayores.append(elemento)

            menores_combinados = QuickSort(menores, orden, por)
            mayores_combinados = QuickSort (mayores, orden, por)
        else:
            pivote_diccionario=Arreglo[-1]
            pivote=pivote_diccionario[f'{por}']

            menores=[]
            mayores=[]
            
            for elemento in Arreglo[:-1]:
                if elemento[f'{por}'] > pivote:
                    menores.append(elemento)
                else:
                    mayores.append(elemento)

            menores_combinados = QuickSort(menores, orden, por)
            mayores_combinados = QuickSort (mayores, orden, por)

    return menores_combinados + [pivote_diccionario] + mayores_combinados

# -------------------------------- ALGORITMOS DE BUSQUEDA -------------------------------- #

def LinearSearch(Arreglo, buscar, por):
    # Complejidad temporal O(n)

    Encontrados=[]
    for i in range(len(Arreglo)):
        if Arreglo[i][f'{por}']==buscar:
            Encontrados.append(Arreglo[i])
    return Encontrados

def BinarySearch(Arreglo, buscar, por):
    # Complejidad temporal O(n log n)

    for i in range(len(Arreglo)):
        for j in range(len(Arreglo) - 1):
            if Arreglo[j][f'{por}'] >= Arreglo[j + 1][f'{por}']:
                Temporal = Arreglo[j]
                Arreglo[j] = Arreglo[j + 1]
                Arreglo[j + 1] = Temporal

    Encontrados = []

    Inicio = 0
    Fin = len(Arreglo) - 1

    while Inicio <= Fin:
        Medio = (Inicio + Fin) // 2
        ElementoMedio = Arreglo[Medio]

        if buscar == ElementoMedio[f'{por}']:
            Encontrados.append(Arreglo[Medio])
            izquierda = Medio - 1
            derecha = Medio + 1

            while izquierda >= 0 and Arreglo[izquierda][f'{por}'] == buscar:
                Encontrados.append(Arreglo[izquierda])
                izquierda -= 1

            while derecha < len(Arreglo) and Arreglo[derecha][f'{por}'] == buscar:
                Encontrados.append(Arreglo[derecha])
                derecha += 1

            break
        elif buscar < ElementoMedio[f'{por}']:
            Fin = Medio - 1
        elif buscar > ElementoMedio[f'{por}']:
            Inicio = Medio + 1
        else:
            break

    return Encontrados

def InterpolationSearch(Arreglo, buscar, por):
    # Complejidad temporal O(n log n)

    for i in range(len(Arreglo)):
        for j in range(len(Arreglo) - 1):
            if Arreglo[j][f'{por}'] >= Arreglo[j + 1][f'{por}']:
                Temporal = Arreglo[j]
                Arreglo[j] = Arreglo[j + 1]
                Arreglo[j + 1] = Temporal

    Encontrados = []

    Inicio = 0
    Fin = len(Arreglo) - 1

    while Inicio <= Fin and Arreglo[Inicio][f'{por}'] <= buscar <= Arreglo[Fin][f'{por}']:
        Indice_buscado = Inicio + ((buscar - Arreglo[Inicio][f'{por}']) * (Fin - Inicio)) // (Arreglo[Fin][f'{por}'] - Arreglo[Inicio][f'{por}'])
        Indice_buscado = int(Indice_buscado)

        if Indice_buscado < 0 or Indice_buscado >= len(Arreglo):
            break

        Comparar = Arreglo[Indice_buscado][f'{por}']

        if buscar == Comparar:
            Encontrados.append(Arreglo[Indice_buscado])
            izquierda = Indice_buscado - 1
            derecha = Indice_buscado + 1

            while izquierda >= 0 and Arreglo[izquierda][f'{por}'] == buscar:
                Encontrados.append(Arreglo[izquierda])
                izquierda -= 1

            while derecha < len(Arreglo) and Arreglo[derecha][f'{por}'] == buscar:
                Encontrados.append(Arreglo[derecha])
                derecha += 1

            break
        elif buscar < Comparar:
            Fin = Indice_buscado - 1
        else:
            Inicio = Indice_buscado + 1

    return Encontrados

# -------------------------------- INICIO SESION -------------------------------- #

Imagen1=PhotoImage(file="Imagenes/logo_esfot_buho.png")
Label(Ventana1, image=Imagen1, width=700, height=640).grid(row=0, column=0)

Label(Ventana2, text="Inicie Sesión", font=("Times New Roman", 30, "bold", "italic")
      ).grid(row=0, column=0, columnspan=2, sticky="nsew", pady=25)

Label(Ventana2, text="Ingrese su correo: ", font=("Times New Roman", 15), anchor="w"
      ).grid(row=1, column=0, columnspan=2, sticky="ew", padx=22)

Label(Ventana2, text="Ingrese su contraseña: ", font=("Times New Roman", 15), anchor="w"
      ).grid(row=3, column=0, columnspan=2, sticky="ew", padx=22)

Entry(Ventana2, show="∙ ", textvariable=Contrasena, justify="left", fg=Gris2, font=("Times New Roman", 15, "bold")
      ).grid(row=4, column=0, columnspan=2, sticky="ew", padx=25)

Entry(Ventana2, width=40, textvariable=Correo, justify="left", fg=Gris2, font=("Times New Roman", 15)
      ).grid(row=2, column=0, columnspan=2, sticky="ew", padx=25)

Button(Ventana2, command=ValidarCredenciales, text="Entrar", font=("Times New Roman", 15, "bold"), cursor="hand2", bg=Azul2, fg="white"
       ).grid(row=5, column=0, sticky="e", padx=10, pady=10)

Button(Ventana2, command=Raiz.destroy, text="Salir", font=("Times New Roman", 15, "bold"), cursor="hand2", bg="antiquewhite4", fg="white"
       ).grid(row=5, column=1, sticky="w", padx=10, pady=10)

# -------------------------------- MENU PRINCIPAL -------------------------------- #

Imagen2=PhotoImage(file="Imagenes/150.png")
ImagenReducida=Imagen2.subsample(2,2)
ImagenMenu=Label(VentanaMenu, image=ImagenReducida)
ImagenMenu.grid(row=0, column=0, sticky="nsew")

def Opcion1():
    VentanaMenu.grid_forget()

    VentanaRegistro.grid(row=0, column=0, sticky="nsew")
    VentanaApoyo1.grid(row=0, column=0, sticky="nsew")
    BarraDespla1.grid(row=0, column=1, sticky="ns")
    VentanaApoyo1.configure(yscrollcommand=BarraDespla1.set)
    VentanaApoyo1.create_window((0, 0), window=ContenidoRegistro, anchor="nw")
    VentanaR1.grid(row=1, column=0, sticky="ew", pady=60, padx=120)
    BotonVolver.grid(row=0, column=0, sticky="nw")

def Opcion2():
    if IndiceEstudiantes != 0 and Docente.get():
        VentanaMenu.grid_forget()

        VentanaOrdenamiento.grid(row=0, column=0, sticky="nsew")
        VentanaApoyo2.grid(row=0, column=0, sticky="nsew")
        BarraDespla2.grid(row=0, column=1, sticky="ns")
        VentanaApoyo2.configure(yscrollcommand=BarraDespla2.set)
        VentanaApoyo2.create_window((0, 0), window=ContenidoOrdenamiento, anchor="nw")
        VentanaO1.grid(row=1, column=0, sticky="ew", pady=60, padx=120)
        BotonVolver.grid(row=0, column=0, sticky="nw")
    else:
        messagebox.showerror("Datos Inexistentes", "No existen calificaciones registradas\n\nRecuerde ingresar a la opción 1 y guardar su registro en el archivo de texto")

def Opcion3():
    if IndiceEstudiantes != 0 and Docente.get():
        VentanaMenu.grid_forget()
        VentanaBuscar.grid(row=0, column=0, sticky="nsew")
        VentanaApoyo3.grid(row=0, column=0, sticky="nsew")
        BarraDespla3.grid(row=0, column=1, sticky="ns")
        VentanaApoyo3.configure(yscrollcommand=BarraDespla3.set)
        VentanaApoyo3.create_window((0, 0), window=ContenidoBuscar, anchor="nw")
        VentanaB1.grid(row=1, column=0, sticky="ew", pady=60, padx=120)
        BotonVolver.grid(row=0, column=0, sticky="nw")
    else:
        messagebox.showerror("Datos Inexistentes", "No existen calificaciones registradas\n\nRecuerde ingresar a la opción 1 guardar su registro en el archivo de texto")

Label(VentanaMenu, text="Bienvenido al Sistema de Gestión de Calficaciones", font=("Times New Roman", 30), width=55
      ).grid(row=1, column=0, pady=15)

Button(VentanaMenu, text="1. Registrar calificaciones", bg=Azul2, fg="white", font=("Times New Roman", 20, "bold"), width=40, 
        command=Opcion1).grid(row=2, column=0, pady=15)

Button(VentanaMenu, text="2. Ordenar calificaciones", bg=Azul2, fg="white", font=("Times New Roman", 20, "bold"), width=40, 
        command=Opcion2).grid(row=3, column=0, pady=15)

Button(VentanaMenu, text="3. Buscar calificacion", bg=Azul2, fg="white", font=("Times New Roman", 20, "bold"), width=40,
        command=Opcion3).grid(row=4, column=0, pady=15)

Button(VentanaMenu, text="4. Salir", bg=Azul2, fg="white", font=("Times New Roman", 20, "bold"), width=40, 
        command=Salir).grid(row=5, column=0, pady=15)

# -------------------------------- REGISTRAR CALIFICACIONES -------------------------------- #

Label(VentanaR1, width=66, height=3, text="ESCUELA DE FORMACIÓN DE TECNOLOGOS\nREPORTE DE CALIFICACIONES", bd=1, relief="solid", bg=Azul2, fg="white", font=("Times New Roman", 18, "bold")
      ).grid(row=0, column=0, columnspan=14, sticky="nsew")

TextoSemestre=Label(VentanaR1, text=" Año/Semestre: ", anchor="w", bd=1, relief="solid", font=("Times New Roman", 12, "bold"))
TextoSemestre.grid(row=2, column=0, columnspan=14, sticky="nsew")

EntradaSemestre=Entry(TextoSemestre, textvariable=Semestre, font=("Times New Roman", 11))
EntradaSemestre.grid(row=2, column=1, sticky="nsew", padx=110)

TextoMateria=Label(VentanaR1, text=" Materia: ", anchor="w", bd=1, relief="solid", font=("Times New Roman", 12, "bold"))
TextoMateria.grid(row=3, column=0, columnspan=14, sticky="nsew")

EntradaMateria=Entry(TextoMateria, textvariable=Materia, font=("Times New Roman", 11))
EntradaMateria.grid(row=3, column=1, sticky="nsew", padx=70)
EntradaMateria.bind("<KeyRelease>", Palabras)

TextoEstudiantes=Label(VentanaR1, text=" Estudiantes: ", anchor="w" , bd=1, relief="solid", font=("Times New Roman", 12, "bold"))
TextoEstudiantes.grid(row=4, column=0, columnspan=14, sticky="nsew")

def ModificarTabla():
    global TablaEntrada, RegistroArchivo, ArregloEstudiantes
    RegistroArchivo=[]
    ArregloEstudiantes=[]
    for Fila in TablaEntrada:
        Fila['Nombre'].config(state="normal", font=("Times New Roman", 12))
        Fila['Apellido'].config(state="normal", font=("Times New Roman", 12))
        Fila['Correo'].config(state="normal", font=("Times New Roman", 12))
        Fila['Nota1'].config(state="normal", font=("Times New Roman", 12))
        Fila['Nota2'].config(state="normal", font=("Times New Roman", 12))
    VentanaR3.grid_forget()
    BotonModificarT.grid_forget()
    BotonRegistrar.grid(row=IndiceEstudiantes+6, column=0, columnspan=14, pady=10)

def Modificar():
    EntradaEstudiantes['state']="normal"
    EntradaMateria['state']="normal"
    EntradaSemestre['state']="normal"
    BotonModificar.grid_forget()
    BotonIngresar.grid(row=0, column=0, sticky="nsew", padx=170)

def NuevoReporte():
    global CantidadEstudiantes, Semestre, Materia, Docente, NumeroDocente, TablaEntrada, RegistroArchivo, IndiceEstudiantes, ArregloEstudiantes
    Nuevo=messagebox.askquestion("Nuevo Reporte", "¿Está seguro de generar un nuevo reporte?")
    if Nuevo == "yes":
        for widget in VentanaR2.winfo_children():
            widget.grid_forget()

        for widget in VentanaR3.winfo_children():
            widget.grid_forget()

        EntradaSemestre['state']="normal"
        EntradaMateria['state']="normal"
        EntradaEstudiantes['state']="normal"
        BotonModificar.grid_forget()
        BotonIngresar.grid(row=0, column=0, sticky="nsew", padx=170)

        VentanaR2.grid_forget()
        VentanaR3.grid_forget()
        ContenidoRegistro.update_idletasks()
        VentanaApoyo1.config(scrollregion=VentanaApoyo1.bbox("all"))
        VentanaRegistro.grid_forget()
        VentanaRegistro.grid(row=0, column=0)

        CantidadEstudiantes.set(0)
        Semestre.set("")
        Materia.set("")
        Docente.set("")
        NumeroDocente.set("")

        IndiceEstudiantes=0
        TablaEntrada=[]
        RegistroArchivo=[]
        ArregloEstudiantes=[]

def GuardarRegistro():
    global Docente
    if Docente.get() != "" and NumeroDocente.get() != "":
        Respuesta=messagebox.askquestion("Sistema de Gestión de Calificaiones", "¿Está seguro de guardar los datos registrados?")
        if Respuesta == "yes":
            with open("Base de datos/calificaciones.txt", "w") as archivo:
                archivo.write("\t\t\t\t   ESCUELA DE FORMACION DE TECNOLOGOS\n")
                archivo.write("\t\t\t\t\tREPORTE DE CALIFACIONES\n\n")
                archivo.write("Año/Semestre: {}\n".format(Semestre.get()))
                archivo.write(f"Materia: {Materia.get()}\n\n")
                archivo.write("N°\tNombre\t\tApellido\tCorreo\t\t\t\tNota 1\tNota 2\tTotal\n")

                for Estudiante in RegistroArchivo:
                    archivo.write(Estudiante+"\n")

                archivo.write("\n\nRESUMEN\n\nPromedio del Curso: {}\nEstudiantes Aprobados (14 - 20): {}\n".format(round(PromedioCurso, 2), Aprobados))
                archivo.write("Estudiantes Suspensos (09 - 13): {}\nEstudiantes Reprobados (01 - 08): {}\n".format(Suspensos, Reprobados))
                archivo.write(f"\n\t\t\t\t\t\t{Docente.get()}\n\t\t\t\t\t\t\tDocente\n\t\t\t\t\t\t\tESFOT\n\t\t\t\t\t\t     {NumeroDocente.get()}")

            print("\n=======================================================================================================================\n")

            print(Negro+"\t\t\t\t   ESCUELA DE FORMACION DE TECNOLOGOS")
            print("\t\t\t\t\tREPORTE DE CALIFACIONES\n")
            print(Azul+"Año/Semestre:"+Blanco+" {}".format(Semestre.get()))
            print(Azul+"Materia:"+Blanco+f" {Materia.get()}\n")
            print(Azul+"N°\tNombre\t\tApellido\tCorreo\t\t\t\tNota 1\tNota 2\tTotal"+Blanco)

            for Estudiante in RegistroArchivo:
                print(Estudiante)

            print(Negro+"\nRESUMEN\n\n"+Azul+"Promedio del Curso: "+Blanco+"{}\n".format(round(PromedioCurso, 2))+Verde+"Estudiantes Aprobados (14 - 20):"+Blanco+f" {Aprobados}")
            print(Amarillo+"Estudiantes Suspensos (09 - 13): "+Blanco+str(Suspensos)+"\n"+Rojo+"Estudiantes Reprobados (01 - 08): "+Blanco+"{}".format(Reprobados))
            print(f"\n\t\t\t\t\t{Docente.get()}\n\t\t\t\t\t\t"+Negro+"Docente\n\t\t\t\t\t\tESFOT\n\t\t\t\t\t     "+Blanco+f"{NumeroDocente.get()}")

            print("\n=======================================================================================================================\n")

            VentanaRegistro.grid_forget()
            BotonVolver.grid_forget()
            VentanaMenu.grid(row=0, column=0, pady=30)
            messagebox.showinfo("Nuevo registro creado", "¡Datos registrados en calificaciones.txt exitosamente!\n\nRevise la carpeta Base de Datos y la consola del IDE")
    else:
        messagebox.showerror("Datos vacíos", "¡Rellene los espacios vacios!")

def CrearResumen():

    global PromedioCurso, Aprobados, Reprobados, Suspensos, ArregloEstudiantes, RegistroArchivo

    SumaTotales=0
    Aprobados=0
    Suspensos=0
    Reprobados=0
    k=0

    BotonModificarT.grid(row=IndiceEstudiantes+6, column=0, columnspan=14, pady=10)

    for Fila in TablaEntrada:
        NumEst=Fila['Numero']
        NomEst=Fila['Nombre'].get()
        ApeEst=Fila['Apellido'].get()
        CorEst=Fila['Correo'].get()
        No1Est=Fila['Nota1'].get()
        No2Est=Fila['Nota2'].get()

        if not NomEst or not ApeEst or not CorEst or not No1Est or not No2Est:
            messagebox.showwarning("Tabla Incompleta","¡Rellene todas las entradas!")
            MostrarResumen=False
            break
        elif No1Est and No2Est:
            No1Est=float(No1Est)
            No2Est=float(No2Est)

            if No1Est>=0 and No1Est<=20 and No2Est>=0 and No2Est<=20:

                TotEst=(No1Est+No2Est)/2
                Fila['Total']=TotEst
                SumaTotales+=TotEst

                Fila['Nombre'].config(state="disabled", font=("Times New Roman", 12, "bold"))
                Fila['Apellido'].config(state="disabled", font=("Times New Roman", 12, "bold"))
                Fila['Correo'].config(state="disabled", font=("Times New Roman", 12, "bold"))
                Fila['Nota1'].config(state="disabled", font=("Times New Roman", 12, "bold"))
                Fila['Nota2'].config(state="disabled", font=("Times New Roman", 12, "bold"))

                if TotEst>=14:
                    Label(VentanaR2, bd=1, width=5, text=TotEst, relief="solid", bg="#73ff69", font=("Times New Roman", 12), anchor="w").grid(row=6+k, column=7, sticky="ew") 
                elif TotEst>=9:
                    Label(VentanaR2, bd=1, width=5, text=TotEst, relief="solid", bg="#fff469", font=("Times New Roman", 12), anchor="w").grid(row=6+k, column=7, sticky="ew")
                else:
                    Label(VentanaR2, bd=1, width=5, text=TotEst, relief="solid", bg="#ff6969", font=("Times New Roman", 12), anchor="w").grid(row=6+k, column=7, sticky="ew")
                
                k+=1

                if TotEst >=14:
                    Aprobados+=1
                elif TotEst >=9:
                    Suspensos+=1
                else:
                    Reprobados+=1

                MostrarResumen=True
            else:
                messagebox.showerror("Notas invalidas","¡Nota(s) Invalida(s)! Revise su registro\n\nRecuerde colocar numeros en el rango permitido (0 - 20)")
                MostrarResumen=False
                break

        TabC="\t\t\t\t"
        for i in range(len(CorEst)//8):
            TabC=TabC.replace("\t", "", 1)

        TabN="\t\t"
        for i in range(len(NomEst)//8):
            TabN=TabN.replace("\t", "", 1)

        TabA="\t\t"
        for i in range(len(ApeEst)//8):
            TabA=TabA.replace("\t", "", 1)

        RegistroEstudiante=f"{NumEst}\t{NomEst}{TabN}{ApeEst}{TabA}{CorEst}{TabC}{No1Est}\t{No2Est}\t{TotEst}"
        
        Estudiante={'Numero':NumEst,
            'Nombre': NomEst, 'Apellido': ApeEst,
            'Correo': CorEst, 'Nota1': No1Est,
            'Nota2': No2Est, 'Total': TotEst
        }

        ArregloEstudiantes.append(Estudiante)

        RegistroArchivo.append(RegistroEstudiante)

    PromedioCurso=SumaTotales/IndiceEstudiantes

    if MostrarResumen == True:
        BotonRegistrar.grid_forget()

        VentanaR3.grid(row=3, column=0, pady=60)

        Label(VentanaR3, text="RESUMEN", bg="aquamarine3", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
              ).grid(row=0, column=0, columnspan=14, sticky="ew")

        Label(VentanaR3, text="Promedio\ndel curso:", bd=1, relief="solid", font=("Times New Roman", 12, "bold")
              ).grid(row=1, column=0, columnspan=1, sticky="ew")

        Label(VentanaR3, text=round(PromedioCurso, 2), bd=1, relief="solid", font=("Times New Roman", 11)
              ).grid(row=1, column=1, columnspan=13, sticky="nsew")

        Label(VentanaR3, text="Total", bd=1, relief="solid", font=("Times New Roman", 12, "bold")
              ).grid(row=2, rowspan=3, column=0, columnspan=1, sticky="nsew")

        Label(VentanaR3, text="Aprobados (14 - 20)", bd=1, relief="solid", font=("Times New Roman", 11)
              ).grid(row=2, column=1, columnspan=11, sticky="ew")

        Label(VentanaR3, text=Aprobados, bd=1, relief="solid", bg="#73ff69", font=("Times New Roman", 11)
              ).grid(row=2, column=12, columnspan=2, sticky="ew")

        Label(VentanaR3, text="Suspensos (09 - 13)", bd=1, relief="solid", font=("Times New Roman", 11)
              ).grid(row=3, column=1, columnspan=11, sticky="ew")

        Label(VentanaR3, text=Suspensos, bd=1, relief="solid", bg="#fff469", font=("Times New Roman", 11)
              ).grid(row=3, column=12, columnspan=2, sticky="ew")

        Label(VentanaR3, text="Reprobados (01 - 12)", bd=1, relief="solid", font=("Times New Roman", 11)
              ).grid(row=4, column=1, columnspan=11, sticky="ew")

        Label(VentanaR3, text=Reprobados, bd=1, relief="solid", bg="#ff6969", font=("Times New Roman", 11)
              ).grid(row=4, column=12, columnspan=2, sticky="ew")

        TextoDocente=Label(VentanaR3, text="\nDocente\nESFOT\n", bd=1, relief="solid", font=("Times New Roman", 12, "bold"))
        TextoDocente.grid(row=5, column=0, columnspan=14, sticky="nsew")

        Entry(TextoDocente, textvariable=Docente, font=("Times New Roman", 11), justify="center", bd=1, relief="solid"
              ).grid(row=0, padx=500, pady=18)

        Entry(TextoDocente, textvariable=NumeroDocente, font=("Times New Roman", 11), justify="center", bd=1, relief="solid"
              ).grid(row=1, padx=500, pady=18)

        BotonGuardarInfo.grid(row=6, columnspan=14, pady=10, sticky="e", padx=10)
        BotonNuevoReporte.grid(row=6, columnspan=14, pady=10, sticky="e", padx=160)

        ContenidoRegistro.update_idletasks()
        VentanaApoyo1.config(scrollregion=VentanaApoyo1.bbox("all"))

def CrearTablaNotas():
    global IndiceEstudiantes, TablaEntrada

    IndiceEstudiantes=int(CantidadEstudiantes.get())

    VentanaR2.grid(row=2, column=0, pady=10)

    if IndiceEstudiantes>40 or IndiceEstudiantes<3: 
        messagebox.showerror("Numero de estudiantes inválido", "¡Ingrese correctamente el número de estudiantes!\n\nRango permitido entre 3 y 40 estudiantes")
    elif not Materia.get() or not Semestre.get():
        messagebox.showwarning("Datos sin rellenar","Rellene todos los espacios en blanco")
    else:
        TablaEntrada=[]

        for widget in VentanaR2.winfo_children():
            widget.grid_forget()

        for widget in VentanaR3.winfo_children():
            widget.grid_forget()

        EntradaEstudiantes['state']="disabled"
        EntradaMateria['state']="disabled"
        EntradaSemestre['state']="disabled"
        BotonModificar.grid(row=0, column=0, sticky="nsew", padx=170)

        TextoNumero=Label(VentanaR2, width=5, text=" N°", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w")
        TextoNumero.grid(row=5, column=1, columnspan=1, sticky="ew")

        TextoNombre=Label(VentanaR2, width=12, text=" Estudiante", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w")
        TextoNombre.grid(row=5, column=2, columnspan=2, sticky="ew")

        TextoApellido=Label(VentanaR2, width=12, text=" Apellido", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w")
        TextoApellido.grid(row=5, column=3, columnspan=2, sticky="ew")

        TextoCorreo=Label(VentanaR2, width=30, text=" Correo", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w")
        TextoCorreo.grid(row=5, column=4, columnspan=4, sticky="ew")

        TextoNota1=Label(VentanaR2, width=8, text=" Nota 1", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w")
        TextoNota1.grid(row=5, column=5, columnspan=1, sticky="ew")

        TextoNota2=Label(VentanaR2, width=8, text=" Nota 2", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w")
        TextoNota2.grid(row=5, column=6, columnspan=1, sticky="ew")

        TextoTotal=Label(VentanaR2, width=8, text=" Total", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w")
        TextoTotal.grid(row=5, column=7, columnspan=1, sticky="ew")

        for i in range(IndiceEstudiantes):

            Label(VentanaR2, text=" "+str(i+1), bd=1,  width=5, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w").grid(row=6+i, column=1, sticky="ew")
            
            Nom=Entry(VentanaR2, width=12, bd=1, relief="solid", font=("Times New Roman", 12), justify="left")
            Nom.grid(row=6+i, column=2, sticky="ew")

            Ape=Entry(VentanaR2, width=12, bd=1, relief="solid", font=("Times New Roman", 12), justify="left")
            Ape.grid(row=6+i, column=3, sticky="ew")

            Cor=Entry(VentanaR2, width=30, bd=1, relief="solid", font=("Times New Roman", 12), justify="left")
            Cor.grid(row=6+i, column=4, sticky="ew")

            No1=Entry(VentanaR2, width=8, bd=1, relief="solid", font=("Times New Roman", 12), justify="left")
            No1.grid(row=6+i, column=5, sticky="ew")
            No1.bind("<KeyRelease>", Decimales)

            No2=Entry(VentanaR2, width=8, bd=1, relief="solid", font=("Times New Roman", 12), justify="left")
            No2.grid(row=6+i, column=6, sticky="ew")
            No2.bind("<KeyRelease>", Decimales)

            Tot=Label(VentanaR2, width=8, bd=1, relief="solid", font=("Times New Roman", 12)).grid(row=6+i, column=7, sticky="ew")

            InformacionEntrada={'Numero':i+1,
                'Nombre':Nom,
                'Apellido':Ape,
                'Correo':Cor,
                'Nota1':No1,
                'Nota2':No2,
                'Total':Tot
            }

            TablaEntrada.append(InformacionEntrada)

            BotonRegistrar.grid(row=IndiceEstudiantes+6, column=0, columnspan=14, pady=10)

            ContenidoRegistro.update_idletasks()
            VentanaApoyo1.config(scrollregion=VentanaApoyo1.bbox("all"))

EntradaEstudiantes=ttk.Spinbox(TextoEstudiantes, textvariable=CantidadEstudiantes, from_=3, to=40, width=3, font=("Times New Roman", 11),
                            state="normal")
EntradaEstudiantes.grid(row=0, column=0, sticky="w", padx=90)
CantidadEstudiantes.set(5)
EntradaEstudiantes.bind("<KeyRelease>", Enteros)

BotonIngresar=Button(TextoEstudiantes, text="Ingresar", command=CrearTablaNotas, font=("Times New Roman", 8, "bold"), bg=Azul2, fg="white")
BotonIngresar.grid(row=0, column=0, sticky="nsew", padx=170)

BotonModificar=Button(TextoEstudiantes, text="Modificar", command=Modificar, font=("Times New Roman", 8, "bold"), bg=Azul2, fg="white")
BotonModificar.grid_forget()

BotonRegistrar=Button(VentanaR2, width=15, text="Registrar notas", command=CrearResumen, font=("Times New Roman", 11, "bold"), bg=Azul2, fg="white")
BotonRegistrar.grid_forget()

BotonModificarT=Button(VentanaR2, width=15, text="Modificar tabla", command=ModificarTabla, font=("Times New Roman", 11, "bold"), bg=Azul2, fg="white")
BotonModificarT.grid_forget()

BotonGuardarInfo=Button(VentanaR3, width=15, height=3, text="Guardar en\n calificaciones.txt", command=GuardarRegistro, font=("Times New Roman", 11, "bold"), bg=Azul2, fg="white")
BotonGuardarInfo.grid_forget()

BotonNuevoReporte=Button(VentanaR3, width=15, height=3, text="Generar\nnuevo reporte", command=NuevoReporte, font=("Times New Roman", 11, "bold"), bg="Aqua", fg="white")
BotonNuevoReporte.grid_forget()

TextoSemestre2=Label(TextoSemestre, font=("Times New Roman", 11))
TextoSemestre2.grid_forget()

TextoMateria2=Label(TextoMateria, font=("Times New Roman", 11))
TextoMateria2.grid_forget()

TextoEstudiantes2=Label(TextoEstudiantes, font=("Times New Roman", 11))
TextoEstudiantes2.grid_forget()

# -------------------------------- ORDENAR CALIFICACIONES -------------------------------- #

def GuardarOrdenamiento():
    Respuesta=messagebox.askquestion("Sistema de Gestión de Calificaiones", "¿Está seguro de guardar los datos ordenados?")
    if Respuesta == "yes":

        global RegistroArchivo
        RegistroArchivo=[]

        for Estudiante in EstudiantesOrdenados:
            TabC="\t\t\t\t"
            for i in range(len(Estudiante['Correo'])//8):
                TabC=TabC.replace("\t", "", 1)

            TabN="\t\t"
            for i in range(len(Estudiante['Nombre'])//8):
                TabN=TabN.replace("\t", "", 1)

            TabA="\t\t"
            for i in range(len(Estudiante['Apellido'])//8):
                TabA=TabA.replace("\t", "", 1)
            RegistroArchivo.append(f"{Estudiante['Numero']}\t{Estudiante['Nombre']}{TabN}{Estudiante['Apellido']}{TabA}{Estudiante['Correo']}{TabC}{Estudiante['Nota1']}\t{Estudiante['Nota2']}\t{Estudiante['Total']}")

        with open("Base de datos/ordenamiento.txt", "w") as archivo:
            archivo.write("\t\t\t\tESCUELA DE FORMACION DE TECNOLOGOS\n")
            archivo.write("\t\t\t\t    REPORTE DE CALIFICACIONES\n\n")
            archivo.write("Año/Semestre: {}\n".format(Semestre.get()))
            archivo.write(f"Materia: {Materia.get()}\n\n")
            archivo.write("Ordenados %smente por: %s\n" %((Ord.get()).lower(), Segun.get()))
            archivo.write("Algoritmo de ordenamiento escogido: %s\n\n" %Tipo_de_Ord.get())
            archivo.write("N°\tNombre\t\tApellido\tCorreo\t\t\t\tNota 1\tNota 2\tTotal\n")

            for Estudiante in RegistroArchivo:
                archivo.write(Estudiante+"\n")

            archivo.write(f"\n\t\t\t\t\t\t{Docente.get()}\n\t\t\t\t\t\t\tDocente\n\t\t\t\t\t\t\tESFOT\n\t\t\t\t\t\t     {NumeroDocente.get()}")
        
        print("\n=======================================================================================================================\n")

        print(Negro+"\t\t\t\t   ESCUELA DE FORMACION DE TECNOLOGOS")
        print("\t\t\t\t\tREPORTE DE CALIFACIONES\n")
        print(Azul+"Año/Semestre:"+Blanco+" {}".format(Semestre.get()))
        print(Azul+"Materia:"+Blanco+f" {Materia.get()}\n")
        print(Verde+"Ordenados %smente por:"%(Ord.get()).lower(),Blanco+"%s"%Segun.get())
        print(Verde+"Algoritmo de ordenamiento escogido: "+Blanco+"%s\n" %Tipo_de_Ord.get())
        print(Azul+"N°\tNombre\t\tApellido\tCorreo\t\t\t\tNota 1\tNota 2\tTotal"+Blanco)

        for Estudiante in RegistroArchivo:
            print(Estudiante)

        print(f"\n\t\t\t\t\t{Docente.get()}\n\t\t\t\t\t\t"+Negro+"Docente\n\t\t\t\t\t\tESFOT\n\t\t\t\t\t     "+Blanco+f"{NumeroDocente.get()}")

        print("\n=======================================================================================================================\n")

        VentanaOrdenamiento.grid_forget()
        BotonVolver.grid_forget()
        VentanaMenu.grid(row=0, column=0, pady=30)
        messagebox.showinfo("Nuevo registro creado", "¡Datos registrados en ordenamiento.txt exitosamente!\n\nRevise la carpeta Base de Datos y la consola del IDE")

def Ordenar():
    global ArregloEstudiantes, EstudiantesOrdenados
    Tipo = Tipo_de_Ord.get()
    Orden = Ord.get()
    Por = Segun.get()

    for widget in VentanaO2.winfo_children():
        widget.grid_forget()

    for widget in VentanaO3.winfo_children():
            widget.grid_forget()

    VentanaO2.grid_forget()
    VentanaO3.grid_forget()

    VentanaO2.grid(row=2, column=0, pady=10)

    if Tipo == "Bubble Sort": EstudiantesOrdenados=BubbleSort(ArregloEstudiantes, Orden, Por)
    elif Tipo == "Selective Sort": EstudiantesOrdenados=SelectiveSort(ArregloEstudiantes, Orden, Por)
    elif Tipo == "Insertion Sort": EstudiantesOrdenados=InsertionSort(ArregloEstudiantes, Orden, Por)
    elif Tipo == "Heap Sort": EstudiantesOrdenados=HeapSort(ArregloEstudiantes, Orden, Por)
    elif Tipo == "Merge Sort": EstudiantesOrdenados=MergeSort(ArregloEstudiantes, Orden, Por)
    elif Tipo == "Quick Sort": EstudiantesOrdenados=QuickSort(ArregloEstudiantes, Orden, Por)

    Label(VentanaO2, text="Hay "+str(IndiceEstudiantes)+f" estudiantes, su orden {Orden.lower()} según sus {Por.lower()}s es:\n", 
          font=("Times New Roman", 12, "bold")).grid(row=0, column=0, columnspan=14, sticky="ew")

    Label(VentanaO2, width=3, text=" N°", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
          ).grid(row=1, column=0, columnspan=1, sticky="ew")

    Label(VentanaO2, width=12, text=" Estudiante", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
          ).grid(row=1, column=1, columnspan=2, sticky="ew")

    Label(VentanaO2, width=12, text=" Apellido", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
          ).grid(row=1, column=3, columnspan=2, sticky="ew")

    Label(VentanaO2, width=30, text=" Correo", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
          ).grid(row=1, column=5, columnspan=4, sticky="ew")

    Label(VentanaO2, width=7, text=" Nota 1", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
          ).grid(row=1, column=9, columnspan=2, sticky="ew")

    Label(VentanaO2, width=7, text=" Nota 2", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
          ).grid(row=1, column=11, columnspan=2, sticky="ew")

    Label(VentanaO2, width=7, text=" Total", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
          ).grid(row=1, column=13, columnspan=1, sticky="ew")

    i=2
    for Estudiante in EstudiantesOrdenados:

        Label(VentanaO2, width=3, text=" "+str(i-1), bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
              ).grid(row=6+i, column=0, columnspan=1, sticky="ew")
        
        Label(VentanaO2, width=12, text=" "+str(Estudiante['Nombre']), bd=1, relief="solid", font=("Times New Roman", 12), anchor="w"
              ).grid(row=6+i, column=1, columnspan=2, sticky="ew")

        Label(VentanaO2, width=12, text=" "+str(Estudiante['Apellido']), bd=1, relief="solid", font=("Times New Roman", 12), anchor="w"
              ).grid(row=6+i, column=3, columnspan=2, sticky="ew")

        Label(VentanaO2, width=30, text=" "+str(Estudiante['Correo']), bd=1, relief="solid", font=("Times New Roman", 12), anchor="w"
              ).grid(row=6+i, column=5, columnspan=4, sticky="ew")

        Label(VentanaO2, width=7, text=" "+str(Estudiante['Nota1']), bd=1, relief="solid", font=("Times New Roman", 12), anchor="w"
              ).grid(row=6+i, column=9, columnspan=2, sticky="ew")

        Label(VentanaO2, width=7, text=" "+str(Estudiante['Nota2']), bd=1, relief="solid", font=("Times New Roman", 12), anchor="w"
              ).grid(row=6+i, column=11, columnspan=2, sticky="ew")

        Label(VentanaO2, width=7, text=" "+str(Estudiante['Total']), bd=1, relief="solid", font=("Times New Roman", 12), anchor="w"
              ).grid(row=6+i, column=13, columnspan=1, sticky="ew")
        
        i+=1

    VentanaO3.grid(row=3, column=0, pady=60)

    Label(VentanaO3, width=100, text=Docente.get(), bd=1, relief="solid", font=("Times New Roman", 12)
          ).grid(row=0, column=0, columnspan=14, sticky="ew")

    Label(VentanaO3, text="Docente\nESFOT", bd=1, relief="solid", font=("Times New Roman", 12, "bold")
          ).grid(row=1, column=0, columnspan=14, sticky="ew")

    Label(VentanaO3, text=NumeroDocente.get(), bd=1, relief="solid", justify="center", font=("Times New Roman", 12)
          ).grid(row=2, column=0, columnspan=14, sticky="ew")

    Button(VentanaO3, width=15, height=3, text="Guardar en\nordenamiento.txt", command=GuardarOrdenamiento, font=("Times New Roman", 12, "bold"), bg=Azul2, fg="white"
       ).grid(row=4, column=0, columnspan=14, pady=10)

    ContenidoOrdenamiento.update_idletasks()
    VentanaApoyo2.config(scrollregion=VentanaApoyo2.bbox("all"))

Label(VentanaO1, width=66, height=3, text="ESCUELA DE FORMACIÓN DE TECNOLOGOS\nREPORTE DE CALIFICACIONES", bd=1, relief="solid", bg=Azul2, fg="white", font=("Times New Roman", 18, "bold")
      ).grid(row=0, column=0, columnspan=14, sticky="nsew")

Label(VentanaO1, text="Calificaciones Ordenadas", font=("Times New Roman", 12, "bold"), bd=1, relief="solid"
      ).grid(row=2, column=0, columnspan=14, sticky="nsew")

Label(VentanaO1, text="Algoritmo: ", font=("Times New Roman", 12, "bold"), bd=1, relief="solid", anchor="e"
      ).grid(row=3, column=0, columnspan=2, sticky="nsew")

ttk.Combobox(VentanaO1, textvariable=Tipo_de_Ord, state="readonly", 
                       values=("Bubble Sort", "Selective Sort", "Insertion Sort",
                               "Heap Sort", "Merge Sort", "Quick Sort"),
                        font=("Times New Roman", 11)).grid(row=3, column=2, columnspan=3, sticky="nsew")
Tipo_de_Ord.set("Bubble Sort")

Label(VentanaO1, text="Orden: ", font=("Times New Roman", 12, "bold"), bd=1, relief="solid", anchor="e"
      ).grid(row=3, column=5, columnspan=2, sticky="nsew")

ttk.Combobox(VentanaO1, textvariable=Ord, state="readonly", 
                       values=("Ascendente", "Descendente"),
                        font=("Times New Roman", 11)).grid(row=3, column=7, columnspan=3, sticky="nsew")
Ord.set("Descendente")

Label(VentanaO1, text="Segun su: ", font=("Times New Roman", 12, "bold"), bd=1, relief="solid", anchor="e"
      ).grid(row=3, column=10, columnspan=2, sticky="nsew")

ttk.Combobox(VentanaO1, textvariable=Segun, state="readonly", 
                       values=("Nombre", "Apellido", "Total"),
                        font=("Times New Roman", 11)).grid(row=3, column=12, columnspan=2, sticky="nsew")
Segun.set("Total")

Button(VentanaO1, text="Ordenar", command=Ordenar, font=("Times New Roman", 12, "bold"), bg=Azul2, fg="white"
       ).grid(row=4, column=0, columnspan=14, pady=10)

# -------------------------------- BUSCAR CALIFICACIONES -------------------------------- #

def Escoger(event):
    Buscar.set("")
    if SegunB.get()=="Total":
        Entra_Bus.bind("<KeyRelease>", Decimales)
    else:
        Entra_Bus.bind("<KeyRelease>", Palabras)

def GuardarBusqueda():
    Respuesta=messagebox.askquestion("Sistema de Gestión de Calificaiones", "¿Está seguro de guardar los datos ordenados?")
    if Respuesta == "yes":

        global RegistroArchivo
        RegistroArchivo=[]

        for Estudiante in EstudiantesEncontrados:
            TabC="\t\t\t\t"
            for i in range(len(Estudiante['Correo'])//8):
                TabC=TabC.replace("\t", "", 1)

            TabN="\t\t"
            for i in range(len(Estudiante['Nombre'])//8):
                TabN=TabN.replace("\t", "", 1)

            TabA="\t\t"
            for i in range(len(Estudiante['Apellido'])//8):
                TabA=TabA.replace("\t", "", 1)
            RegistroArchivo.append(f"{Estudiante['Numero']}\t{Estudiante['Nombre']}{TabN}{Estudiante['Apellido']}{TabA}{Estudiante['Correo']}{TabC}{Estudiante['Nota1']}\t{Estudiante['Nota2']}\t{Estudiante['Total']}")

        with open("Base de datos/busqueda.txt", "w") as archivo:
            archivo.write("\t\t\t\t   ESCUELA DE FORMACION DE TECNOLOGOS\n")
            archivo.write("\t\t\t\t\tBUSQUEDA DE ESTUDIANTE(S)\n\n")
            archivo.write("Año/Semestre: {}\n".format(Semestre.get()))
            archivo.write(f"Materia: {Materia.get()}\n\n")
            archivo.write("Estudiante buscado por su %s de: %s\n" %((SegunB.get()).lower(), Buscar.get()))
            archivo.write("Algoritmo de busqueda escogido: %s\n\n" %Tipo_de_Bus.get())
            archivo.write("N°\tNombre\t\tApellido\tCorreo\t\t\t\tNota 1\tNota 2\tTotal\n")

            for Estudiante in RegistroArchivo:
                archivo.write(Estudiante+"\n")

            archivo.write(f"\n\t\t\t\t\t{Docente.get()}\n\t\t\t\t\t\tDocente\n\t\t\t\t\t\tESFOT\n\t\t\t\t\t\t     {NumeroDocente.get()}")
        
        print("\n=======================================================================================================================\n")

        print(Negro+"\t\t\t\t   ESCUELA DE FORMACION DE TECNOLOGOS")
        print("\t\t\t\t\tBUSQUEDA DE ESTUDIANTES(S)\n")
        print(Azul+"Año/Semestre:"+Blanco+" {}".format(Semestre.get()))
        print(Azul+"Materia:"+Blanco+f" {Materia.get()}\n")
        print(Verde+"Estudiante buscado por su %s de:"%(Segun.get()).lower(),Blanco+"%s"%Buscar.get())
        print(Verde+"Algoritmo de busqueda escogido: "+Blanco+"%s\n" %Tipo_de_Bus.get())
        print(Azul+"N°\tNombre\t\tApellido\tCorreo\t\t\t\tNota 1\tNota 2\tTotal"+Blanco)

        for Estudiante in RegistroArchivo:
            print(Estudiante)

        print(f"\n\t\t\t\t\t{Docente.get()}\n\t\t\t\t\t\t"+Negro+"Docente\n\t\t\t\t\t\tESFOT\n\t\t\t\t\t     "+Blanco+f"{NumeroDocente.get()}")

        print("\n=======================================================================================================================\n")


        VentanaBuscar.grid_forget()
        BotonVolver.grid_forget()
        VentanaMenu.grid(row=0, column=0, pady=30)
        messagebox.showinfo("Nuevo registro creado", "¡Datos registrados en busqueda.txt exitosamente!\n\nRevise la carpeta Base de Datos y la consola del IDE")

def Busqueda():
    global ArregloEstudiantes, EstudiantesEncontrados

    if Buscar.get():
        Tipo=Tipo_de_Bus.get()
        Por=SegunB.get()
        Elemento_Buscar=Buscar.get()
        EstudiantesEncontrados=[]
        if Por == "Total":
            Elemento_Buscar=float(Elemento_Buscar)
            
        if Tipo == "Linear Search": EstudiantesEncontrados=LinearSearch(ArregloEstudiantes, Elemento_Buscar, Por)
        elif Tipo == "Binary Search": EstudiantesEncontrados=BinarySearch(ArregloEstudiantes, Elemento_Buscar, Por)
        elif Tipo == "Interpolation Search" and Por == "Total": EstudiantesEncontrados=InterpolationSearch(ArregloEstudiantes, Elemento_Buscar, Por)
        elif Tipo == "Interpolation Search":
            messagebox.showwarning("¡Algoritmo de busqueda no válido!","El algoritmo Interpolation Search únicamente funciona con números enteros y decimales.\n\nUselo para buscar totales, no nombres.")
            SegunB.set("Total")

        if len(EstudiantesEncontrados)>0:
            VentanaB2.grid(row=2, column=0, pady=10)

            for widget in VentanaB2.winfo_children():
                widget.grid_forget()

            for widget in VentanaB3.winfo_children():
                    widget.grid_forget()

            if len(EstudiantesEncontrados)==1:
                Label(VentanaB2, text="Los datos del estudiante con el "+str(Por).lower()+f" de {Buscar.get()} de son:\n", font=("Times New Roman", 13, "bold"), anchor="w"
                    ).grid(row=0, column=0, columnspan=14, sticky="ew")
            else:
                Label(VentanaB2, text="Los datos de los estudiantes con el "+str(Por).lower()+f" de {Buscar.get()} de son:\n", font=("Times New Roman", 13, "bold"), anchor="w"
                  ).grid(row=0, column=0, columnspan=14, sticky="ew")

            Label(VentanaB2, width=3, text=" N°", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
                ).grid(row=1, column=0, columnspan=1, sticky="ew")

            Label(VentanaB2, width=12, text=" Estudiante", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
                ).grid(row=1, column=1, columnspan=2, sticky="ew")

            Label(VentanaB2, width=12, text=" Apellido", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
                ).grid(row=1, column=3, columnspan=2, sticky="ew")

            Label(VentanaB2, width=30, text=" Correo", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
                ).grid(row=1, column=5, columnspan=4, sticky="ew")

            Label(VentanaB2, width=7, text=" Nota 1", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
                ).grid(row=1, column=9, columnspan=2, sticky="ew")

            Label(VentanaB2, width=7, text=" Nota 2", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
                ).grid(row=1, column=11, columnspan=2, sticky="ew")

            Label(VentanaB2, width=7, text=" Total", bg=Azul2, fg="white", bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
                ).grid(row=1, column=13, columnspan=1, sticky="ew")

            i=2
            for Estudiante in EstudiantesEncontrados:

                Label(VentanaB2, width=3, text=" "+str(i-1), bd=1, relief="solid", font=("Times New Roman", 12, "bold"), anchor="w"
                    ).grid(row=6+i, column=0, columnspan=1, sticky="ew")
                
                Label(VentanaB2, width=12, text=" "+str(Estudiante['Nombre']), bd=1, relief="solid", font=("Times New Roman", 12), anchor="w"
                    ).grid(row=6+i, column=1, columnspan=2, sticky="ew")

                Label(VentanaB2, width=12, text=" "+str(Estudiante['Apellido']), bd=1, relief="solid", font=("Times New Roman", 12), anchor="w"
                    ).grid(row=6+i, column=3, columnspan=2, sticky="ew")

                Label(VentanaB2, width=30, text=" "+str(Estudiante['Correo']), bd=1, relief="solid", font=("Times New Roman", 12), anchor="w"
                    ).grid(row=6+i, column=5, columnspan=4, sticky="ew")

                Label(VentanaB2, width=7, text=" "+str(Estudiante['Nota1']), bd=1, relief="solid", font=("Times New Roman", 12), anchor="w"
                    ).grid(row=6+i, column=9, columnspan=2, sticky="ew")

                Label(VentanaB2, width=7, text=" "+str(Estudiante['Nota2']), bd=1, relief="solid", font=("Times New Roman", 12), anchor="w"
                    ).grid(row=6+i, column=11, columnspan=2, sticky="ew")

                Label(VentanaB2, width=7, text=" "+str(Estudiante['Total']), bd=1, relief="solid", font=("Times New Roman", 12)
                    ).grid(row=6+i, column=13, columnspan=1, sticky="ew")
                
                i+=1

            VentanaB3.grid(row=3, column=0, pady=60)

            Label(VentanaB3, width=100, text=Docente.get(), bd=1, relief="solid", font=("Times New Roman", 12)
                ).grid(row=0, column=0, columnspan=14, sticky="ew")

            Label(VentanaB3, text="Docente\nESFOT", bd=1, relief="solid", font=("Times New Roman", 12, "bold")
                ).grid(row=1, column=0, columnspan=14, sticky="ew")

            Label(VentanaB3, text=NumeroDocente.get(), bd=1, relief="solid", justify="center", font=("Times New Roman", 12)
                ).grid(row=2, column=0, columnspan=14, sticky="ew")

            Button(VentanaB3, width=15, height=3, text="Guardar en\nbusqueda.txt", command=GuardarBusqueda, font=("Times New Roman", 12, "bold"), bg=Azul2, fg="white"
                   ).grid(row=3, column=0, columnspan=14, pady=10)

            ContenidoBuscar.update_idletasks()
            VentanaApoyo3.config(scrollregion=VentanaApoyo3.bbox("all"))
        else:
            messagebox.showerror("¡Elemento no encontrado!", "Estudiante inexistente, revise sus datos de entrada")
            VentanaB2.grid_forget()
            VentanaB3.grid_forget()
            Buscar.set("")
    else:
        messagebox.showerror("Datos insuficientes","Ingrese el elemento del estudiante a buscar")

Label(VentanaB1, width=65, height=3, text="ESCUELA DE FORMACIÓN DE TECNOLOGOS\nREPORTE DE CALIFICACIONES", bd=1, relief="solid", bg=Azul2, fg="white", font=("Times New Roman", 18, "bold")
      ).grid(row=0, column=0, columnspan=14, sticky="nsew")

Label(VentanaB1, text="Búsqueda de Calificaciones", font=("Bold", 20), bd=1, relief="solid"
      ).grid(row=2, column=0, columnspan=14, sticky="nsew")

Label(VentanaB1, text="Algoritmo: ", font=("Times New Roman", 12, "bold"), bd=1, relief="solid", anchor="e"
      ).grid(row=3, column=0, columnspan=2, sticky="nsew")

ttk.Combobox(VentanaB1, textvariable=Tipo_de_Bus, state="readonly", 
                       values=("Linear Search", "Binary Search", "Interpolation Search"),
                        font=("Times New Roman", 11)).grid(row=3, column=2, columnspan=3, sticky="nsew")
Tipo_de_Bus.set("Linear Search")

Label(VentanaB1, text="Segun su: ", font=("Times New Roman", 12, "bold"), bd=1, relief="solid", anchor="e"
      ).grid(row=3, column=5, columnspan=2, sticky="nsew")

Esco_Segun=ttk.Combobox(VentanaB1, textvariable=SegunB, state="readonly", 
                       values=("Nombre", "Apellido", "Total"),
                        font=("Times New Roman", 11))
Esco_Segun.grid(row=3, column=7, columnspan=3, sticky="nsew")
SegunB.set("Total")
Esco_Segun.bind("<<ComboboxSelected>>", Escoger)

Label(VentanaB1, text="Buscar: ", font=("Times New Roman", 12, "bold"), bd=1, relief="solid", anchor="e"
      ).grid(row=3, column=10, columnspan=2, sticky="nsew")

Entra_Bus=Entry(VentanaB1, textvariable=Buscar, font=("Times New Roman", 12), bd=1, relief="solid"
      )
Entra_Bus.grid(row=3, column=12, columnspan=2, sticky="nsew")
Entra_Bus.bind("<KeyRelease>", Decimales)

Button(VentanaB1, text="Iniciar Busqueda", command=Busqueda, font=("Times New Roman", 12, "bold"), bg=Azul2, fg="white"
       ).grid(row=4, columnspan=14, pady=10)

BotonVolver=Button(Raiz, width=10, height=2, text="Volver", command=Anterior, font=("Times New Roman", 12, "bold"), bg=Azul2, fg="white")
BotonVolver.grid_forget()

Raiz.mainloop()