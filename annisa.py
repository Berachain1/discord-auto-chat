import os
import asyncio
import discord
from colorama import init, Fore, Style
import time
from datetime import datetime
import pytz  # Untuk menangani zona waktu
import random  # Untuk pemilihan pesan random

import subprocess

try:
    subprocess.run(["python3", "../PROJECT/tampilan.py"], check=True)
except subprocess.CalledProcessError as e:
    print("Gagal menampilkan tampilan awal:", e)


init(autoreset=True)

red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
black = Fore.LIGHTBLACK_EX
white = Fore.LIGHTWHITE_EX
reset = Style.RESET_ALL
magenta = Fore.LIGHTMAGENTA_EX

def get_timestamp():
    # Menggunakan zona waktu Asia/Jakarta (WIB)
    wib = pytz.timezone('Asia/Jakarta')
    now = datetime.now(wib)
    return f"{blue}[{now.strftime('%H:%M:%S')}]{reset}"

def log_info(message):
    print(f"{get_timestamp()} {white}INFO{reset}    | {message}")

def log_success(message):
    print(f"{get_timestamp()} {green}SUCCESS{reset} | {message}")

def log_warning(message):
    print(f"{get_timestamp()} {yellow}WARNING{reset} | {message}")

def log_error(message):
    print(f"{get_timestamp()} {red}ERROR{reset}   | {message}")

# Banner
def print_banner():
    print(f"\n{green}{'★' * 40}{reset}")
    print(f"{white}      Discord Auto level-up      {reset}")
    print(f"{yellow}         by: Annisaazzahra          {reset}")
    print(f"{green}{'★' * 40}{reset}\n")

print_banner()

