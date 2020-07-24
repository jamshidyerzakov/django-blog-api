from django.db import models


class PostManager(models.Manager):
    """Custom manager for Post model to perform adding tags"""
    def _create_post(self, **data):
        tags = None

        if data.get('tags', None):  # getting tags if they exist
            tags = data['tags'][0].split(",")  # split tags by "," and save as a list
            del data['tags']  # delete tags from 'data' dictionary

        post_obj = self.model(**data)
        post_obj.save(using=self._db)

        post_obj.tags.add(*tags) if tags else None  # add tags by using TaggableManager

        return post_obj

    def create_post(self, **data):
        return self._create_post(**data)