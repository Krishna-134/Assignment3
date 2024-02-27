list_of_dict =[
    {'id':1, 'name':'anu'},
    {'id':2, 'name':'anju'},
    {'id':3, 'name':'manju'},
    {'id':4, 'name':'kunju'},
]
required_id=2

filtered_dict=list(filter(lambda x:x['id']==required_id,list_of_dict))
print("filtered dictionary: ",filtered_dict)







