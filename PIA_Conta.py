# Solicitamos la información
# Balance general
# **************************
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
print("Capital Contable Total: ", tCapCont)

# Suma de Pasivo y Capital
sum_pasCapital = (pas_tot + tCapCont)
print("Suma del PASIVO y CAPITAL: ",sum_pasCapital)

# ***************************
# Requerimiento de materiales
# ***************************
print('-'*20)
print("\t\tRequerimientos de Materiales")
print("Material A")
matPrima_A1 = int(input("Producto CF: "))
matPrima_A2 = int(input("Producto CD: "))
matPrima_A3 = int(input("Producto CP: "))
print('-'*20)

print("Material B")
matPrima_B1 = int(input("Producto CF: "))
matPrima_B2 = int(input("Producto CD: "))
matPrima_B3 = int(input("Producto CP: "))
print('-'*20)

print("Material C")
matPrima_C1 = int(input("Producto CF: "))
matPrima_C2 = int(input("Producto CD: "))
matPrima_C3 = int(input("Producto CP: "))
print('-'*20)

print('Horas de Mano de Obra')
hrs_ManoObra_1 = int(input("Producto CF: "))
hrs_ManoObra_2 = int(input("Producto CD: "))
hrs_ManoObra_3 = int(input("Producto CP: "))
print('-'*20)

# ***************************
# Información de Inventarios
# ***************************
print('\t\t- - - Información de Invenarios - - -')
print('-'*20)

print("Inventario Inicial Primer Semestre")
matA_1s = int(input("Material A: "))
matB_1s = int(input("Material B: "))
matC_1s = int(input("Material C: "))
prodCF_1s = int(input("Producto CF: "))
prodCD_1s = int(input("Producto CD: "))
prodCP_1s = int(input("Producto CP: "))
print('-'*20)

print("Inventario Final Segundo Semestre")
matA_2s = int(input("Material A: "))
matB_2s = int(input("Material B: "))
matC_2s = int(input("Material C: "))
prodCF_2s= int(input("Producto CF: "))
prodCD_2s = int(input("Producto CF: "))
prodCP_2s = int(input("Producto CF: "))
print('-'*20)

print("Costo Primer Semestre")
matA_Costo_1s = int(input("Material A: $"))
matB_Costo_1s = int(input("Material B: $"))
matC_Costo_1s = int(input("Material C: $"))
print('-'*20)

print("Costo Segundo Semestre")
matA_Costo_2s = int(input("Material A: $"))
matB_Costo_2s = int(input("Material B: $"))
matC_Costo_2s = int(input("Material C: $"))
print('-'*20)

# ***************************
# Información de Inventarios
# ***************************
print("\t\t- - - Productos - - -")
print('-'*20)

print('Precio de Venta Primer Semestre')
cl_1s = int(input('CL: $'))
ce_1s = int(input('CE: $'))
cr_1s = int(input('CR: $'))
print('-'*20)

print('Precio de Venta Segundo Semestre')
cl_2s = int(input('CL: $'))
cl_2s = int(input('CL: $'))
cl_2s = int(input('CL: $'))
print('-'*20)

print('Ventas Planeadas Primer Semestre')
cl_ventas_1s = int(input('CL: '))
cl_ventas_1s = int(input('CL: '))
cl_ventas_1s = int(input('CL: '))
print('-'*20)

print('Ventas Planeadas Segundo Semestre')
cl_ventas_1s = int(input('CL: '))
cl_ventas_1s = int(input('CL: '))
cl_ventas_1s = int(input('CL: '))
print('-'*20)

# ***************************
# Gastos de Administración y Ventas
# ***************************
print("Gastos de Administración y Ventas:")
depreciacion_A = int(input("Depreciacion - Anuales: "))
sueldosS_A = int(input("Sueldos y salarios - Anuales: "))
comisiones = int(input("Comisiones - Porcentaje de las ventas: "))
varios_1s = int(input("Varios - Primer Semestre: "))
varios_2s = int(input("Varios - Segundo Semestre): "))
intereses_prestamo_A = int(input("Interes por Prestamo - Anuales: "))
print('-'*20)
