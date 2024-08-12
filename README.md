# FastHTML Tailwind Boilderplate

This repository contains a boilderplate built with [FastHTML](https://github.com/your-repo/python-fasthtml) and [Tailwind CSS](https://tailwindcss.com/). It was created by [Danilo Marano](https://github.com/danilommarano) for anyone start as fast as possible a website. FastHTML is a lightweight and fast web framework for Python, leveraging the power of [HTMX](https://htmx.org/) to create dynamic and interactive web applications without relying on heavy JavaScript frameworks.

## Features

- **FastHTML Integration**: Easily build dynamic web pages using Python and HTMX.
- **Tailwind CSS**: A utility-first CSS framework for rapidly building custom designs.
- **Responsive Design**: Pre-configured to be fully responsive out of the box.
- **Easy Setup**: Start your project quickly with a ready-to-use boilderplate.
- **Customizable Components**: Modify or extend the existing components to suit your needs.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/danilommarano/boilerplate-fasthtml-tailwind my-website
   cd my-website
   ```

2. **Install dependencies:**

   Ensure you have Python 3.7+ installed.

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server:**

   ```bash
   python main.py
   ```

4. **Build Tailwind CSS:**

   If you need to rebuild the Tailwind CSS, you can do so using the following command (assuming you have Node.js and npm installed):

   ```bash
   tailwindcss -i ./src/input.css -o ./dist/output.css --watch
   ```

5. **Access Home Page:**

   Finnaly go to http://0.0.0.0:5001

## Project Structure

```
boilderplate-fasthtml-tailwind/
├── app
│   ├── app.py
├── components
│   └── __init__.py
├── styles
│   ├── global.css
│   └── output.css
├── README.md
├── requirements.txt
└── tailwind.config.js
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas or improvements.

## Acknowledgments

- [FastHTML](https://www.fastht.ml/) for providing a powerful Python framework.
- [Tailwind CSS](https://tailwindcss.com/) for the amazing utility-first CSS framework.
