# OpenCV-Facial-Recognition

## About The Project

The OpenCV-Facial-Recognition project provides a way to check for blacklisted people in a directory of images using facial recognition. It uses OpenCV to check for faces within images and compares these detected faces against a pre-defined list of blacklisted images based on their facial histograms. The core functionality includes loading images, detecting face regions, computing face histograms for detailed comparison and identifying matches within faces.

### Built With

[![Python][Python-badge]][Python-url]
[![OpenCV][OpenCV-badge]][OpenCV-url]

### Features

Upon populating the "blacklisted" and "to_check" folders and running "main.py", the code will run a comparison check between two folders. It will output the username based on the filename of the images. Additionally, a popup of the face region of each image will be presented and you can skip through these images by pressing any character on your keyboard.<br /><br />
**PLEASE NOTE: This code requires you to place your images of faces in the "blacklisted" and "to_check" folders and the code will not run without doing so. This code is also based upon the assumption that the filename of the image represents a username, however the code will still run without this implemented.**

## Getting Started

To get this project running on your local machine, follow these steps.

### Prerequisites

- `Python 3.6 or later`
- `pip`

### Setup

1. Clone the repository: `git clone https://github.com/AbdullahHDev/OpenCV-Facial-Recognition.git`
2. Install requirements: `pip install -r requirements.txt`
3. Run the script: `python main.py`
4. **Please ensure you have put your blacklisted images into the blacklisted folder and your images to compare in the to_check folder**

## Usage
This project is designed to automate the process of facial recognition against a blacklist. It can be utilized in various ways such as:

- Security checkpoints to prevent unauthorized access
- Automated surveillance systems for real-time monitoring
- Access control systems in sensitive areas

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b OpenCV-Facial-Recognition/feature`)
3. Commit your Changes (`git commit -m 'Add a feature'`)
4. Push to the Branch (`git push origin OpenCV-Facial-Recognition/feature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

Abdullah Hussain - A.A.Hussain1@newcastle.ac.uk

Project Link: [https://github.com/AbdullahHDev/OpenCV-Facial-Recognition](https://github.com/AbdullahHDev/OpenCV-Facial-Recognition)

## Acknowledgments

* [Python](https://www.python.org/)
* [OpenCV](https://opencv.org/)


[Python-badge]: https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=yellow
[Python-url]: https://www.python.org/doc/
[OpenCV-badge]: https://img.shields.io/badge/OpenCV-5C3EE8.svg?style=for-the-badge&logo=opencv&logoColor=white
[OpenCV-url]: https://opencv.org/
