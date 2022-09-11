segundos_str = input("Por favor,entre com o número de segundos que deseja converter:")

total_segs = int(segundos_str)

horas=total_segs//3600
#"horas"(variavel) recebe "total_seg" dividido inteiro por 3600(60min x 60segndos)

segs_restantes = total_segs % 3600
#segs_restantes(variavel) recebe "total_segs" resto da divisão por 3600

minutos = segs_restantes//60
#"minutos"(variavel) recebe "seg_restantes" dividido inteiro por "60"

segs_restantes_final = segs_restantes % 60

print(horas,"horas,",minutos, "minutos e",segs_restantes_final,"segundos.")
