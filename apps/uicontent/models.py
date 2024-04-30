from django.db import models

# Create your models here.
class Uicontent(models.Model):
    # id = models.AutoField(primary_key=True)
    header_text = models.CharField(max_length=255,default='')
    owner= models.CharField(max_length=255,default='')
    created_date = models.DateField()
    updated_date = models.DateField(null=True)
    status = models.IntegerField(default=1)
    # role_data = models.ManyToManyField(Role)

    class Meta:
        db_table = 'tbl_uicontent'

    def __str__(self):
        return self.name
