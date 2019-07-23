# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RItemRating(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    clicknum = models.IntegerField(db_column='clickNum', blank=True, null=True)  # Field name made lowercase.
    islike = models.TextField(db_column='isLike', blank=True, null=True)  # Field name made lowercase.
    point = models.IntegerField(blank=True, null=True)
    processdate = models.TextField(db_column='processDate', blank=True, null=True)  # Field name made lowercase.
    productidx = models.TextField(db_column='productIdx', blank=True, null=True)  # Field name made lowercase.
    regdate = models.TextField(db_column='regDate', blank=True, null=True)  # Field name made lowercase.
    stayduration = models.IntegerField(db_column='stayDuration', blank=True, null=True)  # Field name made lowercase.
    useridx = models.TextField(db_column='userIdx', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R_ITEM_RATING'


class RItemRatingTendency(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    useridx = models.TextField(db_column='userIdx', blank=True, null=True)  # Field name made lowercase.
    productidx = models.TextField(db_column='productIdx', blank=True, null=True)  # Field name made lowercase.
    ppr = models.FloatField(blank=True, null=True)
    cid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'R_ITEM_RATING_TENDENCY'


class RPprAvg(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    productidx = models.TextField(db_column='productIdx', blank=True, null=True)  # Field name made lowercase.
    cid = models.IntegerField(blank=True, null=True)
    ppravg = models.FloatField(db_column='pprAvg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R_PPR_AVG'


class RRecInter(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    useridx = models.TextField(db_column='userIdx', blank=True, null=True)  # Field name made lowercase.
    cid = models.IntegerField(blank=True, null=True)
    productidx = models.TextField(db_column='productIdx', blank=True, null=True)  # Field name made lowercase.
    predictpref = models.FloatField(db_column='predictPref', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R_REC_INTER'


class RTendency(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    useridx = models.TextField(db_column='userIdx', blank=True, null=True)  # Field name made lowercase.
    cid = models.IntegerField(blank=True, null=True)
    wr = models.FloatField(blank=True, null=True)
    wc = models.FloatField(blank=True, null=True)
    ws = models.FloatField(blank=True, null=True)
    wl = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'R_TENDENCY'


class RTimeWeight(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    useridx = models.TextField(db_column='userIdx', blank=True, null=True)  # Field name made lowercase.
    productidx = models.TextField(db_column='productIdx', blank=True, null=True)  # Field name made lowercase.
    regdate = models.TextField(db_column='regDate', blank=True, null=True)  # Field name made lowercase.
    preference = models.FloatField(blank=True, null=True)
    cid = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'R_TIME_WEIGHT'


class RUserSimilarity(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    destidx = models.TextField(db_column='destIdx', blank=True, null=True)  # Field name made lowercase.
    sim = models.IntegerField(blank=True, null=True)
    sourceidx = models.TextField(db_column='sourceIdx', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R_USER_SIMILARITY'


class TCrawlNaver(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    topic = models.TextField(blank=True, null=True)
    writer_name = models.TextField(blank=True, null=True)
    data_source = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    create_at = models.TextField(db_column='create_At', blank=True, null=True)  # Field name made lowercase.
    bloggerlink = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_CRAWL_NAVER'


class TItemIpa(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    productidx = models.TextField(db_column='productIdx', blank=True, null=True)  # Field name made lowercase.
    create_at = models.TextField(db_column='create_At', blank=True, null=True)  # Field name made lowercase.
    mtfidf = models.TextField(db_column='mTFIDF', blank=True, null=True)  # Field name made lowercase.
    ipain = models.FloatField(db_column='IPAin', blank=True, null=True)  # Field name made lowercase.
    ipa = models.FloatField(db_column='IPA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_ITEM_IPA'


class TItemService(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    productidx = models.TextField(db_column='productIdx', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(blank=True, null=True)
    numstaycount = models.IntegerField(db_column='numStayCount', blank=True, null=True)  # Field name made lowercase.
    likecount = models.IntegerField(db_column='likeCount', blank=True, null=True)  # Field name made lowercase.
    avg_point_field = models.FloatField(db_column='avg(point)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    create_at = models.TextField(db_column='create_At', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_ITEM_SERVICE'


class TItemSns(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    word = models.TextField(blank=True, null=True)
    prev_idf = models.FloatField(blank=True, null=True)
    cur_idf = models.IntegerField(blank=True, null=True)
    mtfidf = models.IntegerField(db_column='mTFIDF', blank=True, null=True)  # Field name made lowercase.
    windowsize = models.TextField(db_column='windowSize', blank=True, null=True)  # Field name made lowercase.
    starttime = models.TextField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_ITEM_SNS'


class TTokenInfo(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    word = models.TextField(blank=True, null=True)
    freq = models.IntegerField(blank=True, null=True)
    create_at = models.TextField(db_column='create_At', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_TOKEN_INFO'


class TDictionary(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    dict = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_dictionary'


class TStopword(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    stopword = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_stopword'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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


class UxMybtem(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    useridx = models.TextField(db_column='userIdx', blank=True, null=True)  # Field name made lowercase.
    productidx = models.TextField(db_column='productIdx', blank=True, null=True)  # Field name made lowercase.
    regdate = models.TextField(db_column='regDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ux_mybtem'


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


class UxSearchLog(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    searchkeyword = models.TextField(db_column='searchKeyword', blank=True, null=True)  # Field name made lowercase.
    searchdate = models.TextField(db_column='searchDate', blank=True, null=True)  # Field name made lowercase.
    useridx = models.TextField(db_column='userIdx', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ux_search_log'


class UxSearchLogDestination(models.Model):
    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    searchidx = models.TextField(db_column='searchIdx', blank=True, null=True)  # Field name made lowercase.
    clicktime = models.TextField(db_column='clickTime', blank=True, null=True)  # Field name made lowercase.
    backtime = models.TextField(db_column='backTime', blank=True, null=True)  # Field name made lowercase.
    productidx = models.TextField(db_column='productIdx', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ux_search_log_destination'


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
