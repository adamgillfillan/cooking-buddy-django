from django.db import models


class Event(models.Model):
    """
        Event model is a table for logging. The following is captures:
        Timestamp of the action
        Confidence level the ASR has in the utterance (0.951231414)
        Utterance that the person made ("Please go to the next step")
        Current Step the user is on in the recipe (1, 2, 3, 4, ..., etc.)
        Action that was taken (i.e. go back, go forward, say how many eggs are needed, etc.)
    """
    # This timestamp is created when the event is inserted in the db. No need to determine timestamp on the client
    # username = models.CharField()
    timestamp = models.DateTimeField(auto_now_add=True)
    confidence = models.FloatField(default=0.0)
    utterance = models.CharField()
    current_step = models.IntegerField()
    action = models.CharField()