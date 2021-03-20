# -*- coding: utf-8 -*-
"""density-areas.ipynb

Automatically generated by Colaboratory.
"""

import sympy as sym # Import the SymPy module
import numpy as np  # Import the NumPy module

from scipy.integrate import quad # Import the function 'quad' from the 'scipy.integrate' sub-package
from scipy.integrate import dblquad # Import the function 'dblquad' from the 'scipy.integrate' sub-package


def PoissonWasserstein_R2(tau, rho, function1, function2, numerical=False):
    """ Computes the Poisson bracket of two linear functionals on the space P^{OO}(Q), of measures with a smooth 
        positive density function on the open unit square Q = (0, 1) x (0, 1), at a measure in P^{OO}(Q). 
        
        The Poisson bracket on P^{OO}(Q) is induced by a Poisson bivector field pi_{tau} on Q.
        Let (x1,x2) be Cartesian coordinates on Q. Then pi_{tau} has the following representation,
            
            pi_{tau} = tau * d/dx1 ^ d/dx2, ----------> (1)
        
        for some conformal factor tau on Q. Hence, the Poisson bracket on P^{OO}(Q) is given by

            {F_{f}, F_{h}}(mu_{rho}) = int_{0}^{1} int_{0}^{1} (df/dx1 * dh/dx2 - dh/dx1 * df/dx2) * tau * rho * dx1dx2,
                                                                                                         ----------> (2)
        where F_{f} and F_{h} are linear functionals on P^{OO}(Q) induced by scalar functions f and h on Q, and

            mu_{rho} = rho * |dx1^dx2| ----------> (3)
        
        is a measure in P^{OO}(Q).

        Parameters
        ==========
        tau: string literal expression 
            Represents the conformal factor tau in (1)

        rho: string literal expression
            Represents the density function rho in (1)

        function1: string literal expression
            Represents the function f in (2)

        function2: string literal expression
            Represents the function h in (2)

        numerical: Boolean expression, optional
            Indicates numerical computation. By default, numerical == False.

        Returns: a symbolic expression or a tuple
        =======
            * A symbolic expression of the double integral in (2)
            * A tuple (numerical approximation of the double integral in (2), estimated error)
    """
    # Define the symbolic variables x1 and x2
    x1, x2 = sym.symbols('x1 x2')

    # Convert the string literal expressions tau, rho, function1 and function2 into symbolic variables, in that order
    tau = sym.sympify(tau)  
    rho = sym.sympify(rho)
    ff = sym.sympify(function1)
    hh = sym.sympify(function2)

    # Compute the Poisson bracket of function1 and function2 induced by pi_{tau} in (1):
    # (dff/dx1 * dhh/dx2 - dhh/dx1 * dff/dx2) * tau
    bracket_ff_hh = (sym.diff(ff, x1) * sym.diff(hh, x2) - sym.diff(hh, x1) * sym.diff(ff, x2)) * tau

    # Compute the integrand of the double integral in (2)
    integrand = bracket_ff_hh * rho

    if numerical == True:   # Indicate numerical computation
        # Transform the symbolic variable 'integrand' into a NumPy function that allows a numerical evaluation 
        integrand = sym.lambdify([x1, x2], integrand, 'numpy')

        # Return a tuple: (numerical approximation of the double integral in (2), estimated error)
        return dblquad(integrand, 0, 1, lambda x2: 0, lambda x2: 1)

    # Compute the the double integral in (2)
    integrand = sym.integrate(integrand, (x1, 0, 1))
    integral = sym.integrate(integrand, (x2, 0, 1))

    # Return a symbolic expression of the double integral in (2)
    return integral


