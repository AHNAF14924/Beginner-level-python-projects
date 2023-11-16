# URL Shortener

## Introduction

This program is a simple URL shortener built in Python. It uses the Cutt.ly URL shortening service API to create shortened links for long URLs. The program takes a long URL as input, interacts with the API to generate the shortened link, and then displays the shortened link if the process is successful. In case of any errors or issues during the process, appropriate error messages are displayed to the user.

## Requirements

To run this program, you need the following:

- Python 3.x installed on your system.
- The requests library, which can be installed using

```
pip install requests
```

## Usage

1. Clone the repository or download the **app.py** file.

2. Ensure you have Python and the **requests** library installed on your system.

3. Run the program from the terminal or command prompt:

```
python app.py
```

4. Enter the long URL that you want to shorten when prompted.

5. The program will interact with the Cutt.ly API to generate a shortened link for your input URL. If successful, the shortened link will be displayed on the screen. If there are any errors or issues, appropriate error messages will be shown.

## Code Explanation

- The program starts by importing the necessary **requests** library.

- The `shorten_link()` function is the main function that performs the URL shortening process.

- Inside the function, we define the **api_key**, which acts as a secret password to access the Cutt.ly API. You can obtain your own API key by signing up on the Cutt.ly website.

- The **base_url** variable stores the API endpoint URL for the Cutt.ly service.

- The **payload** dictionary holds the necessary data to be sent along with the API request. It contains the **api_key** and the long URL to be shortened.

- We use a **try-except** block to handle potential errors during the URL shortening process.

- The program sends a GET request to the Cutt.ly API using the `requests.get()` method and the provided **payload**.

- The response from the API is then converted to a Python dictionary using the `.json()` method.

- If the shortening process is successful (indicated by a **status** code of **7**), the shortened link is extracted from the response data and displayed to the user.

- If the shortening process encounters any errors (e.g., invalid URL, API key issues, etc.), the **else** block is executed. The appropriate error message is displayed based on the **status** code returned by the API.

- The **except** blocks catch specific exceptions that might occur during the URL shortening process. If there are any issues related to the request (e.g., network errors) or the response data (e.g., missing fields), the respective error messages are displayed.

- The program also includes a `__name__ == "__main__"` check to ensure that the shorten_link() function is called only when the script is run directly and not when it is imported as a module in another program.

## Conclusion

This URL shortener program is a simple yet powerful tool that allows users to convert long URLs into shorter, more shareable links. By leveraging the Cutt.ly API and the **requests** library in Python, the program interacts with the URL shortening service and handles various scenarios gracefully, providing meaningful error messages to the user.

Feel free to use, modify, and extend this program according to your needs. Happy shortening!
