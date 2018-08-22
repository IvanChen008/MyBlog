import www.orm
from www.models import User, Blog, Comment
# import asyncio

def test():
    yield from www.orm.create_pool(user='www_data', password='www_data', database="awesome")

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()


# for x in test():
#     pass
if __name__ == "__main__":
    test()
