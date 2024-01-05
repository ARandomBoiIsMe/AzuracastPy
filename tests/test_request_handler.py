import requests

import unittest
from unittest import TestCase, mock

from AzuracastPy.request_handler import RequestHandler
from AzuracastPy.exceptions import (
    AccessDeniedException, AzuracastAPIException, UnexpectedErrorException, ClientException
)

class TestRequestHandler(TestCase):
    def setUp(self) -> None:
        self.request_handler = RequestHandler('')
        self.response = requests.Response()

    def test__send_request_good_200_returns_result(self):
        self.response.status_code = 200
        self.response._content = '{}'.encode()

        with mock.patch("requests.request", return_value=self.response):
            result = self.request_handler._send_request('GET', '')
            self.assertIsInstance(result, dict)

    def test__send_request_200_bad_json_raises_unexpected_error_exception(self):
        self.response.status_code = 200
        self.response._content = '{"really bad json": '.encode()

        with mock.patch("requests.request", return_value=self.response):
            with self.assertRaises(UnexpectedErrorException):
                self.request_handler._send_request('GET', '')

    def test__send_request_200_bad_html_raises_unexpected_error_exception(self):
        self.response.status_code = 200
        self.response._content = """
        TYPE html>
            <html lang="en"
                data-bs-theme="">
            <head
                <meta charset="utf-8">
                meta htequiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <ti>Log In - AzuraCa
                </head>
            <body class="page-minimal ">
            </body>
        </html>
        """.encode()

        with mock.patch("requests.request", return_value=self.response):
            with self.assertRaises(UnexpectedErrorException):
                self.request_handler._send_request('GET', '')

    def test__send_request_bad_200_raises_access_denied_exception(self):
        self.response.status_code = 200
        self.response._content = """
        <!DOCTYPE html>
            <html lang="en"
                data-bs-theme="">
            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Log In - AzuraCast</title>
                </head>
            <body class="page-minimal ">
            </body>
        </html>
        """.encode()

        with mock.patch("requests.request", return_value=self.response):
            with self.assertRaises(AccessDeniedException):
                self.request_handler._send_request('GET', '')

    def test__send_request_500_bad_json_raises_unexpected_error_exception(self):
        self.response.status_code = 500
        self.response._content = '{"type": "error_type"}'.encode()

        with mock.patch("requests.request", return_value=self.response):
            with self.assertRaises(UnexpectedErrorException):
                self.request_handler._send_request('GET', '')

    def test__send_request_500_bad_html_raises_unexpected_error_exception(self):
        self.response.status_code = 500
        self.response._content = """
        <!DOCTYPE html>
            <html lang="en"
                data-bs-theme="">
            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Log In - AzuraCast</title>
                </head>
            <body class="page-minimal ">
            </body>
        </html>
        """.encode()

        with mock.patch("requests.request", return_value=self.response):
            with self.assertRaises(UnexpectedErrorException):
                self.request_handler._send_request('GET', '')

    def test__send_request_500_good_json_raises_azuracast_api_exception(self):
        self.response.status_code = 500
        self.response._content = '{"type": "error_type", "message": "error_message"}'.encode()

        with mock.patch("requests.request", return_value=self.response):
            with self.assertRaises(AzuracastAPIException):
                self.request_handler._send_request('GET', '')

    def test__send_request_500_good_html_raises_azuracast_api_exception(self):
        self.response.status_code = 500
        self.response._content = """
        <!DOCTYPE html>
        <html lang="en"
            data-bs-theme="">
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Error - AzuraCast</title>
        </head>
        <body class="page-minimal error-content">
        <main>
        <div class="public-page">
            <div class="card p-3">
                <div class="card-body">
                    <h2 class="display-4">Error</h2>
                    <h4>Station not found.</h4>
                    <p class="text-muted card-text">
                        src/Exception/NotFoundException.php : L34            </p>
                </div>
            </div>
        </div>
        </body>
        </html>
        """.encode()

        with mock.patch("requests.request", return_value=self.response):
            with self.assertRaises(AzuracastAPIException):
                self.request_handler._send_request('GET', '')

    def test__send_request_403_raises_access_denied_exception(self):
        self.response.status_code = 403
        self.response._content = '{"bruh": "lol"}'.encode()

        with mock.patch("requests.request", return_value=self.response):
            with self.assertRaises(AccessDeniedException):
                self.request_handler._send_request('GET', '')

    def test__send_request_404_raises_client_exception_(self):
        self.response.status_code = 404
        self.response._content = '{"bruh": "lol"}'.encode()

        with mock.patch("requests.request", return_value=self.response):
            with self.assertRaises(ClientException):
                self.request_handler._send_request('GET', '')

if __name__ == '__main__':
    unittest.main()