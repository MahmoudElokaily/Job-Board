from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
# Create your models here.
JPB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time', 'Part Time'),
)

def image_upload(instance , filename):
    imageame  , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

class Job(models.Model):
    owner = models.ForeignKey(User , on_delete=models.CASCADE , related_name='job_owner')
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15 , choices=JPB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(null=True , blank= True)
    def __str__(self):
        return self.title

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwargs)




class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job , on_delete=models.CASCADE , related_name='apply_job')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name