from django.db import models



CATEGORY = [
    ('Programming', 'Programming'),
    ('Languages', 'Languages'),
    ('Jobs', 'Jobs'),
    ('Python', 'Python'),
    ('Django', 'Django'),
]



class Post(models.Model):

    title = models.CharField(max_length=100)
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField()
    category = models.CharField(max_length=15, choices=CATEGORY)

    created_at = models.DateTimeField(auto_now_add=True) 
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}__ "




