import json
import os
import time
import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm


# Configuration constants
NOT_HTTP_DEBUGGER = True
OUTPUT_FOLDER = "img"
MAX_WORKERS = 10

# HTTP headers for requests
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
}

def save_img(product_id: int, url: str, filename: str) -> None:
    """
    Download and save an image from the given URL.
    
    Args:
        product_id: Product ID (for potential future use)
        url: URL of the image to download
        filename: Local filename to save the image
    """
    try:
        response = requests.get(url, verify=NOT_HTTP_DEBUGGER, headers=HEADERS)
        response.raise_for_status()
        
        if not os.path.exists(OUTPUT_FOLDER):
            os.makedirs(OUTPUT_FOLDER)
            
        with open(filename, 'wb') as f:
            f.write(response.content)
    except requests.RequestException as e:
        print(f"Error downloading image for product {product_id}: {e}")


def leech_img(product_id: int) -> None:
    """
    Download the main image for a given product ID.
    
    Args:
        product_id: The ID of the product to download images for
    """
    try:
        api_url = f"https://api.digikala.com/v2/product/{product_id}/"
        response = requests.get(api_url, verify=NOT_HTTP_DEBUGGER, headers=HEADERS)
        response.raise_for_status()
        
        data = response.json()
        main_image_url = data["data"]["product"]["images"]["main"]["url"][0]
        filename = f'{OUTPUT_FOLDER}/main-{time.time()}.jpg'
        
        save_img(product_id, main_image_url, filename)
        
    except (requests.RequestException, KeyError, json.JSONDecodeError) as e:
        print(f"Error processing product {product_id}: {e}")


def get_product_ids(page: int) -> list:
    """
    Get product IDs from a specific page of the kids bodysuit category.
    
    Args:
        page: Page number to fetch
        
    Returns:
        List of product IDs
    """
    try:
        search_url = (
            f"https://api.digikala.com/v1/categories/kids-bodysuit/search/"
            f"?page={page}&sort22&seo_url=%2Fcategory-kids-bodysuit%2F"
            f"%3Fpage%3D11%26sort%3D21"
        )
        
        response = requests.get(search_url, verify=NOT_HTTP_DEBUGGER, headers=HEADERS)
        response.raise_for_status()
        
        data = response.json()
        return [product["id"] for product in data["data"]["products"]]
        
    except (requests.RequestException, KeyError, json.JSONDecodeError) as e:
        print(f"Error fetching products for page {page}: {e}")
        return []


def main():
    """Main function to orchestrate the image downloading process."""
    print(f"Starting image download to folder: {OUTPUT_FOLDER}")
    
    for page in range(50, 101):
        print(f"Processing page {page}...")
        
        product_ids = get_product_ids(page)
        if not product_ids:
            print(f"No products found on page {page}, skipping...")
            continue
            
        print(f"Found {len(product_ids)} products on page {page}")
        
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            list(tqdm(
                executor.map(leech_img, product_ids), 
                total=len(product_ids),
                desc=f"Page {page}"
            ))
    
    print("Download completed!")


if __name__ == "__main__":
    main()