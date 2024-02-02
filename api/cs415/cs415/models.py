from django.db import models

class Characters(models.Model):
    characterid = models.AutoField(db_column='characterID', primary_key=True)  # Field name made lowercase.
    charname = models.CharField(db_column='charName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    race = models.CharField(max_length=30, blank=True, null=True)
    skill1 = models.CharField(max_length=30, blank=True, null=True)
    skill2 = models.CharField(max_length=30, blank=True, null=True)
    skill3 = models.CharField(max_length=30, blank=True, null=True)
    raceid = models.ForeignKey('Races', models.DO_NOTHING, db_column='raceID')  # Field name made lowercase.
    classid = models.ForeignKey('Classes', models.DO_NOTHING, db_column='classID')  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Characters'

    def __str__(self):
        return f'{self.charname}'


class Classskills(models.Model):
    cskills = models.AutoField(db_column='cSkills', primary_key=True)  # Field name made lowercase.
    skill = models.CharField(max_length=30, blank=True, null=True)
    roll = models.CharField(max_length=30, blank=True, null=True)
    skilltype = models.CharField(db_column='skillType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    magic = models.CharField(max_length=30, blank=True, null=True)
    classid = models.ForeignKey('Classes', models.DO_NOTHING, db_column='classID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClassSkills'

    def __str__(self):
        return f'{self.skill}'


class Classes(models.Model):
    classid = models.AutoField(db_column='classID', primary_key=True)  # Field name made lowercase.
    classname = models.CharField(db_column='className', max_length=30, blank=True, null=True)  # Field name made lowercase.
    classbonus = models.CharField(db_column='classBonus', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Classes'

    def __str__(self):
        return f'{self.classname}'


class Raceskills(models.Model):
    rskill = models.AutoField(db_column='rSkill', primary_key=True)  # Field name made lowercase.
    skill = models.CharField(max_length=30, blank=True, null=True)
    roll = models.CharField(max_length=30, blank=True, null=True)
    skilltype = models.CharField(db_column='skillType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    magic = models.CharField(max_length=30, blank=True, null=True)
    raceid = models.ForeignKey('Races', models.DO_NOTHING, db_column='raceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RaceSkills'

    def __str__(self):
        return f'{self.skill}'


class Races(models.Model):
    raceid = models.AutoField(db_column='raceID', primary_key=True)  # Field name made lowercase.
    racename = models.CharField(db_column='raceName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    racebonus = models.CharField(db_column='raceBonus', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Races'

    def __str__(self):
        return f'{self.racename}'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    characterid = models.IntegerField(db_column='characterID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'

    def __str__(self):
        return f'{self.username}'