from django.db import models
from django.utils.text import slugify
from froala_editor.fields import FroalaField

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = FroalaField()
    website_url = models.URLField(blank=True, null=True)  # Add a field for the website URL
    #embed_code = models.TextField()  # HTML iframe for embedding
    thumbnail = models.ImageField(upload_to="thumbnails/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='games')
    slug = models.SlugField(unique=True, blank=True)  # For SEO-friendly URLs
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
