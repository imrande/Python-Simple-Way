## Valid combination of except block

- except ZeroDivisionError:
- except ZeroDivisionError as error:
- except (ZeroDivisionError):
- except (ZeroDivisionError) as error:
- except (ValueError, ZeroDivisionError):
- except (ValueError, ZeroDivisionError) as error:

## Invalid combination of except block

- except (ZeroDivisionError as error):
- except ZeroDivisionError, ValueError:
- except ZeroDivisionError, ValueError as error: