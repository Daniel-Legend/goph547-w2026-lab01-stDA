import numpy as np

from goph547lab01.gravity import (
    gravity_potential_point,
    gravity_effect_point,
)


def test_gravity_origin():
    G = 6.674e-11
    m = 100.0
    x = np.zeros((3,))
    xm = np.array((0.0, 0.0, -15.0))

    U_exp = G * m / np.abs(xm[2])
    g_exp = G * m * (-xm[2]) / np.abs(xm[2]) ** 3

    U_act = gravity_potential_point(x, xm, m)
    g_act = gravity_effect_point(x, xm, m)

    U_err = np.abs((U_exp - U_act) / U_exp)
    g_err = np.abs((g_exp - g_act) / g_exp)

    print()
    print(f"Test m={m} kg, x={x} m, xm={xm} m")
    print(f"U_exp: {U_exp:.3e} m^2/s^2, U_act: {U_act:.3e} m^2/s^2, U_err: {U_err:.3e}")
    print(f"g_exp: {g_exp:.3e} m/s^2, g_act: {g_act:.3e} m/s^2, g_err: {g_err:.3e}")
    print()


def test_gravity_point():
    G = 6.674e-11
    m = 125.0
    x = np.array((5.0, -8.0, 12.0))
    xm = np.array((-3.0, 2.0, -20.0))

    r = np.linalg.norm(x - xm)

    U_exp = G * m / r
    g_exp = G * m * (x[2] - xm[2]) / r**3

    U_act = gravity_potential_point(x, xm, m)
    g_act = gravity_effect_point(x, xm, m)

    U_err = np.abs((U_exp - U_act) / U_exp)
    g_err = np.abs((g_exp - g_act) / g_exp)

    print()
    print(f"Test m={m} kg, x={x} m, xm={xm} m")
    print(f"U_exp: {U_exp:.3e} m^2/s^2, U_act: {U_act:.3e} m^2/s^2, U_err: {U_err:.3e}")
    print(f"g_exp: {g_exp:.3e} m/s^2, g_act: {g_act:.3e} m/s^2, g_err: {g_err:.3e}")
    print()


if __name__ == "__main__":
    test_gravity_origin()
    test_gravity_point()
