# 1. Create a tuple called fav_apps containing the names of your 5 most-used mobile apps and print the tuple.
fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')
print("Task 1:", fav_apps)

# 2. Access and print the 2nd and 4th app names from your fav_apps tuple using indexing.
# Remember, indexing starts at 0, so the 2nd app is index 1 and the 4th is index 3.
print("\nTask 2:")
print("2nd app:", fav_apps[1])
print("4th app:", fav_apps[3])

# 3. Try to change the first element of your fav_apps tuple to 'YouTube' and observe the error message. 
# Write a comment explaining why this happens based on tuple immutability.


# fav_apps[0] = 'YouTube' 


# 4. Use tuple slicing to print the middle three app names from your fav_apps tuple.
# Hint: Use tuple[start:end] syntax to select a range of elements.
# The middle three elements are at indices 1, 2, and 3. The end index is exclusive, so we use 4.
middle_apps = fav_apps[1:4]
print("\nTask 4 (Middle three apps):", middle_apps)

# 5. Create another tuple called new_apps with two more app names you want to try. 
# Concatenate fav_apps and new_apps into a single tuple called all_apps and print the result.
new_apps = ('YouTube', 'Notion')
all_apps = fav_apps + new_apps
print("\nTask 5 (All apps concatenated):", all_apps)

