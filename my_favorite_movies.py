my_favorite_movies= ['leo','pathan','jawan']
search_movie = input("enter your favorite movie")
i=0
while i<3:
    if search_movie==my_favorite_movies[i]:
        print("it is a your favorite movie named as : "+my_favorite_movies[i])
        i=i+1
        
    elif i>=3:
        print("no movie like this added in your list")
    else :
        i=i+1
    
    
    