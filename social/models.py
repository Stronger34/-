from django.db import models
from jsonfield import JSONField


class Users(models.Model):
    name = models.CharField(max_length=50)
    #-------------------------------------------------------------
    insta_bio = models.CharField(max_length=1000, blank=True)
    insta_timestamps = JSONField(blank=True)
    insta_bio_url = models.CharField(max_length=1000, blank=True, null=True)
    insta_followers = models.CharField(max_length=10, blank=True)
    insta_follow = models.CharField(max_length=10,blank=True)
    insta_name = models.CharField(max_length=50)
    insta_profile_pic = models.CharField(max_length=1000, default="/static/images/socialpath.png")
    insta_descriptions = JSONField(blank=True)
    insta_captions = JSONField(blank=True)
    insta_locations = JSONField(blank=True)
    insta_similar = JSONField(blank=True)
    insta_exists = models.BooleanField(default=False)
    #-------------------------------------------------
    twitter_bio = models.CharField(max_length=500, blank=True)
    twitter_created_at = models.CharField(max_length=25, blank=True)
    twitter_profile_pic = models.CharField(max_length=25, default="/static/images/socialpath.png")
    twitter_hashtags = JSONField(blank=True)
    twitter_symbols = JSONField(blank=True)
    twitter_user_mentions = JSONField(blank=True)
    twitter_url = JSONField(blank=True)
    twitter_text = JSONField(blank=True)
    twitter_timestamps = JSONField(blank=True)
    twitter_geo = JSONField(blank=True)
    twitter_favourites = models.CharField(max_length=10,blank=True)
    twitter_followers =models.CharField(max_length=10,blank=True)
    twitter_following = models.CharField(max_length=10,blank=True)
    twitter_similar = JSONField(blank=True)
    twitter_exists = models.BooleanField(default=False)
    #--------------------------------------------------
    reddit_karma = models.CharField(max_length=10, blank=True)
    reddit_joined = models.CharField(max_length=25, blank=True)
    reddit_profile_pic = models.CharField(max_length=1000, default="/static/images/socialpath.png")
    reddit_subreddits = JSONField(blank=True)
    reddit_timestamps = JSONField(blank=True)
    reddit_ups = JSONField(blank=True)
    reddit_text = JSONField(blank=True)
    reddit_exists = models.BooleanField(default=False)
    # --------------------------------------------------
    facebook_username = models.CharField(max_length=50, blank=True)
    facebook_timestamp = JSONField(blank=True)
    facebook_words = JSONField(blank=True)
    facebook_likes = JSONField(blank=True)
    facebook_comments = JSONField(blank=True)
    facebook_exists = models.BooleanField(default=False)
    #----------------------------------------------------1
    stackoverflow_created_at = models.CharField(max_length=25, blank=True)
    stackoverflow_location = models.CharField(max_length=100, blank=True)
    stackoverflow_profile_pic = models.CharField(max_length=1000,default="/static/images/socialpath.png")
    stackoverflow_reputation = models.CharField(max_length=50, blank=True)
    stackoverflow_last_access = models.CharField(max_length=25, blank=True)
    stackoverflow_url = models.CharField(max_length=200, blank=True)
    stackoverflow_score = JSONField(blank=True)
    stackoverflow_tags = JSONField(blank=True)
    stackoverflow_text = JSONField(blank=True)
    stackoveflow_timestamps = JSONField(blank=True)
    stackoverflow_similar = JSONField(blank=True,default={})
    stackoverflow_user_url = models.CharField(max_length=200, blank=True)
    stackoverflow_exists = models.BooleanField(default=False)


