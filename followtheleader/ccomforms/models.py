from django.db import models
from django.contrib.auth.models import User

import dbarray

# Model for the T02 form
# We decided to name our fields based on the
# numbers on the form itself.
# Ex. The first field in the form is f1.
class T02(models.Model):

    def __unicode__(self):
        self.date_filled

    date_filled = models.DateField(null=False)
    professor = models.ForeignKey(User)

    Ano_Fiscal = models.IntegerField()
    Num_Referencia = models.IntegerField()
    Transaccion = models.CharField(max_length=50)
    # Name
    f1 = models.CharField(max_length=50)
    # SSN
    f2 = models.IntegerField(max_length=9)
    # Transaccion (P16)
    f3 = models.CharField(max_length=50)
    # Horas Periodo Pago
    f5 = models.FloatField()
    # Proposito (P16)
    f6 = models.CharField(max_length=50)
    # Fecha de Efectividad
    f8 = models.DateField()
    # Fecha de terminacion
    f9 = models.DateField()
    # For entries f10-f18
    # index 0: 'Vigentes'
    # index 1: 'Despues del Cambio'
    # Grupo de Trabajo/Codigo de Asignacion
    f10 = dbarray.CharArrayField(max_length=50)
    # Facultad, Departamento/Decanato, Oficina
    f11 = dbarray.CharArrayField(max_length=50)
    # Numero de Plaza
    f12 = dbarray.CharArrayField(max_length=50)
    # Cuenta(s) a afectarse
    f13 = dbarray.CharArrayField(max_length=50)
    # Titulo/Rango
    f14 = dbarray.CharArrayField(max_length=50)
    # Tipo de Nombramiento
    f15 = dbarray.CharArrayField(max_length=50)
    # Clase de Servicio
    f16 = dbarray.CharArrayField(max_length=50)
    # Codigo de Pago y/o  CAL ID
    f17 = dbarray.CharArrayField(max_length=50)
    # Escala / Rate
    f18 = dbarray.CharArrayField(max_length=50)
    # field 19 is an array of 2 integers
    # index 0: 'Vigentes'
    # index 1: 'Despues del cambio'
    # Sueldo Total Bimensual, Fijo?
    f19 = dbarray.IntegerArrayField()
    # field 20 is an array of 6 floats
    # index 0: Sobresueldo
    # index 1: Prep. Acad.
    # index 2: Bonificacion
    # index 3: Diferencial Docente
    # index 4: Aumentos Concedidos
    # index 5: Quinq. Ret. 
    # Desglose de Salario (bimensual) fuera de Escala (P16)
    f20 = dbarray.FloatArrayField()
    # field 21 is an char array with 11 entries
    # index 0: Grupo
    # index 1: Codigo Asignado
    # index 2: Status
    # index 3: Tipo de Transaccion
    # index 4: Razon
    # index 5: Fecha de Terminacion Mes
    # index 6: Fecha de Terminacion Dia
    # index 7: Fecha de Terminacion Ano
    # index 8: Fecha de separacion Mes
    # index 9: Fecha de separacion Dia
    # index 10:Fecha de separacion Ano
    # Terminacion de Asignacion o Separacion:  P48 y P49
    f21 = dbarray.CharArrayField(max_length=50)
    # AEELA
    f22 = models.BooleanField()
    # form 23 is a char array with 2 entries
    # index 0: Retiro?
    # index 1: Tipo de Cotizacion
    f23 = dbarray.CharArrayField(max_length=50)
    # Jornada 0: completa, 1:parcial
    f24 = models.BooleanField()
    # Asignacion Principal
    f25 = models.BooleanField()
    # Decanato, Facultad, Depto. u Oficina que genera
    # la compensacion adicional
    f26 = models.CharField(max_length=50)
    # field 27 is a char array with 4 entries
    # index 0: (1)
    # index 1: Descripcion (1)
    # index 2: (2)
    # index 3: Descripcion (2)
    # Descripcion de la tarea o cursos en C/A  (dias, horario, seccion y creditos)
    f27 = dbarray.CharArrayField(max_length=50)
    # Observaciones y/o Programa Academico para C/A
    f30 = models.CharField(max_length=50)


# Model for the 125-A form
# We went for abbreviations of the field names
# since this form isn't numbered
class A125(models.Model):

    def __unicode__(self):
        return self.date_filled

    date_filled = models.DateField(null=False)
    professor = models.ForeignKey(User)

    name = models.CharField(max_length=50, null=True)
    ssn = models.IntegerField(max_length=9, null=True)
    title = models.CharField(max_length=1, null=True)
    base_salary = models.FloatField(null=True)
    period = models.CharField(max_length=1, null=True)
    effective_date = models.DateField(null=True)
    multi_campus = models.BooleanField()

    # Modulo 5
    sponsored_accounts = dbarray.CharArrayField(max_length=50, null=True)
    # Modulo 5
    cost_sharing = dbarray.CharArrayField(max_length=50, null=True)
    # Modulo 5
    university_funds = dbarray.CharArrayField(max_length=50, null=True)
    # Only 2 entries
    total_compensation = dbarray.CharArrayField(max_length=50, null=True)
    # Modulo 3
    payments_paid = dbarray.CharArrayField(max_length=50, null=True)

    comments = models.TextField(null=True)