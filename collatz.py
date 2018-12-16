def the_function(n):
    if n%2==0:
        return int(n/2)
    else:
        return (3*n)+1

def generate_sequence(n,print_seq=True):
    seq = []
    seq.append(n)
    while (n!=1):
        n=the_function(n)
        seq.append(n)
    if print_seq==True:
        print(seq)
    print("steps:",len(seq))