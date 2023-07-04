# Automatic PowerPoint Generator

Welcome to the GitHub page for the program that automates the process of creating a PowerPoint presentation from an image album and automatically advance slide. This tool simplifies the task of creating presentations by eliminating the manual effort of creating slides and organizing images.

## Features
- **Automatic Slide Creation**: The program automatically creates slides in a PowerPoint presentation based on the images in the album. Each image will be placed on a separate slide.
- **Slide Show Generation**: Once the slides are created, the program automatically generates a slide show from the slides, allowing you to easily present your images.


## Installation
 
To get started, follow these steps:

1. Clone this repository to your local machine or download the source code as a ZIP file.
2. Ensure that you have Python 3.8 or a higher version installed.
3. Navigate to the project directory.

   ```bash
   cd automatic-powerpoint-generator
   ```

4. It is recommended to create a virtual environment to manage project dependencies.

   ```bash
   python3 -m venv venv
   ```

5. Activate the virtual environment.

   - For Windows:

     ```bash
     venv\Scripts\activate
     ```

   - For macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

7. You're all set!

## Usage

To use the program, follow these steps:

1. Prepare your train images, validation images, surface image to corresponding folders of data/y, data/y_valid, surface
2. Change the camera of your choice in main.py
3. Run the program by executing the following command:

   ```bash
   python main.py
   ```

4. The program will then do the slide advancing and capture images using the camera of your choice and put them to corresponding folder

## Contributing

If you would like to enhance the program or report any issues, please open an issue or submit a pull request on the [GitHub repository](https://github.com/your-repository-link).

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to explore the code, modify it, and adapt it to your needs. If you find it helpful, we would appreciate it if you could acknowledge our work by giving us credit somewhere in your project.

