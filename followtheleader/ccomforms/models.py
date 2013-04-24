from django.db import models
from django.contrib.auth.models import User
from djorm_pgarray.fields import ArrayField
from djorm_expressions.models import ExpressionManager
from django.forms import ModelForm

# Model for the T02 form
# We decided to name our fields based on the
# numbers on the form itself.
# Ex. The first field in the form is f1.
class T02(models.Model):

    date_filled = models.DateField(null=False)
    professor = models.ForeignKey(User)

    Ano_Fiscal = models.IntegerField()
    Num_Referencia = models.IntegerField(null=False)
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
    f10 = ArrayField(dbtype='text')
    # Facultad, Departamento/Decanato, Oficina
    f11 = ArrayField(dbtype='text')
    # Numero de Plaza
    f12 = ArrayField(dbtype='text')
    # Cuenta(s) a afectarse
    f13 = ArrayField(dbtype='text')
    # Titulo/Rango
    f14 = ArrayField(dbtype='text')
    # Tipo de Nombramiento
    f15 = ArrayField(dbtype='text')
    # Clase de Servicio
    f16 = ArrayField(dbtype='text')
    # Codigo de Pago y/o  CAL ID
    f17 = ArrayField(dbtype='text')
    # Escala / Rate
    f18 = ArrayField(dbtype='text')
    # field 19 is an array of 2 integers
    # index 0: 'Vigentes'
    # index 1: 'Despues del cambio'
    # Sueldo Total Bimensual, Fijo?
    f19 = ArrayField(dbtype='int')
    # field 20 is an array of 6 floats
    # index 0: Sobresueldo
    # index 1: Prep. Acad.
    # index 2: Bonificacion
    # index 3: Diferencial Docente
    # index 4: Aumentos Concedidos
    # index 5: Quinq. Ret. 
    # Desglose de Salario (bimensual) fuera de Escala (P16)
    f20 = ArrayField(dbtype='real')
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
    f21 = ArrayField(dbtype='text')
    # AEELA
    f22 = models.BooleanField()
    # form 23 is a char array with 2 entries
    # index 0: Retiro?
    # index 1: Tipo de Cotizacion
    f23 = ArrayField(dbtype='text')
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
    f27 = ArrayField(dbtype='text')
    # Observaciones y/o Programa Academico para C/A
    f30 = models.CharField(max_length=50)
    objects = ExpressionManager()

    def __unicode__(self):
        return u'%s %s: %s' % (self.professor.first_name, self.professor.last_name, self.date_filled)



# Model for the 125-A form
# We went for abbreviations of the field names
# since this form isn't numbered
class A125(models.Model):

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
    sponsored_accounts = ArrayField(dbtype='text')
    # Modulo 5
    cost_sharing = ArrayField(dbtype='text')
    # Modulo 5
    university_funds = ArrayField(dbtype='text')
    # Only 2 entries
    total_compensation = ArrayField(dbtype='text')
    # Modulo 3
    payments_paid = ArrayField(dbtype='text')

    comments = models.TextField(null=True)
    objects = ExpressionManager()

    def __unicode__(self):
        return u'%s %s: %s' % (self.professor.first_name, self.professor.last_name, self.date_filled)

'''
Modify the clean() method so it will fix the Arrays
Hay que ver como va a ser el user input para entonces
saber como hacer el clean
'''
class T02Form(ModelForm):
    class Meta:
        model = T02

    # Magic function that fixes how ArrayFields are displayed
    def fix_instance(self):
        self.initial['f10'] = ",".join([str(x) for x in self.initial['f10']])
        self.initial['f11'] = ",".join([str(x) for x in self.initial['f11']])
        self.initial['f12'] = ",".join([str(x) for x in self.initial['f12']])
        self.initial['f13'] = ",".join([str(x) for x in self.initial['f13']])
        self.initial['f14'] = ",".join([str(x) for x in self.initial['f14']])
        self.initial['f15'] = ",".join([str(x) for x in self.initial['f15']])
        self.initial['f16'] = ",".join([str(x) for x in self.initial['f16']])
        self.initial['f17'] = ",".join([str(x) for x in self.initial['f17']])
        self.initial['f18'] = ",".join([str(x) for x in self.initial['f18']])
        self.initial['f19'] = ",".join([str(x) for x in self.initial['f19']])
        self.initial['f20'] = ",".join([str(x) for x in self.initial['f20']])
        self.initial['f21'] = ",".join([str(x) for x in self.initial['f21']])
        self.initial['f23'] = ",".join([str(x) for x in self.initial['f23']])
        self.initial['f27'] = ",".join([str(x) for x in self.initial['f27']])


class A125Form(ModelForm):
    class Meta:
        model = A125

    # Magic function that fixes how ArrayFields are displayed
    def fix_instance(self):
        self.initial['sponsored_accounts'] = ",".join([str(x) for x in self.initial['sponsored_accounts']])
        self.initial['cost_sharing'] = ",".join([str(x) for x in self.initial['cost_sharing']])
        self.initial['university_funds'] = ",".join([str(x) for x in self.initial['university_funds']])
        self.initial['total_compensation'] = ",".join([str(x) for x in self.initial['total_compensation']])
        self.initial['payments_paid'] = ",".join([str(x) for x in self.initial['payments_paid']])

