class TimestampedModel(models.Model):
    """
    Abstract Model for timestamping create and updates.
    """

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
