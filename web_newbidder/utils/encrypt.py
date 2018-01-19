from hashlib import md5


def get_hash(str, salt=None):  # salt 盐
    '''取一个字符串的hash值'''
    # 提高字符串的复杂度
    # if salt:
    #     str = str + salt
    # 取str　hash值
    # print(str)
    sh = md5()
    sh.update(str.encode('utf-8'))
    # print(sh.hexdigest())
    return sh.hexdigest()


if __name__ == '__main__':
    get_hash('chuck@newbidder.com')
