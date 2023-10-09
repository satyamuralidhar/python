import argparse

if __name__ == "__main__":

    #initialize the parser
    parser = argparse.ArgumentParser(
        description="Basic Arg Parser"
    )

    #optional and positional args
    '''
    positional:
    ----------
    parser.add_argument("num1",help="Number1",type=int)
    parser.add_argument("num2",help="Number2",type=int)
    parser.add_argument("operation",help="provide operator")
    '''

    #optional:

    parser.add_argument("-n1","--num1",help="Number1",type=int,metavar='',required=True)
    parser.add_argument("-n2","--num2",help="Number2",type=int,metavar='',required=True)
    parser.add_argument("-o","--operation",help="provide operator",default="*",metavar='',required=True)
    
    #exec: python argparser/basic.py -n1 10 -n2 2 -o '*' or  python argparser/basic.py -n1=10 -n2=2 -o=*

    #parse the arguments
    args = parser.parse_args()
    print(args)

    result = None
    if args.operation == '+':
        result=args.num1 + args.num2
    elif args.operation == '-':
        result=args.num1 - args.num2
    elif args.operation == '*':
        result=args.num1 * args.num2
    elif args.operation == '/':
        result=args.num1 / args.num2
    else:
        print("please enter correct operators")
    print(f'Result: ',result)

    '''
    o/p:
    ----
    $ python argparser/basic.py 10 2 +
    Namespace(num1='10', num2='2', operation='+')
    output we get the string format num1='10' and num2='2'
    we have to convert into integer or float

    python argparser/basic.py -h

    positional arguments:
        num1        Number1
        num2        Number2
        operation   provider operator


    positional : 
        parser.add_argument("num1",help="Number1",type=int)
        exec: python argparser/basic.py 10 2 '*'
    optional:
        parser.add_argument("--num1",help="Number1",type=int)
        and we can also create short form for this optional params
        parser.add_argument("o","--operation",help="provide operator",default="*")
        exec: python argparser/basic.py --num1 10 --num2 2 --operator '*'
        in this case default value will work ==> default = "*"

        required = True if its mandatory

        metavar:  if we cant used metavar which seaching help is not proper indentation
         python argparser/basic.py -h
           -h, --help            show this help message and  
                        exit
        -n1 NUM1, --num1 NUM1
                                    Number1
        -n2 NUM2, --num2 NUM2
                                    Number2
        -o OPERATION, --operation OPERATION
                                    provide operator

        after using metavars :
        options:
            -h, --help         show this help message and exit
            -n1 , --num1       Number1
            -n2 , --num2       Number2
            -o , --operation   provide operator



    '''

    
    
