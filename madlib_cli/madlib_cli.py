import re

print("""         ********************* Welcome to the Madlib Game *********************
********************* I hope that you enjoy our simple yet fun game *********************
                  ********************* Have fun *********************
______________________________________________________________________________________________________________
        This game have a pretty simple rules actually:
        You will be asked to input a series of words in the cli 
        these words could be a noun, a verb, an adjective & so on 
        and when you are done you will be provided with story you created
        let's see how "Mad" it can get ;-)
     """)

# This func takes a path for a file check if it's correct reads it and then return its content
def read_template(path):
     """
    This function takes a path for a file and checks if it is correct, reads it, and then returns its content.

    Args:
        path (str): A string that represents the path to the file to be read.

    Returns:
        str: A string that contains the content of the file.

    Raises:
        FileNotFoundError: If the path is incorrect and the file is not found.

    """
     if path != '/assets/output_game.txt' and path != 'assets/madlib_game_file.txt':
       raise FileNotFoundError("Error : the reading path is not correct")
     with open(path, "r") as file:
       return file.read()
   
def parse_template(template):
    """
    This function takes a template string and parses it to extract the parts that need to be replaced and the text parts that do not need to be replaced.

    Args:
        template (str): A string that represents the template to be parsed.

    Returns:
        tuple: A tuple containing two values. The first value is a string that represents the text parts that do not need to be replaced, and the second value is a tuple that contains the parts that need to be replaced.

    """
    actual_stripped = ''
    actual_parts = []
    x=template.split(' ')
    regex=r"^{[\w ]+}" # This regex is to specify the placeholders in the text file.

    # Loop over the x where x is an array that holds the dissected template string 
    for i in x:
        if re.match(regex,i) == None :
            actual_stripped += f"{i} " # Add the parts that does not match the regex in actual_stripped
        else : # Otherwise we are at two cases (last word , mid or first words)
            if i == x[-1]:
                actual_stripped += '{}.' # To add it to the stripped
                actual_parts += [i[1:-2]] # For the last word cuz it has a dot after split
            else:
                actual_parts += [i[1:-1]]  # For the other words to remove the {} and add it to the actual_parts
                actual_stripped += '{} ' # To add it to the stripped

    # Convert actual_parts from an array to a tuple then return it and return actual_stripped as a string
    actual_parts = tuple(actual_parts)
    return (actual_stripped,actual_parts)

def merge(text,template): # This func takes every index in the tuple and replace it instead of the placeholder
    """
    This function takes a text and a tuple of parts to replace and merges them to create a new text string.

    Args:
        text (str): A string that represents the text to be merged.
        template (tuple): A tuple that contains the parts to be replaced.

    Returns:
        str: A string that represents the merged text.

    """
    return text.format(*template)

# This write inside my file that founded assets/output_game.txt
def create_ofile(result ,file_to_write_on_it):
    """
    This function takes the result of the Madlib game and overwrites the file with the new story that the user wrote.

    Args:
        result (str): A string that represents the new story created by the user.
        file_to_write_on_it (str): A string that represents the path of the file to be overwritten.

    """
    with open(file_to_write_on_it, "w") as file:
        file.write(result)
        

def start_game(file_toRead,file_toWrite):
    """
    This function starts the Madlib game by calling other functions to read the template, parse it, get user input, and create a new story.

    Args:
        file_toRead (str): A string that represents the path of the file to be read.
        file_toWrite (str): A string that represents the path of the file to be overwritten with the new story.

    """
    text = read_template(file_toRead)
    stripped_text, parts_tuple = parse_template(text)
    user_input = []
    
    for i in range(len(parts_tuple)):
        x = input('enter a {} > '.format(parts_tuple[i]))
        user_input.append(x)
    result = stripped_text.format(*user_input)
    print(f"Check out your weird creation xD: \n{result}")
    create_ofile(result,file_toWrite)

if __name__=="__main__":
    start_game("assets/madlib_game_file.txt","assets/output_game.txt")