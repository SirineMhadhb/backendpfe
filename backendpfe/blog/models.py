from turtle import title
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class CategoriesPost(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class ParcoursPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    Categories =  models.ForeignKey(CategoriesPost, on_delete=models.PROTECT, default=1)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time  = models.CharField(max_length=100)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    year = models.CharField(max_length=20)
    content = models.TextField()
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = ParcoursPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = ParcoursPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug
        
        super(ParcoursPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title    

class LevelPost(models.Model):
     title = models.CharField(max_length=50)
     parcours = models.ForeignKey(ParcoursPost , on_delete=models.PROTECT, default=1)
     slug = models.SlugField()
     Categories =  models.ForeignKey(CategoriesPost, on_delete=models.PROTECT, default=1)
     thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
     time = models.CharField(max_length=20)
     month = models.CharField(max_length=3)
     day = models.CharField(max_length=2)
     year = models.CharField(max_length=20)
     content = models.TextField()
     date_created = models.DateTimeField(default=datetime.now, blank=True)
     
     def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = LevelPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = LevelPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug   
        
        super(LevelPost, self).save(*args, **kwargs)

        
     def __str__(self):
          return self.title    

class CoursesPost(models.Model):
    title = models.CharField(max_length=50)
    level = models.ForeignKey(LevelPost , on_delete=models.PROTECT, default=1)
    slug = models.SlugField()
    Categories =  models.ForeignKey(CategoriesPost, on_delete=models.PROTECT, default=1)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time  = models.CharField(max_length=100)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    year = models.CharField(max_length=20)
    content = models.TextField()
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = CoursesPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = CoursesPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug
        
        super(CoursesPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class SectionPost(models.Model):
     title = models.CharField(max_length=50)
     courses = models.ForeignKey(CoursesPost , on_delete=models.PROTECT, default=1)
     slug = models.SlugField()
     Categories =  models.ForeignKey(CategoriesPost, on_delete=models.PROTECT, default=1)
     thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
     time = models.CharField(max_length=20)
     month = models.CharField(max_length=3)
     day = models.CharField(max_length=2)
     year = models.CharField(max_length=20)
     content = models.TextField()
     date_created = models.DateTimeField(default=datetime.now, blank=True)
     
     def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = SectionPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = SectionPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug   
        
        super(SectionPost, self).save(*args, **kwargs)

        
     def __str__(self):
          return self.title

class StepsPost(models.Model):
     title = models.CharField(max_length=50)
     section = models.ForeignKey(SectionPost , on_delete=models.PROTECT, default=1)
     slug = models.SlugField()
     Categories =  models.ForeignKey(CategoriesPost, on_delete=models.PROTECT, default=1)
     thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
     time = models.CharField(max_length=20)
     month = models.CharField(max_length=3)
     day = models.CharField(max_length=2)
     year = models.CharField(max_length=20)
     content = models.TextField()
     date_created = models.DateTimeField(default=datetime.now, blank=True)
     
     def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = StepsPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = StepsPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug   
        
        super(StepsPost, self).save(*args, **kwargs)

        
     def __str__(self):
          return self.title
