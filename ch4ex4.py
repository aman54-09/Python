#operating overloading
class point:
    def __init__ (s,a=10,b=20):      #contractor with default value
        s.x=a
        s.y=b
        print('contructor..')
    def disp(s):
        print('value of x is ',s.x,'\n value of y is',s.y)
    def __add__ (s,n):               #operator overloading for '+'
        s.x=s.x+n
        s.y=s.y+n
        return s
    def __sub__ (s,n):               #operator overloading for '-'
        s.x=s.x-n
        s.y=s.y-n
        return s
    def __mul__ (s,n):               #operator overloading for '*'
        s.x=s.x*n
        s.y=s.y*n
        return s
    def __div__ (s,n):
        s.x=s.x%n
        s.y=s.y%n
        return s
    
    P1=point()
    P1.disp()

    P2=point(23,34)
    P2.disp()

    P1=p1+10
    P1.disp()

    P2=p2-20
    P2.disp()

    P3=p3*5
    P3.disp()

    P4=p4%10
    P4.disp()
