
# Currency Converter Pro


A sleek, modern, and responsive web application built with Flask to convert currencies in real-time using the [currencyapi.com](https://currencyapi.com/) API. Featuring an elegant UI with glassmorphism design, hover animations, and support for 50+ currencies, this tool is both functional and visually stunning.

---

## Features

- **Real-Time Conversion**: Fetches live exchange rates via the currencyapi.com API.
- **50+ Currencies**: Supports a wide range of global currencies (USD, EUR, JPY, INR, AED, etc.).
- **Responsive Design**: Adapts seamlessly to mobile, tablet, laptop, and split-screen layouts.
- **Interactive UI**: Includes Convert, Swap, and Reset buttons with smooth animations and glowing inputs.
- **Glassmorphism**: Premium design with a frosted-glass card and gradient background.
- **Error-Free**: Fully tested for functionality and responsiveness.


---

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, Tailwind CSS (via CDN), Font Awesome (via CDN), Custom CSS
- **API**: [currencyapi.com](https://currencyapi.com/) (Free tier: 300 requests/month)
- **Fonts**: Poppins (via Google Fonts)
- **IDE**: Visual Studio Code

---

## Prerequisites

- **Python 3.8+**: Installed on your system ([Download](https://www.python.org/downloads/)).
- **Git**: Installed and configured ([Download](https://git-scm.com/downloads)).
- **GitHub Account**: Sign up at [github.com](https://github.com/) if you don’t have one.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/currency-converter-pro.git
   cd currency-converter-pro
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install flask requests
   ```

4. **Get an API Key**:
   - Sign up for a free account at [currencyapi.com](https://currencyapi.com/).
   - Copy your API key and replace "YOUR_API_KEY_HERE" in `app.py`.

5. **Run the App**:
   ```bash
   python app.py
   ```
   Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## Usage

1. Enter an amount in the input field.
2. Select "From" and "To" currencies from the dropdowns.
3. Click Convert to see the result.
4. Use Swap to flip currencies or Reset to clear the form and result.

---

## Project Structure

```text
currency-converter-pro/
├── app.py              # Flask backend logic
├── templates/
│   └── index.html      # Responsive frontend UI
├── README.md           # Project documentation
└── venv/               # Virtual environment (not tracked)
```

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License.
