from django.db import models

class Zona(models.Model):
    nombre_zona = models.CharField(max_length=100)
    tarifa_por_kg = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre_zona

class Repartidor(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True) # blank y null permiten que sea opcional

    def __str__(self):
        return self.nombre

class Envio(models.Model):
    # Foreign Keys que relacionan el envío con el repartidor y la zona
    repartidor = models.ForeignKey(Repartidor, on_delete=models.CASCADE, related_name='envios')
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name='envios')
    
    peso_kg = models.DecimalField(max_digits=6, decimal_places=2)
    fecha_envio = models.DateField()

    def __str__(self):
        return f"Envío {self.id} - {self.repartidor.nombre} ({self.fecha_envio})"