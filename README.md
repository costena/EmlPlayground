# Eml Playground

An interactive mathematical playground for exploring the `eml(x, y) = e^x - log(y)` function through symbolic manipulation and visual expression synthesis.

## Overview

Eml Playground is a desktop application built with PyQt6 and SymPy that provides an intuitive drag-and-drop interface for constructing mathematical expressions. The core focus is the `eml` function (exponential minus logarithm), but the system supports a wide range of mathematical operations through SymPy's symbolic algebra capabilities.

The application is designed as an educational tool for exploring function composition, symbolic simplification, and mathematical discovery through guided tasks.

## Features

- **Interactive Expression Building**: Drag-and-drop interface for constructing complex expressions from basic components
- **Symbolic Computation**: Powered by SymPy for accurate mathematical simplification and evaluation
- **Task System**: Progressive challenges that guide users through mathematical discovery
- **Expression Inventory**: Save and reuse discovered expressions
- **LaTeX Rendering**: Beautiful mathematical typesetting with real-time LaTeX rendering
- **Persistent Storage**: Automatic saving of progress and inventory
- **Extensible Architecture**: Custom function definitions (eml, sigmoid) with full SymPy integration

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd EmlPlayground
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. **Launch the application**: Run `python main.py` to start the Eml Playground.

2. **Understand the interface**:
   - **Top Panel**: Current task and target expression
   - **Left Panel**: Expression inventory (drag from here)
   - **Right Panel**: Synthesis area (drop expressions here)

3. **Complete tasks**:
   - Drag expressions from inventory to the synthesis area
   - Fill expression slots to build composite expressions
   - Click "Synthesize" to evaluate and discover new expressions
   - Successfully created expressions are added to your inventory

4. **Progress through challenges**:
   - The task panel shows current target (E, exp(x), log(x), etc.)
   - Each discovered expression unlocks new mathematical possibilities
   - The system guides you from basic to advanced mathematical concepts

## Project Structure

```
EmlPlayground/
├── main.py                 # Application entry point
├── Eml.py                  # Core eml function definition
├── EmlPlaygroundWidget.py  # Main application window
├── InventoryWidget.py      # Expression inventory panel
├── ExpressionWidget.py     # Interactive expression widget
├── ExpressionSlotWidget.py # Drag-and-drop expression slots
├── SynthesisWidget.py      # Expression synthesis area
├── TaskWidget.py          # Task/challenge system
├── SymbolsWidget.py       # Symbol selection panel
├── LatexRenderer.py       # LaTeX to pixmap rendering
├── Sigmoid.py             # Sigmoid function definition
├── Archive.py             # Progress saving/loading
├── style.qss              # Qt stylesheet
├── requirements.txt       # Python dependencies
└── save.yaml              # User progress (auto-generated)
```

## Dependencies

- **PyQt6**: GUI framework
- **SymPy**: Symbolic mathematics library
- **Matplotlib**: LaTeX rendering backend
- **PyYAML**: Progress serialization

See `requirements.txt` for exact versions.

## Development

### Adding New Functions

The system is designed to be extensible. To add a new custom function:

1. Create a new file following the pattern in `Eml.py` or `Sigmoid.py`
2. Define a SymPy `Function` subclass with appropriate evaluation rules
3. Import and register the function in relevant widgets

### Code Style

- Follow PEP 8 conventions
- Use descriptive variable names
- Add docstrings for public methods
- Type hints are encouraged but not required

### Testing

Run the application and verify:
- Expression dragging works correctly
- Synthesis produces mathematically correct results
- Tasks progress as expected
- Progress saves and loads properly

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Acknowledgments

- Built with [SymPy](https://www.sympy.org/) for symbolic mathematics
- GUI powered by [PyQt6](https://www.riverbankcomputing.com/software/pyqt/)
- LaTeX rendering via [Matplotlib](https://matplotlib.org/)
- Inspired by interactive mathematical exploration tools

## Contact

For questions or feedback, please open an issue on the project repository.