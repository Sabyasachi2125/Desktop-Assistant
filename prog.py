"""
Desktop Assistant - A Python-based voice/text controlled system automation tool.

This program responds to user text commands to perform various system tasks
including launching applications, playing games, and providing information.

Features:
- Application management (Chrome, Notepad, Paint, Calculator)
- Camera access
- Entertainment (jokes, games)
- Web search capabilities
- Cross-platform support (Windows, macOS, Linux)

Author: IIEC RISE Community
Mentor: Mr. Vimal Daga (World Record Holder)
"""

import os
import sys
import pyttsx3
import random
import subprocess

# Command sets for different operations
run_commands = {"run", "launch", "open"}          # Commands to start applications
close_commands = {"close", "kill", "exit"}        # Commands to terminate applications
exit_program_keywords = {"terminate", 'quit', "exit"}  # Program exit commands
camera_keywords = {"camera", "selfie", "photo"}   # Camera-related keywords
linux_platforms = {"linux", 'linux2'}             # Linux platform identifiers

def main():
    """
    Main function that runs the desktop assistant loop.
    
    Continuously listens for user commands and executes corresponding actions.
    Supports voice feedback through text-to-speech.
    
    The assistant responds to commands in the format:
    - "run/open/launch [application]" to start applications
    - "close/kill/exit [application]" to terminate applications
    - Special commands for games, jokes, and system info
    
    Example commands:
    - "run chrome" -> Opens Chrome browser
    - "open notepad" -> Launches Notepad
    - "tell me a joke" -> Shares a random joke
    """
    while True:
        # Prompt user for input with voice feedback
        pyttsx3.speak("How can I help you:")
        user_input = input("How can I help you:")
        
        # Normalize input for consistent processing
        user_input = user_input.strip().lower()
        command = user_input.split(' ')[0]  # Extract first word as command
        
        # Handle application launch commands
        if command in run_commands:
            handle_run_commands(user_input)
            
        # Handle application close commands  
        elif command in close_commands:
            handle_close_commands(user_input)
            
        # Handle program exit commands
        elif command in exit_program_keywords:
            handle_exit()
            
        # Handle special commands
        else:
            handle_special_commands(user_input)

def handle_run_commands(user_input):
    """
    Process commands to launch/run applications.
    
    Args:
        user_input (str): Normalized user command string
    """
    # Chrome/Google Search handling
    if "chrome" in user_input or "browser" in user_input:
        site = input("What you want to search:")
        site = site.replace(' ', '+')  # Format for URL
        
        pyttsx3.speak('Request Initiated')
        print('Request Initiated')
        
        # Platform-specific Chrome launching
        if sys.platform in linux_platforms:
            command = "google-chrome " + f'www.google.com/search?q={site}'
        elif sys.platform == "darwin":  # macOS
            command = 'open -a "Google Chrome" ' + 'www.google.com/search?q=' + site   
        elif sys.platform == "win32":   # Windows
            command = "start chrome " + 'www.google.com/search?q=' + site  
        
        try:
            subprocess.Popen(command, stderr=subprocess.STDOUT, shell=True)
        except Exception as e:
            error_msg = "Sorry user. Check whether Google Chrome is installed or not in your system. If it installed check the requirements are satisfied..!"
            pyttsx3.speak(error_msg)
            
    # Notepad handling
    elif 'editor' in user_input or 'notepad' in user_input:
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system('start notepad')
        
    # Paint handling
    elif 'paint' in user_input or 'draw' in user_input:
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system('start mspaint')
        
    # Calculator handling with cross-platform support
    elif 'calculator' in user_input or 'calc' in user_input:
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        
        if sys.platform in linux_platforms:
            try:
                # Try GUI calculator first
                subprocess.Popen('gnome-calculator', shell=True)
            except Exception:
                # Fall back to command-line calculator
                subprocess.Popen('bc', shell=True)
        elif sys.platform == 'win32':
            subprocess.Popen('calc', shell=True)
        elif sys.platform == 'darwin':
            pyttsx3.speak('Mac users please update this.!')  # TODO: Implement macOS calculator

