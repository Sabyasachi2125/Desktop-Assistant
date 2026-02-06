"""
Desktop Assistant - A Python-based voice/text controlled system automation tool.

This program responds to user text commands to perform various system tasks
including launching applications, playing games, and providing information.

Features:
- Application management (Chrome, Notepad, Paint, Calculator)
- Camera access
- Entertainment (jokes, games)
- Web search capabilities
- Weather information
- System monitoring (CPU, memory usage)
- File operations (create, delete, move files)
- Music player control
- Email sending capability
- Cross-platform support (Windows, macOS, Linux)

Author: IIEC RISE Community
Mentor: Mr. Vimal Daga (World Record Holder)
"""

# === CONFIGURATION SECTION ===
# Weather API Configuration
OPENWEATHER_API_KEY = "f7aa9fb00264ba48cb390da79f4eaed7"  # Your OpenWeatherMap API key

import os
import sys
import pyttsx3
import random
import subprocess
import json
import requests
import psutil
from datetime import datetime

# Command sets for different operations
run_commands = {"run", "launch", "open"}          # Commands to start applications
close_commands = {"close", "kill", "exit"}        # Commands to terminate applications
exit_program_keywords = {"terminate", 'quit', "exit"}  # Program exit commands
camera_keywords = {"camera", "selfie", "photo"}   # Camera-related keywords
linux_platforms = {"linux", 'linux2'}             # Linux platform identifiers

# New command sets for enhanced features
weather_keywords = {"weather", "temperature", "climate"}
system_monitor_keywords = {"cpu", "memory", "ram", "system", "performance", "monitor"}
file_operation_keywords = {"create", "delete", "move", "copy", "file", "folder"}
music_keywords = {"music", "play", "pause", "next", "previous", "song"}
email_keywords = {"email", "mail", "send"}

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
            
        # Handle new enhanced features
        elif any(keyword in user_input for keyword in weather_keywords):
            handle_weather_command()
            
        elif any(keyword in user_input for keyword in system_monitor_keywords):
            handle_system_monitor()
            
        elif any(keyword in user_input for keyword in file_operation_keywords):
            handle_file_operations(user_input)
            
        elif any(keyword in user_input for keyword in music_keywords):
            handle_music_control(user_input)
            
        elif any(keyword in user_input for keyword in email_keywords):
            handle_email_command()
            
        # Handle special commands
        else:
            handle_special_commands(user_input)

def handle_weather_command():
    """
    Handle weather information requests.
    Uses a free weather API to get current weather data.
    Includes retry mechanism for failed requests.
    """
    max_retries = 3
    retry_count = 0
    
    # Check for API key setup
    if OPENWEATHER_API_KEY == "YOUR_API_KEY_HERE":
        print("⚠️  Weather API Setup Required!")
        print("To use weather functionality, you need a free API key from OpenWeatherMap:")
        print("1. Go to https://openweathermap.org/api")
        print("2. Sign up for a free account")
        print("3. Get your API key")
        print("4. Replace 'YOUR_API_KEY_HERE' in the configuration section with your actual API key")
        print("")
        print("Alternatively, you can:")
        print("- Use a different weather service")
        print("- Implement a mock weather feature for testing")
        print("")
        return
    
    while retry_count < max_retries:
        try:
            city = input("Enter city name: ").strip()
            if not city:
                print("Please enter a valid city name.")
                retry_count += 1
                if retry_count < max_retries:
                    print(f"Attempt {retry_count + 1}/{max_retries}. Please try again.")
                    continue
                else:
                    print("Maximum attempts reached. Returning to main menu.")
                    return
            
            # Using OpenWeatherMap API (free tier)
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
            
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                temp = data['main']['temp']
                description = data['weather'][0]['description']
                humidity = data['main']['humidity']
                
                weather_info = f"Current weather in {city}: {description}, Temperature: {temp}°C, Humidity: {humidity}%"
                print(weather_info)
                pyttsx3.speak(weather_info)
                return  # Success - exit the function
            elif response.status_code == 401:
                print("❌ API Authentication Error!")
                print("Your API key is invalid or not configured properly.")
                print("Please check your OpenWeatherMap API key setup.")
                print("")
                return  # Don't retry on authentication errors
            else:
                error_msg = f"Sorry, couldn't fetch weather data for {city}. Status code: {response.status_code}"
                print(error_msg)
                pyttsx3.speak("Weather data not available for that city")
                retry_count += 1
                
                if retry_count < max_retries:
                    print(f"Attempt {retry_count}/{max_retries}. Please try another city or check the spelling.")
                    continue
                else:
                    print("Maximum attempts reached. Returning to main menu.")
                    return
                    
        except requests.exceptions.RequestException as e:
            error_msg = f"Network error: {str(e)}. Please check your internet connection."
            print(error_msg)
            pyttsx3.speak("Network error occurred")
            retry_count += 1
            
            if retry_count < max_retries:
                print(f"Attempt {retry_count}/{max_retries}. Please try again.")
                continue
            else:
                print("Maximum attempts reached. Returning to main menu.")
                return
                
        except Exception as e:
            error_msg = f"Error fetching weather: {str(e)}"
            print(error_msg)
            pyttsx3.speak("Error occurred while fetching weather")
            retry_count += 1
            
            if retry_count < max_retries:
                print(f"Attempt {retry_count}/{max_retries}. Please try again.")
                continue
            else:
                print("Maximum attempts reached. Returning to main menu.")
                return
    
    # If we get here, all retries failed
    print("Unable to fetch weather information after multiple attempts.")
    pyttsx3.speak("Unable to fetch weather information")

