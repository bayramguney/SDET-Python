# Kwargs allow us to pass variable number of keyword like funcname(name='tim',team='school')

def my_three(a,b,c):
    print(a,b,c)
kwargs = {'a':'tim','b':'school','c':'usa'}
my_three(**kwargs)    # tim school usa

# exp2
def my_func(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
my_func(name='tom',spot='football',roll=10)  # name tom  spot football  roll 10
