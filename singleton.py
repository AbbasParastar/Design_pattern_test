class singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(*args, **kwargs).__new__(cls)
        return cls.instance
class Database(singleton):
    pass



class SSHConnection(singleton):
    pass


if  __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 == db2)

    ssh1 = SSHConnection()
    ssh2 = SSHConnection()
    print(ssh1 == ssh2)

    print(id(db1))
    print(id(db2))
    print(id(ssh1)) 
    print(id(ssh2))