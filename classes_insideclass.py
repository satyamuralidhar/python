# classes inside a class
class DevOps:
    def __init__(self):
        print('devops course')
    class Aws:
        def __init__(self):
            print('aws cloud environmet')
        def ec2(self):
            print('instance in aws')
        class Azure:
            def __init__(self):
                print('azure cloud environment')
            def vm(self):
                print("vm's in azure ")
D=DevOps()
a=D.Aws()
a.ec2()
# b=D.a.Azure() ~> b=a.Azure because a=D.Aws
b=a.Azure()
b.vm()



