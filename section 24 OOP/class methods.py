class User:
    active_users = 0
    @classmethod
    def _dispaly_active_users(cls):
        return f"there are currently {cls.active_users} active users"

    @classmethod
    def form_string(cls,data_str):
        first,last,age = data_str.split(",")
        return cls(first,last, int(age))

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
