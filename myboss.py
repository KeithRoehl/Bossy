import time

class NosyBoss:
    def __init__(self, name):
        self.name = name

    def check_progress(self):
        print(f"{self.name}: Hey, how's the work going?")
    
    def look_overShoulder(self):
        print(f"{self.name}: I'm just checking your screen, making sure you're on track!")

class Employee:
    def __init__(self, name):
        self.name = name
        self.work_done = 0

    def work(self):
        print(f"{self.name}: I'm working on the task...")
        self.work_done += 1
        time.sleep(2)  # Simulate time taken to work

    def update_progress(self):
        print(f"{self.name}: I've completed {self.work_done} tasks so far.")

def main():
    boss = NosyBoss("Mr. Smith")
    employee = Employee("Keith")
    
    # Simulating the workday
    for _ in range(5):
        employee.work()
        employee.update_progress()
        boss.check_progress()
        boss.look_overShoulder()  # Corrected method name here
        
    print(f"{employee.name}: Finished all tasks for the day!")

if __name__ == "__main__":
    main()
