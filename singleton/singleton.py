class Singleton(type):
    objects = {}

    def __call__(cls, *args, **kwargs):
        try:
            object = Singleton.objects["{}.{}".format(cls.__module__, cls.__name__)]
            return object
        except KeyError as e:
            object = super().__call__(*args, **kwargs)
            Singleton.objects.update({"{}.{}".format(cls.__module__, cls.__name__): object})
            return object
