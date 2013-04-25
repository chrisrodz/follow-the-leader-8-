from django.db import models
from django.contrib.auth.models import User
from djorm_pgarray.fields import ArrayField
from djorm_expressions.models import ExpressionManager
from django import forms

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
Add temporary form fields for each element in model array fields.
'''
class T02Form(forms.ModelForm):

    f10_1 = forms.CharField(max_length=100)
    f11_1 = forms.CharField(max_length=100)
    f12_1 = forms.CharField(max_length=100)
    f13_1 = forms.CharField(max_length=100)
    f14_1 = forms.CharField(max_length=100)
    f15_1 = forms.CharField(max_length=100)
    f16_1 = forms.CharField(max_length=100)
    f17_1 = forms.CharField(max_length=100)
    f18_1 = forms.CharField(max_length=100)
    f19_1 = forms.IntegerField()
    f20_1 = forms.FloatField()
    f20_2 = forms.FloatField()
    f20_3 = forms.FloatField()
    f20_4 = forms.FloatField()
    f20_5 = forms.FloatField()
    f21_1 = forms.CharField(max_length=100)
    f21_2 = forms.CharField(max_length=100)
    f21_3 = forms.CharField(max_length=100)
    f21_4 = forms.CharField(max_length=100)
    f21_5 = forms.CharField(max_length=100)
    f21_6 = forms.CharField(max_length=100)
    f21_7 = forms.CharField(max_length=100)
    f21_8 = forms.CharField(max_length=100)
    f21_9 = forms.CharField(max_length=100)
    f21_10 = forms.CharField(max_length=100)
    f23_1 = forms.CharField(max_length=100)
    f27_1 = forms.CharField(max_length=100)
    f27_2 = forms.CharField(max_length=100)
    f27_3 = forms.CharField(max_length=100)

    class Meta:
        model = T02

    # Magic function that displays ArrayFields as separate input boxes
    def fix_instance(self):
        data10 = ",".join([str(x) for x in self.initial['f10']])
        data10 = data10.split(',')
        self.initial['f10'] = data10[0]
        self.initial['f10_1'] = data10[1]

        data11 = ",".join([str(x) for x in self.initial['f11']])
        data11 = data11.split(',')
        self.initial['f11'] = data11[0]
        self.initial['f11_1'] = data11[1]

        data12 = ",".join([str(x) for x in self.initial['f12']])
        data12 = data12.split(',')
        self.initial['f12'] = data12[0]
        self.initial['f12_1'] = data12[1]

        data13 = ",".join([str(x) for x in self.initial['f13']])
        data13 = data13.split(',')
        self.initial['f13'] = data13[0]
        self.initial['f13_1'] = data13[1]

        data14 = ",".join([str(x) for x in self.initial['f14']])
        data14 = data14.split(',')
        self.initial['f14'] = data14[0]
        self.initial['f14_1'] = data14[1]

        data15 = ",".join([str(x) for x in self.initial['f15']])
        data15 = data15.split(',')
        self.initial['f15'] = data15[0]
        self.initial['f15_1'] = data15[1]

        data16 = ",".join([str(x) for x in self.initial['f16']])
        data16 = data16.split(',')
        self.initial['f16'] = data16[0]
        self.initial['f16_1'] = data16[1]

        data17 = ",".join([str(x) for x in self.initial['f17']])
        data17 = data17.split(',')
        self.initial['f17'] = data17[0]
        self.initial['f17_1'] = data17[1]

        data18 = ",".join([str(x) for x in self.initial['f18']])
        data18 = data18.split(',')
        self.initial['f18'] = data18[0]
        self.initial['f18_1'] = data18[1]

        data19 = ",".join([str(x) for x in self.initial['f19']])
        data19 = data19.split(',')
        self.initial['f19'] = data19[0]
        self.initial['f19_1'] = data19[1]

        data20 = ",".join([str(x) for x in self.initial['f20']])
        data20 = data20.split(',')
        self.initial['f20'] = data20[0]
        self.initial['f20_1'] = data20[1]
        self.initial['f20_2'] = data20[2]
        self.initial['f20_3'] = data20[3]
        self.initial['f20_4'] = data20[4]
        self.initial['f20_5'] = data20[5]

        data21 = ",".join([str(x) for x in self.initial['f21']])
        data21 = data21.split(',')
        self.initial['f21'] = data21[0]
        self.initial['f21_1'] = data21[1]
        self.initial['f21_2'] = data21[2]
        self.initial['f21_3'] = data21[3]
        self.initial['f21_4'] = data21[4]
        self.initial['f21_5'] = data21[5]
        self.initial['f21_6'] = data21[6]
        self.initial['f21_7'] = data21[7]
        self.initial['f21_8'] = data21[8]
        self.initial['f21_9'] = data21[9]
        self.initial['f21_10'] = data21[10]

        data23 = ",".join([str(x) for x in self.initial['f23']])
        data23 = data23.split(',')
        self.initial['f23'] = data23[0]
        self.initial['f23_1'] = data23[1]

        data27 = ",".join([str(x) for x in self.initial['f27']])
        data27 = data27.split(',')
        self.initial['f27'] = data27[0]
        self.initial['f27_1'] = data27[1]
        self.initial['f27_2'] = data27[2]
        self.initial['f27_3'] = data27[3]

    # I use clean to group the array data into one input variable
    def clean(self):
        self.cleaned_data['f10'] = [self.cleaned_data['f10'],self.cleaned_data['f10_1']]
        self.cleaned_data['f11'] = [self.cleaned_data['f11'],self.cleaned_data['f11_1']]
        self.cleaned_data['f12'] = [self.cleaned_data['f12'],self.cleaned_data['f12_1']]
        self.cleaned_data['f13'] = [self.cleaned_data['f13'],self.cleaned_data['f13_1']]
        self.cleaned_data['f14'] = [self.cleaned_data['f14'],self.cleaned_data['f14_1']]
        self.cleaned_data['f15'] = [self.cleaned_data['f15'],self.cleaned_data['f15_1']]
        self.cleaned_data['f16'] = [self.cleaned_data['f16'],self.cleaned_data['f16_1']]
        self.cleaned_data['f17'] = [self.cleaned_data['f17'],self.cleaned_data['f17_1']]
        self.cleaned_data['f18'] = [self.cleaned_data['f18'],self.cleaned_data['f18_1']]
        self.cleaned_data['f19'] = [self.cleaned_data['f19'],self.cleaned_data['f19_1']]
        self.cleaned_data['f20'] = [self.cleaned_data['f20'],self.cleaned_data['f20_1'],self.cleaned_data['f20_2'],self.cleaned_data['f20_3'],self.cleaned_data['f20_4'],self.cleaned_data['f20_5']]
        self.cleaned_data['f21'] = [self.cleaned_data['f21'],self.cleaned_data['f21_1'],self.cleaned_data['f21_2'],self.cleaned_data['f21_3'],self.cleaned_data['f21_4'],self.cleaned_data['f21_5'],self.cleaned_data['f21_6'],self.cleaned_data['f21_7'],self.cleaned_data['f21_8'],self.cleaned_data['f21_9'],self.cleaned_data['f21_10']]
        self.cleaned_data['f23'] = [self.cleaned_data['f23'],self.cleaned_data['f23_1']]
        self.cleaned_data['f27'] = [self.cleaned_data['f27'],self.cleaned_data['f27_1'],self.cleaned_data['f27_2'],self.cleaned_data['f27_3']]

        return self.cleaned_data


class A125Form(forms.ModelForm):
    class Meta:
        model = A125

    # Magic function that fixes how ArrayFields are displayed
    def fix_instance(self):
        self.initial['sponsored_accounts'] = ",".join([str(x) for x in self.initial['sponsored_accounts']])
        self.initial['cost_sharing'] = ",".join([str(x) for x in self.initial['cost_sharing']])
        self.initial['university_funds'] = ",".join([str(x) for x in self.initial['university_funds']])
        self.initial['total_compensation'] = ",".join([str(x) for x in self.initial['total_compensation']])
        self.initial['payments_paid'] = ",".join([str(x) for x in self.initial['payments_paid']])