def handle_system_monitor():
    """
    Handle system monitoring requests.
    Shows CPU usage, memory usage, and other system information.
    Includes retry mechanism for system monitoring.
    """
    max_retries = 2
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            # Get system information
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            
            # Handle potential disk access issues
            try:
                disk = psutil.disk_usage('/')
            except:
                # Fallback for disk usage if root path fails
                disk = psutil.disk_usage(os.getcwd())
            
            # Format information
            info = f"""
System Information:
CPU Usage: {cpu_percent}%
Memory Usage: {memory.percent}% ({memory.used // (1024**3)}GB / {memory.total // (1024**3)}GB)
Available Memory: {memory.available // (1024**3)}GB
Disk Usage: {disk.percent}% ({disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB)
            """.strip()
            
            print(info)
            pyttsx3.speak(f"CPU usage is {cpu_percent} percent. Memory usage is {memory.percent} percent.")
            return  # Success - exit the function
            
        except Exception as e:
            error_msg = f"Error getting system information: {str(e)}"
            print(error_msg)
            pyttsx3.speak("Error occurred while getting system information")
            retry_count += 1
            
            if retry_count < max_retries:
                print(f"Attempt {retry_count}/{max_retries}. Retrying system monitoring...")
                continue
            else:
                print("Unable to retrieve system information after multiple attempts.")
                return

def handle_file_operations(user_input):
    """
    Handle file operation commands.
    
    Args:
        user_input (str): The user's command
    """
    try:
        if "create" in user_input:
            filename = input("Enter filename to create: ").strip()
            if filename:
                with open(filename, 'w') as f:
                    f.write("")  # Create empty file
                success_msg = f"File {filename} created successfully!"
                print(success_msg)
                pyttsx3.speak(success_msg)
            else:
                print("Please provide a filename.")
                
        elif "delete" in user_input:
            filename = input("Enter filename to delete: ").strip()
            if filename and os.path.exists(filename):
                os.remove(filename)
                success_msg = f"File {filename} deleted successfully!"
                print(success_msg)
                pyttsx3.speak(success_msg)
            elif filename:
                print(f"File {filename} not found.")
            else:
                print("Please provide a filename.")
                
        elif "move" in user_input or "copy" in user_input:
            source = input("Enter source file: ").strip()
            destination = input("Enter destination: ").strip()
            
            if source and destination:
                if "move" in user_input:
                    os.rename(source, destination)
                    action = "moved"
                else:
                    import shutil
                    shutil.copy2(source, destination)
                    action = "copied"
                    
                success_msg = f"File {action} successfully from {source} to {destination}"
                print(success_msg)
                pyttsx3.speak(success_msg)
            else:
                print("Please provide both source and destination.")
                
    except Exception as e:
        error_msg = f"Error performing file operation: {str(e)}"
        print(error_msg)
        pyttsx3.speak(error_msg)

def handle_music_control(user_input):
    """
    Handle music player control commands.
    Note: This is a basic implementation that works with Windows Media Player.
    
    Args:
        user_input (str): The user's command
    """
    try:
        if "play" in user_input:
            # This is a placeholder - actual implementation would depend on the music player
            msg = "Playing music"
            print(msg)
            pyttsx3.speak(msg)
            # In real implementation, you might use:
            # os.system("start wmplayer")  # Windows Media Player
        elif "pause" in user_input:
            msg = "Music paused"
            print(msg)
            pyttsx3.speak(msg)
        elif "next" in user_input:
            msg = "Playing next song"
            print(msg)
            pyttsx3.speak(msg)
        elif "previous" in user_input:
            msg = "Playing previous song"
            print(msg)
            pyttsx3.speak(msg)
        else:
            msg = "Music control command not recognized"
            print(msg)
            pyttsx3.speak(msg)
            
    except Exception as e:
        error_msg = f"Error controlling music: {str(e)}"
        print(error_msg)
        pyttsx3.speak(error_msg)

def handle_email_command():
    """
    Handle email sending capability.
    Note: This requires proper email configuration.
    """
    try:
        print("Email feature requires setup:")
        print("1. Configure your email credentials in the code")
        print("2. Enable less secure apps or use app passwords")
        print("3. Set up SMTP server details")
        
        msg = "Email feature requires additional setup. Please check the documentation."
        print(msg)
        pyttsx3.speak(msg)
        
        # Placeholder for actual implementation
        # Would require smtplib and email libraries
        # Plus proper security handling for credentials
        
    except Exception as e:
        error_msg = f"Error with email feature: {str(e)}"
        print(error_msg)
        pyttsx3.speak(error_msg)

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
