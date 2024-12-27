# Process Control Teaching Tool

## Overview

This project is a Python-based graphical application designed to simulate and visualize process control dynamics. It incorporates a first-order process model and a PID controller, allowing users to experiment with control parameters and observe the system's response in real-time. The application serves as a teaching aid for students and professionals learning about process control concepts.

## Features

- **First-Order Process Model:** Simulates a process with adjustable gain, time constant, and step size.
- **PID Controller:** Configurable Proportional (Kp), Integral (Ki), and Derivative (Kd) gains.
- **Real-Time Visualization:** Graphically displays the process variable and setpoint over time.
- **Interactive Controls:**
  - Start, stop, pause, and reset the simulation.
  - Adjust controller parameters dynamically.
- **Responsive GUI:** Built with Tkinter for ease of use and portability.

## Requirements

- Python 3.7+
- The following Python libraries:
  - `tkinter` (included with Python standard library)
  - `matplotlib`
  - `numpy`

Install required libraries using:

```bash
pip install matplotlib numpy
```

## How to Run

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the main script:

   ```bash
   python process_control_app.py
   ```

4. The application window will open. Adjust the control parameters and observe the simulation.

## Project Structure

- `process_control_app.py`: Main application file containing the process model, PID controller, and GUI implementation.

## Usage

1. Launch the application.
2. Adjust the **Kp**, **Ki**, **Kd**, and **Setpoint** values in the control panel.
3. Click **Start Simulation** to observe the process response.
4. Use **Pause Simulation**, **Stop Simulation**, or **Reset Simulation** as needed.
5. Observe the real-time graph updating with the process variable and setpoint.

## Example

- **Initial Setup:**
  - Kp: 1.0
  - Ki: 0.0
  - Kd: 0.0
  - Setpoint: 1.0
- **Adjust Parameters:** Increase Ki to observe the effect of integral action.

## Future Enhancements

- Add support for higher-order processes.
- Implement additional controller types (e.g., PI, PD).
- Save simulation results for offline analysis.
- Include a feature to export plots as images.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## Contact

For questions or suggestions, please contact:

- **Name:** Samuel Boluwatife Giwa
- **Email:** <Samuelgiwa41@gmail.com>
- **LinkedIn:** 

---
Thank you for using the Process Control Teaching Tool!
