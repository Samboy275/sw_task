

def serialize_category(category):
    """
        Converts category into a dict representation.

        Args:
            Category instance to serialize.

        Returns:
            dict: dictionary with keys id and display_name
    """
    return {
                'id' : category.id,
                'display_name' : category.__str__()
            }


def serialize_categories(categories):
    """
        Converts a list of categories into a list of dicts representing them.

        Args:
            Category instances to be serialized.

        Returns:
            dict : dictionary with categories key which holds a list of dict representation of categories
    """
    return {'categories' : [serialize_category(category) for category in categories]}
