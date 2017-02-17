user_input=input("Do you want to \n |add key| |Remove Key| |Remove value| \n |Update| |Print| |Exit| ?: ").lower

dictionary={

}


def Dictionary_add():
    if user_input=="add key":
        user_key=input("Enter a new key: ")
        user_value=input("What's the value?: ")
        if user_key in dictionary:
            print("is in schedule")
        else:
            dictionary[user_key]=user_value
            print("is not in schedule, now added")
    elif user_input=="remove key":
        remove_key=input("Which key?: ")
        if remove_key in dictionary:
            del dictionary[remove_key]
            print("is removed")
        else:
            dictionary[user_key]=user_value
            print("is not in schedule")
        
        
        
# for key in dictionary:
#             if dictionary[key] == user_key:
#                 print("Exists as key!")
#                 break
#             else: 
    
    
    
    for key in dictionary:
            if dictionary[key] == user_key:
                print("Exists as key!")
                break
            else: 
                dictionary[user_key]=user_value
   
    
    
    
