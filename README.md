# Digikala Image Crawler

A Python-based image crawler designed to systematically download product images from Digikala's API endpoints. This project was developed as part of a challenge to test the feasibility of automated data collection.

## ⚠️ Disclaimer

**Important Notice:** This project was created for educational and research purposes as part of a Digikala challenge to test whether systematic data collection was possible. It was developed to win prizes in a legitimate contest and to demonstrate technical capabilities.

**Please Note:**
- This code should only be used for educational, research, or legitimate testing purposes
- Always respect website terms of service and robots.txt files
- Be mindful of rate limiting and server resources
- Ensure compliance with applicable laws and regulations regarding web scraping
- The authors are not responsible for any misuse of this code

## 📁 Project Structure

```
Digikala_img_Crawler/
├── main.py          # Main crawler script
├── sorter.py        # Image filtering and sorting utility
└── README.md        # This file
```

## 🚀 Features

- **Concurrent Downloads**: Multi-threaded image downloading for improved performance
- **Progress Tracking**: Real-time progress bars using tqdm
- **Error Handling**: Robust error handling for network requests and file operations
- **Image Filtering**: Automatic filtering of images based on file size criteria
- **API Integration**: Direct integration with Digikala's public API endpoints

## 📋 Requirements

```python
requests
tqdm
numpy
concurrent.futures (built-in)
```

## 🛠️ Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Digikala_img_Crawler
```

2. Install required dependencies:
```bash
pip install requests tqdm numpy
```

## 💻 Usage

### Main Crawler (`main.py`)

The main script downloads product images from Digikala's kids bodysuit category:

```bash
python main.py
```

**Configuration Options:**
- `OUTPUT_FOLDER`: Directory to save downloaded images (default: "img")
- `MAX_WORKERS`: Number of concurrent download threads (default: 10)
- `NOT_HTTP_DEBUGGER`: SSL verification setting (default: True)

**Process:**
1. Fetches product listings from pages 50-100
2. Extracts product IDs from each page
3. Downloads main product images concurrently
4. Saves images with timestamp-based filenames

### Image Sorter (`sorter.py`)

Filters downloaded images based on file size criteria:

```bash
python sorter.py
```

**Functionality:**
- Scans the downloaded images folder
- Filters images between 70-90 KB in size
- Copies filtered images to a "product" folder
- Provides progress tracking during processing

## 🔧 Technical Details

### API Endpoints Used

- **Product Search**: `https://api.digikala.com/v1/categories/kids-bodysuit/search/`
- **Product Details**: `https://api.digikala.com/v2/product/{product_id}/`

### Headers Configuration

The crawler uses browser-like headers to ensure proper API responses:
```python
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
}
```

### Error Handling

- Network request failures are logged and skipped
- JSON parsing errors are handled gracefully
- File I/O errors are caught and reported
- Missing product data is handled without crashing

## 📊 Performance

- **Concurrent Processing**: Up to 10 simultaneous downloads
- **Progress Tracking**: Real-time progress bars for both page processing and individual downloads
- **Memory Efficient**: Processes images in chunks to minimize memory usage

## 🔒 Ethical Considerations

This project was developed with the following principles:

1. **Legitimate Purpose**: Created for a contest/challenge scenario
2. **Rate Limiting**: Implements concurrent limits to avoid overwhelming servers
3. **Public APIs**: Uses only publicly accessible API endpoints
4. **Educational Value**: Demonstrates web scraping techniques and best practices

## 🐛 Troubleshooting

**Common Issues:**

1. **Network Errors**: Check internet connection and firewall settings
2. **SSL Verification**: Adjust `NOT_HTTP_DEBUGGER` setting if needed
3. **Permission Errors**: Ensure write permissions for output directories
4. **API Changes**: API endpoints may change over time

## 📝 License

This project is provided as-is for educational purposes. Please ensure compliance with all applicable laws and terms of service before use.

## 🤝 Contributing

This project was created for a specific challenge, but suggestions and improvements are welcome for educational purposes.

---

**Remember**: Always use web scraping tools responsibly and in compliance with website terms of service and applicable laws.
