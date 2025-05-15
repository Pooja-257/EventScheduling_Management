import tkinter as tk
from tkinter import messagebox

class Event:
    def __init__(self, event_id, title, duration, priority):
        self.event_id = event_id
        self.title = title
        self.duration = duration
        self.priority = priority

class EventManagementSystem:
    def __init__(self):
        self.events = []
        self.next_id = 1


    def add_event(self, title, duration, priority):
        event = Event(self.next_id, title, duration, priority)
        self.events.append(event)
        self.next_id += 1

    def get_events(self):
        return self.events

    def clear_events(self):
        self.events = []
        self.next_id = 1

class SchedulingAlgorithms:
    @staticmethod
    def fcfs(events):
        return sorted(events, key=lambda x: x.event_id)

    @staticmethod
    def sjn(events):
        return sorted(events, key=lambda x: x.duration)

    @staticmethod
    def priority_scheduling(events):
        return sorted(events, key=lambda x: x.priority, reverse=True)

class EventManagementGUI:
    def __init__(self, root):
        self.ems = EventManagementSystem()
        self.root = root
        self.root.title("Event Management System")

        # Add Event Frame
        self.add_event_frame = tk.Frame(root, padx=10, pady=10)
        self.add_event_frame.pack(pady=10)

        tk.Label(self.add_event_frame, text="Event Title:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.title_entry = tk.Entry(self.add_event_frame, width=30)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.add_event_frame, text="Duration (hours):").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.duration_entry = tk.Entry(self.add_event_frame, width=30)
        self.duration_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.add_event_frame, text="Priority:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.priority_entry = tk.Entry(self.add_event_frame, width=30)
        self.priority_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.add_event_frame, text="Add Event", command=self.add_event, width=15).grid(row=3, columnspan=2, pady=10)

        # View Events Button
        tk.Button(root, text="View Events", command=self.view_events, width=20).pack(pady=5)

        # Schedule Events Frame
        self.schedule_frame = tk.Frame(root, padx=10, pady=10)
        self.schedule_frame.pack(pady=10)

        tk.Label(self.schedule_frame, text="Schedule using:").pack(pady=5)
        tk.Button(self.schedule_frame, text="FCFS", command=self.schedule_fcfs, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(self.schedule_frame, text="SJN", command=self.schedule_sjn, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(self.schedule_frame, text="Priority", command=self.schedule_priority, width=15).pack(side=tk.LEFT, padx=5)

        # Clear Events Button
        tk.Button(root, text="Clear Events", command=self.clear_events, width=20).pack(pady=5)

    def add_event(self):
        title = self.title_entry.get()
        try:
            duration = int(self.duration_entry.get())
            priority = int(self.priority_entry.get())
            self.ems.add_event(title, duration, priority)
            messagebox.showinfo("Success", "Event added successfully!")
            # Clear the input fields
            self.title_entry.delete(0, tk.END)
            self.duration_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for duration and priority.")

    def view_events(self):
        events = self.ems.get_events()
        events_str = "\n".join([f"ID: {event.event_id}, Title: {event.title}, Duration: {event.duration}, Priority: {event.priority}" for event in events])
        messagebox.showinfo("Events", events_str if events_str else "No events available.")

    def schedule_fcfs(self):
        self.show_scheduled_events(SchedulingAlgorithms.fcfs(self.ems.get_events()))

    def schedule_sjn(self):
        self.show_scheduled_events(SchedulingAlgorithms.sjn(self.ems.get_events()))

    def schedule_priority(self):
        self.show_scheduled_events(SchedulingAlgorithms.priority_scheduling(self.ems.get_events()))

    def show_scheduled_events(self, events):
        events_str = "\n".join([f"ID: {event.event_id}, Title: {event.title}, Duration: {event.duration}, Priority: {event.priority}" for event in events])
        messagebox.showinfo("Scheduled Events", events_str if events_str else "No events to schedule.")

    def clear_events(self):
        self.ems.clear_events()
        messagebox.showinfo("Success", "All events cleared.")

if __name__== "__main__":
    root = tk.Tk()
    app = EventManagementGUI(root)
    root.mainloop()
