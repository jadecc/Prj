# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class C3Potesttable(models.Model):
#     a = models.CharField(max_length=1, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'c3potesttable'
#
#
# class DicBrand(models.Model):
#     company_sdi = models.IntegerField()
#     brand_code = models.CharField(primary_key=True, max_length=255)
#     brand_name = models.CharField(max_length=255)
#     brand_english_name = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_brand'
#
#
# class DicCfpqLevel(models.Model):
#     company_sid = models.IntegerField(primary_key=True)
#     cfpq_level_code = models.CharField(max_length=255)
#     cfpq_level_name = models.CharField(max_length=255)
#     cfpq_level_english_name = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_cfpq_level'
#         unique_together = (('company_sid', 'cfpq_level_code'),)
#
#
# class DicCity(models.Model):
#     city_code = models.CharField(primary_key=True, max_length=255)
#     city_name = models.CharField(max_length=255)
#     city_english_name = models.CharField(max_length=255, blank=True, null=True)
#     province_code = models.CharField(max_length=255)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_city'
#
#
# class DicCompanyIndustry(models.Model):
#     company_industry_code = models.CharField(primary_key=True, max_length=255)
#     company_industry = models.CharField(max_length=255)
#     company_industry_english_name = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_company_industry'
#
#
# class DicCountryRegion(models.Model):
#     country_region_code = models.CharField(primary_key=True, max_length=255)
#     country_region = models.CharField(max_length=255)
#     country_region_english_name = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_country_region'
#
#
# class DicCounty(models.Model):
#     county_code = models.CharField(primary_key=True, max_length=255)
#     county_name = models.CharField(max_length=255)
#     county_english_name = models.CharField(max_length=255, blank=True, null=True)
#     city_code = models.CharField(max_length=255)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_county'
#
#
# class DicFarmWorkOperate(models.Model):
#     industry_code = models.CharField(max_length=255)
#     farm_work_variety_code = models.ForeignKey('DicFarmWorkVariety', models.DO_NOTHING, db_column='farm_work_variety_code')
#     farm_work_operate_code = models.CharField(primary_key=True, max_length=255)
#     farm_work_operate_name = models.CharField(max_length=255)
#     farm_work_operate_english_name = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_farm_work_operate'
#         unique_together = (('farm_work_operate_code', 'farm_work_variety_code', 'industry_code'),)
#
#
# class DicFarmWorkVariety(models.Model):
#     industry_code = models.CharField(max_length=255)
#     farm_work_variety_code = models.CharField(primary_key=True, max_length=255)
#     farm_work_variety_name = models.CharField(max_length=255)
#     farm_work_variety_english_name = models.CharField(max_length=255)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_farm_work_variety'
#         unique_together = (('farm_work_variety_code', 'industry_code'),)
#
#
# class DicFpqLevel(models.Model):
#     industry_code = models.CharField(primary_key=True, max_length=255)
#     fpq_level_code = models.CharField(max_length=255)
#     fpq_level_name = models.CharField(max_length=255)
#     fpq_level_english_name = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_fpq_level'
#         unique_together = (('industry_code', 'fpq_level_code'),)
#
#
# class DicFreshLeafLevel(models.Model):
#     company_sid = models.IntegerField(primary_key=True)
#     fresh_leaf_level_code = models.CharField(max_length=255)
#     fresh_leaf_level_name = models.CharField(max_length=255)
#     fresh_leaf_level_english_name = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_fresh_leaf_level'
#         unique_together = (('company_sid', 'fresh_leaf_level_code'),)
#
#
# class DicMeasureDataUnit(models.Model):
#     measure_data_unit_id = models.AutoField(primary_key=True)
#     measure_data_unit_name = models.CharField(max_length=255)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'dic_measure_data_unit'
#
#
# class DicMeasureItem(models.Model):
#     measure_item_id = models.AutoField(primary_key=True)
#     measure_item_name = models.CharField(max_length=255)
#     measure_data_unit_name = models.CharField(max_length=255)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'dic_measure_item'
#
#
# class DicProcessCraftVariety(models.Model):
#     industry_code = models.CharField(primary_key=True, max_length=255)
#     process_craft_variety_code = models.CharField(max_length=255)
#     process_craft_variety_name = models.CharField(max_length=255)
#     process_craft_variety_english_name = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_process_craft_variety'
#         unique_together = (('industry_code', 'process_craft_variety_code'),)
#
#
# class DicProcessVariety(models.Model):
#     company_sid = models.IntegerField(primary_key=True)
#     product_process_code = models.CharField(max_length=255)
#     product_process_name = models.CharField(max_length=255)
#     product_process_english_name = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_process_variety'
#         unique_together = (('company_sid', 'product_process_code'),)
#
#
# class DicProducingAreaClassification(models.Model):
#     producing_area_classification_code = models.CharField(primary_key=True, max_length=255)
#     producing_area_classification_name = models.CharField(max_length=255)
#     producing_area_classification_english_name = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_producing_area_classification'
#
#
# class DicProductStage(models.Model):
#     company_sid = models.IntegerField(primary_key=True)
#     product_stage_code = models.CharField(max_length=255)
#     product_stage_name = models.CharField(max_length=255)
#     product_stage_english_name = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_product_stage'
#         unique_together = (('company_sid', 'product_stage_code'),)
#
#
# class DicProvince(models.Model):
#     province_code = models.CharField(primary_key=True, max_length=255)
#     province_name = models.CharField(max_length=255)
#     province_english_name = models.CharField(max_length=255, blank=True, null=True)
#     country_region_code = models.CharField(max_length=255)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_province'
#
#
# class DicTeaSpecies(models.Model):
#     tea_species_code = models.CharField(primary_key=True, max_length=255)
#     process_craft_variety_code = models.CharField(max_length=255)
#     tea_species_name = models.CharField(max_length=255)
#     tea_species_english_name = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_tea_species'
#
#
# class DicTeatreeVariety(models.Model):
#     company_sid = models.IntegerField()
#     tea_tree_variety = models.CharField(primary_key=True, max_length=255)
#     tea_tree_name = models.CharField(max_length=255)
#     tea_tree_english_name = models.CharField(max_length=10)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_teatree_variety'
#         unique_together = (('tea_tree_variety', 'company_sid'),)
#
#
# class DicThemeContent(models.Model):
#     theme_content_code = models.CharField(primary_key=True, max_length=255)
#     theme_content = models.CharField(max_length=255)
#     theme_content_english_name = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_theme_content'
#
#
# class DicTownStreet(models.Model):
#     town_street_code = models.CharField(primary_key=True, max_length=255)
#     town_street_name = models.CharField(max_length=255)
#     town_street_english_name = models.CharField(max_length=255, blank=True, null=True)
#     county_code = models.CharField(max_length=255)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_town_street'
#
#
# class DicVillage(models.Model):
#     village_code = models.CharField(primary_key=True, max_length=255)
#     village_name = models.CharField(max_length=255)
#     village_english_name = models.CharField(max_length=255, blank=True, null=True)
#     town_street_code = models.CharField(max_length=255)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'dic_village'
#
#
# class DicWeatherLocation(models.Model):
#     position_sid = models.AutoField(primary_key=True)
#     position_weather_code = models.CharField(max_length=255, blank=True, null=True)
#     position_name = models.CharField(max_length=255)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'dic_weather_location'
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class TArticle(models.Model):
#     company_sid = models.IntegerField()
#     article_inf_sid = models.AutoField(primary_key=True)
#     theme_content_code = models.CharField(max_length=255)
#     theme_content = models.CharField(max_length=255)
#     theme_content_sid = models.IntegerField()
#     theme_content_name = models.CharField(max_length=255)
#     discription = models.CharField(max_length=16383)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_article'
#
#
# class TBaseExpand(models.Model):
#     company_sid = models.IntegerField(primary_key=True)
#     base_sid = models.IntegerField(unique=True)
#     base_no = models.CharField(max_length=255)
#     base_province = models.CharField(max_length=255, blank=True, null=True)
#     province_code = models.CharField(max_length=255, blank=True, null=True)
#     base_city = models.CharField(max_length=255, blank=True, null=True)
#     city_code = models.CharField(max_length=255, blank=True, null=True)
#     base_county = models.CharField(max_length=255, blank=True, null=True)
#     county_code = models.CharField(max_length=255, blank=True, null=True)
#     base_town_street = models.CharField(max_length=255, blank=True, null=True)
#     town_street_code = models.CharField(max_length=255, blank=True, null=True)
#     base_village = models.CharField(max_length=255, blank=True, null=True)
#     village_code = models.CharField(max_length=255, blank=True, null=True)
#     base_producing_area_classification = models.CharField(max_length=255, blank=True, null=True)
#     producing_area_classification_code = models.CharField(max_length=255, blank=True, null=True)
#     village_base_no = models.CharField(max_length=255, blank=True, null=True)
#     base_administrative_code = models.CharField(max_length=32, blank=True, null=True)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_base_expand'
#         unique_together = (('company_sid', 'base_no'),)
#
#
# class TBaseInf(models.Model):
#     company_sid = models.IntegerField()
#     base_sid = models.AutoField(unique=True)
#     base_no = models.CharField(primary_key=True, max_length=255)
#     base_name = models.CharField(max_length=255)
#     company_no = models.CharField(max_length=255)
#     company_full_name = models.CharField(max_length=255)
#     base_address = models.CharField(max_length=255, blank=True, null=True)
#     base_admin_name = models.CharField(max_length=255, blank=True, null=True)
#     base_admin_workno = models.CharField(max_length=255, blank=True, null=True)
#     base_area = models.FloatField(blank=True, null=True)
#     area_unit = models.CharField(max_length=50, blank=True, null=True)
#     update_writer_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_base_inf'
#         unique_together = (('base_no', 'company_sid'),)
#
#
# class TCamera(models.Model):
#     camera_sid = models.AutoField(unique=True)
#     company_sid = models.IntegerField(primary_key=True)
#     company_no = models.CharField(max_length=255)
#     company_short_name = models.CharField(max_length=255)
#     company_full_name = models.CharField(max_length=255)
#     camera_name = models.CharField(max_length=255)
#     camera_type_code = models.CharField(max_length=255, blank=True, null=True)
#     camera_type_name = models.CharField(max_length=255, blank=True, null=True)
#     camera_ip = models.CharField(max_length=255, blank=True, null=True)
#     camera_serial_number = models.CharField(max_length=255, blank=True, null=True)
#     camera_verificationcode = models.CharField(max_length=255, blank=True, null=True)
#     play_type_code = models.CharField(max_length=255, blank=True, null=True)
#     play_type_name = models.CharField(max_length=255, blank=True, null=True)
#     device_status_info = models.CharField(max_length=255, blank=True, null=True)
#     device_status = models.IntegerField(blank=True, null=True)
#     camera_url = models.CharField(max_length=255)
#     video_address = models.CharField(max_length=255, blank=True, null=True)
#     location_type_code = models.CharField(max_length=255, blank=True, null=True)
#     location_type_name = models.CharField(max_length=255, blank=True, null=True)
#     camera_location = models.CharField(max_length=255, blank=True, null=True)
#     base_sid = models.IntegerField(blank=True, null=True)
#     base_no = models.CharField(max_length=255, blank=True, null=True)
#     base_name = models.CharField(max_length=255, blank=True, null=True)
#     land_sid = models.IntegerField(blank=True, null=True)
#     land_no = models.CharField(max_length=255, blank=True, null=True)
#     land_name = models.CharField(max_length=255, blank=True, null=True)
#     camera_admin_name = models.CharField(max_length=255, blank=True, null=True)
#     camera_admin_workno = models.CharField(max_length=255, blank=True, null=True)
#     discription = models.CharField(max_length=255, blank=True, null=True)
#     update_timestamp = models.IntegerField()
#     exception_info = models.CharField(max_length=255, blank=True, null=True)
#     exception_value = models.IntegerField(blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_camera'
#         unique_together = (('company_sid', 'camera_name'),)
#
#
# class TCompany(models.Model):
#     company_sid = models.AutoField(primary_key=True)
#     company_short_name = models.CharField(max_length=255)
#     company_key = models.CharField(max_length=255)
#     company_system_create_time = models.IntegerField()
#     company_system_end_time = models.IntegerField(blank=True, null=True)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_company'
#
#
# class TCompanyDepartmentInf(models.Model):
#     company_sid = models.IntegerField(primary_key=True)
#     department_sid = models.AutoField(unique=True)
#     department_no = models.CharField(max_length=255)
#     company_full_name = models.CharField(max_length=255, blank=True, null=True)
#     department_phone = models.CharField(max_length=255, blank=True, null=True)
#     department_name = models.CharField(max_length=255)
#     department_location = models.CharField(max_length=255, blank=True, null=True)
#     department_manager_name = models.CharField(max_length=255, blank=True, null=True)
#     department_manager_workno = models.CharField(max_length=255, blank=True, null=True)
#     update_writer_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_company_department_inf'
#         unique_together = (('company_sid', 'department_no'),)
#
#
# class TCompanyEmployeeInf(models.Model):
#     company_sid = models.IntegerField(primary_key=True)
#     employee_sid = models.AutoField(unique=True)
#     employee_name = models.CharField(max_length=255)
#     employee_workno = models.CharField(max_length=255)
#     sex = models.CharField(max_length=1)
#     birthdate = models.IntegerField()
#     identity_card_no = models.CharField(max_length=255)
#     highest_education = models.CharField(max_length=255, blank=True, null=True)
#     highest_offering = models.CharField(max_length=255, blank=True, null=True)
#     employee_phone = models.CharField(max_length=255)
#     politics_status = models.CharField(max_length=255, blank=True, null=True)
#     employee_qq = models.CharField(db_column='employee_QQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     employee_wechart = models.CharField(max_length=255, blank=True, null=True)
#     employee_address = models.CharField(max_length=255)
#     employee_mail = models.CharField(max_length=255, blank=True, null=True)
#     employee_hiredate = models.IntegerField()
#     employee_departuredate = models.IntegerField(blank=True, null=True)
#     employee_position = models.CharField(max_length=255, blank=True, null=True)
#     employee_state = models.CharField(max_length=1)
#     update_writer_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_company_employee_inf'
#         unique_together = (('company_sid', 'employee_workno'),)
#
#
# class TCompanyExpand(models.Model):
#     company_sid = models.IntegerField()
#     company_no = models.CharField(primary_key=True, max_length=255)
#     company_short_name = models.CharField(max_length=255)
#     company_full_name = models.CharField(max_length=255)
#     company_zip_code = models.CharField(max_length=255, blank=True, null=True)
#     company_website = models.CharField(max_length=255, blank=True, null=True)
#     company_phone = models.CharField(max_length=255)
#     company_address = models.CharField(max_length=255)
#     company_register_date = models.IntegerField(blank=True, null=True)
#     company_register_no = models.CharField(max_length=32)
#     company_identification_no = models.CharField(max_length=255)
#     country_region_code = models.CharField(max_length=255, blank=True, null=True)
#     country_region = models.CharField(max_length=255, blank=True, null=True)
#     company_province_code = models.CharField(max_length=255, blank=True, null=True)
#     company_province = models.CharField(max_length=255, blank=True, null=True)
#     company_city_code = models.CharField(max_length=255, blank=True, null=True)
#     company_city = models.CharField(max_length=255, blank=True, null=True)
#     company_county_code = models.CharField(max_length=255, blank=True, null=True)
#     company_county = models.CharField(max_length=255, blank=True, null=True)
#     company_industry_code = models.CharField(max_length=255, blank=True, null=True)
#     company_industry = models.CharField(max_length=255)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_company_expand'
#
#
# class TCompanyExpend2(models.Model):
#     company_sid = models.IntegerField()
#     company_code = models.CharField(primary_key=True, max_length=255)
#     whether_deeply_cooperate = models.CharField(max_length=1)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_company_expend2'
#
#
# class TCompanyUserRelation(models.Model):
#     affiliation_sid = models.AutoField(primary_key=True)
#     user_sid = models.IntegerField()
#     user_no = models.CharField(max_length=255)
#     company_sid = models.IntegerField()
#     company_no = models.CharField(max_length=255)
#     user_workno = models.CharField(max_length=255)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_company_user_relation'
#
#
# class TComplaint(models.Model):
#     cid = models.AutoField(primary_key=True)
#     company_no = models.IntegerField()
#     time = models.BigIntegerField(blank=True, null=True)
#     content = models.CharField(max_length=255)
#     state = models.IntegerField(blank=True, null=True)
#     cellphone = models.CharField(max_length=255)
#     unified_product_no = models.CharField(max_length=255)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     note1 = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_complaint'
#
#
# class TConsumerComplaints(models.Model):
#     complaint_sid = models.AutoField(unique=True)
#     consumer_cellphone = models.CharField(primary_key=True, max_length=255)
#     company_sid = models.IntegerField()
#     company_no = models.CharField(max_length=255)
#     company_full_name = models.CharField(max_length=255)
#     product_name = models.CharField(max_length=255)
#     pack_no = models.CharField(max_length=255)
#     complaint_time = models.IntegerField()
#     complaint_content = models.CharField(max_length=255)
#     company_reply_state = models.CharField(max_length=1)
#     company_reply_content = models.CharField(max_length=255, blank=True, null=True)
#     company_reply_time = models.IntegerField(blank=True, null=True)
#     reply_employee_name = models.CharField(max_length=255, blank=True, null=True)
#     reply_employee_workno = models.CharField(max_length=255, blank=True, null=True)
#     government_reply_state = models.CharField(max_length=1)
#     government_reply_content = models.CharField(max_length=255, blank=True, null=True)
#     government_reply_time = models.IntegerField(blank=True, null=True)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_consumer_complaints'
#         unique_together = (('consumer_cellphone', 'pack_no', 'complaint_time'),)
#
#
# class TConsumerInformation(models.Model):
#     inf_sid = models.BigAutoField(primary_key=True)
#     trace_number = models.CharField(max_length=255)
#     company_sid = models.IntegerField()
#     product_sid = models.IntegerField()
#     search_time = models.IntegerField(blank=True, null=True)
#     longitude = models.CharField(max_length=255, blank=True, null=True)
#     latitude = models.CharField(max_length=255, blank=True, null=True)
#     ip_address = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_consumer_information'
#
#
# class TCustomer(models.Model):
#     customer_sid = models.AutoField()
#     customer_no = models.CharField(primary_key=True, max_length=255)
#     customer_short_name = models.CharField(max_length=255)
#     customer_full_name = models.CharField(max_length=255, blank=True, null=True)
#     company_sid = models.IntegerField()
#     contact_phone = models.CharField(max_length=255, blank=True, null=True)
#     contact_address = models.CharField(max_length=255, blank=True, null=True)
#     zip_code = models.CharField(max_length=255, blank=True, null=True)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     notes = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_customer'
#         unique_together = (('customer_no', 'company_sid'),)
#
#
# class TDicInf(models.Model):
#     dic_sid = models.AutoField(unique=True)
#     dic_code = models.CharField(max_length=255)
#     dic_name = models.CharField(primary_key=True, max_length=255)
#     note = models.CharField(max_length=255, blank=True, null=True)
#     display = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 't_dic_inf'
#
#
# class TDirectory(models.Model):
#     directory_sid = models.AutoField()
#     directory_no = models.CharField(primary_key=True, max_length=255)
#     directory_name = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_directory'
#
#
# class TEamilSetting(models.Model):
#     seting_sid = models.AutoField(primary_key=True)
#     switch = models.IntegerField()
#     frequency = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_eamil_setting'
#
#
# class TEmail(models.Model):
#     email_sid = models.AutoField(primary_key=True)
#     email_title = models.CharField(max_length=255, blank=True, null=True)
#     email_content = models.CharField(max_length=10000, blank=True, null=True)
#     update_timestamp = models.IntegerField(blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_email'
#
#
# class TEmailReceiveUser(models.Model):
#     email_sid = models.IntegerField(primary_key=True)
#     user_sid = models.IntegerField()
#     send_status = models.IntegerField()
#     update_timestamp = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_email_receive_user'
#         unique_together = (('email_sid', 'user_sid'),)
#
#
# class TEmployeeDepartmentRelation(models.Model):
#     company_sid = models.IntegerField()
#     affiliation_sid = models.AutoField(unique=True)
#     employee_post = models.CharField(max_length=255)
#     employee_sid = models.IntegerField(primary_key=True)
#     employee_workno = models.CharField(max_length=255)
#     department_sid = models.IntegerField()
#     department_no = models.CharField(max_length=255)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_employee_department_relation'
#         unique_together = (('employee_sid', 'department_sid'),)
#
#
# class TFarmWorkManegement(models.Model):
#     company_sid = models.IntegerField()
#     farm_work_sid = models.BigAutoField(primary_key=True)
#     land_sid = models.IntegerField()
#     land_no = models.ForeignKey('TLandInf', models.DO_NOTHING, db_column='land_no')
#     base_sid = models.IntegerField()
#     farm_work_variety_code = models.CharField(max_length=255)
#     farm_work_variety_name = models.CharField(max_length=255)
#     farm_work_operate_code = models.CharField(max_length=255)
#     farm_work_operate_name = models.CharField(max_length=255)
#     execute_datetime = models.IntegerField()
#     executor_name = models.CharField(max_length=255)
#     executor_workno = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     check_status = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_farm_work_manegement'
#
#
# class TFarmerAccountManegement(models.Model):
#     sid = models.AutoField(primary_key=True)
#     company_sid = models.IntegerField()
#     tea_farmer_no = models.CharField(max_length=255)
#     tea_farmer_name = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     phone = models.CharField(max_length=255)
#     sex = models.IntegerField()
#     address = models.CharField(max_length=255)
#     birth_date = models.IntegerField()
#     base_sid = models.IntegerField()
#     base_no = models.CharField(max_length=255)
#     base_name = models.CharField(max_length=255)
#     land_sid = models.IntegerField(blank=True, null=True)
#     land_no = models.CharField(max_length=255, blank=True, null=True)
#     land_name = models.CharField(max_length=255, blank=True, null=True)
#     regist_time = models.IntegerField(blank=True, null=True)
#     update_writer_no = models.CharField(max_length=255)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#     status = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 't_farmer_account_manegement'
#
#
# class TFileCollectionDirectory(models.Model):
#     file_collection_directory_sid = models.AutoField(unique=True)
#     directory_sid = models.IntegerField(blank=True, null=True)
#     directory_no = models.CharField(primary_key=True, max_length=255)
#     directory_name = models.CharField(max_length=255)
#     department_name = models.CharField(max_length=255)
#     start_date = models.IntegerField()
#     end_date = models.IntegerField(blank=True, null=True)
#     executor_name = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_file_collection_directory'
#         unique_together = (('directory_no', 'department_name', 'start_date'),)
#
#
# class TFilePath(models.Model):
#     file_path_sid = models.AutoField(primary_key=True)
#     file_submit_sid = models.IntegerField()
#     file_path = models.CharField(max_length=255)
#     company_sid = models.IntegerField(blank=True, null=True)
#     update_writer_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_file_path'
#
#
# class TFileSubmit(models.Model):
#     file_submit_sid = models.AutoField()
#     file_source = models.CharField(max_length=1)
#     file_collection_directory_sid = models.IntegerField(primary_key=True)
#     file_name = models.CharField(max_length=255)
#     file_keyword = models.CharField(max_length=255)
#     company_sid = models.IntegerField(blank=True, null=True)
#     company_no = models.CharField(max_length=255, blank=True, null=True)
#     company_name = models.CharField(max_length=255, blank=True, null=True)
#     update_writer_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_file_submit'
#         unique_together = (('file_collection_directory_sid', 'file_name'),)
#
#
# class THleafRecord(models.Model):
#     company_sid = models.IntegerField()
#     hleaf_record_sid = models.AutoField(primary_key=True)
#     product_sid = models.IntegerField()
#     unified_product_no = models.CharField(max_length=255)
#     product_name = models.CharField(max_length=255)
#     product_level_code = models.CharField(max_length=255)
#     product_level_name = models.CharField(max_length=255)
#     produce_date = models.IntegerField()
#     product_batch_no = models.CharField(max_length=255)
#     product_specification = models.CharField(max_length=255, blank=True, null=True)
#     product_amount = models.FloatField(blank=True, null=True)
#     product_amount_unit = models.CharField(max_length=255, blank=True, null=True)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_hleaf_record'
#
#
# class TInformationCheck(models.Model):
#     information_check_sid = models.AutoField(primary_key=True)
#     company_sid = models.IntegerField()
#     theme_content_code = models.CharField(max_length=255)
#     theme_content = models.CharField(max_length=255)
#     theme_content_no = models.CharField(max_length=255)
#     theme_content_sid = models.IntegerField()
#     check_status = models.CharField(max_length=1)
#     check_department_no = models.CharField(max_length=255, blank=True, null=True)
#     check_department_name = models.CharField(max_length=255, blank=True, null=True)
#     update_writer_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_information_check'
#
#
# class TInputsManegeInf(models.Model):
#     company_sid = models.IntegerField()
#     input_order_sid = models.BigAutoField(primary_key=True)
#     farm_work_sid = models.ForeignKey(TFarmWorkManegement, models.DO_NOTHING, db_column='farm_work_sid')
#     chemical_name = models.CharField(max_length=255)
#     chemical_variety = models.CharField(max_length=255, blank=True, null=True)
#     effective_constituent = models.CharField(max_length=255, blank=True, null=True)
#     function = models.CharField(max_length=255, blank=True, null=True)
#     producer_name = models.CharField(max_length=255, blank=True, null=True)
#     producer_no = models.CharField(max_length=255, blank=True, null=True)
#     usage_amount_int = models.IntegerField()
#     usage_amount_numerato = models.IntegerField()
#     usage_amount_denominator = models.IntegerField()
#     usage_unit = models.CharField(max_length=50)
#     safe_interval = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_timestamp = models.IntegerField()
#     check_status = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_inputs_manege_inf'
#
#
# class TLandInf(models.Model):
#     company_sid = models.IntegerField()
#     land_sid = models.AutoField(unique=True)
#     land_no = models.CharField(primary_key=True, max_length=255)
#     land_name = models.CharField(max_length=255)
#     land_address = models.CharField(max_length=255, blank=True, null=True)
#     land_area = models.FloatField(blank=True, null=True)
#     area_unit = models.CharField(max_length=50, blank=True, null=True)
#     land_admin_name = models.CharField(max_length=255, blank=True, null=True)
#     land_admin_workno = models.CharField(max_length=255, blank=True, null=True)
#     land_discription = models.CharField(max_length=255, blank=True, null=True)
#     tea_variety = models.CharField(max_length=255, blank=True, null=True)
#     tree_age_year = models.IntegerField(blank=True, null=True)
#     tree_age_month = models.IntegerField(blank=True, null=True)
#     company_full_name = models.CharField(max_length=255)
#     company_no = models.CharField(max_length=255)
#     base_sid = models.IntegerField()
#     base_name = models.CharField(max_length=255)
#     base_no = models.ForeignKey(TBaseInf, models.DO_NOTHING, db_column='base_no')
#     update_writer_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_land_inf'
#         unique_together = (('land_no', 'company_sid'),)
#
#
# class TLed(models.Model):
#     led_sid = models.AutoField(unique=True)
#     company_sid = models.IntegerField(primary_key=True)
#     led_name = models.CharField(max_length=255)
#     led_ip = models.CharField(max_length=255, blank=True, null=True)
#     company_no = models.CharField(max_length=255)
#     company_short_name = models.CharField(max_length=255)
#     company_full_name = models.CharField(max_length=255)
#     location_type_code = models.CharField(max_length=255, blank=True, null=True)
#     location_type_name = models.CharField(max_length=255, blank=True, null=True)
#     base_sid = models.IntegerField(blank=True, null=True)
#     base_no = models.CharField(max_length=255, blank=True, null=True)
#     base_name = models.CharField(max_length=255, blank=True, null=True)
#     led_admin_name = models.CharField(max_length=255, blank=True, null=True)
#     led_admin_workno = models.CharField(max_length=255, blank=True, null=True)
#     discription = models.CharField(max_length=255, blank=True, null=True)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_led'
#         unique_together = (('company_sid', 'led_name'),)
#
#
# class TLogs(models.Model):
#     sid = models.AutoField(primary_key=True)
#     company_sid = models.IntegerField(blank=True, null=True)
#     version = models.CharField(max_length=20, blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     method = models.CharField(max_length=255, blank=True, null=True)
#     types = models.CharField(max_length=10, blank=True, null=True)
#     requestip = models.CharField(db_column='requestIp', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     exception_code = models.CharField(max_length=255, blank=True, null=True)
#     exception_detail = models.CharField(max_length=255, blank=True, null=True)
#     params = models.CharField(max_length=255, blank=True, null=True)
#     create_by = models.CharField(max_length=255, blank=True, null=True)
#     createdate = models.IntegerField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 't_logs'
#
#
# class TMeasureData(models.Model):
#     company_sid = models.IntegerField()
#     record_sid = models.AutoField(primary_key=True)
#     measure_item_data = models.FloatField()
#     measure_time = models.IntegerField()
#     module_sid = models.IntegerField()
#     measure_data_source = models.CharField(max_length=1)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#     measure_item_id = models.IntegerField()
#     measure_data_unit_id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 't_measure_data'
#
#
# class TMeasureDataCount(models.Model):
#     record_sid = models.AutoField(primary_key=True)
#     company_sid = models.IntegerField()
#     module_sid = models.IntegerField()
#     measure_item_name = models.CharField(max_length=255)
#     average_data = models.FloatField()
#     max_data = models.FloatField()
#     min_data = models.FloatField()
#     measure_date = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_measure_data_count'
#
#
# class TMessage(models.Model):
#     message_sid = models.AutoField(unique=True)
#     company_sid = models.IntegerField()
#     sender_no = models.CharField(primary_key=True, max_length=255)
#     send_time = models.IntegerField()
#     receiver_no = models.CharField(max_length=255)
#     receive_time = models.IntegerField()
#     text = models.CharField(max_length=16383)
#     theme = models.CharField(max_length=255, blank=True, null=True)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_message'
#         unique_together = (('sender_no', 'send_time', 'receiver_no', 'receive_time'),)
#
#
# class TMessagefilePath(models.Model):
#     message_path_sid = models.AutoField(primary_key=True)
#     company_sid = models.IntegerField()
#     message_sid = models.IntegerField()
#     messagefile_path = models.CharField(max_length=255)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_messagefile_path'
#
#
# class TModule(models.Model):
#     company_sid = models.IntegerField()
#     module_name = models.CharField(primary_key=True, max_length=255)
#     module_sid = models.IntegerField()
#     base_sid = models.IntegerField()
#     base_no = models.CharField(max_length=255)
#     base_name = models.CharField(max_length=255)
#     module_admin_name = models.CharField(max_length=255)
#     module_admin_no = models.CharField(max_length=255)
#     update_timestamp = models.IntegerField()
#     share_status = models.CharField(max_length=1)
#     longitude_position = models.CharField(db_column='longitude_ position', max_length=255)  # Field renamed to remove unsuitable characters.
#     latitude_position = models.CharField(db_column='latitude_ position', max_length=255)  # Field renamed to remove unsuitable characters.
#     base_location = models.CharField(max_length=255)
#     position_sid = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_module'
#         unique_together = (('module_name', 'company_sid'),)
#
#
class TOldMeasureData(models.Model):
    company_sid = models.IntegerField(null=True)
    record_sid = models.AutoField(primary_key=True)
    measure_item_data = models.FloatField(null=True)
    measure_time = models.IntegerField(null=True)
    update_timestamp = models.IntegerField(null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    module_sid = models.IntegerField(null=True)
    measure_item_id = models.IntegerField(null=True)
    measure_data_unit_id = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 't_old_measure_data'
#
#
# class TPackMap(models.Model):
#     company_sid = models.IntegerField()
#     pack_map_sid = models.AutoField(unique=True)
#     product_sid = models.IntegerField()
#     product_name = models.CharField(max_length=255)
#     unified_product_no = models.CharField(max_length=255)
#     produce_date = models.IntegerField()
#     batch_no = models.CharField(max_length=255)
#     pack_no = models.CharField(primary_key=True, max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_pack_map'
#
#
# class TPackPrintRecord(models.Model):
#     company_sid = models.IntegerField()
#     print_record_sid = models.AutoField(primary_key=True)
#     pack_supplier = models.CharField(max_length=255, blank=True, null=True)
#     product_sid = models.IntegerField()
#     unified_product_no = models.CharField(max_length=255)
#     product_name = models.CharField(max_length=255)
#     application_date = models.IntegerField()
#     delivery_date = models.IntegerField(blank=True, null=True)
#     quantity = models.CharField(max_length=10, blank=True, null=True)
#     start_number = models.CharField(max_length=25)
#     end_number = models.CharField(max_length=25)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_pack_print_record'
#
#
# class TPhoto(models.Model):
#     company_sid = models.IntegerField()
#     photo_inf_sid = models.AutoField(primary_key=True)
#     theme_content_code = models.CharField(max_length=255)
#     theme_content = models.CharField(max_length=255)
#     theme_content_sid = models.IntegerField()
#     theme_content_name = models.CharField(max_length=255)
#     photo_address = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_photo'
#
#
# class TPrivilege(models.Model):
#     privilege_sid = models.AutoField()
#     privilege_no = models.CharField(primary_key=True, max_length=255)
#     privilege_name = models.CharField(max_length=255)
#     privilege_address = models.CharField(max_length=255)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_privilege'
#
#
# class TProcessMap(models.Model):
#     company_sid = models.IntegerField()
#     process_map_sid = models.AutoField(primary_key=True)
#     process_name = models.CharField(max_length=255)
#     pre_product_sid = models.IntegerField()
#     pre_product_stage_name = models.CharField(max_length=255)
#     pre_unified_product_no = models.CharField(max_length=255)
#     pre_produce_name = models.CharField(max_length=255)
#     pre_level_name = models.CharField(max_length=255)
#     pre_product_batch_no = models.CharField(max_length=255)
#     pre_produce_date = models.IntegerField()
#     pre_product_specification = models.CharField(max_length=255, blank=True, null=True)
#     pre_product_amount = models.FloatField()
#     pre_amount_unit = models.CharField(max_length=255)
#     post_product_sid = models.IntegerField()
#     post_product_stage_name = models.CharField(max_length=255)
#     post_unified_product_no = models.CharField(max_length=255)
#     post_produce_name = models.CharField(max_length=255)
#     post_level_name = models.CharField(max_length=255)
#     post_product_batch_no = models.CharField(max_length=255)
#     post_produce_date = models.IntegerField()
#     post_product_specification = models.CharField(max_length=255, blank=True, null=True)
#     post_product_amount = models.FloatField()
#     post_amount_unit = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_process_map'
#
#
# class TProduct(models.Model):
#     company_sid = models.IntegerField()
#     product_sid = models.AutoField(unique=True)
#     unified_product_no = models.CharField(primary_key=True, max_length=255)
#     product_no = models.CharField(max_length=255)
#     product_name = models.CharField(max_length=255)
#     product_stage_code = models.CharField(max_length=255)
#     product_stage_name = models.CharField(max_length=255)
#     product_process_code = models.CharField(max_length=255, blank=True, null=True)
#     product_process_name = models.CharField(max_length=255, blank=True, null=True)
#     fresh_leaf_level_code = models.CharField(max_length=255, blank=True, null=True)
#     fresh_leaf_level_name = models.CharField(max_length=255, blank=True, null=True)
#     fresh_variety_code = models.CharField(max_length=255, blank=True, null=True)
#     fresh_variety_name = models.CharField(max_length=255, blank=True, null=True)
#     fpq_level_code = models.CharField(max_length=255, blank=True, null=True)
#     fpq_level_name = models.CharField(max_length=255, blank=True, null=True)
#     cfpq_level_code = models.CharField(max_length=255, blank=True, null=True)
#     cfpq_level_name = models.CharField(max_length=255, blank=True, null=True)
#     process_craft_large_variety_code = models.CharField(max_length=255, blank=True, null=True)
#     process_craft_large_variety_name = models.CharField(max_length=255, blank=True, null=True)
#     process_craft_small_variety_code = models.CharField(max_length=255, blank=True, null=True)
#     process_craft_small_variety_name = models.CharField(max_length=255, blank=True, null=True)
#     tea_species_code = models.CharField(max_length=255, blank=True, null=True)
#     tea_species_name = models.CharField(max_length=255, blank=True, null=True)
#     brand_code = models.CharField(max_length=255, blank=True, null=True)
#     brand_name = models.CharField(max_length=255, blank=True, null=True)
#     product_specification = models.CharField(max_length=255, blank=True, null=True)
#     product_description = models.CharField(max_length=255, blank=True, null=True)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_product'
#
#
# class TProductExpand1(models.Model):
#     company_sid = models.IntegerField()
#     product_sid = models.IntegerField()
#     unified_product_no = models.CharField(primary_key=True, max_length=255)
#     product_stage_name = models.CharField(max_length=255)
#     product_name = models.CharField(max_length=255)
#     goods_barcode = models.CharField(max_length=255)
#     exe_standard = models.CharField(max_length=16, blank=True, null=True)
#     se_content = models.FloatField(blank=True, null=True)
#     se_content_unit = models.CharField(max_length=8, blank=True, null=True)
#     guarantee_period = models.CharField(max_length=255, blank=True, null=True)
#     storage_method = models.CharField(max_length=255, blank=True, null=True)
#     product_series = models.CharField(max_length=255, blank=True, null=True)
#     burde_sheet = models.CharField(max_length=255, blank=True, null=True)
#     goods_pack_type = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_product_expand1'
#
#
# class TProductExpand2(models.Model):
#     company_sid = models.IntegerField()
#     product_sid = models.IntegerField()
#     product_stage_name = models.CharField(max_length=255)
#     product_name = models.CharField(max_length=255)
#     unified_product_no = models.CharField(max_length=255)
#     goods_barcode = models.CharField(primary_key=True, max_length=255)
#     product_price_int = models.IntegerField()
#     product_price_demical = models.IntegerField()
#     product_price_unit = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_product_expand2'
#
#
# class TProductLandMap(models.Model):
#     company_sid = models.IntegerField()
#     product_base_relation_sid = models.IntegerField(primary_key=True)
#     product_sid = models.IntegerField()
#     unified_product_no = models.CharField(max_length=255)
#     product_name = models.CharField(max_length=255)
#     level_name = models.CharField(max_length=255)
#     produce_date = models.IntegerField()
#     product_batch_no = models.CharField(max_length=255)
#     product_specification = models.CharField(max_length=255)
#     product_amount = models.CharField(max_length=255)
#     base_sid = models.IntegerField(blank=True, null=True)
#     base_no = models.CharField(max_length=255, blank=True, null=True)
#     base_name = models.CharField(max_length=255, blank=True, null=True)
#     land_sid = models.IntegerField()
#     land_no = models.CharField(max_length=255)
#     land_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_product_land_map'
#
#
# class TPurchaseLink(models.Model):
#     company_sid = models.IntegerField()
#     product_sid = models.IntegerField()
#     product_stage_name = models.CharField(max_length=255)
#     product_name = models.CharField(max_length=255)
#     unified_product_no = models.CharField(max_length=255)
#     goods_barcode = models.CharField(primary_key=True, max_length=255)
#     purchase_link = models.CharField(max_length=255, blank=True, null=True)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_purchase_link'
#
#
# class TPurchaseRecord(models.Model):
#     company_sid = models.IntegerField(primary_key=True)
#     purchase_record_sid = models.AutoField()
#     record_no = models.CharField(max_length=255)
#     fleaf_product_sid = models.IntegerField()
#     fleaf_unified_product_no = models.CharField(max_length=255)
#     fleaf_product_name = models.CharField(max_length=255)
#     fleaf_level_code = models.CharField(max_length=255)
#     fleaf_level_name = models.CharField(max_length=255)
#     fleaf_weight = models.FloatField()
#     fleaf_weight_unit = models.CharField(max_length=255)
#     standard_uprice = models.FloatField(blank=True, null=True)
#     actual_uprice = models.FloatField()
#     standard_tprice = models.FloatField(blank=True, null=True)
#     actual_tprice = models.FloatField()
#     standard_price_unit = models.CharField(max_length=255, blank=True, null=True)
#     actual_price_unit = models.CharField(max_length=255)
#     hleaf_product_sid = models.IntegerField()
#     hleaf_unified_product_no = models.CharField(max_length=255)
#     hleaf_product_name = models.CharField(max_length=255)
#     hleaf_level_code = models.CharField(max_length=255)
#     hleaf_level_name = models.CharField(max_length=255)
#     hleaf_batch_no = models.CharField(max_length=255)
#     tea_farmer_idcard_number = models.CharField(max_length=255)
#     tea_farmer_name = models.CharField(max_length=255)
#     base_sid = models.IntegerField()
#     base_no = models.CharField(max_length=255)
#     base_name = models.CharField(max_length=255)
#     land_sid = models.IntegerField(blank=True, null=True)
#     land_no = models.CharField(max_length=255, blank=True, null=True)
#     land_name = models.CharField(max_length=255, blank=True, null=True)
#     purchaser_workno = models.CharField(max_length=255)
#     purchaser_name = models.CharField(max_length=255)
#     purchase_date = models.IntegerField()
#     finance_expenditure_status = models.CharField(max_length=1, blank=True, null=True)
#     finance_staff_workno = models.CharField(max_length=255, blank=True, null=True)
#     finance_staff_name = models.CharField(max_length=255, blank=True, null=True)
#     finance_expenditure_date = models.IntegerField(blank=True, null=True)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_purchase_record'
#         unique_together = (('company_sid', 'purchase_record_sid'),)
#
#
# class TQueryTimes(models.Model):
#     company_sid = models.IntegerField()
#     query_sid = models.AutoField(unique=True)
#     pack_no = models.CharField(primary_key=True, max_length=255)
#     query_times = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_query_times'
#
#
# class TReceiveMessage(models.Model):
#     receive_message_sid = models.AutoField(unique=True)
#     company_sid = models.IntegerField()
#     receiver_name = models.CharField(max_length=255)
#     receiver_workno = models.CharField(max_length=255)
#     receiver_no = models.CharField(primary_key=True, max_length=255)
#     receiver_department_name = models.CharField(max_length=255, blank=True, null=True)
#     receive_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_receive_message'
#         unique_together = (('receiver_no', 'receive_time'),)
#
#
# class TReceiveUser(models.Model):
#     user_sid = models.AutoField(primary_key=True)
#     user_email = models.CharField(max_length=255, blank=True, null=True)
#     user_name = models.CharField(max_length=255, blank=True, null=True)
#     user_tel = models.CharField(max_length=255, blank=True, null=True)
#     user_type = models.CharField(max_length=255)
#     selected_status = models.IntegerField(blank=True, null=True)
#     update_timestamp = models.IntegerField(blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_receive_user'
#
#
# class TReferData(models.Model):
#     record_sid = models.AutoField(primary_key=True)
#     measure_item_data = models.FloatField()
#     measure_time = models.IntegerField()
#     pos_sid = models.IntegerField()
#     measure_item_id = models.IntegerField()
#     measure_data_unit_id = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_refer_data'
#
#
# class TReplaceNumberMap(models.Model):
#     map_sid = models.AutoField(unique=True)
#     replace_number = models.CharField(primary_key=True, max_length=255)
#     trace_number = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 't_replace_number_map'
#
#
# class TRole(models.Model):
#     company_sid = models.IntegerField(primary_key=True)
#     role_sid = models.AutoField()
#     role_no = models.CharField(max_length=255)
#     role_name = models.CharField(max_length=255)
#     if_internal_role = models.CharField(max_length=1)
#     role_group = models.CharField(max_length=255, blank=True, null=True)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_role'
#         unique_together = (('company_sid', 'role_no'),)
#
#
# class TRoleAgbd(models.Model):
#     role_id = models.IntegerField(primary_key=True)
#     role_name = models.CharField(max_length=255)
#     role_value = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_role_agbd'
#
#
# class TRolePrivilege(models.Model):
#     company_sid = models.IntegerField()
#     role_privilege_sid = models.AutoField()
#     role_sid = models.IntegerField(primary_key=True)
#     role_no = models.CharField(max_length=255)
#     privilege_sid = models.IntegerField()
#     privilege_no = models.CharField(max_length=255)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_role_privilege'
#         unique_together = (('role_sid', 'privilege_sid'),)
#
#
# class TScm(models.Model):
#     company_sid = models.IntegerField()
#     scm_sid = models.AutoField()
#     scm_no = models.CharField(max_length=255)
#     scm_mac = models.CharField(max_length=20)
#     module_sid = models.IntegerField(primary_key=True)
#     module_name = models.CharField(max_length=255)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_scm'
#         unique_together = (('module_sid', 'scm_no'),)
#
#
# class TSendMessage(models.Model):
#     send_message_sid = models.AutoField(unique=True)
#     company_sid = models.IntegerField()
#     sender_name = models.CharField(max_length=255)
#     sender_workno = models.CharField(max_length=255)
#     sender_no = models.CharField(primary_key=True, max_length=255)
#     sender_department_name = models.CharField(max_length=255, blank=True, null=True)
#     send_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_send_message'
#         unique_together = (('sender_no', 'send_time'),)
#
#
# class TSimpleGoods(models.Model):
#     company_sid = models.IntegerField()
#     product_sid = models.AutoField()
#     product_name = models.CharField(max_length=255)
#     unified_product_no = models.CharField(primary_key=True, max_length=255)
#     burde_sheet = models.CharField(max_length=255, blank=True, null=True)
#     shelf_life = models.CharField(max_length=255, blank=True, null=True)
#     shelf_life_unit = models.CharField(max_length=10, blank=True, null=True)
#     level = models.CharField(max_length=255, blank=True, null=True)
#     brand_name = models.CharField(max_length=255, blank=True, null=True)
#     net_content = models.CharField(max_length=255, blank=True, null=True)
#     net_content_unit = models.CharField(max_length=10, blank=True, null=True)
#     storage_method = models.CharField(max_length=255, blank=True, null=True)
#     product_standard_code = models.CharField(max_length=20, blank=True, null=True)
#     production_license_number = models.CharField(max_length=20, blank=True, null=True)
#     nutrition_facts = models.CharField(max_length=255, blank=True, null=True)
#     raw_material_provenance = models.CharField(max_length=255, blank=True, null=True)
#     origin = models.CharField(max_length=255, blank=True, null=True)
#     specification = models.CharField(max_length=255, blank=True, null=True)
#     goods_barcode = models.CharField(max_length=255)
#     product_description = models.CharField(max_length=255, blank=True, null=True)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_simple_goods'
#
#
# class TSimpleGoodsBatch(models.Model):
#     company_sid = models.IntegerField()
#     batch_map_sid = models.AutoField()
#     product_sid = models.IntegerField()
#     product_name = models.CharField(max_length=255, blank=True, null=True)
#     unified_product_no = models.CharField(max_length=255)
#     goods_barcode = models.CharField(max_length=255)
#     produce_date = models.IntegerField()
#     batch_no = models.CharField(max_length=12)
#     trace_number = models.CharField(primary_key=True, max_length=25)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_simple_goods_batch'
#
#
# class TSimpleGoodsPhoto(models.Model):
#     company_sid = models.IntegerField()
#     photo_sid = models.AutoField(primary_key=True)
#     product_sid = models.IntegerField()
#     product_name = models.CharField(max_length=255)
#     unified_product_no = models.CharField(max_length=255)
#     photo_address = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_simple_goods_photo'
#
#
# class TSimpleGoodsPrice(models.Model):
#     company_sid = models.IntegerField()
#     product_sid = models.IntegerField()
#     product_name = models.CharField(max_length=255)
#     unified_product_no = models.CharField(max_length=255)
#     goods_barcode = models.CharField(primary_key=True, max_length=255)
#     product_price_int = models.IntegerField()
#     product_price_demical = models.IntegerField()
#     product_price_unit = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_simple_goods_price'
#
#
# class TSimplePackingNumbersSection(models.Model):
#     company_sid = models.IntegerField()
#     packing_numbers_section_sid = models.AutoField(primary_key=True)
#     batch_map_sid = models.IntegerField()
#     quantity = models.CharField(max_length=10)
#     start_number = models.CharField(max_length=25)
#     end_number = models.CharField(max_length=25)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_simple_packing_numbers_section'
#
#
# class TSimplePurchaseLink(models.Model):
#     company_sid = models.IntegerField()
#     product_sid = models.IntegerField()
#     product_name = models.CharField(max_length=255)
#     unified_product_no = models.CharField(max_length=255)
#     goods_barcode = models.CharField(primary_key=True, max_length=255)
#     purchase_link = models.CharField(max_length=255, blank=True, null=True)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_simple_purchase_link'
#
#
# class TTeaFarmer(models.Model):
#     company_sid = models.IntegerField()
#     tea_farmer_sid = models.AutoField(unique=True)
#     tea_farmer_name = models.CharField(max_length=255)
#     idcard_number = models.CharField(primary_key=True, max_length=255)
#     sex = models.CharField(max_length=1)
#     address = models.CharField(max_length=255)
#     birth_date = models.IntegerField()
#     idcard_issuing_authority = models.CharField(max_length=255)
#     idcard_valid_term = models.CharField(max_length=255)
#     whether_sign_contract = models.CharField(max_length=1)
#     contract_signing_date = models.IntegerField(blank=True, null=True)
#     registration_date = models.IntegerField()
#     base_sid = models.IntegerField()
#     base_no = models.CharField(max_length=255)
#     base_name = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_tea_farmer'
#
#
# class TTeaFarmerExpand(models.Model):
#     tea_farmer_sid = models.IntegerField(primary_key=True)
#     product_sid = models.IntegerField()
#     company_sid = models.IntegerField(blank=True, null=True)
#     whether_sign_contract = models.CharField(max_length=1, blank=True, null=True)
#     product_name = models.CharField(max_length=255, blank=True, null=True)
#     fresh_leaf_level_name = models.CharField(max_length=255, blank=True, null=True)
#     product_stage_name = models.CharField(max_length=255, blank=True, null=True)
#     warning_output = models.CharField(max_length=255, blank=True, null=True)
#     stop_output = models.CharField(max_length=255, blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_tea_farmer_expand'
#         unique_together = (('tea_farmer_sid', 'product_sid'),)
#
#
# class TTeaFarmerExpand2(models.Model):
#     company_sid = models.IntegerField(primary_key=True)
#     whether_limit = models.CharField(max_length=1)
#     update_timestamp = models.IntegerField(blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_tea_farmer_expand2'
#
#
# class TTeaGardenArea(models.Model):
#     area_sid = models.AutoField(primary_key=True)
#     company_sid = models.IntegerField()
#     tea_garden_type = models.CharField(max_length=1)
#     tea_garden_area = models.FloatField()
#     area_time = models.CharField(max_length=255)
#     country_region_code = models.CharField(max_length=255)
#     province_code = models.CharField(max_length=255)
#     city_code = models.CharField(max_length=255)
#     county_code = models.CharField(max_length=255)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_tea_garden_area'
#
#
# class TThirdPartIr(models.Model):
#     thirdpart_ir_sid = models.AutoField(unique=True)
#     checked_company_ir_no = models.CharField(primary_key=True, max_length=255)
#     company_sid = models.IntegerField()
#     checked_company_full_name = models.CharField(max_length=255)
#     checked_company_short_name = models.CharField(max_length=255)
#     thirdpart_ir_no = models.CharField(max_length=255)
#     thirdpart_inspection_institution_name = models.CharField(max_length=255)
#     unified_product_no = models.CharField(max_length=255)
#     product_name = models.CharField(max_length=255)
#     checked_product_birthdate = models.IntegerField()
#     entrust_institution_name = models.CharField(max_length=255)
#     entrust_date = models.IntegerField()
#     production_company_name = models.CharField(max_length=255)
#     inspection_variety = models.CharField(max_length=255)
#     inspection_item = models.CharField(max_length=255)
#     inspection_standard = models.CharField(max_length=255)
#     inspection_date = models.IntegerField()
#     update_writer_name = models.CharField(max_length=255)
#     update_writer_no = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_third_part_ir'
#         unique_together = (('checked_company_ir_no', 'company_sid'),)
#
#
# class TThirdPartIrPhoto(models.Model):
#     thirdpart_ir_photo_sid = models.AutoField(primary_key=True)
#     thirdpart_ir_sid = models.IntegerField()
#     checked_company_ir_no = models.CharField(max_length=255)
#     company_sid = models.IntegerField()
#     photo_address = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_third_part_ir_photo'
#
#
# class TTracecodeExpand(models.Model):
#     company_sid = models.CharField(max_length=255)
#     company_no = models.IntegerField()
#     company_full_name = models.CharField(max_length=255, blank=True, null=True)
#     application_time = models.IntegerField()
#     all_amount = models.IntegerField()
#     use_amount = models.IntegerField()
#     unuse_amount = models.IntegerField()
#     use_rate = models.FloatField()
#     whether_deeply_cooperate = models.CharField(max_length=2)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_tracecode_expand'
#
#
# class TUser(models.Model):
#     user_sid = models.AutoField(unique=True)
#     user_no = models.CharField(primary_key=True, max_length=255)
#     user_name = models.CharField(max_length=255, blank=True, null=True)
#     whether_mail_active = models.IntegerField()
#     mail_number = models.CharField(max_length=255, blank=True, null=True)
#     whether_bind_qq = models.IntegerField()
#     qq_number = models.CharField(max_length=255, blank=True, null=True)
#     whether_bind_wx = models.IntegerField()
#     wx_number = models.CharField(max_length=255, blank=True, null=True)
#     whether_bind_mobile = models.IntegerField()
#     mobile_number = models.CharField(max_length=255, blank=True, null=True)
#     password = models.CharField(max_length=255)
#     regist_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_user'
#
#
# class TUserAgbd(models.Model):
#     user_id = models.IntegerField(primary_key=True)
#     user_no = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     role_id = models.IntegerField()
#     region_code = models.CharField(max_length=255)
#     region_name = models.CharField(max_length=255)
#     province_code = models.CharField(max_length=255)
#     province_name = models.CharField(max_length=255)
#     city_code = models.CharField(max_length=255)
#     city_name = models.CharField(max_length=255)
#     county_code = models.CharField(max_length=255)
#     county_name = models.CharField(max_length=255)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_user_agbd'
#
#
# class TUserExpand(models.Model):
#     user_sid = models.IntegerField()
#     user_no = models.CharField(primary_key=True, max_length=255)
#     user_name = models.CharField(max_length=255, blank=True, null=True)
#     contact_phone = models.CharField(max_length=255, blank=True, null=True)
#     contact_address = models.CharField(max_length=255, blank=True, null=True)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_user_expand'
#
#
# class TUserRole(models.Model):
#     company_sid = models.IntegerField(primary_key=True)
#     user_role_sid = models.AutoField()
#     user_sid = models.IntegerField()
#     user_no = models.CharField(max_length=255)
#     role_sid = models.IntegerField()
#     role_no = models.CharField(max_length=255)
#     update_timestamp = models.IntegerField()
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_user_role'
#         unique_together = (('company_sid', 'user_sid', 'role_sid'),)
#
#
# class TVendor(models.Model):
#     vendor_sid = models.AutoField(unique=True)
#     vendor_no = models.CharField(primary_key=True, max_length=255)
#     vendor_short_name = models.CharField(max_length=255)
#     vendor_full_name = models.CharField(max_length=255, blank=True, null=True)
#     company_sid = models.IntegerField()
#     contact_phone = models.CharField(max_length=255, blank=True, null=True)
#     contact_address = models.CharField(max_length=255, blank=True, null=True)
#     zip_code = models.CharField(max_length=255, blank=True, null=True)
#     update_writer_no = models.CharField(max_length=255)
#     update_writer_name = models.CharField(max_length=255)
#     update_time = models.IntegerField()
#     update_timestamp = models.IntegerField()
#     notes = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_vendor'
#         unique_together = (('vendor_no', 'company_sid'),)
#
#
# class TempArticle(models.Model):
#     company_sid = models.IntegerField(blank=True, null=True)
#     article_inf_sid = models.AutoField(primary_key=True)
#     theme_content_code = models.CharField(max_length=255, blank=True, null=True)
#     theme_content = models.CharField(max_length=255, blank=True, null=True)
#     theme_content_sid = models.IntegerField(blank=True, null=True)
#     theme_content_name = models.CharField(max_length=255, blank=True, null=True)
#     discription = models.CharField(max_length=16383, blank=True, null=True)
#     update_writer_no = models.CharField(max_length=255, blank=True, null=True)
#     update_writer_name = models.CharField(max_length=255, blank=True, null=True)
#     update_time = models.IntegerField(blank=True, null=True)
#     update_timestamp = models.IntegerField(blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'temp_article'
#
#
# class TempCompany(models.Model):
#     company_sid = models.AutoField(primary_key=True)
#     company_short_name = models.CharField(max_length=255, blank=True, null=True)
#     company_key = models.CharField(max_length=255, blank=True, null=True)
#     company_system_create_time = models.IntegerField(blank=True, null=True)
#     update_timestamp = models.IntegerField(blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'temp_company'
#
#
# class TempCompanyExpand(models.Model):
#     company_sid = models.IntegerField(blank=True, null=True)
#     company_no = models.CharField(primary_key=True, max_length=255)
#     company_short_name = models.CharField(max_length=255, blank=True, null=True)
#     company_full_name = models.CharField(max_length=255, blank=True, null=True)
#     company_zip_code = models.CharField(max_length=255, blank=True, null=True)
#     company_website = models.CharField(max_length=255, blank=True, null=True)
#     company_phone = models.CharField(max_length=255, blank=True, null=True)
#     company_address = models.CharField(max_length=255, blank=True, null=True)
#     company_register_date = models.IntegerField(blank=True, null=True)
#     company_register_no = models.CharField(max_length=32, blank=True, null=True)
#     company_identification_no = models.CharField(max_length=255, blank=True, null=True)
#     country_region_code = models.CharField(max_length=255, blank=True, null=True)
#     country_region = models.CharField(max_length=255, blank=True, null=True)
#     company_province_code = models.CharField(max_length=255, blank=True, null=True)
#     company_province = models.CharField(max_length=255, blank=True, null=True)
#     company_city_code = models.CharField(max_length=255, blank=True, null=True)
#     company_city = models.CharField(max_length=255, blank=True, null=True)
#     company_county_code = models.CharField(max_length=255, blank=True, null=True)
#     company_county = models.CharField(max_length=255, blank=True, null=True)
#     company_industry_code = models.CharField(max_length=255, blank=True, null=True)
#     company_industry = models.CharField(max_length=255, blank=True, null=True)
#     update_timestamp = models.IntegerField(blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'temp_company_expand'
#
#
# class TempCompanyExpend2(models.Model):
#     company_sid = models.IntegerField(blank=True, null=True)
#     company_code = models.CharField(primary_key=True, max_length=255)
#     whether_deeply_cooperate = models.CharField(max_length=1, blank=True, null=True)
#     update_timestamp = models.IntegerField(blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'temp_company_expend2'
#
#
# class TempCompanyUserRelation(models.Model):
#     affiliation_sid = models.AutoField(primary_key=True)
#     user_sid = models.IntegerField(blank=True, null=True)
#     user_no = models.CharField(max_length=255, blank=True, null=True)
#     company_sid = models.IntegerField(blank=True, null=True)
#     company_no = models.CharField(max_length=255, blank=True, null=True)
#     user_workno = models.CharField(max_length=255, blank=True, null=True)
#     update_timestamp = models.IntegerField(blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'temp_company_user_relation'
#
#
# class TempUser(models.Model):
#     user_sid = models.AutoField(primary_key=True)
#     user_no = models.CharField(max_length=255, blank=True, null=True)
#     user_name = models.CharField(max_length=255, blank=True, null=True)
#     whether_mail_active = models.IntegerField(blank=True, null=True)
#     mail_number = models.CharField(max_length=255, blank=True, null=True)
#     whether_bind_qq = models.IntegerField(blank=True, null=True)
#     qq_number = models.CharField(max_length=255, blank=True, null=True)
#     whether_bind_wx = models.IntegerField(blank=True, null=True)
#     wx_number = models.CharField(max_length=255, blank=True, null=True)
#     whether_bind_mobile = models.IntegerField(blank=True, null=True)
#     mobile_number = models.CharField(max_length=255, blank=True, null=True)
#     password = models.CharField(max_length=255, blank=True, null=True)
#     regist_time = models.IntegerField(blank=True, null=True)
#     update_timestamp = models.IntegerField(blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'temp_user'
#
#
# class TempUserExpand(models.Model):
#     user_sid = models.IntegerField(blank=True, null=True)
#     user_no = models.CharField(primary_key=True, max_length=255)
#     user_name = models.CharField(max_length=255, blank=True, null=True)
#     contact_phone = models.CharField(max_length=255, blank=True, null=True)
#     contact_address = models.CharField(max_length=255, blank=True, null=True)
#     update_timestamp = models.IntegerField(blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'temp_user_expand'
#
#
# class TempUserRole(models.Model):
#     company_sid = models.IntegerField(blank=True, null=True)
#     user_role_sid = models.AutoField(primary_key=True)
#     user_sid = models.IntegerField(blank=True, null=True)
#     user_no = models.CharField(max_length=255, blank=True, null=True)
#     role_sid = models.IntegerField(blank=True, null=True)
#     role_no = models.CharField(max_length=255, blank=True, null=True)
#     update_timestamp = models.IntegerField(blank=True, null=True)
#     note = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'temp_user_role'
#
#
# # class TUserExpand(models.Model):
# #     user_sid = models.CharField(max_length=255, blank=True, null=True)
# #     user_no = models.CharField(max_length=255, blank=True, null=True)
# #     user_name = models.CharField(max_length=255, blank=True, null=True)
# #     contact_phone = models.CharField(max_length=255, blank=True, null=True)
# #     contact_address = models.CharField(max_length=255, blank=True, null=True)
# #     update_timestamp = models.CharField(max_length=255, blank=True, null=True)
# #     note = models.CharField(max_length=255, blank=True, null=True)
# #
# #     class Meta:
# #         managed = False
# #         db_table = '�û���չ��(t_user_expand)'
