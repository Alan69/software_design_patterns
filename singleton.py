class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

# Example usage:
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True
