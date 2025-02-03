import os
import pytest
from openpyxl import Workbook
from src.utils.excel_reader import ExcelReader
from src.utils.logger import get_logger

# Obtain a logger instance for these tests.
logger = get_logger("test_excel_reader")


def create_sample_workbook(file_path):
    """
    Creates a sample Excel workbook with two sheets.

    Sheet1:
      - Headers: Name, Age
      - Rows: [("Alice", 30), ("Bob", 25)]

    Sheet2:
      - Headers: Header1, Header2
      - Row: [("Value1", "Value2")]
    """
    wb = Workbook()
    # Configure Sheet1
    ws1 = wb.active
    ws1.title = "Sheet1"
    ws1.append(["Name", "Age"])
    ws1.append(["Alice", 30])
    ws1.append(["Bob", 25])

    # Configure Sheet2
    ws2 = wb.create_sheet("Sheet2")
    ws2.append(["Header1", "Header2"])
    ws2.append(["Value1", "Value2"])

    wb.save(file_path)
    logger.info("Created sample workbook at: %s", file_path)


def test_file_not_found(tmp_path):
    logger.info("Running test_file_not_found")
    file_path = tmp_path / "non_existent.xlsx"
    with pytest.raises(FileNotFoundError):
        ExcelReader(str(file_path))
    logger.info("test_file_not_found passed.")


def test_get_sheet_names(tmp_path):
    logger.info("Running test_get_sheet_names")
    file_path = tmp_path / "test.xlsx"
    create_sample_workbook(file_path)

    reader = ExcelReader(str(file_path))
    sheet_names = reader.get_sheet_names()
    logger.info("Retrieved sheet names: %s", sheet_names)

    assert "Sheet1" in sheet_names
    assert "Sheet2" in sheet_names


def test_get_sheet_data(tmp_path):
    logger.info("Running test_get_sheet_data")
    file_path = tmp_path / "test.xlsx"
    create_sample_workbook(file_path)

    reader = ExcelReader(str(file_path))
    data = reader.get_sheet_data("Sheet1")
    logger.info("Sheet1 data: %s", data)

    # Validate that two rows of data are returned.
    assert isinstance(data, list)
    assert len(data) == 2
    # Verify the data in the first row.
    assert data[0]["Name"] == "Alice"
    assert data[0]["Age"] == 30
    # Verify the data in the second row.
    assert data[1]["Name"] == "Bob"
    assert data[1]["Age"] == 25


def test_get_cell_value(tmp_path):
    logger.info("Running test_get_cell_value")
    file_path = tmp_path / "test.xlsx"
    create_sample_workbook(file_path)

    reader = ExcelReader(str(file_path))
    # Test retrieving a cell value using numeric column indexing.
    value_numeric = reader.get_cell_value("Sheet2", row=2, column=1)
    logger.info("Retrieved cell value (numeric index): %s", value_numeric)
    assert value_numeric == "Value1"

    # Test retrieving a cell value using a letter column.
    value_letter = reader.get_cell_value("Sheet2", row=2, column="A")
    logger.info("Retrieved cell value (letter index): %s", value_letter)
    assert value_letter == "Value1"
