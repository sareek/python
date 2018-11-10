#function for adding items to inventory
def addToInventory(inv, dragonLoot):
    # your code goes here
    length=len(dragonLoot)
    for k,v in inv.items():
        
        for i in range(length):
            if k==dragonLoot[i]:
               inv[k]+=1
                  
    

    for i in range(length):
        count=0
        if dragonLoot[i] not in inv:
            for j in range(length):
                if dragonLoot[j]==dragonLoot[i]:
                    count+=1
                    
          
            inv.update({dragonLoot[i]:count})
            # print('jsjsjs')
            # print(inv)
            # addToInventory(inv,dragonLoot)
    return inv
            

#function for displaying inventory items
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE 
        print(v,k)
        item_total+= int(v)

    print("Total number of items: " + str(item_total))            
               
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','ruby','dagger']
inv=addToInventory(inv, dragonLoot)

print(inv)

displayInventory(inv)