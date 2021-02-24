data = {1:'satya',2:'sai',3:'sumanth'}
print(data[3])      #
print(data.get(1))
keys= ['satya','sai','sumanth']
vals= ['aprjc','dnr','home']
dat = dict(zip(keys,vals))
print(dat)


dat['gold']= 'home'
print(dat)
del dat['gold']
print(dat)


prog={'grandpa':'manik','sis':['anu','nandhita'],'atha':{'1st':'lakshmi','2nd':'hema','3rd':'samatha'}}
print(prog['grandpa'])
print(prog['sis'])
print(prog['sis'][0])
print(prog['sis'][1])
print(prog['atha'])
print(prog['atha']['2nd'])

# help() for help ...then topics..

