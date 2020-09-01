from django.db import models


# Create your models here.
class Post(models.Model):
    header_image = models.ImageField(null=True, blank=True)
    is_mobile = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=250)
    body = models.TextField(null=True,blank=True)
    

    screenshot_1 = models.ImageField(null=True,blank=True)
    title_1 = models.CharField(null=True,blank=True,max_length=255,default="screenshot")
    screenshot_2 = models.ImageField(null=True,blank=True)
    title_2 = models.CharField(null=True,blank=True,max_length=255,default="screenshot")
    screenshot_3 = models.ImageField(null=True,blank=True)
    title_3 = models.CharField(null=True,blank=True,max_length=255,default="screenshot") 
    screenshot_4 = models.ImageField(null=True,blank=True)
    title_4 = models.CharField(null=True,blank=True,max_length=255,default="screenshot")   
    screenshot_5 = models.ImageField(null=True,blank=True)
    title_5 = models.CharField(null=True,blank=True,max_length=255,default="screenshot") 
    screenshot_6 = models.ImageField(null=True,blank=True)
    title_6 = models.CharField(null=True,blank=True,max_length=255,default="screenshot") 
    screenshot_7 = models.ImageField(null=True,blank=True)
    title_7 = models.CharField(null=True,blank=True,max_length=255,default="screenshot") 
    screenshot_8 = models.ImageField(null=True,blank=True)
    title_8 = models.CharField(null=True,blank=True,max_length=255,default="screenshot") 
    screenshot_9 = models.ImageField(null=True,blank=True)
    title_9 = models.CharField(null=True,blank=True,max_length=255,default="screenshot")     
    screenshot_10 = models.ImageField(null=True,blank=True)
    title_10 = models.CharField(null=True,blank=True,max_length=255,default="screenshot") 


    features_1 = models.CharField(null=True, blank=True, max_length=50)
    features_2 = models.CharField(null=True, blank=True, max_length=50)
    features_3 = models.CharField(null=True, blank=True, max_length=50)
    features_4 = models.CharField(null=True, blank=True, max_length=50)
    features_5 = models.CharField(null=True, blank=True, max_length=50)
    features_6 = models.CharField(null=True, blank=True, max_length=50)
    features_7 = models.CharField(null=True, blank=True, max_length=50)
    features_8 = models.CharField(null=True, blank=True, max_length=50)
    features_9 = models.CharField(null=True, blank=True, max_length=50)
    features_10 = models.CharField(null=True, blank=True, max_length=50)
    features_11 = models.CharField(null=True, blank=True, max_length=50) 
    features_12 = models.CharField(null=True, blank=True, max_length=50)
    features_13 = models.CharField(null=True, blank=True, max_length=50)  

    technologies_1 = models.CharField(null=True, blank=True, max_length=50) 
    technologies_2 = models.CharField(null=True, blank=True, max_length=50) 
    technologies_3 = models.CharField(null=True, blank=True, max_length=50) 
    technologies_4 = models.CharField(null=True, blank=True, max_length=50) 
    technologies_5 = models.CharField(null=True, blank=True, max_length=50) 
    technologies_6 = models.CharField(null=True, blank=True, max_length=50) 
    technologies_7 = models.CharField(null=True, blank=True, max_length=50) 
    technologies_8 = models.CharField(null=True, blank=True, max_length=50) 
    
   



    def __str__(self):
        return self.title
    


