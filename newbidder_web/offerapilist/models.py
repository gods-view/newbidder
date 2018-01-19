from django.db import models
from db.base_manager import BaseManager
from db.base_model import BaseModel


# Create your models here.
class ThirdPartyOfferManager(BaseManager):
    """账户模型管理器类"""

    # def add_one_passport(self, username, password, email):
    #     '''添加一个注册用户信息'''
    #     obj = self.create_one_object(username=username, password=get_hash(password), email=email)
    #     # 返回对象
    #     return obj
    def get_offers_by_type(self, offerid=None, offername=None, limit=None, sort='default', sorttype=3):
        """查找offer信息"""
        order_by = ('-id',)
        # print(sort, sorttype)
        if sort == 'offername':
            order_by = ('name',)
            if sorttype == '0':
                order_by = ('-name',)
        elif sort == 'countrycode':
            order_by = ('countryCode',)
            if sorttype == '0':
                order_by = ('-countryCode',)
        elif sort == 'payoutvalue':
            order_by = ('payoutValue',)
            if sorttype == '0':
                order_by = ('-payoutValue',)
        elif sort == 'category':
            order_by = ('category',)
            if sorttype == '0':
                order_by = ('-category',)
        elif sort == 'carrier':
            order_by = ('carrier',)
            if sorttype == '0':
                order_by = ('-carrier',)
        elif sort == 'platform':
            order_by = ('platform',)
            if sorttype == '0':
                order_by = ('-platform',)
        # 注意：get_object_list的参数中,filters是字典类型，order_by是元组类型
        # 参数类型要正确
        # print(order_by)
        if offerid is not None:
            print("search by offerid")
            offers_li = self.filter(
                models.Q(offerId__icontains=offerid)).order_by(*order_by)
            # offers_li = self.get_object_list_by_condition(filters={'offerId': offerid, 'name': offername},
            #                                               order_by=order_by)
        elif offername is not None:
            print("search by offername")
            offers_li = self.filter(
                models.Q(models.Q(name__icontains=offername))).order_by(*order_by)
        else:
            offers_li = self.get_object_list(order_by=order_by)
        # 根据传入的limit取出查询集中的几条数据
        if limit:
            # 对查询集进行切片
            offers_li = offers_li[:limit]
        return offers_li

    def get_offers_by_Mobile(self, type=None, limit=None, sort='default'):
        print("get offer by mobile")
        # 指定排序规则
        order_by = ('id',)
        if sort == 'offername':
            order_by = ('name',)
        elif sort == 'countrycode':
            order_by = ('countryCode',)
        elif sort == 'payoutvalue':
            order_by = ('payoutValue',)
        elif sort == 'category':
            order_by = ('category',)
        elif sort == 'carrier':
            order_by = ('carrier',)
        elif sort == 'platform':
            order_by = ('platform',)
        print(type)
        offers_li = self.get_object_list(order_by=order_by)
        if type == 'Mobile':
            offers_li = self.filter(
                models.Q(category__startswith='application') | models.Q(category__istartswith='Mobile') | models.Q(
                    category__istartswith='diet') | models.Q(category__istartswith='hairloss') | models.Q(
                    category__istartswith='skin') | models.Q(category__istartswith='dating') | models.Q(
                    category__istartswith='game') | models.Q(category__istartswith='gambling') | models.Q(
                    category__istartswith='mainstream') | models.Q(category__istartswith='mobile content') | models.Q(
                    category__istartswith='Adult') | models.Q(category__istartswith='sweepstake') | models.Q(
                    category__istartswith='Male Enhancement'))
        # offers_li = self.get_object_list(order_by=order_by)
        # 根据传入的limit取出查询集中的几条数据
        if limit:
            # 对查询集进行切片
            offers_li = offers_li[:limit]
        return offers_li


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
    payoutValue = models.CharField(max_length=11, null=False, default=0)
    category = models.TextField()
    carrier = models.TextField()
    platform = models.TextField()
    detail = models.TextField()
    sourcename = models.CharField(max_length=20, default='')
    updatetime = models.TimeField()

    objects = ThirdPartyOfferManager()

    class Meta:
        db_table = "ThirdPartyOffer"
