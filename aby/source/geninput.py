# this file should live in the examples directory

import random, argparse, os, math
HOME='/root/ABY/src/examples/'

def create_dirs(program):
    dirname = HOME + program + "/data"
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError as e:
            if e.errno != errno.EEXIST: raise

def gen_mult3_input():
    # 5 bit inputs for a max of 16 bit result
    BITS = 5;
    f0 = open(HOME+"mult3/data/mult3.0.dat",'w+')
    f1 = open(HOME+"mult3/data/mult3.1.dat",'w+')

    product = 1
    for _ in range(3):
        x = random.getrandbits(BITS)
        left = random.randrange(x)

        f0.write("%d\n"%(x-left))
        f1.write("%d\n"%left)

        product *= x
    
    f0.close()
    f1.close()

    print("Expected result: %d"%product)

def gen_innerprod_input(l):
    BITS = (16 - int(math.log(10,2))) / 2 

    xs = [random.getrandbits(BITS) for _ in range(l)]
    ys = [random.getrandbits(BITS) for _ in range(l)]
    result = sum([x*y for x,y in zip(xs,ys)])

    for i,arr in zip([0,1], [xs,ys]):
        with open(HOME+"innerprod/data/innerprod.%d.dat"%i,'w+') as f:
            for a in arr:
                f.write("%d\n"%a)

    print("Expected value: %d"%result)

def gen_add_input():
    # 15 bit inputs for a max of 16 bit result
    BITS = 15;
    f0 = open(HOME+"add/data/add.0.dat",'w+')
    f1 = open(HOME+"add/data/add.1.dat",'w+')

    sum = 0
    for _ in range(2):
        x = random.getrandbits(BITS)
        left = random.randrange(x)

        f0.write("%d\n"%(x-left))
        f1.write("%d\n"%left)

        sum += x
    
    f0.close()
    f1.close()

    print("Expected result: %d"%sum)
    
def gen_mult_input():
    # 8 bit inputs for a max of 16 bit result
    BITS = 8;
    f0 = open(HOME+"mult/data/mult.0.dat",'w+')
    f1 = open(HOME+"mult/data/mult.1.dat",'w+')

    product = 1
    for _ in range(2):
        x = random.getrandbits(BITS)
        left = random.randrange(x)

        f0.write("%d\n"%(x-left))
        f1.write("%d\n"%left)

        product *= x
    
    f0.close()
    f1.close()

    print("Expected result: %d"%product)

def gen_and_input():
    BITS = 16;
    f0 = open(HOME+"and/data/and.0.dat",'w+')
    f1 = open(HOME+"and/data/and.1.dat",'w+')

    x = random.getrandbits(BITS)
    left = random.randrange(x)
    f0.write("%d\n"%(x-left))
    f1.write("%d\n"%left)
    
    y = random.getrandbits(BITS)
    left = random.randrange(y)
    f0.write("%d\n"%(y-left))
    f1.write("%d\n"%left)
    
    result = x & y
    
    f0.close()
    f1.close()

    print("Expected result: %d"%result)

def gen_xor_input():
    BITS = 16
    f0 = open(HOME+"xor/data/xor.0.dat",'w+')
    f1 = open(HOME+"xor/data/xor.1.dat",'w+')

    x = random.getrandbits(BITS)
    left = random.randrange(x)
    f0.write("%d\n"%(x-left))
    f1.write("%d\n"%left)
    
    y = random.getrandbits(BITS)
    left = random.randrange(y)
    f0.write("%d\n"%(y-left))
    f1.write("%d\n"%left)
    
    result = x ^ y
    
    f0.close()
    f1.close()

    print("Expected result: %d"%result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='generates input for ABY sample programs')
    
    #parser.add_argument('-n', default=32, type=int, 
    #    help="integer bit length")

    parser.add_argument('-l', default=10, type=int, 
        help="array length (for innerprod, xtabs)")

    programs = ["add","mult","xor","and","mult3","innerprod","xtabs"]
    parser.add_argument('-e', default="xtabs", choices = programs,
        help="program selection")

    args = parser.parse_args()

    create_dirs(args.e)

    if args.e == "mult3":
        gen_mult3_input()

    elif args.e == "innerprod":
        gen_innerprod_input(args.l)
        
    elif args.e == "add":
        gen_add_input()
        
    elif args.e == "mult":
        gen_mult_input()

    elif args.e == "and":
        gen_and_input()
        
    elif args.e == "xor":
        gen_xor_input()

    elif args.e == "xtabs":
        print "xtabs not yet implemented"

