# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acccat(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=1)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccCat'


class Account(models.Model):
    username = models.CharField(db_column='Username', primary_key=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=32)  # Field name made lowercase.
    typeid = models.ForeignKey(Acccat, models.DO_NOTHING, db_column='TypeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Account'


class Address(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey('Person', models.DO_NOTHING, db_column='PersonID')  # Field name made lowercase.
    num = models.IntegerField(db_column='Num')  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=15)  # Field name made lowercase.
    ward = models.CharField(db_column='Ward', max_length=15, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=15, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=15)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=15, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Address'


class Book(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=20, blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='Publisher', max_length=20, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    stock = models.SmallIntegerField(db_column='Stock', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Book'


class Bookcategory(models.Model):
    bookid = models.OneToOneField(Book, models.DO_NOTHING, db_column='BookID', primary_key=True)  # Field name made lowercase.
    categoryid = models.ForeignKey('Category', models.DO_NOTHING, db_column='CategoryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BookCategory'
        unique_together = (('bookid', 'categoryid'),)


class Category(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='parentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Category'

    def __str__(self):
        return "{},{},{}".format(self.id, self.name, self.parentid)


class Deliveryinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DeliveryInfo'


class Orderdelivery(models.Model):
    orderid = models.OneToOneField('Orders', models.DO_NOTHING, db_column='OrderID', primary_key=True)  # Field name made lowercase.
    infoid = models.ForeignKey(Deliveryinfo, models.DO_NOTHING, db_column='InfoID')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderDelivery'
        unique_together = (('orderid', 'infoid'),)


class Orderdetail(models.Model):
    orderid = models.OneToOneField('Orders', models.DO_NOTHING, db_column='OrderID', primary_key=True)  # Field name made lowercase.
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.
    amount = models.SmallIntegerField(db_column='Amount')  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderDetail'
        unique_together = (('orderid', 'bookid'),)


class Orders(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dateorder = models.DateTimeField(db_column='DateOrder', blank=True, null=True)  # Field name made lowercase.
    paymentmethod = models.ForeignKey('Payment', models.DO_NOTHING, db_column='PaymentMethod')  # Field name made lowercase.
    paid = models.BooleanField(db_column='Paid')  # Field name made lowercase.
    totalprice = models.DecimalField(db_column='TotalPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orders'


class Payment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment'


class Person(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.OneToOneField(Account, models.DO_NOTHING, db_column='Username', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DoB', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person'


class Stock(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    datein = models.DateTimeField(db_column='DateIn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stock'


class Stockdetail(models.Model):
    stockid = models.OneToOneField(Stock, models.DO_NOTHING, db_column='StockID', primary_key=True)  # Field name made lowercase.
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.
    amount = models.SmallIntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockDetail'
        unique_together = (('stockid', 'bookid'),)


class Voucher(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    catid = models.ForeignKey('Vouchercategory', models.DO_NOTHING, db_column='CatID')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Voucher'


class Vouchercategory(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VoucherCategory'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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
    action_flag = models.SmallIntegerField()
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
