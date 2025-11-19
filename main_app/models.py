from django.db import models

class AboutMe(models.Model):
    content = models.TextField(help_text="Enter your about me or summary content.")
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True)
    
    def __str__(self):
        return "About Me / Summary"

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

class Project(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    date_completed = models.DateField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_received = models.DateField()
    image = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # null or blank if current job
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experience"

class Publication(models.Model):
    title = models.CharField(max_length=300)
    publication_date = models.DateField(null=True, blank=True)
    publisher = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"

class LeadershipActivity(models.Model):
    role = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.role} at {self.organization}"

    class Meta:
        verbose_name = "Leadership Activity"
        verbose_name_plural = "Leadership Activities"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50, blank=True)  # e.g. Beginner, Intermediate, Expert

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} from {self.institution}"

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
