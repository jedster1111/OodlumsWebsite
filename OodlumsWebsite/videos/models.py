from django.db import models

class Video(models.Model):
    title_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    description_text = models.TextField('video description', blank=True)
    youtubeKey_text = models.CharField(max_length=20)
    sellfyMusicVideoKey_text = models.CharField("The Music Video Key for Sellfy", max_length=10, blank=True)
    sellfyLyricVideoKey_text = models.CharField("The Lyric Video Key for Sellfy", max_length=10, blank=True)
    sellfyStitchedVideoKey_text = models.CharField("The Combined Music and Lyric Video Key for Sellfy", max_length=10, blank=True)
    amazonPurchaseLink_text = models.URLField("Amazon purchase link", blank=True)
    iTunesPurchaseLink_text = models.URLField("Itunes purchase link", blank=True)



    def __str__(self):
        return self.title_text

