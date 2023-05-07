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
