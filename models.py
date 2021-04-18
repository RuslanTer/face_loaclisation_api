from tortoise import fields, models


class Users(models.Model):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    #: This is a username
    username = fields.CharField(max_length=20, unique=True)
    name = fields.CharField(max_length=50, null=True)
    family_name = fields.CharField(max_length=50, null=True)
    category = fields.CharField(max_length=30, default="user")
    password_hash = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    image: fields.ReverseRelation["Image"]

    def full_name(self) -> str:
        """
        Returns the best name
        """
        if self.name or self.family_name:
            return f"{self.name or ''} {self.family_name or ''}".strip()
        return self.username

    class PydanticMeta:
        computed = ["full_name"]


class Image(models.Model):
    """
    The image model
    """
    id = fields.IntField(pk=True)
    description = fields.TextField()
    user = fields.ForeignKeyField('models.Users', on_delete=fields.CASCADE)
    image = fields.BinaryField()
    count_faces = fields.IntField()
    faces: fields.ReverseRelation["Faces"]

    class PydanticMeta:
        exclude = ['image']


class Faces(models.Model):
    """
        The face info model
    """
    id = fields.IntField(pk=True)
    box = fields.TextField()
    confidence = fields.FloatField()
    left_eye = fields.TextField()
    right_eye = fields.TextField()
    nose = fields.TextField()
    mouth_left = fields.TextField()
    mouth_right = fields.TextField()
    image = fields.ForeignKeyField('models.Image', on_delete=fields.CASCADE)



