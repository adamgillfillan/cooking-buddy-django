from django.db import models


class Event(models.Model):
    """Event model is a table for logging. The following is captured:
    Timestamp of the action
    Confidence level the ASR has in the utterance (0.951231414)
    Utterance that the person made ("Please go to the next step")
    Current Step the user is on in the recipe (1, 2, 3, 4, ..., etc.)
    Action that was taken (i.e. go back, go forward, say how many eggs are needed, etc.)
    """
    # This timestamp is created when the event is inserted in the db. No need to determine timestamp on the client
    name = models.CharField(default='', max_length=100)
    session_id = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    recipe = models.CharField(default='', max_length=100)
    confidence = models.FloatField(default=0.0)
    utterance = models.CharField(max_length=400)
    current_step = models.IntegerField()
    action = models.CharField(default='nothing', max_length=50)
    # keep timestamp.editable here so we can view the timestamp on admin page
    # you must comment it out if you migrate the table, however. uncomment it after a migration
    timestamp.editable = True

    def __unicode__(self):
        return self.action