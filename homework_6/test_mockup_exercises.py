# -*- coding: utf-8 -*-

"""
Mock up testing examples
"""
import unittest
from subprocess import CalledProcessError
from unittest.mock import mock_open, patch

# Importacion directa del módulo (sin prefijo de paquete)
from mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestFetchDataFromApi(unittest.TestCase):
    """
    Fetch data from API unittest class.
    """

    @patch("mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case.
        """
        mock_get.return_value.json.return_value = {"key": "value"}

        result = fetch_data_from_api("https://api.example.com/data")

        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Perform Action Based On Time unittest class.
    """

    @patch("mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_a(self, mock_time):
        """
        Action A.
        """
        mock_time.return_value = 5
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")

    @patch("mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_b(self, mock_time):
        """
        Action B.
        """
        mock_time.return_value = 15
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")


class TestReadDataFromFile(unittest.TestCase):
    """
    Read data from file unittest class.
    """

    @patch(
        "mockup_exercises.open",
        new_callable=mock_open,
        read_data="contenido del archivo",
    )
    def test_read_data_from_file_success(self, mock_file):
        """
        Success case: file exists and is readable.
        """
        filename = "datos.txt"
        result = read_data_from_file(filename)

        self.assertEqual(result, "contenido del archivo")
        mock_file.assert_called_once_with(filename, encoding="utf-8")

    @patch("mockup_exercises.open")
    def test_read_data_from_file_not_found(self, mock_file):
        """
        Error case: file does not exist, FileNotFoundError is raised.
        """
        mock_file.side_effect = FileNotFoundError
        filename = "no_existe.txt"

        with self.assertRaises(FileNotFoundError):
            read_data_from_file(filename)


class TestExecuteCommand(unittest.TestCase):
    """
    Execute command unittest class.
    """

    @patch("mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Success case: command executes successfully and returns stdout.
        """
        mock_run.return_value.stdout = "comando ejecutado\n"
        mock_run.return_value.stderr = ""

        command = ["echo", "hola"]
        result = execute_command(command)

        self.assertEqual(result, "comando ejecutado\n")
        mock_run.assert_called_once_with(
            command, capture_output=True, check=False, text=True
        )

    @patch("mockup_exercises.subprocess.run")
    def test_execute_command_failure(self, mock_run):
        """
        Error case: command fails, CalledProcessError is raised.
        """
        mock_run.side_effect = CalledProcessError(returncode=1, cmd="comando")

        command = ["comando", "invalido"]
        with self.assertRaises(CalledProcessError):
            execute_command(command)


if __name__ == "__main__":
    unittest.main()
