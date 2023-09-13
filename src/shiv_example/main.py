import logging

import requests

logging.basicConfig(
    format="%(asctime)s - %(process)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main():
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    r.status_code
    logger.info(r)


if __name__ == "__main__":
    main()
