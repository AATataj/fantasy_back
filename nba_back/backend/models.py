# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Availabilitydata(models.Model):
    playerid = models.IntegerField(db_column='playerID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    home = models.CharField(max_length=4, blank=True, null=True)
    away = models.CharField(max_length=4, blank=True, null=True)
    recenttitle = models.CharField(db_column='recentTitle', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    recentcontent = models.CharField(db_column='recentContent', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    played = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'availabilityData'


class Boxscores(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=8, blank=True, null=True)
    position = models.CharField(max_length=5, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    team = models.CharField(max_length=6, blank=True, null=True)
    homeaway = models.CharField(db_column='homeAway', max_length=2, blank=True, null=True)  # Field name made lowercase.
    opponent = models.CharField(max_length=6, blank=True, null=True)
    result = models.CharField(max_length=2, blank=True, null=True)
    started = models.CharField(max_length=1, blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    fgm = models.IntegerField(blank=True, null=True)
    fga = models.IntegerField(blank=True, null=True)
    fgper = models.FloatField(db_column='fgPer', blank=True, null=True)  # Field name made lowercase.
    number_2fgm = models.IntegerField(db_column='2fgm', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2fga = models.IntegerField(db_column='2fga', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2fgper = models.FloatField(db_column='2fgPer', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3fgm = models.IntegerField(db_column='3fgm', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3fga = models.IntegerField(db_column='3fga', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3fgper = models.FloatField(db_column='3fgPer', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    ftm = models.IntegerField(blank=True, null=True)
    fta = models.IntegerField(blank=True, null=True)
    ftper = models.FloatField(db_column='ftPer', blank=True, null=True)  # Field name made lowercase.
    orb = models.IntegerField(blank=True, null=True)
    drb = models.IntegerField(blank=True, null=True)
    trb = models.IntegerField(blank=True, null=True)
    ast = models.IntegerField(blank=True, null=True)
    stl = models.IntegerField(blank=True, null=True)
    blk = models.IntegerField(blank=True, null=True)
    tov = models.IntegerField(blank=True, null=True)
    pf = models.IntegerField(blank=True, null=True)
    pts = models.IntegerField(blank=True, null=True)
    #gmsc = models.FloatField(blank=True, null=True)
    playerid = models.IntegerField(db_column='playerID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'boxscores'


class Boxscoresbackup(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=8, blank=True, null=True)
    position = models.CharField(max_length=5, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    team = models.CharField(max_length=6, blank=True, null=True)
    homeaway = models.CharField(db_column='homeAway', max_length=2, blank=True, null=True)  # Field name made lowercase.
    opponent = models.CharField(max_length=6, blank=True, null=True)
    result = models.CharField(max_length=2, blank=True, null=True)
    started = models.CharField(max_length=1, blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    fgm = models.IntegerField(blank=True, null=True)
    fga = models.IntegerField(blank=True, null=True)
    fgper = models.DecimalField(db_column='fgPer', max_digits=4, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    number_2fgm = models.IntegerField(db_column='2fgm', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2fga = models.IntegerField(db_column='2fga', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2fgper = models.DecimalField(db_column='2fgPer', max_digits=4, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3fgm = models.IntegerField(db_column='3fgm', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3fga = models.IntegerField(db_column='3fga', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3fgper = models.DecimalField(db_column='3fgPer', max_digits=4, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    ftm = models.IntegerField(blank=True, null=True)
    fta = models.IntegerField(blank=True, null=True)
    ftper = models.DecimalField(db_column='ftPer', max_digits=4, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    orb = models.IntegerField(blank=True, null=True)
    drb = models.IntegerField(blank=True, null=True)
    trb = models.IntegerField(blank=True, null=True)
    ast = models.IntegerField(blank=True, null=True)
    stl = models.IntegerField(blank=True, null=True)
    blk = models.IntegerField(blank=True, null=True)
    tov = models.IntegerField(blank=True, null=True)
    pf = models.IntegerField(blank=True, null=True)
    pts = models.IntegerField(blank=True, null=True)
    gmsc = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    playerid = models.IntegerField(db_column='playerID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'boxscoresBackup'


class Boxscorespre(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=8, blank=True, null=True)
    position = models.CharField(max_length=5, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    team = models.CharField(max_length=6, blank=True, null=True)
    homeaway = models.CharField(db_column='homeAway', max_length=2, blank=True, null=True)  # Field name made lowercase.
    opponent = models.CharField(max_length=6, blank=True, null=True)
    result = models.CharField(max_length=2, blank=True, null=True)
    started = models.CharField(max_length=1, blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    fgm = models.IntegerField(blank=True, null=True)
    fga = models.IntegerField(blank=True, null=True)
    fgper = models.FloatField(db_column='fgPer', blank=True, null=True)  # Field name made lowercase.
    number_2fgm = models.IntegerField(db_column='2fgm', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2fga = models.IntegerField(db_column='2fga', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2fgper = models.DecimalField(db_column='2fgPer', max_digits=4, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3fgm = models.IntegerField(db_column='3fgm', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3fga = models.IntegerField(db_column='3fga', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3fgper = models.FloatField(db_column='3fgPer', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    ftm = models.IntegerField(blank=True, null=True)
    fta = models.IntegerField(blank=True, null=True)
    ftper = models.FloatField(db_column='ftPer', blank=True, null=True)  # Field name made lowercase.
    orb = models.IntegerField(blank=True, null=True)
    drb = models.IntegerField(blank=True, null=True)
    trb = models.IntegerField(blank=True, null=True)
    ast = models.IntegerField(blank=True, null=True)
    stl = models.IntegerField(blank=True, null=True)
    blk = models.IntegerField(blank=True, null=True)
    tov = models.IntegerField(blank=True, null=True)
    pf = models.IntegerField(blank=True, null=True)
    pts = models.IntegerField(blank=True, null=True)
    gmsc = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    playerid = models.IntegerField(db_column='playerID', blank=True, null=True)  # Field name made lowercase.
    fgpertemp = models.FloatField(db_column='fgPerTemp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'boxscoresPre'


class Boxscoressafe(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=8, blank=True, null=True)
    position = models.CharField(max_length=5, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    team = models.CharField(max_length=6, blank=True, null=True)
    homeaway = models.CharField(db_column='homeAway', max_length=2, blank=True, null=True)  # Field name made lowercase.
    opponent = models.CharField(max_length=6, blank=True, null=True)
    result = models.CharField(max_length=2, blank=True, null=True)
    started = models.CharField(max_length=1, blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    fgm = models.IntegerField(blank=True, null=True)
    fga = models.IntegerField(blank=True, null=True)
    fgper = models.DecimalField(db_column='fgPer', max_digits=4, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    number_2fgm = models.IntegerField(db_column='2fgm', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2fga = models.IntegerField(db_column='2fga', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2fgper = models.DecimalField(db_column='2fgPer', max_digits=4, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3fgm = models.IntegerField(db_column='3fgm', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3fga = models.IntegerField(db_column='3fga', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3fgper = models.DecimalField(db_column='3fgPer', max_digits=4, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    ftm = models.IntegerField(blank=True, null=True)
    fta = models.IntegerField(blank=True, null=True)
    ftper = models.DecimalField(db_column='ftPer', max_digits=4, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    orb = models.IntegerField(blank=True, null=True)
    drb = models.IntegerField(blank=True, null=True)
    trb = models.IntegerField(blank=True, null=True)
    ast = models.IntegerField(blank=True, null=True)
    blk = models.IntegerField(blank=True, null=True)
    tov = models.IntegerField(blank=True, null=True)
    pf = models.IntegerField(blank=True, null=True)
    pts = models.IntegerField(blank=True, null=True)
    gmsc = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    playerid = models.IntegerField(db_column='playerID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'boxscoresSafe'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Featureslist(models.Model):
    feature = models.CharField(max_length=10000, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'featuresList'


class Inputvectors(models.Model):
    index = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    playerid = models.IntegerField(db_column='playerID', blank=True, null=True)  # Field name made lowercase.
    fgper = models.DecimalField(db_column='fgPer', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ftper = models.DecimalField(db_column='ftPer', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    number_3fgm = models.IntegerField(db_column='3fgm', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    pts = models.IntegerField(blank=True, null=True)
    trb = models.IntegerField(blank=True, null=True)
    ast = models.IntegerField(blank=True, null=True)
    stl = models.IntegerField(blank=True, null=True)
    blk = models.IntegerField(blank=True, null=True)
    tov = models.IntegerField(blank=True, null=True)
    ptsavg7days = models.DecimalField(db_column='ptsAvg7Days', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ptsavg14days = models.DecimalField(db_column='ptsAvg14Days', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ptsavg30days = models.DecimalField(db_column='ptsAvg30Days', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ptsavgseason = models.DecimalField(db_column='ptsAvgSeason', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ptsavgcareer = models.DecimalField(db_column='ptsAvgCareer', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minsavg7days = models.DecimalField(db_column='minsAvg7Days', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minsavg14days = models.DecimalField(db_column='minsAvg14Days', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minsavg30days = models.DecimalField(db_column='minsAvg30Days', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minsavgcareer = models.DecimalField(db_column='minsAvgCareer', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    playergamenum = models.DecimalField(db_column='playerGameNum', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minsavgseason = models.DecimalField(db_column='minsAvgSeason', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    trbavg7days = models.DecimalField(db_column='trbAvg7Days', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    trbavg14days = models.DecimalField(db_column='trbAvg14Days', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    trbavg30days = models.DecimalField(db_column='trbAvg30Days', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    trbavgseason = models.DecimalField(db_column='trbAvgSeason', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    trbavgcareer = models.DecimalField(db_column='trbAvgCareer', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inputvectors'


class Inputvectorsbackup(models.Model):
    index = models.IntegerField()
    name = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    playerid = models.IntegerField(db_column='playerID', blank=True, null=True)  # Field name made lowercase.
    fgper = models.DecimalField(db_column='fgPer', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ftper = models.DecimalField(db_column='ftPer', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    number_3fgm = models.IntegerField(db_column='3fgm', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    pts = models.IntegerField(blank=True, null=True)
    trb = models.IntegerField(blank=True, null=True)
    ast = models.IntegerField(blank=True, null=True)
    stl = models.IntegerField(blank=True, null=True)
    blk = models.IntegerField(blank=True, null=True)
    tov = models.IntegerField(blank=True, null=True)
    ptsavg7days = models.DecimalField(db_column='ptsAvg7Days', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ptsavg14days = models.DecimalField(db_column='ptsAvg14Days', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ptsavg30days = models.DecimalField(db_column='ptsAvg30Days', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ptsavgseason = models.DecimalField(db_column='ptsAvgSeason', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inputvectorsBackup'


class Playerhashes(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    playerid = models.AutoField(db_column='playerID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playerHashes'


class Playerhashesbackup(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    playerid = models.IntegerField(db_column='playerID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playerHashesBackup'


class Playerhashesinit(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    playerid = models.AutoField(db_column='playerID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playerHashesInit'


class Playerhashesold(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    playerid = models.AutoField(db_column='playerID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playerHashesOld'


class Rotoworld(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    posteam = models.CharField(db_column='posTeam', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=1000, blank=True, null=True)
    content = models.CharField(max_length=5000, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    playerid = models.IntegerField(db_column='playerID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rotoworld'


class Rotoworldbackup(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    posteam = models.CharField(db_column='posTeam', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=1000, blank=True, null=True)
    content = models.CharField(max_length=5000, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    playerid = models.IntegerField(db_column='playerID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rotoworldBackup'


class Rotoworldorig(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    posteam = models.CharField(db_column='posTeam', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=1000, blank=True, null=True)
    content = models.CharField(max_length=5000, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    playerid = models.IntegerField(db_column='playerID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rotoworldOrig'


class Rotoworldprebackup(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    posteam = models.CharField(db_column='posTeam', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=1000, blank=True, null=True)
    content = models.CharField(max_length=5000, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    playerid = models.IntegerField(db_column='playerID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rotoworldPreBackup'