def PoissonWasserstein_T2(tau, rho, function1, function2, numerical=False):
    """ Computes the Poisson bracket of two linear functionals on the space P^{OO}(T^2), of measures with a smooth 
        positive density function on the 2-torus T^2, at a measure in P^{OO}(T^2). 
        
        The Poisson bracket on P^{OO}(T^2) is induced by a Poisson bivector field pi_{tau} on T^2.
        Let (theta1, theta2) be natural coordinates on T^2 = S^1 x S^1. Then pi_{tau} has the following representation,
            
            pi_{tau} = tau * d/d{theta1} ^ d/d{theta2}, ----------> (1)
        
        for some conformal factor tau on T^2. Hence, the Poisson bracket on P^{OO}(T^2) is given by

            {F_{f}, F_{h}}(mu_{rho}) = 1/(4*pi**2) * int_{0}^{2*pi} int_{0}^{2*pi} (df/d{theta1} * dh/d{theta2} 
                                                        - dh/d{theta1} * df/d{theta2}) * tau * rho * d{theta1}d{theta2},
                                                                                                         ----------> (2)
        where F_{f} and F_{h} are linear functionals on P^{OO}(T^2) induced by scalar functions f and h on T^2, and

            mu_{rho} = rho * |d{theta1}^d{theta2}| ----------> (3)
        
        is a measure in P^{OO}(T^2).

        Parameters
        ==========
        tau: string literal expression 
            Represents the conformal factor tau in (1)

        rho: string literal expression
            Represents the density function rho in (1)

        function1: string literal expression
            Represents the function f in (2)

        function2: string literal expression
            Represents the function h in (2)

        numerical: Boolean expression, optional
            Indicates numerical computation. By default, numerical == False.

        Returns: a symbolic expression or a tuple
        =======
            * A symbolic expression of the double integral in (2)
            * A tuple (numerical approximation of the double integral in (2), estimated error)
    """
    # Define the symbolic variables theta1 and theta2
    theta1, theta2 = sym.symbols('theta1 theta2')

    # Convert the string literal expressions tau, rho, function1 and function2 into symbolic variables, in that order
    tau = sym.sympify(tau)  
    rho = sym.sympify(rho)
    ff = sym.sympify(function1)
    hh = sym.sympify(function2)

    # Compute the Poisson bracket of function1 and function2 induced by pi_{tau} in (1):
    # (df/d{theta1} * dh/d{theta2} - dh/d{theta1} * df/d{theta2}) * tau
    bracket_ff_hh = (sym.diff(ff, theta1) * sym.diff(hh, theta2) - sym.diff(hh, theta1) * sym.diff(ff, theta2)) * tau

    # Compute the integrand of the double integral in (2)
    integrand = bracket_ff_hh * rho

    if numerical == True:   # Indicate numerical computation
        # Transform the symbolic variable 'integrand' into a NumPy function that allows a numerical evaluation 
        integrand = sym.lambdify([theta1, theta2], 1/(4*sym.pi**2) * integrand, 'numpy')

        # Return a tuple: (numerical approximation of the double integral in (2), estimated error)
        return dblquad(integrand, 0, 2*sym.pi, lambda theta2: 0, lambda theta2: 2*sym.pi)

    # Compute the the double integral in (2)
    integrand = sym.integrate(integrand, (theta1, 0, 2*sym.pi))
    integral = sym.integrate(integrand, (theta2, 0, 2*sym.pi))

    # Return a symbolic expression of the double integral in (2)
    return 1/(4*sym.pi**2) * integral


