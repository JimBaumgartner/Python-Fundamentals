to_filter=[
{
    "name" :  "Jim",
    "age":  0
},
{
    "name" :  "something",
    "age": 67
},
{
    "name" : "second guy",
    "age": 55
}
]


def filter_by_age(value):
    return value["age"]> 50

greater_than50 = filter(filter_by_age,to_filter)




def im_goona_be_a_callback(x): #this turns im gonna be a callback into (x)
    print(x)  # we are printing x here

def i_take_callbacks(cb):  # this turns i take callbacks into cb
    cb("Hello World")  #this turns cb into "hello world"


i_take_callbacks(im_goona_be_a_callback) # this turns im gonnA be comeback into i take callbacks,  then on line 
# 22 it turns in (x)  ,  then we are printing x,  

# line 29 im_goona_be_a_callback (which is (x)  from line 22  changes to i_take_callbacks
# which is (cb) from line 25

# print line on 23 will be hello world 

