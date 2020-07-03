from django.db import models
import computed_property

class Post(models.Model):
    Boast = 'Boast'
    Roast = 'Roast'

    POST_CHOICES = [
        (Boast, 'Boast'),
        (Roast, 'Roast')
    ]

    text = models.CharField(max_length=280)
    post_time = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    post_choice = models.CharField(choices=POST_CHOICES, default=Boast, max_length=6)
    score = computed_property.ComputedIntegerField(compute_from='get_score')

    @property
    def get_score(self):
        vote_score = self.upvotes - self.downvotes
        return vote_score
 
    def __str__(self):
        return self.text