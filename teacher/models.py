from djongo import models


class School(models.Model):
    teacher = models.OneToOneField('account.Teacher', on_delete=models.CASCADE, primary_key=True)
    # all required params


class Class(models.Model):
    school = models.ManyToManyField(School)
    # all required params


class PersonalPlanner(models.Model):
    teacher = models.ManyToManyField('account.Teacher')
    # all required params


class SupplyInventory(models.Model):
    teacher = models.ManyToManyField('account.Teacher')
    # all required params


class Subscription(models.Model):
    teacher = models.OneToOneField('account.Teacher', on_delete=models.CASCADE, primary_key=True)
    # all required params
