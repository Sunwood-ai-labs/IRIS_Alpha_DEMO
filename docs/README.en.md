## 🚀 IRIS v7.1.0 Release Notes

## 📋 Overview

IRIS v7.1.0 is a release focused on improving documentation and code organization. This version significantly enhances the structure and content of the README, improving the user experience. Additionally, the automatic release notes generation feature has been removed, and related code has been reorganized to enhance project maintainability.

## ✨ New Features
- 🎉 **S3 File Upload:** Added functionality to upload files to S3. Specify AWS credentials, bucket name, and file path to upload files to S3. Upon successful upload, the file URL on S3 can be retrieved.
- 🎉 **GitHub CDN Service:** Added functionality to upload files to GitHub CDN. Obtain the repository ID, release ID, and file path to upload files using the GitHub API. Upon successful upload, the file URL on the CDN can be retrieved.
- 🎉 **S3 Bucket Public Settings:** Added settings to publish header images for private repositories on S3. By configuring public read policies for the S3 bucket and disabling public access blocks, files within the S3 bucket can be made publicly accessible.

## 🛠 Improvements
- 🚀 **Significant improvement in the structure and content of the README**
- 🚀 **Removal of the automatic release notes generation feature**

## 🐛 Bug Fixes
- 🐛 **Temporary disablement of automatic README update processing**

## ⚠️ Important Changes
- 🔥 **Removal of Automatic Release Notes Generation:** The automatic release notes generation feature has been removed in this version.
- 🗑️ **Removal of S3 Upload Processing:**  Following the removal of the automatic release notes generation feature, the S3 upload processing has been removed.
- 🗑️ **Removal of GitHub CDN Upload Processing:**  Following the removal of the automatic release notes generation feature, the GitHub CDN upload processing has been removed.
- 🗑️ **Removal of S3 Public Settings Processing:**  Following the removal of the automatic release notes generation feature, the S3 public settings processing has been removed.

## 📦 Upgrade Instructions

There are no specific upgrade instructions for this version.

## 👏 Acknowledgements

Thank you to the following contributors for their contributions to this release:

- Maki
- iris-s-coon
- github-actions[bot]

---

# IRIS_Alpha_DEMO

![Project Logo](https://raw.githubusercontent.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/main/docs/release_notes/header_image/release_header_latest.png)

IRIS_Alpha_DEMO is an innovative Python project that blends image analysis, natural language processing, and the concept of the Fibonacci sequence. It combines mathematical beauty with practical applications, offering users a unique experience.

[![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-7.1.0-green.svg)](https://github.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/releases)

## 🌟 Key Features

- 🖼️ **Golden Ratio Analysis of Images:** Analyzes images and evaluates composition based on the golden ratio.
- 🔢 **Calculation and Exploration of the Fibonacci Sequence:** Generates sequences, determines specific numbers, and searches for the nearest values.
- 🧠 **Interactive Fibonacci Quiz:**  Learn about the sequence in a fun and engaging way.
- 🌀 **Visualization of the Fibonacci Spiral:** Graphically represents the beautiful mathematical pattern.
- 📚 **Generation of Fibonacci Words:** Explore intriguing linguistic patterns.

## 🚀 Getting Started

### Prerequisites

- Python 3.9
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Sunwood-ai-labs/IRIS_Alpha_DEMO.git
   ```

2. Navigate to the project directory:
   ```
   cd IRIS_Alpha_DEMO
   ```

3. Install the necessary libraries:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Run the main program:
   ```
   python fibonacci_game.py
   ```

2. Follow the on-screen instructions to select the desired game or tool.

3. To use the image analysis feature:
   ```
   python examples/image_golden_ratio_analyzer.py
   ```
   Enter the image path as prompted.

## 📘 Documentation

Detailed documentation can be found on the [Wiki page](https://github.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/wiki).

## 🛠️ Development

If you are interested in contributing to the project, please refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## 📅 Updates

### v7.1.0 (August 12, 2024)
- Significantly improved structure and content of the README
- Removed automatic release notes generation feature
- Temporarily disabled automatic README update processing
- Other minor fixes and improvements

All update history can be found in the [releases](https://github.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/releases).

## 📄 License

This project is released under the MIT license. For details, see the [LICENSE](LICENSE) file.

## 🤝 Contributors

Thank you to all contributors for making this project possible.