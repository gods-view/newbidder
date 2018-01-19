from django.db import models
from db.base_manager import BaseManager
from db.base_model import BaseModel
from utils.encrypt import get_hash


class UserManager(BaseManager):
    '''账户模型管理器类'''

    def add_one_passport(self, username, password, email):
        '''添加一个注册用户信息'''
        obj = self.create_one_object(username=username, password=get_hash(password), email=email)
        # 返回对象
        return obj

    def get_one_passport(self, email, password=None):
        '''查找账户信息'''
        print(email, password)
        if password is None:
            # 根据用户名查找账户信息
            obj = self.get_one_object(email=email)
        else:
            # 根据用户名和密码查找账户信息
            obj = self.get_one_object(email=email, password=get_hash(password))
        return obj


# Create your models here.
class User(BaseModel):
    '''账户模型类'''
    id = models.IntegerField(max_length=11, null=False, primary_key=True)
    email = models.CharField(max_length=50, verbose_name='账户名称')
    password = models.CharField(max_length=256, verbose_name='密码')
    status = models.IntegerField(default=0, verbose_name='状态')
    deleted = models.IntegerField(default=0, verbose_name='是否删除')
    emailVerified = models.IntegerField(default=0, verbose_name="邮箱是否验证")

    objects = UserManager()  # 自定义模型管理器类对象

    class Meta:
        db_table = 'User'


# class Offer(models.Model):
#     '''账户模型类'''
#     email = models.CharField(max_length=50, verbose_name='账户名称')
#     password = models.CharField(max_length=256, verbose_name='密码')
#     status = models.IntegerField(default=0, verbose_name='状态')
#     deleted = models.IntegerField(default=0, verbose_name='是否删除')
#     emailVerified = models.IntegerField(default=0, verbose_name="邮箱是否验证")
#
#     objects = UserManager()  # 自定义模型管理器类对象
#
#     class Meta:
#         db_table = 'User'

class ThirdPartyOfferManager(BaseManager):
    '''账户模型管理器类'''

    # def add_one_passport(self, username, password, email):
    #     '''添加一个注册用户信息'''
    #     obj = self.create_one_object(username=username, password=get_hash(password), email=email)
    #     # 返回对象
    #     return obj
    def get_one_objects(self, offerid=None, taskid=None):
        '''查找账户信息'''
        print(offerid)
        if offerid is None:
            # pass
            obj = self.get_all_object()
        else:
            obj = self.get_one_object(offerId=offerid, taskId=taskid)
            # obj = self.get_one_object(email=email, password=get_hash(password))
            # pass
        return obj


class ThirdPartyOffer(BaseModel):
    """
    offer
    """
    id = models.IntegerField(max_length=11, null=False, primary_key=True)
    userId = models.IntegerField(max_length=11, null=False)
    taskId = models.IntegerField(max_length=11, null=False)
    status = models.IntegerField(max_length=11)
    offerId = models.TextField()
    name = models.CharField(max_length=256, null=False, default='')
    previewLink = models.TextField()
    trackingLink = models.TextField()
    countryCode = models.TextField()
    payoutMode = models.IntegerField(max_length=11, null=False, default=1)
    payoutValue = models.DecimalField(max_digits=10, decimal_places=5, null=False, default='0.00000')
    payoutValue = models.CharField(max_length=11, null=False, default=0)
    category = models.TextField()
    carrier = models.TextField()
    platform = models.TextField()
    detail = models.TextField()

    objects = ThirdPartyOfferManager()

    class Meta:
        db_table = "ThirdPartyOffer"
