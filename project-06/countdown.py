import time
import winsound  # For Windows alarm sound
import os
from threading import Thread

class CountdownTimer:
    def __init__(self):
        self.running = False
        self.paused = False
        self.remaining_time = 0
    
    def start_timer(self, hours, minutes, seconds):
        self.running = True
        self.paused = False
        self.remaining_time = hours * 3600 + minutes * 60 + seconds
        
        while self.remaining_time > 0 and self.running:
            if not self.paused:
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
                self.display_time(self.remaining_time)
                time.sleep(1)
                self.remaining_time -= 1
            else:
                time.sleep(0.1)  # Small sleep to reduce CPU usage when paused
        
        if self.running:  # Only play sound if timer wasn't stopped manually
            self.play_alarm()
            print("\nTime's up!")
    
    def display_time(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        mins, secs = divmod(remainder, 60)
        print(f"\nCountdown Timer (Press 'p' to pause, 's' to stop)")
        print("="*40)
        print(f"  ⏰  {hours:02d}:{mins:02d}:{secs:02d}  ⏰")
        print("="*40)
    
    def play_alarm(self):
        # Windows sound
        if os.name == 'nt':
            winsound.Beep(1000, 2000)  # frequency, duration
        else:  # Mac/Linux alternative
            print('\a')  # System beep
    
    def pause_timer(self):
        self.paused = True
    
    def resume_timer(self):
        self.paused = False
    
    def stop_timer(self):
        self.running = False

def get_time_input():
    while True:
        try:
            hours = int(input("Enter hours: ") or 0)
            minutes = int(input("Enter minutes: ") or 0)
            seconds = int(input("Enter seconds: ") or 0)
            
            if hours < 0 or minutes < 0 or seconds < 0:
                print("Please enter positive numbers!")
                continue
                
            if hours == 0 and minutes == 0 and seconds == 0:
                print("Please enter some time!")
                continue
                
            return hours, minutes, seconds
        except ValueError:
            print("Please enter valid numbers!")

def main():
    timer = CountdownTimer()
    
    print("=== COUNTDOWN TIMER ===")
    print("Set your timer duration:")
    hours, minutes, seconds = get_time_input()
    
    # Start timer in separate thread
    timer_thread = Thread(target=timer.start_timer, args=(hours, minutes, seconds))
    timer_thread.start()
    
    # Handle user input while timer runs
    while timer_thread.is_alive():
        user_input = input().lower()
        if user_input == 'p':
            if timer.paused:
                timer.resume()
                print("Timer resumed")
            else:
                timer.pause()
                print("Timer paused")
        elif user_input == 's':
            timer.stop()
            print("Timer stopped")
            break
    
    timer_thread.join()

if __name__ == "__main__":
    main()