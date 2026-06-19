from django.shortcuts import render
from django.db.models import Sum, Count, F
from .models import Repartidor, Envio

def calcular_reporte_costos(request):
    # 1. Capturamos las fechas que el usuario enviará desde el formulario HTML (método GET)
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    
    resultados = []

    if fecha_inicio and fecha_fin:
        # 2. FILTRADO: Traemos solo los envíos que coinciden con el rango de fechas
        envios_en_rango = Envio.objects.filter(fecha_envio__range=[fecha_inicio, fecha_fin])

        # 3. CÁLCULO MATEMÁTICO EN BASE DE DATOS (Mejor práctica que hacerlo con for loops en Python)
        # Usamos F() para referenciar columnas y multiplicarlas (peso_kg * tarifa_por_kg)
        datos_calculados = envios_en_rango.values(
            'repartidor__nombre',
            'zona__nombre_zona',
            'zona__tarifa_por_kg'
        ).annotate(
            total_envios=Count('id'),
            total_kg=Sum('peso_kg'),
            costo_total=Sum(F('peso_kg') * F('zona__tarifa_por_kg'))
        )

        repartidores_activos = set()

        # 4. Formateamos los datos calculados para enviarlos ordenados a la vista (Template)
        for item in datos_calculados:
            resultados.append({
                'nombre': item['repartidor__nombre'],
                'envios': item['total_envios'],
                'total_kg': item['total_kg'],
                'zona': item['zona__nombre_zona'],
                'tarifa': item['zona__tarifa_por_kg'],
                'costo': item['costo_total'],
            })
            repartidores_activos.add(item['repartidor__nombre'])

        # 5. REQUERIMIENTO: Mostrar repartidores sin envíos en el período con $0.00 (Ejemplo: Luis)
        todos_los_repartidores = Repartidor.objects.all()
        for repartidor in todos_los_repartidores:
            if repartidor.nombre not in repartidores_activos:
                resultados.append({
                    'nombre': repartidor.nombre,
                    'envios': 0,
                    'total_kg': '—',
                    'zona': '—',
                    'tarifa': '—',
                    'costo': 0.00, # Costo en cero para quienes no trabajaron
                })

    # 6. Empaquetamos todo en un diccionario "context" para mandarlo al HTML
    context = {
        'resultados': resultados,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin
    }
    
    return render(request, 'logistica/reporte.html', context)