# TODO: start the actually main function
# TODO: start the setup.py

from canvasscraper import CanvasScraperTester, arg_tools


if __name__ == '__main__':
    args = arg_tools.get_and_validate_args()
    CanvasScraperTester.main(args)
