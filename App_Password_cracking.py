import hashlib
import time
from colorama import init, Fore, Back

# Initialize colorama
init(autoreset=True)

def crack_hash_from_list(password_hash, password_file, time_limit=300):
    start_time = time.time()
    try:
        with open(password_file, 'r') as file:
            for line in file:
                if time.time() - start_time > time_limit:
                    print(Fore.RED + "Waqtiga baarista wuu dhammaaday (5 daqiiqo)!")
                    return None
                password = line.strip()
                if hashlib.sha256(password.encode()).hexdigest() == password_hash:
                    return password
    except FileNotFoundError:
        print(Fore.RED + f"Faylka {password_file} laguma helin!")
    return None

def print_ascii_art():
    print(Fore.BLUE + """
#######################################
               ******                
            ************             
          ****************           
        ********************         
      **********************         
    ***************************      
   **********         **********     
  ********              ********     
 ********                ********    
********                  ********   
********                  ********   
 ********                ********    
  ********              ********     
   **********         **********     
    ***************************      
      **********************         
        ********************         
          ****************           
            ************             
               ******                
#######################################
               SOMALIA               
#######################################
    CODED BY BLACK1446
#######################################
    """)

def main():
    print_ascii_art()
    print(Fore.YELLOW + "Xulo adeegga aad rabto:")
    print("1. TikTok")
    print("2. Facebook")
    print("3. YouTube")
    print("4. Instagram")
    print("5. PUBG")
    
    option = input("Dooro adeegga (1-5): ")
    
    if option in ['1', '2', '3', '4', '5']:
        username = input(Fore.YELLOW + "Gali username-ka: ")
        password_hash = input(Fore.YELLOW + "Gali SHA256 hash-ka password-ka: ")

        # Crack password using a wordlist with a 5-minute limit
        password_file = "passwords.txt"  # Update this file with your password list
        print(Fore.YELLOW + f"Waxaan baarayaa hash-ka {password_hash}...")
        cracked_password = crack_hash_from_list(password_hash, password_file, time_limit=300)

        if cracked_password:
            print(Fore.GREEN + f"Password-ka {username} waa: {cracked_password}")
        else:
            print(Fore.RED + "Password lama helin liiska 'passwords.txt' ama waqtiga wuu dhammaaday!")
    else:
        print(Fore.YELLOW + "Doorasho aan sax ahayn!")

if __name__ == "__main__":
    main()password_hash = input(Fore.YELLOW + "Gali SHA256 hash-ka password-ka: ")def main():
    print_ascii_art()
    print(Fore.YELLOW + "Xulo adeegga aad rabto:")
    print("1. TikTok")
    print("2. Facebook")
    print("3. YouTube")
    print("4. Instagram")
    print("5. PUBG")
    
    option = input("Dooro adeegga (1-5): ")
    
    if option in ['1', '2', '3', '4', '5']:
        username = input(Fore.YELLOW + "Gali username-ka: ")
        password_hash = input(Fore.YELLOW + "Gali SHA256 hash-ka password-ka: ")  # Ensure hash is input here

        # Crack password using a wordlist with a 5-minute limit
        password_file = "passwords.txt"  # Update this file with your password list
        print(Fore.YELLOW + f"Waxaan baarayaa hash-ka {password_hash}...")
        cracked_password = crack_hash_from_list(password_hash, password_file, time_limit=300)

        if cracked_password:
            print(Fore.GREEN + f"Password-ka {username} waa: {cracked_password}")
        else:
            print(Fore.RED + "Password lama helin liiska 'passwords.txt' ama waqtiga wuu dhammaaday!")
    else:
        print(Fore.YELLOW + "Doorasho aan sax ahayn!")
