from django.db import models

class CafeGallery(models.Model):
    title = models.CharField(max_length=100, blank=True, help_text="Image ka naam ya caption (Optional)")
    image = models.ImageField(upload_to='cafe_gallery/', help_text="Premium quality image upload karein")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Cafe Gallery Images"
        ordering = ['-created_at']  # Naye images sabse pehle dikhengi

    def __str__(self):
        return self.title if self.title else f"Gallery Image {self.id}"
    
    
class CafeContact(models.Model):
    name = models.CharField(max_length=100, help_text="Customer ka naam")
    email = models.EmailField(help_text="Customer ka email address")
    phone = models.CharField(max_length=15, help_text="Customer ka phone number")
    message = models.TextField(help_text="Customer ka message ya query")
    submitted_at = models.DateTimeField(auto_now_add=True, help_text="Kab submit hua")

    class Meta:
        verbose_name_plural = "Cafe Contact Queries"
        ordering = ['-submitted_at']  # Nayi enquiries sabse pehle dikhengi

    def __str__(self):
        return f"{self.name} - {self.email}"