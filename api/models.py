from django.db import models

class User(models.Model) :
  user_id = models.CharField(max_length=20)
  user_pw = models.CharField(max_length=20)
  nickname = models.CharField(max_length=20)

class Record(models.Model):
  title = models.CharField(max_length=100)
  tag = models.IntegerField()
  cover_path = models.TextField(null=True, blank=True)
  score = models.IntegerField(null=True, blank=True)
  memo = models.TextField(null=True, blank=True)
  liked = models.BooleanField(null=True, blank=True)
  date = models.DateField(auto_now=True)

class Record_List(models.Model):
  owner_id = models.ForeignKey("User", related_name="record_owner", on_delete=models.CASCADE, db_column="owner_id")
  record_id = models.ForeignKey("Record", related_name="record", on_delete=models.CASCADE, db_column="record_id")

class Wish_Media(models.Model):
  tag = models.IntegerField()
  title = models.CharField(max_length=50)
  memo = models.TextField(blank=True)

class Wish_Media_List(models.Model):
  owner_id = models.ForeignKey("User", related_name="wish_owner", on_delete=models.CASCADE, db_column="owner_id")
  wish_id = models.ForeignKey("Wish_Media", related_name="wish_media", on_delete=models.CASCADE, db_column="wish_id")
