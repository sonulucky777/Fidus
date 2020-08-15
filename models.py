from django.db import models
from django.contrib.auth.models import User
#from address.models import AddressField

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Others")]
    gender = models.CharField(choices=gender_choices, default="M", max_length=1)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=300, default='', blank=True, null=True)
    zip_code = models.CharField('Zip/Post Code', max_length=12,default='', blank=True, null=True)
    #phone = models.CharField('Contact Phone', max_length=13, blank=True)
    #Social_link = models.URLField(blank=True)
    #profile_pic = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.user.username
"""Doctor details """
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=30)
    registration_date = models.DateTimeField('date registered')

    def __str__(self):
        return self.doctor_name

"""Hospital details """
class Hospital(models.Model):
    hospital_name = models.CharField(max_length=30)
    doctor = models.ForeignKey(Doctor, default="", on_delete=models.CASCADE)
    h_address = models.CharField(max_length=100)
    h_contact = models.CharField(max_length=13, null=True)

    def __str__(self):
        return self.hospital_name

class Appointment(models.Model):
    STATUS = (('conformed', 'conformed'), ('pending', 'pending'))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, default="", on_delete=models.CASCADE)
    patient = models.ForeignKey(User, related_name="patients", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, null=True)
    description = models.CharField(max_length=200)
    registration_date = models.DateTimeField("date registered")
    status = models.CharField(max_length=200, null=True, choices = STATUS)

    def __str__(self):
        return self.patient

    #@property
    #def is_waiting(self):
    #    return bool(self.status)


class Prescription(models.Model):
    patient = models.ForeignKey(User, related_name="patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name="doctor", on_delete=models.CASCADE)
    date = models.DateField()
    medication = models.CharField(max_length=100)
    strength = models.CharField(max_length=30)
    instruction = models.CharField(max_length=200)
    refill = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.patient

class MedicalTest(models.Model):
    patient_name = models.ForeignKey(User, related_name="pts", on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor, related_name="docs", on_delete=models.CASCADE)
    private = models.BooleanField(default=True)
    completed = models.BooleanField()

    def __str__(self):
        return self.patient_name

class Medical_history(models.Model):
    BLOOD = (('A+', 'A+ Type'), ('B+', 'B+ Type'), ('AB+', 'AB+ Type'), ('O+', 'O+ Type'), ('A-', 'A- Type'), ('B-', 'B- Type'), ('AB-', 'AB- Type'), ('O-', 'O- Type'),)
    PATIENT_HIST = (('Asthma','Asthma'), ('Cancer', 'Cancer'),('Cardiac disease','Cardiac disease'), ('Diabetes', 'Diabetes'), ('Hypertension', 'Hypertension'), ('Psychiatric disorder', 'Psychiatric disorder'), ('Epilepsy', 'Epilepsy'))
    FAMILY_HIST = (('Asthma','Asthma'), ('Cancer', 'Cancer'),('Cardiac disease','Cardiac disease'), ('Diabetes', 'Diabetes'), ('Hypertension', 'Hypertension'), ('Psychiatric disorder', 'Psychiatric disorder'), ('Epilepsy', 'Epilepsy'))
    PAST_SYMPTOM = (('Fever/Chills', 'Fever/Chills'), ('Unexplained change in weight', 'Unexplained change in weight'), ('Fatigue/Malaise/Generalized weakness', 'Fatigue/Malaise/Generalized weakness'), ('Headaches/Migraines', 'Headaches/Migraines'), ('Headaches/Migraines', 'Headaches/Migraines'), ('Dizziness', 'Dizziness'), ('Sinus Pain/Pressure/Discharge', 'Sinus Pain/Pressure/Discharge'), ('Excessive snoring', 'Excessive snoring'), ('Wheezing/Chronic Cough', 'Wheezing/Chronic Cough'), ('Shortness of breath', 'Shortness of breath'), ('Chest pain, pressure or tightness', 'Chest pain, pressure or tightness'), ('Swelling of hands/feet/ankles', 'Swelling of hands/feet/ankles'), ('Nausea/Vomiting', 'Nausea/Vomiting'), ('Abdominal pain', 'Abdominal pain'), ('Heartburn', 'Heartburn'), ('Constipation or diarrhea', 'Constipation or diarrhea'), ('Stiffness/Pain in joints/muscles', 'Stiffness/Pain in joints/muscles'), ('Joint swelling', 'Joint swelling'), ('Bleeding/Easy bruising', 'Bleeding/Easy bruising'), ('Excessive urination', 'Excessive urination'), ('Excessive thirst/hunger', 'Excessive thirst/hunger'), ('Hot flashes', 'Hot flashes'), ('Painful/Bloody urination', 'Painful/Bloody urination'), ('Difficulty urinating/Night-time urination', 'Difficulty urinating/Night-time urination'), ('Urinary incontinence (leakage)', 'Urinary incontinence (leakage)'), ('Sexual Difficulties/Painful intercourse', 'Sexual Difficulties/Painful intercourse'), ('Rash', 'Rash'), ('Anxiety/Panic Attacks', 'Anxiety/Panic Attacks'), ('Concentration Difficulty', 'Concentration Difficulty'), ('Insomnia/Problems with Sleep', 'Insomnia/Problems with Sleep'), ('Loss of energy', 'Loss of energy'), ('Thoughts of harming self or others', 'Thoughts of harming self or others'))
    name = models.CharField(max_length=50)
    gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Others")]
    gender = models.CharField(choices=gender_choices, default="M", max_length=1)
    blood_group = models.CharField(max_length=32, choices=BLOOD, default='A+ Type',)
    patient_hist = models.CharField(max_length=32, choices=PATIENT_HIST, default='Diabetes',)
    family_hist = models.CharField(max_length=32, choices=FAMILY_HIST, default='Diabetes',)
    past_symptom = models.CharField(max_length=50, choices=PAST_SYMPTOM, default='Fever',)

    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    ongoing_medication = models.BooleanField(choices=BOOL_CHOICES)
    medication_allergy = models.BooleanField(choices=BOOL_CHOICES)
    tobacco_history = models.BooleanField(choices=BOOL_CHOICES)

    ALCOHOL = (('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Occasionally', 'Occasionally'), ('Never', 'Never'))
    alcohol_consumption = models.CharField(max_length=32, choices=ALCOHOL, default="Daily",)