def handle_close_commands(user_input):
    """
    Process commands to close/terminate applications.
    
    Args:
        user_input (str): Normalized user command string
    """
    # Chrome closing
    if "chrome" in user_input or 'browser' in user_input:
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system("taskkill /f /im chrome.exe")
        
    # Notepad closing
    elif 'notepad' in user_input or 'editor' in user_input:
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system("taskkill /f /im notepad.exe")
        
    # Paint closing
    elif 'paint' in user_input or 'draw' in user_input:
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system("taskkill /f /im mspaint.exe")
        
    # Calculator closing (with error handling)
    elif 'calculator' in user_input or 'calc' in user_input:
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        try:
            os.system("taskkill /f /im calculator.exe")
        except:
            print("There is some error on your system")

def handle_exit():
    """
    Handle program termination gracefully.
    """
    goodbye_message = "Ok Bye, See You later"
    print(goodbye_message)
    pyttsx3.speak(goodbye_message)
    exit()

def handle_special_commands(user_input):
    """
    Process special commands that don't fit run/close categories.
    
    Args:
        user_input (str): Normalized user command string
    """
    # Camera access
    if (("take" in user_input) or ("launch" in user_input) or ("open" in user_input)) and (user_input in camera_keywords):
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system('start microsoft.windows.camera:')
    
    # Date information
    elif (("run" in user_input) or ("what" in user_input) or ("open" in user_input)) and ("date" in user_input):
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system('start date')
    
    # Time information
    elif (("run" in user_input) or ("what" in user_input) or ("open" in user_input)) and ("time" in user_input):
        pyttsx3.speak("Request Initiated")
        print("Request Initiated!!")
        os.system('start time')
    
    # Joke telling
    elif (("tell" in user_input) or ("say" in user_input) or ("random" in user_input)) and (("joke" in user_input) or ("fun" in user_input)):
        print("This might make you laugh")
        pyttsx3.speak("This might make you laugh")
        joke = "Write an essay on cricket the teacher told the class, Chintu finishes his work in five minutes, \
                The teacher is impressed, she asks Chintu to read his essay aloud for everyone. Chintu reads \
                'The cricket match is cancelled because of rain :D'"
        print(joke)
        pyttsx3.speak(joke)
    
    # Heads or Tails game
    elif (("play" in user_input) or ("boring" in user_input)) and (("game" in user_input) or ("coin" in user_input) or ("heads" in user_input) or ("tails" in user_input)):
        print("Lets Play Heads or Tails")
        pyttsx3.speak("Lets Play Head or Tail")
        coins = ["Heads", "Tails"]
        
        # Game loop
        while True:
            try:
                user_input = input("Heads or Tails: ").strip().lower()
                
                # Handle empty input
                if not user_input:
                    print("Please enter 'Heads' or 'Tails' (or 'H'/'T')")
                    continue
                
                # Normalize user input to accepted format
                valid_inputs = {
                    'heads': 'Heads', 'head': 'Heads', 'h': 'Heads',
                    'tails': 'Tails', 'tail': 'Tails', 't': 'Tails'
                }
                
                if user_input not in valid_inputs:
                    print(f"Invalid input '{user_input}'. Please enter 'Heads' or 'Tails' (or 'H'/'T')")
                    continue
                
                # Convert to proper format
                toss = valid_inputs[user_input]
                
                pyttsx3.speak(toss)
                computer_choice = random.choice(coins)
                
                # Compare choices and provide feedback
                if toss == computer_choice:
                    print("Bot:", computer_choice)
                    print("Aha you are good at this!")
                    pyttsx3.speak("Wow you are good at this")
                    continue
                print(computer_choice)
                print("  Haha  Not this time")
                pyttsx3.speak("Haha  Not this time")
                
            except KeyboardInterrupt:
                break
            except ValueError:
                print("[-] Error: Invalid value. Try again.")
                continue
            except Exception as e:
                print(f"[-] Error: {e}")
                break
    
    # Handle unrecognized commands
    else:
        error_message = "Sorry, couldn't get that, please try another command"
        print(error_message)
        pyttsx3.speak(error_message)

if __name__ == "__main__":
    """
    Entry point of the application.
    
    Initializes the assistant with a welcome message and starts the main loop.
    """
    print("Hello User")
    pyttsx3.speak("Hello User")
    main()
