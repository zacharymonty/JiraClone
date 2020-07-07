from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)

    STATUS_CHOICES = [("TODO", "To Do"), ("INPROGRESS", "In Progress"), ("DONE", "Done")]
    TYPE_CHOICES = [("BUG", "Bug"), ("RFE", "RFE"), ("DOCUMENTATION", "Documentation")]

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="TODO")
    story_id = models.CharField(max_length=30)
    points = models.PositiveIntegerField(default=0)
    date_created = models.DateField(auto_now=True)
    due_date = models.DateField(auto_now=False)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, default="BUG")
    assignee = models.ForeignKey('User', on_delete=models.CASCADE, null=True)

    # def save(self, *args, **kwargs):
    #     self.title = kwargs['title']
    #     self.description = kwargs['description']
    #     self.status = kwargs['status']
    #     self.due_date = kwargs['due_date']
    #     self.type = kwargs['type']
    #     self.points = kwargs['points']
    #
    #     story_id = 'DEV-' + str(self.id)
    #     self.story_id = story_id

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    @property
    def assigned_stories(self):
        """Return a list of stories that user is assigned to."""
        stories = Story.objects.filter(assignee=self)
        return stories
