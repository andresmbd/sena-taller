"""
Situación
El área de cartera de una distribuidora llama a los clientes 
en el orden en que aparecen en el Excel. Mientras tanto, las 
facturas con más de 90 días de mora siguen creciendo y algunas 
ya son difíciles de recuperar.
"""

def clasificar_cartera(dias_mora):
    
        if dias_mora <= 0:
            return "Al día"
        elif dias_mora >= 1 and dias_mora <= 30:
            return "1-30 días"
        elif dias_mora  >= 31 and dias_mora <= 60:
            return "31-60 días"
        elif dias_mora  >= 61 and dias_mora <= 90:
            return "61-90 días"
        else:
            return "Más de 90 días"
    
    
# Prueba con tus propios datos:
print(clasificar_cartera(45))

