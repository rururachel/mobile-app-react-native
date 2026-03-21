import os
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Check if required environment variables are set
    if 'MOBILE_APP_API_KEY' not in os.environ:
        logging.error('MOBILE_APP_API_KEY environment variable is not set')
        sys.exit(1)

    if 'DATABASE_URL' not in os.environ:
        logging.error('DATABASE_URL environment variable is not set')
        sys.exit(1)

    # Initialize Flask app
    from mobile_app import create_app
    app = create_app()

    # Run Flask app
    if __name__ == '__main__':
        app.run(debug=True)

if __name__ == '__main__':
    main()