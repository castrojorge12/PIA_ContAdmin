#Comenzar el código
# Solicitamos la información
print('\t\t\tBALANCE GENERAL')
print('-'*20)
# Pedimos los Activos
print('\t\t- - - Activos - - -')
print('-'*20)

efectivo = int(input("\tEfectivos: "))
clientes = int(input("\tClientes: "))
deudores = int(input("\tDeudores diversos: "))
funcionarios = int(input("\tFuncionarios y Empleados: "))
inv_mats = int(input("\tInventario de Materiales: "))
inv_ProdFin = int(input("inventario de producto terminado: $"))
tActCircu = (efectivo + clientes + deudores + funcionarios + inv_mats + inv_ProdFin)
print("Total de Activo Circulante: ", tActCircu)

print('-'*20)
terry = int(input("\tTerreno: "))
planta = int(input("\tPlanta y Equipo: "))
despAcum = int(input("\tDepreciacion acomulada: "))
tActNo = (terry + planta - despAcum)
print("Total de Activo No Circulante: ", tActNo)

print('-'*20)
act_tot=(totl_act + total_no)
print("ACTIVO TOTAL: ", tActCircu + tActNo)
print('-'*20)
# Pedimos los Pasivos

print('\t\t- - - Pasivos - - -')
print('-'*20)

proveedores = int(input("\tProveedores: "))
docx = int(input("\tDocumentos por pagar: "))
isr = int(input("ISR por pagar: "))
tPasivosCorto = (proveedores + docx + isr)
print("Total de Pasivo Corto Plazo: ", tPasivosCorto)
print('-'*20)

prestamos = int(input("\tPrestamos bancarios: "))
print("Total de Pasivos a Largo Plazo: ", prestamos)
pas_tot = (tPasivosCorto + prestamos)
print("Pasivo total: ", pas_tot)
print('-'*20)

# Pedimos Capital Contable
print('\t\t- - - Capital Contable - - -')
print('-'*20)

capital_contr = int(input("\tCapital contribuido: "))
capital_ganado = int(input("\tCapital ganado"))
tCapCont = (capital_contr + capital_ganado)
print("Capital contable total: ", tCapCont)

# Suma de Pasivo y Capital
sum_pasCapital = (pas_tot + tCapCont)
print("suma del pasivo y capital: ",sum_pasCapital)
