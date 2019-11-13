# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class DataItem(models.Model):
    uid = models.TextField(blank=True,primary_key=True)
    pid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_item'


class DataRating(models.Model):
    uid = models.TextField(blank=True, null=True)
    pid = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_rating'


class DataUser(models.Model):
    uid = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    skintype = models.TextField(db_column='skinType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_user'



class UxProduct(models.Model):
    id = models.TextField(blank=True, primary_key=True)
    brandname = models.TextField(db_column='brandName', blank=True, null=True)  # Field name made lowercase.
    colortype = models.TextField(db_column='colorType', blank=True, null=True)  # Field name made lowercase.
    companyname = models.TextField(db_column='companyName', blank=True, null=True)  # Field name made lowercase.
    hit = models.IntegerField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    menutype = models.IntegerField(db_column='menuType', blank=True, null=True)  # Field name made lowercase.
    productname = models.TextField(db_column='productName', blank=True, null=True)  # Field name made lowercase.
    producttype = models.IntegerField(db_column='productType', blank=True, null=True)  # Field name made lowercase.
    skintype = models.TextField(db_column='skinType', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(blank=True, null=True)
    statskintype = models.TextField(db_column='statSkinType', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ux_product'


class UxReview(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    content = models.TextField(blank=True, null=True)
    modifydate = models.TextField(db_column='modifyDate', blank=True, null=True)  # Field name made lowercase.
    point = models.IntegerField(blank=True, null=True)
    productidx = models.TextField(db_column='productIdx', blank=True, null=True)  # Field name made lowercase.
    regdate = models.TextField(db_column='regDate', blank=True, null=True)  # Field name made lowercase.
    semantic = models.IntegerField(blank=True, null=True)
    useridx = models.TextField(db_column='userIdx', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ux_review'



class UxUser(models.Model):
    id = models.TextField(blank=True, primary_key=True)
    address = models.TextField(blank=True, null=True)
    addressdetail = models.TextField(db_column='addressDetail', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(blank=True, null=True)
    birthday = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    lastlogindate = models.TextField(db_column='lastLoginDate', blank=True, null=True)  # Field name made lowercase.
    nickname = models.TextField(db_column='nickName', blank=True, null=True)  # Field name made lowercase.
    password = models.IntegerField(blank=True, null=True)
    regdate = models.TextField(db_column='regDate', blank=True, null=True)  # Field name made lowercase.
    skintype = models.TextField(db_column='skinType', blank=True, null=True)  # Field name made lowercase.
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ux_user'

from django.contrib.auth.models import AbstractUser


class Customuser(AbstractUser): 
    age = models.IntegerField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    nickname = models.TextField(db_column='nickName', blank=True, null=True)  # Field name made lowercase.
    skintype = models.TextField(db_column='skinType', blank=True, null=True)  # Field name made lowercase.


class RecommendedItem(models.Model):
    id = models.IntegerField(primary_key=True)
    uid = models.CharField(max_length=45)
    product = models.CharField(max_length=45)
    frequency = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'recommended_item'

class Topk(models.Model):
    keyword = models.CharField(max_length=30, blank=True, primary_key=True)
    tfidf1 = models.FloatField(blank=True, null=True)
    tfidf2 = models.FloatField(blank=True, null=True)
    tfidf3 = models.FloatField(blank=True, null=True)
    tfidf4 = models.FloatField(blank=True, null=True)
    tfidf5 = models.FloatField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topk'

class TrendResult(models.Model):
    time = models.IntegerField(blank=True, primary_key=True)
    tweet = models.IntegerField(blank=True, null=True)
    beauty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trend_result'