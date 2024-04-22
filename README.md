# python-examples

# Flask Text Processing Server

This is a simple Flask server that provides text processing functionalities through a RESTful API. It allows clients to send JSON requests with a specified method and text input, and the server will process the text accordingly and return the result.

## Features

- Uppercase conversion: Convert the provided text input to uppercase.
- Lowercase conversion: Convert the provided text input to lowercase.
- CORS enabled: The server has Cross-Origin Resource Sharing (CORS) enabled for all routes, allowing requests from different origins.
- Error handling: The server provides appropriate error responses for invalid requests or internal server errors.

## Prerequisites

- Python 3.x
- Flask
- Flask-CORS

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/gritholdings/python-examples.git
   ```

2. Navigate to the project directory:

   ```
   cd python-examples
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the server:

   ```
   python server.py
   ```

   The server will run on `http://localhost:5000` by default.

2. Send a POST request to the `/data` endpoint with a JSON payload containing the following fields:
   - `method`: The text processing method to apply. Supported values are `uppercase` and `lowercase`.
   - `text_input`: The text to be processed.

   Example request:
   ```json
   {
     "method": "uppercase",
     "text_input": "Hello, World!"
   }
   ```

3. The server will process the request and return a JSON response with the following fields:
   - `status`: The status of the request. It can be `success` or `error`.
   - `result`: The processed text if the request is successful.
   - `message`: An error message if the request is invalid or an internal server error occurs.

## Configuration

The server can be configured using environment variables:

- `PORT`: The port number on which the server will run. Default is `5000`.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
