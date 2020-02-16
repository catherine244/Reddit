

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to = 'profile_pics/', blank=True, default='profile_pics/default.jpg')

    def save_profile(self):
        self.save()
        
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
            
    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.bio
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        
class Projects(models.Model):
    project_title = models.CharField(max_length=255)
    project_image = models.ImageField(upload_to = 'images/', default='images/default.jpg')
    project_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
    link = models.URLField()
    country = CountryField(blank_label='(select country)', default='NG')

        
    def save_project(self):
        self.save()
    
    def delete_project(self):
        self.delete()        
                