def load_tokens():
    tokens = []
    try:
        with open('token.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() and not line.startswith('#'):
                    tokens.append(line.strip())
            if tokens:
                log_success(f"Berhasil memuat {len(tokens)} token dari token.txt")
            return tokens
    except FileNotFoundError:
        log_error("File token.txt tidak ditemukan!")
        log_info("Buat file token.txt dengan format:")
        print(f"{yellow}TOKEN1{reset}")
        print(f"{yellow}TOKEN2{reset}")
        print(f"{yellow}TOKEN3{reset}")
        exit(1)

class AccountConfig:
    def __init__(self, token, channel_id, message_count, message_delay, delete_mode=True):
        self.token = token
        self.channel_id = channel_id
        self.message_count = message_count
        self.message_delay = message_delay
        self.delete_mode = delete_mode

mainMessages = [
    'Did anyone see the latest episode?',
    'What everyone up to today?',
    'Cant believe its already this late!',
    'Just finished my tasks, finally!',
    'This weather is something else...',
    'Anyone working on something interesting?',
    'Good morning, everyone!',
    'Time for a quick break, anyone else?',
    'Back to the grind.',
    'Anyone have any tips for leveling up faster?',
    'Just got back, what did I miss?',
    'Feeling motivated today!',
    'Lol, thats hilarious!',
    'Totally agree with you.',
    'Thinking about getting some coffee, brb.',
    'Anyone here into coding?',
    'Oh wow, didnt expect that!',
    'Taking things one step at a time.',
    'Almost there!',
    'Hey everyone, how’s it going?',
    'Just dropping by to say hi!',
    'Leveling up little by little!',
    'What’s everyone up to today?',
    'This server is pretty cool!',
    'Taking a short break from studying.',
    'Back again to hang out!',
    'Let’s get this conversation going!',
    'Who else loves memes?',
    'I could use a snack right now.',
    'Let’s make today productive!',
    'Any music recommendations?',
    'Hydration check! Drink some water.',
    'Let’s keep this chat moving!',
    'Haha, that’s a good one!',
    'Guess who’s back?',
    'Almost at the next level!',
    'Let’s gooo, keep the chat alive!',
    'Sharing good vibes only.',
    'What game are you into lately?',
    'Trying to stay active here!',
    'Drop your favorite emoji!',
    'Any tips for staying focused?',
    'Feeling lazy but still here 😅',
    'Good morning, afternoon, or night!',
    'Just vibing with the chat.',
    'Let’s keep leveling together!',
    'Anyone else grinding levels?',
    'Trying to multitask right now.',
    'Today feels like a chill day.',
    'What motivates you lately?',
    'Still here, still typing!',
    'Time flies in this server!',
    'Need a break, so I’m chatting.',
    'Checking in with some good energy!',
    'Typing just to not be idle 😄',
    'This place feels like home.',
    'Enjoying the conversation!',
    'Any good shows to binge?',
    'Just passing by, don’t mind me!',
    'Chat keeps me awake 😂',
    'Late night grinding, who’s with me?',
    'Anyone else procrastinating?',
    'You’ve got this, no matter what!',
    'Keep pushing forward, one step at a time.',
    'Progress is progress, no matter how small.',
    'Let’s crush our goals today!',
    'Every day is a new chance to grow.',
    'Stay focused and stay strong.',
    'We’re all in this together!',
    'Believe in yourself – always.',
    'Success starts with the right mindset.',
    'Let’s bring our best energy today!',
    'No limits, just possibilities.',
    'Your effort matters more than perfection.',
    'The grind never stops!',
    'Let’s make today count.',
    'Small wins lead to big victories.',
    'Positivity is powerful.',
    'Let’s keep moving forward!',
    'Stay calm and keep going.',
    'Choose kindness, always.',
    'You’re stronger than you think.',
    'Hard work always pays off.',
    'Keep showing up – it matters.',
    'Chasing goals with purpose!',
    'Even tough days build strength.',
    'Let’s turn challenges into opportunities.',
    'Confidence starts with action.',
    'Keep your head up!',
    'Motivation is contagious – spread it!',
    'One step at a time – you’re doing great.',
    'Take a deep breath, then conquer.',
    'You’re capable of amazing things.',
    'Let’s rise and shine, friends!',
    'We’re here to grow and glow.',
    'Today feels like a win already!',
    'Let’s be the reason someone smiles today.',
    'Keep chasing those dreams!',
    'You’re doing amazing – seriously!',
    'Let’s light up this space with good vibes.',
    'Don’t forget to hydrate and hustle!',
    'Strength comes from consistency.',
    'Let’s cheer each other on!',
    'Even small steps move you forward.',
    'The best time to start is now!',
    'Keep calm and keep trying.',
    'Let’s make the impossible possible.',
    'Failure is part of the path to success.',
    'Just showing up is already a win!',
    'You’re exactly where you need to be.',
    'Let your light shine today!',
    'Let’s make it happen – together!',
    'Dream big, work smart!',
    'We’ve got this, team!',
    'Don’t stop until you’re proud.',
    'Your goals are worth the effort.',
    'One day at a time, we grow.',
    'Stay true, stay kind, stay you.',
    'You make this space better!',
    'Push your limits – gently but firmly.',
    'Good things take time – keep going.',
    'You’re doing your best – and that’s enough.',
    'Let’s spark some joy today!',
    'Keep your focus fierce.',
    'Progress is better than perfection.',
    'Your mindset shapes your success.',
    'Every effort brings you closer.',
    'Celebrate even the small wins.',
    'You’re not behind – you’re on your path.',
    'Let’s bring our A-game today!',
    'Smash your goals, one task at a time!',
    'Let’s create something great.',
    'Every sunrise brings new energy.',
    'Courage looks good on you.',
    'Your work matters.',
    'Let’s keep the spirit high!',
    'Shout out to everyone showing up today!',
    'Turn doubts into fuel.',
    'Let your purpose lead the way.',
    'Joy is part of the journey.',
    'Hustle with heart.',
    'Show up for yourself today!',
    'Growth happens outside the comfort zone.',
    'Let’s lift each other up!',
    'Today’s effort builds tomorrow’s success.',
    'Your energy sets the tone.',
    'Let’s keep the momentum going!',
    'One task at a time – let’s go!',
    'Every moment is a fresh start.',
    'Determination always beats doubt.',
    'Keep the faith in yourself.',
    'Proud of how far you’ve come!',
    'Keep being awesome!',
    'Let’s make progress together!',
    'Take pride in every effort.',
    'You are not alone in this!',
    'Let your passion drive you.',
    'Let’s keep the good vibes rolling!',
    'We rise by lifting others.',
    'The journey is just as important as the goal.',
    'Smile, you’re doing better than you think.',
    'I like the vibe here.',
    'Let’s keep supporting each other!',
    'Midnight thoughts be like...',
    'Weekend’s almost here!',
    'Staying consistent is hard lol.',
    'Daily dose of random thoughts!',
    'Can’t stop chatting, help 😂',
    'Lets keep pushing forward!',
    'Just chilling here for a bit.',
    'Anyone have any weekend plans?',
    'Anyone tried that new game yet?',
    'Haha, I know right?',
    'Feels like time is flying by.',
    'Well, thats a surprise!',
    'Just here to chat and relax.',
    'Anyone else feeling productive today?',
    'Im here to keep you all company!',
    'Hope everyones doing well!',
    'Taking a quick break, needed it.',
    'Lets keep this chat alive!',
    'Anyone else here love a good challenge?',
    'Feels good to be part of this community.',
    'Enjoying the vibe here!',
    'Thinking of learning something new.',
    'Random question: Cats or dogs?',
    'Its always nice to chat with you all.',
    'That sounds awesome!',
    'Haha, love the energy here!',
    'Alright, time to focus!',
    'Whats everyone watching these days?',
    'Just a casual hello!',
    'Oops, wrong chat haha.',
    'Wondering if anyone has advice on leveling?',
    'Anyone working late tonight?',
    'Hey, Im back!',
    'Hope I didnt miss too much.',
    'Alright, lets do this!',
    'Trying to stay motivated!',
    'Hows everyone feeling today?',
    'Good vibes only!',
    'Just saw something really cool!'
]

class Main(discord.Client):
    def __init__(self, config):
        super().__init__()
        self.config = config
        
    async def on_ready(self):
        log_success(f"Logged in as {self.user}")
        log_info(f"Mencoba membuka channel...")
        
        channel = self.get_channel(self.config.channel_id)
        
        if not channel:
            log_error(f"Channel tidak ditemukan!")
            await self.close()
            return
            
        log_success(f"Berhasil terhubung ke channel #{channel.name}")
        sent_count = 0

        while sent_count < self.config.message_count:
            # Memilih pesan secara random
            msg = random.choice(mainMessages)
            try:
                sent_message = await channel.send(msg)
                log_success(f"[{self.user}] Pesan {sent_count+1}/{self.config.message_count} terkirim")
                
                if self.config.delete_mode:
                    try:
                        await sent_message.delete()
                        log_info(f"[{self.user}] Pesan {sent_count+1} dihapus")
                    except discord.errors.Forbidden:
                        log_warning(f"[{self.user}] Tidak bisa menghapus pesan (tidak ada izin)")
                    except discord.errors.NotFound:
                        log_warning(f"[{self.user}] Pesan sudah dihapus")
                
                sent_count += 1
                
            except discord.errors.Forbidden as e:
                if "Cannot send messages in a voice channel" in str(e):
                    log_error(f"[{self.user}] Tidak bisa mengirim pesan di voice channel!")
                    await self.close()
                    return
                elif "slowmode" in str(e).lower():
                    log_warning(f"[{self.user}] Channel dalam mode slowmode. Menunggu...")
                    await asyncio.sleep(10)
                    continue
                elif "timeout" in str(e).lower():
                    log_error(f"[{self.user}] Akun sedang dalam timeout!")
                    await self.close()
                    return
                else:
                    log_error(f"[{self.user}] Tidak bisa mengirim pesan! ({str(e)})")
                    await self.close()
                    return
                    
            except discord.errors.HTTPException as e:
                if e.code == 429:  # Rate limit
                    retry_after = e.retry_after
                    log_warning(f"[{self.user}] Rate limit terdeteksi. Menunggu {retry_after} detik...")
                    await asyncio.sleep(retry_after)
                    continue
                else:
                    log_error(f"[{self.user}] Error HTTP: {str(e)}")
                    continue
                    
            except Exception as e:
                log_error(f"[{self.user}] Error tidak dikenal: {str(e)}")
                continue
                
            await asyncio.sleep(self.config.message_delay)

        log_success(f"[{self.user}] Berhasil mengirim {self.config.message_count} pesan")
        await self.close()

def main():
    log_info("Memuat token dari token.txt...")
    tokens = load_tokens()
    
    if not tokens:
        log_error("Tidak ada token yang berhasil dimuat!")
        return

    print(f"\n{white}Pilih Mode Leveling:{reset}")
    print(f"{blue}1. {white}Leveling with Delete Message enable{reset}")
    print(f"{blue}2. {white}Leveling without Delete Message{reset}")
    
    while True:
        try:
            mode = int(input(f"\n{magenta}Pilih mode [1/2]: {reset}"))
            if mode in [1, 2]:
                break
            print(f"{red}Pilihan tidak valid! Pilih 1 atau 2.{reset}")
        except ValueError:
            print(f"{red}Input tidak valid! Masukkan angka 1 atau 2.{reset}")
    
    delete_mode = mode == 1
    
    channel_id = int(input(f"{magenta}Masukkan Channel ID: {reset}"))
    message_count = int(input(f"{magenta}Berapa banyak pesan yang akan dikirim: {reset}"))
    message_delay = int(input(f"{magenta}Delay antara setiap pesan (dalam detik): {reset}"))
    
    accounts = []
    for token in tokens:
        accounts.append(AccountConfig(token, channel_id, message_count, message_delay, delete_mode))
    
    # Menjalankan akun satu per satu
    for i, config in enumerate(accounts, 1):
        log_info(f"Menjalankan akun {i} dari {len(accounts)}...")
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            client = Main(config)
            client.run(config.token, bot=False)
        except discord.LoginFailure:
            log_error(f"Token tidak valid atau expired!")
        except discord.PrivilegedIntentsRequired:
            log_error(f"Intents tidak diizinkan!")
        except Exception as e:
            log_error(f"Error: {str(e)}")
        finally:
            try:
                loop.close()
            except:
                pass
            
        if i < len(accounts):
            log_info(f"Menunggu 5 detik sebelum menjalankan akun berikutnya...")
            time.sleep(5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log_warning("Program dihentikan oleh user")
    except Exception as e:
        log_error(f"Terjadi error: {e}")
