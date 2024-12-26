import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# process model
class FirstOrderProcess:
    def __init__(self, gain=1, time_constant=5, dt=0.1):
        self.gain = gain
        self.time_constant = time_constant
        self.dt = dt
        self.output = 0

    def step(self, input_signal):
        # First-order process dynamics
        self.output += (self.dt / self.time_constant) * (self.gain * input_signal - self.output)
        return self.output

# PID Controller
class PIDController:
    def __init__(self, kp=1, ki=0, kd=0, dt=0.1):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt
        self.integral = 0
        self.prev_error = 0

    def compute(self, setpoint, process_variable):
        error = setpoint - process_variable
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative

# Tkinter GUI Application
class ProcessControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Process Control Teaching Tool")

        # process and controller initialization
        self.process = FirstOrderProcess()
        self.controller = PIDController()
        self.setpoint = 1.0
        self.time = 0
        self.running = False  # Flag controls simulation loop
        self.paused = False  #  pausing flag

        # Data for plotting
        self.time_data = [0]
        self.process_data = [0]
        self.setpoint_data = [self.setpoint]

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Control Panel
        control_frame = ttk.LabelFrame(self.root, text="Control Parameters")
        control_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(control_frame, text="Kp").grid(row=0, column=0)
        self.kp_entry = ttk.Entry(control_frame, width=10)
        self.kp_entry.insert(0, "1.0")
        self.kp_entry.grid(row=0, column=1)

        ttk.Label(control_frame, text="Ki").grid(row=1, column=0)
        self.ki_entry = ttk.Entry(control_frame, width=10)
        self.ki_entry.insert(0, "0.0")
        self.ki_entry.grid(row=1, column=1)

        ttk.Label(control_frame, text="Kd").grid(row=2, column=0)
        self.kd_entry = ttk.Entry(control_frame, width=10)
        self.kd_entry.insert(0, "0.0")
        self.kd_entry.grid(row=2, column=1)

        ttk.Label(control_frame, text="Setpoint").grid(row=3, column=0)
        self.setpoint_entry = ttk.Entry(control_frame, width=10)
        self.setpoint_entry.insert(0, "1.0")
        self.setpoint_entry.grid(row=3, column=1)

        self.start_button = ttk.Button(control_frame, text="Start Simulation", command=self.start_simulation)
        self.start_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.stop_button = ttk.Button(control_frame, text="Stop Simulation", command=self.stop_simulation)
        self.stop_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.pause_button = ttk.Button(control_frame, text="Pause Simulation", command=self.pause_simulation)
        self.pause_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.reset_button = ttk.Button(control_frame, text="Reset Simulation", command=self.reset_simulation)
        self.reset_button.grid(row=7, column=0, columnspan=2, pady=5)

        # Plot Frame
        # Plot Frame
        plot_frame = ttk.LabelFrame(self.root, text="Process Response")
        plot_frame.grid(row=0, column=1, padx=10, pady=10)

        self.figure, self.ax = plt.subplots(figsize=(15, 10))
        self.ax.set_title("Process Response")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Process Variable")
        self.ax.set_xlim(0, 50)  # Fix x-axis range, adjust as needed
        self.ax.set_ylim(0, 2)   # Fix y-axis range, adjust as needed
        self.line_process, = self.ax.plot(self.time_data, self.process_data, label="Process Variable")
        self.line_setpoint, = self.ax.plot(self.time_data, self.setpoint_data, label="Setpoint", linestyle="--")
        self.ax.legend()

        self.canvas = FigureCanvasTkAgg(self.figure, plot_frame)
        self.canvas.get_tk_widget().pack()


    def start_simulation(self):
        if not self.running: 
            self.running = True
            self.paused = False
            self.update_controller_parameters()
            self.update_simulation()

    def stop_simulation(self):
        self.running = False

    def pause_simulation(self):
        self.paused = not self.paused
        self.pause_button.config(text="Resume Simulation" if self.paused else "Pause Simulation")

    def reset_simulation(self):
        self.stop_simulation()
        self.time_data = [0]
        self.process_data = [0]
        self.setpoint_data = [self.setpoint]
        self.time = 0
        self.process.output = 0
        self.ax.clear()
        self.ax.set_title("Process Response")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Process Variable")
        self.ax.set_xlim(0, 50)  
        self.ax.set_ylim(0, 2)  
        self.line_process, = self.ax.plot(self.time_data, self.process_data, label="Process Variable")
        self.line_setpoint, = self.ax.plot(self.time_data, self.setpoint_data, label="Setpoint", linestyle="--")
        self.ax.legend()
        self.canvas.draw()


    def update_controller_parameters(self):
        self.controller.kp = float(self.kp_entry.get())
        self.controller.ki = float(self.ki_entry.get())
        self.controller.kd = float(self.kd_entry.get())
        self.setpoint = float(self.setpoint_entry.get())

    def update_simulation(self):
        if self.running and not self.paused:
            dt = self.process.dt

            #  control action compuation
            control_signal = self.controller.compute(self.setpoint, self.process.output)

            # Step the process
            process_variable = self.process.step(control_signal)

            # time update
            self.time += dt

            # data update for plotting
            self.time_data.append(self.time)
            self.process_data.append(process_variable)
            self.setpoint_data.append(self.setpoint)

            # plot update
            self.line_process.set_data(self.time_data, self.process_data)
            self.line_setpoint.set_data(self.time_data, self.setpoint_data)
            self.ax.relim()
            self.ax.autoscale_view()
            self.canvas.draw()

        if self.running:
            self.root.after(int(self.process.dt * 1000), self.update_simulation)


if __name__ == "__main__":
    root = tk.Tk()
    app = ProcessControlApp(root)
    root.mainloop()