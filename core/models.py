from io import BytesIO
from tracemalloc import get_object_traceback
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
from django.core.files import File
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug 
    

class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    intro = models.TextField()
    body =  RichTextUploadingField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'uploads/', blank = True, null = True)
    thumbnail = models.ImageField(upload_to = 'uploads/', blank = True, null = True)
    tags = TaggableManager()

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)
    
    
    def save(self, *args, **kwargs):
        print('Save', self.image.path)
        self.thumbnail = self.make_thumbnail(self.image)
        
        super().save(*args, **kwargs)


    def make_thumbnail(self, image, size= (640 , 360)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality = 85)
        thumbnail = File(thumb_io, name= image.name)
        return thumbnail

