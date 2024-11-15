import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def calc_group():
    pass


@calc_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    type=int,
    help="number of x values between o and 2pi",
    show_default=True,
)
def sin(number):
    """Gives a list of NUMBER values for x and tan(x) between 0 and 2pi.


    NUMBER is the number of point between 0 and 2 pi.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


@calc_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    type=int,
    help="number of x values between o and 2pi",
    show_default=True,
)
def tan(number):
    """Gives a list of NUMBER values for x and tan(x) between 0 and 2pi.


    NUMBER is the number of point between 0 and 2 pi.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    calc_group()
