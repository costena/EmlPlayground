from sympy import Function, exp, log, E


class eml(Function):
    r"""
    The eml function: exp(x) - log(y)

    This function represents the expression exp(x) - log(y).
    It's defined for mathematical operations and simplifications.

    Parameters
    ==========
    x : first argument, exponent in exponential term
    y : second argument, argument of logarithm (must be positive)

    Examples
    ========
    >>> from sympy import symbols, pi, E
    >>> x, y = symbols('x y')
    >>> eml(x, y)
    eml(x, y)
    >>> eml(1, 1)
    E
    >>> eml(0, E)
    1 - 1
    """

    nargs = 2

    # Define evaluation on basic inputs
    @classmethod
    def eval(cls, x, y):
        if x.is_Symbol and y.is_Symbol:
            return None
        return exp(x) - log(y)

    # Define numerical evaluation with evalf()
    def _eval_evalf(self, prec):
        return (exp(self.args[0]) - log(self.args[1]))._eval_evalf(prec)

    # Define basic assumptions/properties
    def _eval_is_real(self):
        x, y = self.args
        # eml(x, y) is real if x is real and y is positive real
        if x.is_real and y.is_positive:
            return True
        # If conditions are not satisfied, return None (unknown)
        return None

    def _eval_is_positive(self):
        x, y = self.args
        # eml(x, y) > 0 if exp(x) > log(y)
        # This is generally true for many cases, but we'll implement simple cases
        if x.is_real and y.is_positive:
            # For x >= 0 and y <= 1, exp(x) >= 1 and log(y) <= 0, so eml >= 1
            if x >= 0 and y <= 1:
                return True
        return None

    def _eval_is_nonnegative(self):
        x, y = self.args
        if x.is_real and y.is_positive:
            # Check if eml(x, y) can be negative
            # For small x and large y, it could be negative
            if x >= 0 and y <= 1:
                return True
        return None

    # Define rewriting rules
    def _eval_rewrite(self, rule, args, **hints):
        if rule == exp:
            # Rewrite in terms of exponential only
            # log(y) can't be directly rewritten in terms of exp without introducing log
            return exp(args[0]) - log(args[1])
        elif rule == log:
            # Rewrite in terms of log only
            return exp(args[0]) - log(args[1])
        return None

    # Define differentiation
    def fdiff(self, argindex=1):
        """
        Differentiate eml(x, y) with respect to its arguments.
        argindex=1: differentiate with respect to x
        argindex=2: differentiate with respect to y
        """
        x, y = self.args

        if argindex == 1:
            # d/dx of exp(x) - log(y) = exp(x)
            return exp(x)
        elif argindex == 2:
            # d/dy of exp(x) - log(y) = -1/y
            return -1 / y
        else:
            raise ValueError("Invalid argindex: expected 1 or 2, got %d" % argindex)

    # Define expansion behavior
    def _eval_expand_basic(self, **hints):
        """Expand basic components"""
        x, y = self.args
        return exp(x) - log(y)

    # For pretty printing and representation
    def _latex(self, printer):
        """LaTeX representation: e^{x} - \log(y)"""
        x, y = self.args
        return r"eml(%s, %s)" % (printer._print(x), printer._print(y))

    def _pretty(self, printer):
        """Pretty printing"""
        from sympy.printing.pretty.stringpict import prettyForm
        x = printer._print(self.args[0])
        y = printer._print(self.args[1])
        return prettyForm("exp(%s) - log(%s)" % (x, y))