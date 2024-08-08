## Project: IRIS_Alpha_DEMO

This repository is an interactive Python project that deals with image analysis, natural language processing, and the Fibonacci sequence.

## Main Features

- **Image Golden Ratio Analysis:** Loads an image, draws dividing lines based on the golden ratio, and analyzes whether the main subject aligns with the golden ratio.
- **Fibonacci Sequence Calculation:** Calculates the Fibonacci sequence up to a given term.
- **Fibonacci Number Check:** Determines whether a given number is part of the Fibonacci sequence.
- **Fibonacci Quiz:** Presents a quiz about the Fibonacci sequence.
- **Closest Fibonacci Number Search:** Finds the Fibonacci number closest to a given number.
- **Fibonacci Spiral Drawing:** Draws a Fibonacci spiral on a graph.
- **Fibonacci Word Exploration:** Generates Fibonacci words and displays their properties.

## Usage

1. Clone the repository.
2. Run `python fibonacci_game.py`.
3. Follow the on-screen instructions to select a game.
4. To use the image analysis feature, run `examples/image_golden_ratio_analyzer.py` and specify the image path.

## Installation Instructions

1. Install Python 3.9.
2. Install the necessary libraries: `pip install -r requirements.txt`

## Updates

- 🎉 **S3 File Upload:** Added the ability to upload files to S3. You can specify AWS credentials, bucket name, and file path to upload files to S3. Upon successful upload, you will receive the file URL on S3.
- 🎉 **GitHub CDN Service:** Added the ability to upload files to GitHub CDN. You can obtain the repository ID, release ID, and file path to upload files using the GitHub API. Upon successful upload, you will receive the file URL on CDN.
- 🎉 **S3 Bucket Public Settings:** Added settings to publish the header image of a private repository on S3. By setting a public read policy on the S3 bucket and disabling the public access block, you can make the files in the S3 bucket publicly accessible.

## Important Changes

- 🔥 **Release Notes Auto-Generation Feature Removed:** The release notes auto-generation feature has been removed in this version.
- 🗑️ **S3 Upload Processing Removed:** The S3 upload processing has been removed due to the removal of the release notes auto-generation feature.
- 🗑️ **GitHub CDN Upload Processing Removed:** The GitHub CDN upload processing has been removed due to the removal of the release notes auto-generation feature.
- 🗑️ **S3 Public Setting Processing Removed:** The S3 public setting processing has been removed due to the removal of the release notes auto-generation feature.

## Documentation

- 📚 [S3 File Upload Documentation](URL)
- 📚 [GitHub CDN Service Documentation](URL)
- 📚 [S3 Bucket Public Settings Documentation](URL)

## License

This project is distributed under the MIT license. For more information, see the LICENSE file.