from django.core.management.base import BaseCommand
from logistica.models import Zona, Repartidor, Envio
from datetime import date

class Command(BaseCommand):
    help = 'Genera datos de prueba precisos para el ejercicio de logística'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Limpiando base de datos existente...'))
        # Borramos datos previos para evitar duplicados si se corre el script varias veces
        Envio.objects.all().delete()
        Repartidor.objects.all().delete()
        Zona.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creando zonas y tarifas...'))
        # 1. Crear las zonas del ejercicio
        zona_norte = Zona.objects.create(nombre_zona='Norte', tarifa_por_kg=1.50)
        zona_sur = Zona.objects.create(nombre_zona='Sur', tarifa_por_kg=2.00)

        self.stdout.write(self.style.SUCCESS('Creando repartidores...'))
        # 2. Crear los repartidores
        andres = Repartidor.objects.create(nombre='Andrés', email='andres@logistica.com')
        camila = Repartidor.objects.create(nombre='Camila', email='camila@logistica.com')
        luis = Repartidor.objects.create(nombre='Luis', email='luis@logistica.com')

        self.stdout.write(self.style.SUCCESS('Creando registros de envíos de mayo 2025...'))
        
        # 3. Envíos de Andrés: 5 envíos que sumen exactamente 32 kg en la zona Norte
        Envio.objects.create(repartidor=andres, zona=zona_norte, peso_kg=10.00, fecha_envio=date(2025, 5, 2))
        Envio.objects.create(repartidor=andres, zona=zona_norte, peso_kg=8.50,  fecha_envio=date(2025, 5, 12))
        Envio.objects.create(repartidor=andres, zona=zona_norte, peso_kg=5.00,  fecha_envio=date(2025, 5, 15))
        Envio.objects.create(repartidor=andres, zona=zona_norte, peso_kg=6.00,  fecha_envio=date(2025, 5, 20))
        Envio.objects.create(repartidor=andres, zona=zona_norte, peso_kg=2.50,  fecha_envio=date(2025, 5, 28))

        # 4. Envíos de Camila: 3 envíos que sumen exactamente 18 kg en la zona Sur
        Envio.objects.create(repartidor=camila, zona=zona_sur, peso_kg=8.00, fecha_envio=date(2025, 5, 5))
        Envio.objects.create(repartidor=camila, zona=zona_sur, peso_kg=6.00, fecha_envio=date(2025, 5, 18))
        Envio.objects.create(repartidor=camila, zona=zona_sur, peso_kg=4.00, fecha_envio=date(2025, 5, 25))

        # Nota: A Luis no le creamos envíos para evaluar cómo responde el sistema ante un repartidor inactivo.

        self.stdout.write(self.style.SUCCESS('¡Datos semilla inyectados con éxito de manera estructurada!'))