def PoissonWasserstein_S2(tau, rho, function1, function2, numerical=False):
    """ Computes the Poisson bracket of two linear functionals on the space P^{OO}(S^2), of measures with a smooth 
        positive density function on the 2-sphere S^2, at a measure in P^{OO}(S^2). 
        
        The Poisson bracket on P^{OO}(S^2) is induced by a Poisson bivector field pi_{tau} on S^2.
        Let (theta, phi) be spherical coordinates on S^2 such that 

            (theta, phi) |-> (sin(theta) * cos(phi), sin(theta) * sin(phi), cos(theta)).

        Then pi_{tau} has the following representation,
            
            pi_{tau} = (tau / sin(theta)) * d/d{theta} ^ d/d{phi}, ----------> (1)
        
        for some conformal factor tau on S^2. Hence, the Poisson bracket on P^{OO}(S^2) is given by

            {F_{f}, F_{h}}(mu_{rho}) = 1/(4*pi) * int_{0}^{2*pi} int_{0}^{pi} (df/d{theta} * dh/d{phi} 
                                                 - dh/d{theta} * df/d{phi}) * tau * rho * sin(theta) d{theta1}d{theta2},
                                                                                                         ----------> (2)
        where F_{f} and F_{h} are linear functionals on P^{OO}(S^2) induced by scalar functions f and h on S^2, and

            mu_{rho} = rho * sin(theta) * |d{theta}^d{phi}| ----------> (3)
        
        is a measure in P^{OO}(S^2).

        Parameters
        ==========
        tau: string literal expression 
            Represents the conformal factor tau in (1)

        rho: string literal expression
            Represents the density function rho in (1)

        function1: string literal expression
            Represents the function f in (2)

        function2: string literal expression
            Represents the function h in (2)

        numerical: Boolean expression, optional
            Indicates numerical computation. By default, numerical == False.

        Returns: a symbolic expression or a tuple
        =======
            * A symbolic expression of the double integral in (2)
            * A tuple (numerical approximation of the double integral in (2), estimated error)
    """
    # Define the symbolic variables theta and phi
    theta, phi = sym.symbols('theta phi')

    # Convert the string literal expressions tau, rho, function1 and function2 into symbolic variables, in that order
    tau = sym.sympify(tau)  
    rho = sym.sympify(rho)
    ff = sym.sympify(function1)
    hh = sym.sympify(function2)

    # Compute the Poisson bracket of function1 and function2 induced by pi_{tau} in (1):
    # (df/d{theta} * dh/d{phi} - dh/d{theta} * df/d{phi}) * tau
    bracket_ff_hh = (sym.diff(ff, theta) * sym.diff(hh, phi) - sym.diff(hh, theta) * sym.diff(ff, phi)) * tau

    # Compute the integrand of the double integral in (2)
    integrand = bracket_ff_hh * rho * sym.sin(theta)

    if numerical == True:   # Indicate numerical computation
        # Transform the symbolic variable 'integrand' into a NumPy function that allows a numerical evaluation 
        integrand = sym.lambdify([theta, phi], 1/(4*sym.pi) * integrand, 'numpy')

        # Return a tuple: (numerical approximation of the double integral in (2), estimated error)
        return dblquad(integrand, 0, 2*np.pi, lambda phi: 0, lambda phi: np.pi)

    # Compute the the double integral in (2)
    integrand = sym.integrate(integrand, (theta, 0, sym.pi))
    integral = sym.integrate(integrand, (phi, 0, 2*sym.pi))

    # Return a symbolic expression of the double integral in (2)
    return 1/(4*sym.pi) * integral


def area_Omega_S2(Omega, I_1, I_2):
    """ Computes symplectic areas of finite regions on the space P^{OO}(S^2), of measures with a smooth 
        positive density function on the 2-sphere S^2.

        Let the maps T_s, R_t: S^2 --> S^2  be generated by flows of hamiltonian vector fields on S^2, with

            s in I_1 := [a, b] \subset (0, pi)    and     t in I_2 := [c, d] \subset (0, 2*pi). ----------> (1)
        
        For mu_{rho} in P^{OO}(S^2), the symplectic area of the finite region

            Omega := (T_s o R_t)*(mu_{rho}) ----------> (2)

        on P^{OO}(S^2) can be calculated by the following quadruple integral:

            {1/(4*pi) * int_{c}^{d} int_{a}^{b} int_{0}^{2*pi} int_{0}^{pi} Omega d{theta}d{phi}dsdt ----------> (3)

        Parameters
        ==========
        Omega: ¿sequence of variable names?
            Represents the finite region in (2)

        I_1: a list [a, b]
            Contains two integer or float variables a < b which are the limits of the interval I_1 in (1)

        I_1: a list [c, d]
            Contains two integer or float variables c < d which are the limits of the interval I_2 in (1)

        Returns: a tuple (numerical approximation of the quadruple integral in (3), estimated error)
        =======
    """
    # Define Omega in (2) as a function of theta, phi, s adn t
    def Omega(theta, phi, s, t):
        #cc = 0.7082398710278981
        return np.sin(theta) * np.cos(phi) #(1 / cc) * np.exp(-( (1/2) * (theta + s + 1)/(theta + s - 1) * np.sin(2*(phi + t)) )**2)

    # Compute the the quadruple integral in (3)
    def integral_theta(phi, s, t):
        return quad(Omega, 0, np.pi, args=(phi, s, t))[0]     # Compute the integral with respect to theta
    def integral_phi(s, t):
        return quad(integral_theta, 0, 2*np.pi, args=(s, t))[0]     # Compute the integral with respect to phi
    def integral_s(t):
        return quad(integral_phi, I_1[0], I_1[1], args=(t))[0]      # Compute the integral with respect to s
    area = quad(lambda t: (1/(4*np.pi)) * integral_s(t), I_2[0], I_2[1])    # Compute the integral with respect to t
    
    # Return a tuple: (numerical approximation of the quadruple integral in (3), estimated error)
    return area
