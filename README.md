# Auto Clicker Project

A Python-based auto-clicker that simulates mouse clicks at random intervals, designed for flexibility and ease of use.

## ✨ Features
- **Start and Stop Easily**: Control the clicker using keyboard shortcuts:
  - Press `o` to toggle clicking on/off.
  - Press `p` to stop the program and save the log.
- **Realistic Behavior**: Simulates human-like clicking with:
  - Randomized click delays.
  - Press and release actions for more natural interaction.
- **Click Logging**: Automatically saves the total clicks to a log file in the `logs` folder.
- **Customizable**: Adjust click delays and other settings via the code.

---

## 🛠 Requirements
- Python 3.7 or higher.
- Dependencies listed in `requirements.txt`.

---

## 📦 Setup
Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jpmf-bogas/auto-clicker.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd auto_clicker
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Run the Auto Clicker**:
   ```bash
   python auto_clicker/clicker.py
   ```

2. **Control the Auto Clicker**:
   - Press `o` to start and stop the auto-clicker.
   - Press `p` to stop the program and save the click log.

3. **View Logs:**
   - Logs are saved in the `logs/click_log.txt` file in the following format:
   ```ruby
   YYYY-MM-DD HH:MM:SS -> Total Clicks: [number_of_clicks]
   ```

## 🧪 Running Tests
Run unit tests to ensure the auto-clicker works as expected:
```bash
pytest
```

## 🛠 Configuration

The clicker settings can be customized by editing the `AutoClicker` class in `auto_clicker/clicker.py`:
- **Delay Range**: Adjust `delay_min` and `delay_max` for randomized click delays.
- **Mouse Button**: Change the button to simulate (`Button.left` or `Button.right`).

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Contributions are welcome! If you'd like to make improvements or report issues:
1. Fork the repository.

2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```

4. Push to your branch
   ```bash
   git push origin feature-name
   ```

5. Open a pull request

## 📄 Acknowledgments
Special thanks to the open-source community for providing inspiration and tools to create this project.


