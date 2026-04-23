from sympy import Function, exp, Integer, oo, tanh


class sigmoid(Function):
    r"""
    The sigmoid function: 1/(1 + exp(-x))

    This function represents the logistic sigmoid function, commonly used
    in machine learning and neural networks. It maps any real input to
    the interval (0, 1).

    Parameters
    ==========
    x : argument, any real number

    Examples
    ========
    >>> from sympy import symbols, oo
    >>> x = symbols('x')
    >>> sigmoid(x)
    sigmoid(x)
    >>> sigmoid(0)
    1/2
    >>> sigmoid(oo)
    1
    >>> sigmoid(-oo)
    0
    """

    nargs = 1

    # Define evaluation on basic inputs
    @classmethod
    def eval(cls, x):
        # Handle specific known values
        if x == 0:
            return Integer(1) / 2
        if x is oo or x == float('inf'):
            return Integer(1)
        if x is -oo or x == float('-inf'):
            return Integer(0)

        # Don't evaluate for symbolic inputs
        if x.is_Symbol:
            return None

        return None

    # Define numerical evaluation with evalf()
    def _eval_evalf(self, prec):
        from sympy import exp
        return (1 / (1 + exp(-self.args[0])))._eval_evalf(prec)

    # Define basic assumptions/properties
    def _eval_is_real(self):
        x = self.args[0]
        # Sigmoid of a real number is always real
        if x.is_real:
            return True
        # For complex numbers, it might be complex
        return None

    def _eval_is_positive(self):
        x = self.args[0]
        # Sigmoid is always > 0 for all real x
        if x.is_real:
            return True
        return None

    def _eval_is_negative(self):
        # Sigmoid is never negative for real x
        x = self.args[0]
        if x.is_real:
            return False
        return None

    def _eval_is_bounded(self):
        # Sigmoid is bounded between 0 and 1 for real x
        x = self.args[0]
        if x.is_real:
            return True
        return None

    # Define rewriting rules
    def _eval_rewrite(self, rule, args, **hints):
        if rule == exp:
            # Rewrite in terms of exponentials
            x = args[0]
            return 1 / (1 + exp(-x))
        elif rule == tanh:
            # Rewrite as (1 + tanh(x/2))/2
            from sympy import tanh
            x = args[0]
            return (1 + tanh(x / 2)) / 2
        return None

    # Define differentiation
    def fdiff(self, argindex=1):
        """
        Differentiate sigmoid(x) with respect to its argument.
        d/dx sigmoid(x) = sigmoid(x) * (1 - sigmoid(x))
        """
        if argindex == 1:
            x = self.args[0]
            return self * (1 - self)
        else:
            raise ValueError("Invalid argindex: expected 1, got %d" % argindex)

    # Define expansion behavior
    def _eval_expand_basic(self, **hints):
        """Expand basic components"""
        x = self.args[0]
        return 1 / (1 + exp(-x))

    # For pretty printing and representation
    def _latex(self, printer):
        """LaTeX representation: \\sigma(x)"""
        x = self.args[0]
        return r"\sigma\left(%s\right)" % printer._print(x)

    def _pretty(self, printer):
        """Pretty printing"""
        from sympy.printing.pretty.stringpict import prettyForm
        x = printer._print(self.args[0])
        return prettyForm("sigmoid(%s)" % x)

    # Helper methods for sigmoid-specific properties
    def _eval_is_increasing(self):
        """Sigmoid is monotonically increasing"""
        x = self.args[0]
        if x.is_real:
            return True
        return None

    def _eval_series(self, x, x0, n, logx, cdir):
        """Series expansion around x=0"""
        from sympy import series
        expr = 1 / (1 + exp(-x))
        return series(expr, x, x0, n, logx, cdir)


# Alternative implementation using the eml pattern more closely
class sigmoid_alt(Function):
    r"""
    Alternative sigmoid implementation: 1/(1 + e^{-x})
    """

    nargs = 1

    @classmethod
    def eval(cls, x):
        if x == 0:
            return Integer(1) / 2
        if x.is_Symbol:
            return None
        # Return None to let it remain as sigmoid(x)
        return None

    def _eval_evalf(self, prec):
        return (1 / (1 + exp(-self.args[0])))._eval_evalf(prec)

    def fdiff(self, argindex=1):
        if argindex == 1:
            x = self.args[0]
            # Derivative: sigmoid(x) * (1 - sigmoid(x))
            return self * (1 - self)
        raise ValueError("Invalid argindex: expected 1")

    def _latex(self, printer):
        return r"\sigma(%s)" % printer._print(self.args[0])
