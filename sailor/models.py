from django.db import models
import uuid
class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)  
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class Advertisement(models.Model):
    type = models.CharField(db_column='Type', max_length=30, blank=True, null=True)  # Field name made lowercase.
    price = models.CharField(db_column='Price', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='Id', primary_key=True,unique=True,default=uuid.uuid4().hex[:6],max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=30)  # Field name made lowercase.
    listing_type = models.CharField(db_column='Listing_type', max_length=30)  # Field name made lowercase.
    bedrooms = models.IntegerField(db_column='Bedrooms', blank=True, null=True)  # Field name made lowercase.
    bathrooms = models.IntegerField(db_column='Bathrooms', blank=True, null=True)  # Field name made lowercase.
    floor_number = models.IntegerField(db_column='Floor_number', blank=True, null=True)  # Field name made lowercase.
    neigborhood = models.CharField(db_column='Neigborhood', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500)  # Field name made lowercase.
    built_up_year = models.CharField(db_column='Built_up_year', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ad_price_type = models.CharField(db_column='Ad_price_type', max_length=30)  # Field name made lowercase.
    expiry = models.DateField(db_column='Expiry')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=30)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=30)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=30)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30)  # Field name made lowercase.
    street_and_house_no = models.CharField(db_column='Street_and_house_no', max_length=50, blank=True, null=True)
    owner = models.CharField(db_column='Owner', max_length=50, blank=True, null=True)
    images = models.ImageField(blank=True, null=True,upload_to="media")
    class Meta:
        managed = False
        db_table = 'advertisement'

    def f():
        d = uuid4()
        str = d.hex
        return str[0:16]

""" class Agent(models.Model):
    email = models.CharField(db_column='Email', max_length=30)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=30, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', primary_key=True, max_length=30)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', unique=True, max_length=35)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=35)  # Field name made lowercase.
    agency_name = models.CharField(db_column='Agency_Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agent' """


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
    first_name = models.CharField(max_length=150)
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


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Newsletter(models.Model):
    email = models.CharField(db_column='Email', primary_key=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'newsletter'



class PropertyCompany(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=30)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact = models.ForeignKey('PropertyCompanyContact', models.DO_NOTHING, db_column='Contact', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'property_company'


class PropertyCompanyContact(models.Model):
    contact = models.CharField(db_column='Contact', primary_key=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'property_company_contact'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)

