from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


# class AvaliableReaction(models.Model):
#     emoji = models.CharField(max_length=1, unique=True)
#     deleted = models.BooleanField(default=False)


class Post(models.Model):
    author = models.ForeignKey("identity.Identity", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    tags = models.ManyToManyField("forum.Tag", blank=True, related_name="posts")  # fmt: skip
    parent = models.ForeignKey("forum.Post", on_delete=models.CASCADE, blank=True, null=True, related_name="children")  # fmt: skip
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_replied_at = models.DateTimeField(auto_now_add=True)
    locked_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    @classmethod
    def get_index_posts(cls, order_by: str):
        return cls.objects.filter(parent=None, deleted_at=None).order_by(order_by)

    @classmethod
    def get_replies(cls, post_id: int):
        post = cls.objects.filter(pk=post_id).first()
        if post:
            return post.children.filter(deleted_at=None).order_by("created_at")
        else:
            return []
        
    def __str__(self):
        return f"{self.pk} - {self.title} - {self.author}"


# class Reaction(models.Model):
#     author = models.ForeignKey("identity.Identity", on_delete=models.CASCADE)
#     post = models.ForeignKey("forum.Post", on_delete=models.CASCADE)
#     reaction = models.ManyToManyField("forum.AvaliableReaction", blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
