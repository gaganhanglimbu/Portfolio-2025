from django.db import models
from django.urls import reverse

class CustomUser(models.Model):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()
    mobile_number = models.PositiveBigIntegerField()
    is_freelance = models.BooleanField()
    designation = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    total_project = models.IntegerField()
    profile_picture = models.ImageField(upload_to='profile_picture')
    description = models.TextField()
    experience = models.IntegerField()
    resume = models.FileField(upload_to='documents/')
    my_award_number = models.IntegerField()
    

    class Meta:
        verbose_name = 'Personal Information'
    
    def __str__(self):
        return self.first_name
    
class Speciality(models.Model):
    icon = models.ImageField(upload_to='service/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_experience')
    start_date = models.DateField()
    end_date =models.DateField(blank=True, null=True)
    company_name = models.CharField(max_length=150)
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name
    
class Education(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date =models.DateField(blank=True, null=True)
    college_name = models.CharField(max_length=150)
    degree = models.CharField(max_length=100)

    def __str__(self):
        return self.college_name
    
class Skill(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    skill_icon = models.ImageField(upload_to='skill_icon/')
    percentage = models.IntegerField()

    def __str__(self):
        return self.skill

class Award(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    award_icon = models.ImageField(upload_to='award_icon/')
    award_title = models.CharField(max_length=100)
    award_name = models.CharField(max_length=100)
    award_date = models.DateField()

    def __str__(self):
        return self.award_title
    

class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tools = models.CharField(max_length=100)
    category = models.CharField(max_length=80)
    overview = models.TextField()
    image = models.ImageField(upload_to='project/')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})
    

TAG_CHOICE = (
    ('UI/UX','UI/UX'),
    ('Web Developement','Web Developement'),
    ('Mobile App','Mobile App'),
    ('AI','AI'),
)    
class Tag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tags')
    tag = models.CharField(max_length=50, choices=TAG_CHOICE)

    def __str__(self):
        return self.project.title

    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.PositiveBigIntegerField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name