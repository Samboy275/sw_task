from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        # Specifying table name in database
        db_table = 'categories'

    name = models.CharField(max_length=255)
    parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE)
    cat_type = models.CharField(max_length=1)

    # Current level of the hierarchy
    level = models.IntegerField(default=0)


    def __str__(self):
        """
            This method returns a string representing the category up to its root category
        """

        # Parts is the list of connected categories all the way to the node category
        parts = []

        # Current category object
        current = self

        # Traversing categories all the way to the root category
        while current:
            # Insert every category at 0 so the root is at index 0
            parts.insert(0, current)
            current = current.parent

        # Getting name of the root category and types down to the lead category
        hierarchy_list = [parts[0].name] + [p.cat_type for p in parts[1:]]

        # Converting the hierarchy to str
        hierarchy_str = str(hierarchy_list[0])

        # If there is sub categories format the string representation accordingly
        if len(hierarchy_list) > 1:
            hierarchy_str += str(hierarchy_list[1]) + ('-' * (len(hierarchy_list) > 2))
            # Adding a dash separator for subsequent categories

            hierarchy_str += '-'.join(hierarchy_list[2:])

        # Producing the prefix of sub based on the depth of the current category
        prefix = " ".join(["SUB"] * self.level)

        return f"{prefix + ' Category ' if prefix else 'Category '}{hierarchy_str}"

    def __repr__(self):
        return self.__str__()
