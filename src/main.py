def arrange_scores():
    # Open file in r+ mode and read all lines
    with open("testfile.txt", "r+") as Score_Manager:
        lines = Score_Manager.readlines()
        # Extract scores
        lined = lines[3:]
        # Extract header
        header = lines[:3]
        # Sort scores, filtering out malformed lines
        lined = [line for line in lined if '|' in line]  # Filter out lines without '|'
        lined.sort(key=lambda line: int(line.split('|')[1].strip()), reverse=True)

    # Open file in w mode and rewrite the sorted scores
    with open("testfile.txt", "w") as Score_Manager:
        # Write header
        Score_Manager.writelines(header)
        # Write sorted scores
        Score_Manager.writelines(lined)

# Function to add player names and scores based on conditions
def score(new_name, new_score):
    # Open file in a+ mode
    with open("testfile.txt", "a+") as Score_Manager:
        # Check if 'new_score' is less than 0; if not, proceed to the 'else' statement.
        if new_score < 0:
            print("Score starts from 0")
            return
        else:
            # Open file using 'a+' mode and read its contents
            with open("testfile.txt", "a+") as Score_Manager:
                Score_Manager.seek(0)
                contents = Score_Manager.read()

                # Display a message (header) if the file does not contain any contents
                if not contents:
                    Score_Manager.write("High scores manager\n".center(75))
                    Score_Manager.write("\n player" + "|".center(24) + "Top scores\n".center(10))

                # Separate file contents into lines by newline (\n), removing spaces, and store as lines
                lines = [line.strip() for line in contents.split('\n')]

                # Loop to check every line; split the line by |
                for line in lines:
                  parts = line.split('|')

                  # Assigned variable containing the name of the player only
                  name = parts[0].strip()

                  # Remove extra spaces only from the beginning of new_name for comparison

                  new_name_stripped = new_name.lstrip()

                  # Check if the stripped names are equal
                  if new_name_stripped == name:
                      print("The name exists")
                      return


                # Write new_name and new_score to the file
                Score_Manager.write(f"{new_name:<17} | {new_score:^30}\n")
                return

# Display messages and options to the user
print("Hello our user to high score manager")
print("Please choose your preferred option\n")
# Create and terminate a file to establish its existence
with open("testfile.txt", "a+") as Score_Manager:
   Score_Manager.close()
  
# infinite Loop with different options
while True:
    # Display options for user input
    option = input("\n(add scores |1| || search  |2|  update |3| || exit |4|) : ")

    # Check if the user chooses option 1
    if option == "1":
        # Request the user to input their name and score
        name = input("\nEnter your name: ")
        user_score = input("Enter your score: ")
        try:
            # Try if name input or user_score input empty, display a message 
            if name == "" or user_score == "":
                print("Empty inputs are invalid")
            # Else call score function and arrange_scores function
            else:
                score(name, int(user_score))
                arrange_scores()
        # Except if user_score is not an integer, display a message
        except ValueError:
            print("Score with numbers only")
# return to the top of the loop

    # Check elif the user chooses option 2
    elif option == "2":
        # Display message then request the user to input search_name
        print("\nSearching for scores.....\n")
        search_name = input("Enter the player's name without unnecessary spaces : ")
        # Assigned found variable to false
        found = False
        # Open file in r+ mode 
        with open("testfile.txt", "r+") as Score_Manager:
            # Loop to check every line; split the line by |
            for line in Score_Manager:
                parts = line.split('|')
                # Check if search_name equals parts[0].strip() 
                if search_name == parts[0].strip():
                    # Display the line related and set found to true
                    print(line) 
                    found = True
        # Executed if the previous condition fails or if the search_name input is empty, displaying a message.
        if not found or search_name == "":
            print("No matching names found\n")
# return to the top of the loop

    # Check elif the user chooses option 3
    elif option == "3":
        # Display message then request the user to input update_name and input new_score1
        print("\nUpdating scores......")             
        update_name = input("\nInput player name for score update without extra spaces : ")
        new_score1 = input("Enter the new score: ")
        # check if update_name input or new_score1 input empty, display a message
        if new_score1 == "" or update_name == "":
            print("Empty inputs are invalid") 
        # check elif new_score1 is alphabet or not positive numbers ,display a message 
        elif new_score1.isalpha() or not new_score1.isnumeric():
            print("Score with postive numbers only")
          # excute when previous statments fail
        else:
            # score_exists1" is set to False, while scores and updated lines assigned as lists
            scored = []
            updated_lines = []  
            score_exists1 = False
            # Open file in r+ mode and read all lines
            with open("testfile.txt", "r") as Score_Manager:
                lines = Score_Manager.readlines()
            # Loop to check every line; split the line by |
            for line in lines:
                parts = line.split('|')
                #  Check if update_name equals parts[0].strip() 
                if parts[0].strip() == update_name:
                  #  Set score_exists1 to True and replace parts[1].strip() with new_score1
                    score_exists1 = True
                    updated_line = line.replace(f" {parts[1].strip()} ", f" {new_score1} ")
                    # Append updated_line to updated_lines and display messgae
                    updated_lines.append(updated_line)
                    print("Score successfully updated")
                  # excute when previous statments fail
                else:
                   # appened the empty list scored to line
                    scored.append(line)
            # If "score_exists1" is still false, display the message 
            if not score_exists1:
                print("Name not found")
            # else Open file in "w" mode, add updated lines with scored to replace old scores  
            else:
              with open("testfile.txt", "w") as Score_Manager:
                  Score_Manager.writelines(scored + updated_lines)
              # call the function to sort scores in descending order
              arrange_scores()  
# return to the top of the loop

    # Check elif the user chooses option 4
    elif option == "4":
        #display message then exit from program 
        print("\nThank you for using the high score manager ")
        print("\nNote, the file saved any changes")
        exit()
    # Execute when beyond the range of available options
    else:
        # display message then return to the top of the loop
        print("\nChoose from available options. Try again")

